"use client"
import React from 'react'
import { FaTrash } from "react-icons/fa";
import { Videogame } from '@/model/logic/videogame';
import ModalDelete from '@/app/components/DashboardsComponents/AdminDashboard/VideoGamesManager/Modals/ModalDelete';
import { ToastProvider } from '@/app/components/Providers/ToastProvider';

interface VideoGamesManagerTableElementProps {
    game: Videogame
}

const VideoGamesManagerTableElement = ({ game }: VideoGamesManagerTableElementProps) => {

  const [isModalOpen, setModalOpen] = React.useState(false);

  const closeOnEscape = (e: KeyboardEvent) => {
    if (e.key === 'Escape') {
        closeModal();
    }
  };

  React.useEffect(() => {

      if (isModalOpen) {
          window.addEventListener('keydown', closeOnEscape);
      }

      return () => {
          window.removeEventListener('keydown', closeOnEscape);
      };

  }, [isModalOpen]);

  const openModal = () => {

    setModalOpen(true);

  };

  const closeModal = () => {

    setModalOpen(false);

  };

  return (
    <tr className="hover">
        <td className="text-left font-extrabold text-md">{game.name}</td>
        <td className="text-right">
          <button className='btn btn-ghost bg-red-500 hover:bg-red-600 my-4 ml-4' onClick={ openModal }><FaTrash /> Supprimer</button>
          <ToastProvider>
            <ModalDelete classId='delete' videoGame={game} isOpen={isModalOpen} onClose={closeModal}/>
          </ToastProvider>
        </td>
    </tr>
  )
}

export default VideoGamesManagerTableElement