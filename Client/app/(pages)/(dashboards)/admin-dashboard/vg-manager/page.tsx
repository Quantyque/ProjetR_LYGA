"use client";
import React, {useState, useEffect, lazy, Suspense} from 'react'
import { IoGameController } from "react-icons/io5";
import { CiBoxList } from "react-icons/ci";
import { IoIosAddCircle } from "react-icons/io";
import { VideogameDao } from '@/model/data/videogame/VideogameDao'
import { Videogame } from '@/model/logic/videogame';
import IVideogameDao from '@/model/data/videogame/IVideogameDao';
import { MdCancel } from "react-icons/md";
import ModalAdd from '@/app/components/DashboardsComponents/AdminDashboard/VideoGamesManager/Modals/ModalAdd';
import { ToastProvider } from '@/app/components/Providers/ToastProvider';

const TableElement = lazy(() =>
  import('@/app/components/DashboardsComponents/AdminDashboard/VideoGamesManager/TableElement')
);

const VgManagerPage = () => {

  const videogameDao : IVideogameDao = new VideogameDao();
  const [videoGames, setVideoGame] = useState<Videogame[]>([]);

  const [isModalAddOpen, setModalAddOpen] = React.useState(false);

  const [searchTerm, setSearchTerm] = useState('');
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('asc');

  const openAddModal = () => {

    setModalAddOpen(true);

  };

  const closeAddModal = () => {

    setModalAddOpen(false);

  };

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
  const filteredVideoGames = videoGames
    .filter((videoGames) => {

      const searchTermLowerCase: string = searchTerm.toLowerCase();
      const isVideoGamesMatch = videoGames.name.toLowerCase().includes(searchTermLowerCase);
      return isVideoGamesMatch;

    }).sort((a, b) => {

      var result;
      
      if (sortOrder === 'asc') {

        result = a.name.localeCompare(b.name);

      } else {

        result = b.name.localeCompare(a.name);

      }

      return result;

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
          <IoGameController className="mb-2 mr-2" />
        </span>
        <h1 className='mb-2 lg:mb-4'>Gestionnaire des jeux audités</h1>
      </div>
      <div className='my-4 mx-6 lg:mx-0 flex items-center border-b-2 border-white w-full'>
        <CiBoxList className="mr-2 text-white w-8 h-8 mb-2" />
        <p className='text-xl mb-2'>Liste des jeux audités</p>
      </div>
      <div className='my-4 mx-6 lg:mx-0 flex justify-between items-center'>
        <div className='flex items-center justify-between'>
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
        <button className='ml-2 p-2 rounded-md bg-green-500 hover:bg-green-300' onClick={() => (document.getElementById('add') as HTMLDialogElement)?.showModal()}>
            <span className='flex items-center'>
              <IoIosAddCircle className="mr-2"/> Ajouter
            </span>
        </button>
        <ToastProvider>        
          <ModalAdd classId='add' isOpen={ isModalAddOpen } onClose={ closeAddModal }/>
        </ToastProvider>
      </div>
      <div className="overflow-x-auto">
        <table className="table">
          {/* head */}
          <thead>
            <tr>
              <th className="text-left">Jeu audité</th>
              <th className="text-right">Options</th>
            </tr>
          </thead>
          {/* body */}
          <tbody>
            <Suspense fallback={
                  <div className="h-screen flex items-center justify-center">
                  <div className="fixed top-0 left-0 w-full h-full bg-opacity-70 flex items-center justify-center">
                      <span className="loading loading-spinner w-[100px] h-[100px]"></span>
                  </div>
              </div>
            }>
            { filteredVideoGames.map((game) => (
                <TableElement game={game} />
            ))}
            </Suspense>
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default VgManagerPage