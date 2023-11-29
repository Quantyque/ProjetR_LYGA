'use client'
import { useEffect, useState } from 'react'
import videogameController from '@/controller/videogameController'
import playerController from '@/controller/playerController'
import { VideogameDao } from '@/model/data/videogame/VideogameDao'
import { PlayerDao } from '@/model/data/player/PlayerDao'
import Rank from '@/app/components/Ranking/Rank'
import { Player } from '@/model/logic/player'
import { Videogame } from '@/model/logic/videogame'

/**
 * Show the page of the ranking
 * @returns an HTML page of the rank
 * @author Antoine Richard
 */
export default function Ranking() {

  let placeOrder = 0;
  const [videogames, setVideogames] = useState<Videogame[]>([]);
  const [players, setPlayers] = useState<Player[]>([]);

  /*
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedRole, setSelectedRole] = useState<number | null>(null);
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('asc');
  const [isModalAddOpen, setModalAddOpen] = React.useState(false);
  
  const openModal = () => {
    setModalAddOpen(true);
  };

  const closeModal = () => {
    setModalAddOpen(false);
  };

  */

  {/* Recuperation des utilisateurs */}
  useEffect(() => {
    const fetchData = async () => {
      try {
        const videogameCtrl: videogameController = new videogameController();
        const videogames = await videogameCtrl.getVideogames();
        const playerCtrl: playerController = new playerController();
        const players = await playerCtrl.getPlayersBySeasonIDVideogameID(1,1386);
        setVideogames(
          videogames.map(
            (data) =>
              new Videogame(data.id, data.name, data.characters, data.image)
          )
        )
        setPlayers(
          players.map(
            (data) =>
              new Player(
                data.id,
                data.name,
                data.date,
                data.prefix,
                data.characters,
                data.elos,
                data.images,
                data.externals_urls,
                data.isDisqualified,
                data.bio
                )
          )
        );
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
            {videogames.map((videogame) => (
              <option key={videogame.id} value={videogame.id}>
                {videogame.name}
              </option>
            ))}
          </select>
          <label>Season</label>
          <input type='number' defaultValue={1} className='input'></input>
          <button type='button' className='btn'>Search</button>
        </div>
        <table className='table'>
          <thead>
              <tr>
                  <th className='text-center'>Place</th>
                  <th>User Profile</th>
                  <th>Team | Name</th>
                  <th className='text-center'>Score</th>
              </tr>
          </thead>
          <tbody>
            {
              players.map((player) => (
                placeOrder = placeOrder + 1,
              <Rank place={placeOrder} user_profile={player.images["profile"]} name={player.name} team={player.prefix} score={Math.round(player.elos[1386].score)} idPlayer={player.id} season_id={1}/>
            ))}
          </tbody>
        </table>
      </div>
    </main>
  )
}