'use client'
import React, { useEffect, useState } from "react";
import "./Profil.css";
import RankingChart from "@/app/(pages)/profil/rankingChart";
import { Elo } from "@/model/logic/elo";
import { useSearchParams } from 'next/navigation'
import { Player } from "@/model/logic/player";
import { Set } from "@/model/logic/set";
import eloController from "@/controller/eloController";
import playerController from "@/controller/playerController";
import setController from "@/controller/setController";

export default function Profil() {
  
  const searchParams = useSearchParams()
  const playerId = searchParams.get('playerId')
  const dataToSend = { player_id: playerId };
  
  const EloController : eloController = new eloController();
  const PlayerController : playerController = new playerController();
  const SetController : setController = new setController();

  const [playerData, setPlayers] = useState<Player | null>(null);
  const [playerEloHistory, setElo] = useState<Elo | null>(null);
  const [playerSet, setSet] = useState<Set | null>(null);
  
  const [currentPage, setCurrentPage] = useState(1);

  const fetchData = async (pageNumber : any) => {
    try {
      const eloHistory = await EloController.getEloHistoryByPlayerID(dataToSend);
      const player = await PlayerController.getPlayerByID(dataToSend);
      const sets = await SetController.getSetByID(dataToSend, { page: pageNumber });

      setElo(eloHistory);
      setPlayers(player);
      setSet(sets);

    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handlePageChange = (direction : any) => {
    setCurrentPage((prevPage) => {
      const newPage = direction === 'left' ? Math.max(prevPage - 1, 1) : Math.min(prevPage + 1, 5);
      fetchData(newPage);
      return newPage;
    });
  };

  useEffect(() => {
    fetchData(currentPage);
  }, [currentPage]);


  return (
    <>
   
      <div id="mainProfil">
       {playerData && playerSet && playerEloHistory && ( 
        <>
          <div id="profilPicture" className="avatar">
          <div className="w-52 rounded-full ring ring-black ring-offset-black ring-offset-8">
            <img id="ImgProfil" alt="" src={playerData.images["profile"] || '/images/undefined_profile_image.jpg'} onError={imageError}/>   
          </div>
          </div>

          <img src={playerData.images["banner"] || '/images/undefined_profile_background_image.jpg'} onError={imageError} alt="" id="BackgroundImage"/>

          <div id="ContactInfoContainer">

              <h1 id="Pseudo">{playerData.name}</h1>

          </div>
          <div id="BiographyContainer">
            <p id="Title">BIOGRAPHY</p>
            <p id="Biography">{playerData?.bio || "Aucune biographie disponible."}</p>
          </div>
          <div id="Details">
            <p id="Title">RANKING</p>
            <div id="Graph" className="mt-3 ml-2">
              <RankingChart eloData={playerEloHistory}/>
            </div>
            <div id="rankingPerGames">
              <div className="scrollable-table-container ">
                <table>
                  <thead>
                  <tr>
                        <th className="profilTH" colSpan={1}>Games</th>
                        <th className="profilTH" colSpan={1}>Favorite Character</th>
                        <th className="profilTH" colSpan={1}>ELO</th>
                        <th className="profilTH" colSpan={1}>Rank</th>
                      </tr>
                  </thead>
                  <tbody id="test" className="custom-scrollbar custom-scrollbar-orange">
                    {Object.values(playerData.elos).map((elo: Elo) => (
                      <tr id="RankingpergameCells" key={elo.id}>
                        <td>{elo.videogame.name}</td>
                        <td></td> 
                        <td>{elo.score.toFixed(0)}</td>
                        <td></td>
                      </tr>
                    ))}
                    </tbody>
                </table>
              </div>
            </div>
          </div>
          <div id="Match_History_container">
              <p id="Title"> LAST SETS</p>
              <div>
                <table id="Profiletable">
                  <thead>
                    <tr>
                      <th className="profilTH" colSpan={1}>Dates</th>
                      <th className="profilTH" colSpan={1}>Games</th>
                      <th className="profilTH" colSpan={1}>Players</th>  
                      <th className="profilTH" colSpan={1}>Rounds</th>
                      <th className="profilTH" colSpan={1}>Opponents</th>
                      <th className="profilTH" colSpan={1}>Results</th>
                    </tr>
                  </thead>
                  <tbody>
                    {Object.values(playerSet).map((Info: any) => {
                    const currentPlayer = Info.players.find((player: { id: number; }) => player.id === playerData.id);
                    const opponent = Info.players.find((player: { id: number; }) => player.id !== playerData.id);

                    return (
                      <tr id="match" key={Info.id}>
                        <td>{DateFromTimestamp(Info.date)}</td>
                        <td>{Info.videogame.name}</td>
                        <td>{currentPlayer.name}</td>
                        <td>
                          {Info.round < 0 ? `Loser Bracket Round ${Math.abs(Info.round)}`: `Winner Bracket Round ${Info.round}`}
                        </td>
                        <td>{opponent.name}</td>
                        <td style={{ color: Info.winner_id === playerData.id ? 'green' : 'red' }}>
                        {Info.winner_id === playerData.id ? 'Victory' : 'Defeat'}
                      </td>
                      </tr>
                    );
                  })}
                  </tbody>
                </table>
              </div>
              <div id="pagination">
                  <button className="spacing" onClick={() => handlePageChange('left')} disabled={currentPage === 1}>
                    Précédent
                  </button>
                  <span className="spacing">Page {currentPage}</span>
                  <button className="spacing" onClick={() => handlePageChange('right')} disabled={currentPage === 5}>
                    Suivant
                  </button>
              </div>
          </div>
        </>
         )}
      </div>
                  
    </>
  );
}

const DateFromTimestamp = (timestamp : any) => {
  const date = new Date(timestamp * 1000); 
  return date.toLocaleDateString();
};

function imageError() {
  var backgroundImage = document.getElementById("BackgroundImage")!;
  backgroundImage.style.display = "none"; // Cacher l'élément image
}
