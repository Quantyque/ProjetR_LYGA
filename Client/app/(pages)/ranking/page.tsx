'use client'
import { useEffect, useState } from 'react'
import videogameController from '@/controller/videogameController'
import playerController from '@/controller/playerController'
import seasonController from '@/controller/seasonController'
import Rank from '@/app/components/Ranking/Rank'
import { Player } from '@/model/logic/player'
import { Videogame } from '@/model/logic/videogame'
import { Season } from '@/model/logic/season'
import './rankingsPage.css'

/**
 * Show the page of the ranking
 * @returns an HTML page of the rank
 * @author Antoine Richard
 */
export default function Ranking() {

  let placeOrder = 0;
  const [videogames, setVideogames] = useState<Videogame[]>([]);
  const [seasons, setSeasons] = useState<Season[]>([]);
  const [players, setPlayers] = useState<Player[]>([]);
  const [currentSeason, SetCurrentSeason] = useState<string>("1");
  const [currentVideogame, SetCurrentVideogame] = useState<number>(1386);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const videogameCtrl: videogameController = new videogameController();
        const videogames = await videogameCtrl.getVideogames();
        const seasonsCtrl: seasonController = new seasonController();
        const seasons = await seasonsCtrl.getAllSeason();
        const playerCtrl: playerController = new playerController();
        const players = await playerCtrl.getPlayersBySeasonIDVideogameID(currentSeason,currentVideogame);
        setVideogames(
          videogames.map(
            (data) =>
              new Videogame(data.id, data.name, data.characters, data.image)
          )
        )
        setSeasons(
          seasons.map(
            (data) =>
              new Season(data.endDate, data.id, data.number, data.startDate)
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
  }, [currentSeason, currentVideogame]);

  return (
    <main>
      <div id='RankingMainContainer'>
        <div className='m-2 space-x-2' id='FilterSelectorContainer'>
          <label>Game</label>
          <select className='btn' onChange={(e) => SetCurrentVideogame(parseInt(e.target.value))}>
            {videogames.map((videogame) => (
              <option key={videogame.id} value={videogame.id}>
                {videogame.name}
              </option>
            ))}
          </select>
          <label>Season</label>
          <select className='btn' onChange={(e) => SetCurrentSeason(e.target.value)}>
            {seasons.map((seasons) => (
              <option key={seasons.id} value={seasons.id}>
                {seasons.number}
              </option>
            ))}
          </select>
        </div>
        <table className='table' id='RankingTable'>
          <thead>
              <tr>
                  <th className='text-center tableHeader'>Place</th>
                  <th className='text-center tableHeader'>User Profile</th>
                  <th className='text-center tableHeader'>Team | Name</th>
                  <th className='text-center tableHeader'>Score</th>
              </tr>
          </thead>
          <tbody>
            {
              players.map((player) => (
                placeOrder = placeOrder + 1,
              <Rank place={placeOrder} 
                    user_profile={player.images["profile"]} 
                    name={player.name} team={player.prefix} 
                    score={player.elos[currentVideogame] !== undefined ? (Math.round(player.elos[currentVideogame].score)) : (null)} 
                    idPlayer={player.id} 
                    season_id={currentSeason}/>
            ))}
          </tbody>
        </table>
      </div>
    </main>
  )
}