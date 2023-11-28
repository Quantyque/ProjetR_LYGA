'use client'
import { useEffect, useState } from 'react'
import { VideogameDao } from '@/model/data/videgame/VideogameDao'
import { PlayerDao } from '@/model/data/player/PlayerDao'
import Rank from '@/app/components/Ranking/Rank'
import { Player } from '@/model/logic/player'
import { Videogame } from '@/model/logic/videogame'

/**
 * Show the page of the ranking
 * @returns an HTML page of the rank
 */
export default function Ranking() {

  let i = 0;
  
  const playerDao : PlayerDao = new PlayerDao();
  const videogameDao : VideogameDao = new VideogameDao();

  const [players, setPlayers] = useState<Player[]>([]);
  const [videoGames, setVideoGame] = useState<Videogame[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const players = await playerDao.fetchPlayers(1,1386);
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
        <div className='m-2 space-x-2'>
          <label>Game</label>
          <select className='btn'>
            {videoGames.map((videoGame) => (
              <option key={videoGame.id} value={videoGame.id}>
                {videoGame.name}
              </option>
            ))}
          </select>
          <label>Season</label>
          <input type='number' value={1} className='input'></input>
        </div>
        <table className='table-auto w-screen'>
          <thead>
              <tr>
                  <th>Place</th>
                  <th>User Profile</th>
                  <th>Team | Name</th>
                  <th>Score</th>
              </tr>
          </thead>
          <tbody>
            {
              players.map((player) => (
              i = i+1,
              <Rank place={i} user_profile={player.images["profile"]} name={player.name} team={player.prefix} score={Number((player.elos[1386].score).toFixed(0))} idPlayer={player.id} season_id={1}/>
            ))}
          </tbody>
        </table>
      </div>
    </main>
  )
}