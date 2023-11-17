'use client'
import React, { useEffect, useState } from "react";
import "./profil.css";
import RankingChart from "@/app/(pages)/profil/rankingChart";
import { Elo } from "@/model/logic/elo";
import { useSearchParams } from 'next/navigation'
import { PlayerDao } from "@/model/data/player/PlayerDao";
import { SetDao } from "@/model/data/set/SetDao";
import { EloDao } from "@/model/data/elo/EloDao";
import { Player } from "@/model/logic/player";
import { Set } from "@/model/logic/set";

export default function Profil() {
  
  const searchParams = useSearchParams()
  const playerId = searchParams.get('playerId')
  const dataToSend = { player_id: playerId };

  const eloDao : EloDao = new EloDao();
  const playerDao : PlayerDao = new PlayerDao();
  const setDao : SetDao = new SetDao();

  const [playerData, setPlayers] = useState<Player | null>(null);
  const [playerEloHistory, setElo] = useState<Elo | null>(null);
  const [playerSet, setSet] = useState<Set | null>(null);
  

  useEffect(() => {
    const fetchData = async () => {
      try {
        const eloHistory = await eloDao.fetchEloHistoryByPlayerID(dataToSend);
        const player = await playerDao.fetchPlayerByID(dataToSend);
        const sets = await setDao.fetchSetsByIdPlayer(dataToSend);
  
        setElo(eloHistory);
        setPlayers(player);
        setSet(sets);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
  
    fetchData();
  }, []);
  


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
                        <th colSpan={1}>Games</th>
                        <th colSpan={1}>Favorite Character</th>
                        <th colSpan={1}>ELO</th>
                        <th colSpan={1}>Rank</th>
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
              <p id="Title"> LAST 3 SETS</p>
              <div>
                <table style={{marginTop:'70px'}}>
                  <thead>
                    <tr>
                      <th colSpan={1}>Dates</th>
                      <th colSpan={1}>Games</th>
                      <th colSpan={1}>Players</th>  
                      <th colSpan={1}>Rounds</th>
                      <th colSpan={1}>Opponents</th>
                      <th colSpan={1}>Results</th>
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
