'use client'
import { useState } from 'react'
import { fetchVideoGames } from '@/model/data/videgame/VideogameDao'
import { fetchPlayers } from '@/model/data/player/PlayerDao'
import Rank from '@/app/components/Rank'
import './ranking.css'

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

  var videoGames = fetchVideoGames();

  var players = fetchPlayers();

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