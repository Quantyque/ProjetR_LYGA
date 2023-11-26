import React from 'react'
import { FaTrash } from "react-icons/fa";
import { Videogame } from '@/model/logic/videogame';
import ModalDelete from '@/app/components/DashboardsComponents/AdminDashboard/VideoGamesManager/Modals/ModalDelete';

interface VideoGamesManagerTableElementProps {
    game: Videogame
}

const VideoGamesManagerTableElement = ({ game }: VideoGamesManagerTableElementProps) => {
  return (
    <tr className="hover">
        <td className="text-left font-extrabold text-md">{game.name}</td>
        <td className="text-right">
          <button className='btn btn-ghost bg-red-500 hover:bg-red-600 my-4 ml-4' onClick={() => (document.getElementById('delete') as HTMLDialogElement)?.showModal()}><FaTrash /> Supprimer</button>
          <ModalDelete classId='delete' videoGame={game}/>
        </td>
    </tr>
  )
}

export default VideoGamesManagerTableElement