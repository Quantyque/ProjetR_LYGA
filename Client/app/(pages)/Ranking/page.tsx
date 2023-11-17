'use client'
import { useEffect, useState } from 'react'
import { VideogameDao } from '@/model/data/videgame/VideogameDao'
import { PlayerDao } from '@/model/data/player/PlayerDao'
import Rank from '@/app/components/Rank'
import './ranking.css'
import { Player } from '@/model/logic/player'
import { Videogame } from '@/model/logic/videogame'

export default function Ranking() {

  let i = 0;

  var [selectedValue, setSelectedValue] = useState<number>(0);
/*
  useEffect(() => {
    const selectElement = document.getElementById('filterGame') as HTMLSelectElement;
    selectElement.addEventListener('change', (event) => {

    setSelectedValue(parseInt(selectElement.options[selectElement.selectedIndex].value));
  });
  })*/
  
  const playerDao : PlayerDao = new PlayerDao();
  const videogameDao : VideogameDao = new VideogameDao();

  const [players, setPlayers] = useState<Player[]>([]);
  const [videoGames, setVideoGame] = useState<Videogame[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const players = await playerDao.fetchPlayers();
        const games = await videogameDao.fetchVideoGames();

        setPlayers(players);
        setVideoGame(games);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
  
    fetchData();
  }, []);
  

  return (
    <main>
      <div>
        <div className="overflow-auto">

          <div className='overflow-auto' id="rankFilter">
            <select className="select select-bordered w-max max-w-xs rankFilterSelect" id='filterGame'>
              {videoGames.map((videoGame) => (
                <option key={videoGame.id} value={videoGame.id}>
                  {videoGame.name}
                </option>
              ))}
            </select>
          </div>

          <table className="table border-collapse">

            <thead>
                <tr className="bg-base-200">
                    <th id='orderPlace'>Place</th>
                    <th>User Profile</th>
                    <th>Team | Name</th>
                    <th className='score'>Score</th>
                </tr>
            </thead>

            <tbody>
              {
                players.map((player) => (
                i = i+1,
                <Rank place={i} user_profile={player.images["profile"]} name={player.name} team={player.prefix} score={Number((player.elos[1386].score).toFixed(0))} idPlayer={player.id}/>
              ))}
            </tbody>

          </table>

        </div>

      </div> 
    </main>
  )
}