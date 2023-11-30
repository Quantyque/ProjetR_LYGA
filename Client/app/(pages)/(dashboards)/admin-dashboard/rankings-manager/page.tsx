"use client";
import React, {lazy, Suspense, useState, useEffect} from 'react'
import { FaRankingStar } from "react-icons/fa6";
import { CiBoxList } from "react-icons/ci";
import { VideogameDao } from '@/model/data/videogame/VideogameDao'
import { Videogame } from '@/model/logic/videogame';
import { MdCancel } from "react-icons/md";
import IVideogameDao from '@/model/data/videogame/IVideogameDao';

const TableElement = lazy(() =>
  import('@/app/components/DashboardsComponents/AdminDashboard/RankingsManager/TableElement')
);

const RankingManagerPage = () => {

  const videogameDao : IVideogameDao = new VideogameDao();
  const [videoGames, setVideoGame] = useState<Videogame[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('asc');

  useEffect(() => {

    const fetchData = async () => {

      try {

        const games = await videogameDao.fetchAuditedVideoGames();
        setVideoGame(games);

      } catch (error) {

        console.error("Error fetching data:", error);

      }

    };
  
    fetchData();

  }, []);

  {/* Filtres */}
  const filteredRankedGames = videoGames
    .filter((videoGames) => {

      const searchTermLowerCase: string = searchTerm.toLowerCase();
      const isVideoGameMatch = videoGames.name.toLowerCase().includes(searchTermLowerCase);
      return isVideoGameMatch;

    })
    .sort((a, b) => {
      if (sortOrder === 'asc') {
        return a.name.localeCompare(b.name);
      } else {
        return b.name.localeCompare(a.name);
      }
    });

  {/* Reinitialisation des filtres */}
  const resetFilters = () => {
    setSearchTerm('');
    setSortOrder('asc');
  };

  return (
    <div>
      <div className='border-b-4 border-orange-500 text-5xl mb-2 mx-6 lg:mx-0 mt-2 lg:mt-0 flex flex-col lg:flex-row items-center'>
        <span>
          <FaRankingStar className="mb-2 mr-2" />
        </span>
        <h1 className='mb-2 lg:mb-4'>Gestionnaire des classements</h1>
      </div>
      <div className='my-4 mx-6 lg:mx-0 flex items-center border-b-2 border-white w-full'>
        <CiBoxList className="mr-2 text-white w-8 h-8 mb-2" />
        <p className='text-xl mb-2'>Liste des classements par jeux audités</p>
      </div>
      <div className='flex items-center'>
        <input type='text' placeholder='Rechercher par nom' className='p-2 border border-gray-300 rounded-md' onChange={(e) => setSearchTerm(e.target.value)} value={searchTerm}/>
        <select value={sortOrder} onChange={(e) => setSortOrder(e.target.value as 'asc' | 'desc')} className='ml-2 p-2 border border-gray-300 rounded-md'>
          <option value='asc'>Tri croissant</option>
          <option value='desc'>Tri décroissant</option>
        </select>
        <button onClick={resetFilters} className='ml-2 p-2 rounded-md border border-gray-300 hover:bg-zinc-700'>
          <span className='flex items-center'>
            <MdCancel className="mr-2" /> Réinitialiser les filtres
          </span>
        </button>
      </div>
      <div className="overflow-x-auto">
        <table className="table">
          {/* head */}
          <thead>
            <tr>
              <th className="text-left">Jeu audité</th>
              <th className="text-left">Prendre en compte les tournois depuis ...</th>
              <th className="text-left">Prendre en compte les tournois jusqu'à ...</th>
              <th className="text-left">Localisation</th>
              <th className="text-left">Rayon</th>
              <th className="text-left">Auto-rafraichissement</th>
              <th className="text-right">Rafraichissement manuel</th>
            </tr>
          </thead>
          {/* body */}
          <tbody>
            {filteredRankedGames.map((videoGame) => (
              <Suspense fallback={
                <div className="h-screen flex items-center justify-center">
                  <div className="fixed top-0 left-0 w-full h-full bg-opacity-70 flex items-center justify-center">
                      <span className="loading loading-spinner w-[100px] h-[100px]"></span>
                  </div>
                </div>
              }>
                <TableElement videoGame={videoGame} />
              </Suspense>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default RankingManagerPage