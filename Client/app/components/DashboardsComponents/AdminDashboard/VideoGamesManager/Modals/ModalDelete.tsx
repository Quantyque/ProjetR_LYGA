"use client"
import React, { useEffect, useState } from 'react'
import { FaTrash } from "react-icons/fa";
import { CgClose } from "react-icons/cg";
import { TiMinus } from "react-icons/ti";
import { Videogame } from '@/model/logic/videogame';
import IVideogameDao from '@/model/data/videogame/IVideogameDao';
import { VideogameDao } from '@/model/data/videogame/VideogameDao';
import { useToast } from '@/app/components/Providers/ToastProvider';

interface ModalDeleteProps {
    classId: string,
    videoGame: Videogame
    isOpen: boolean;
    onClose: () => void;
}

const ModalDelete = ({ classId, videoGame, isOpen, onClose }: ModalDeleteProps) => {

    const { showToast, toast, hideToast } = useToast();
    const [editedVideoGame, setEditedVideoGame] = useState(videoGame.name);
  
    useEffect(() => {

        setEditedVideoGame(videoGame.name);

    }, [videoGame]);

    const handleDelete = async (e: React.FormEvent<HTMLFormElement>) => {

        e.preventDefault();

        try {
            
            if (videoGame.id !== undefined) {

                const videoGameDao: IVideogameDao = new VideogameDao();
                await videoGameDao.deleteAuditedVideoGame(videoGame.id);
                onClose();
                showToast("Le jeu à été supprimé de la liste", "success");
                window.location.reload();

            } else {

                console.error("VideoGame id undefined");
                showToast("Erreur lors de la suppression du jeu de la liste", "error");

            }

            onClose();

        } catch (error) {

            console.error("Erreur lors de la suppresion :", error);
            showToast("Erreur lors de la suppression du jeu de la liste", "error");

        }
    }

    
    return (

        <>
            <dialog id={ classId } className="modal" open={ isOpen } onClose={ onClose }>
                <div className="modal-box">
                    <div className='border-b-2 border-orange-500 flex items-center justify-between'>
                            <div className='flex items-center '>
                                <TiMinus className="mr-2 w-6 h-6" />
                                <h3 className="font-bold text-lg">
                                    Supprimer un jeu
                                </h3>
                            </div>
                            <form method="dialog">
                                <button className='bg-orange-500 hover:bg-orange-600 rounded-md p-3 btn-ghost my-2'><CgClose /></button>
                            </form>
                    </div>
                    <form className='mt-2' onSubmit={ handleDelete }>
                        <p className='mt-8 w-full text-center'>Êtes vous sur de vouloir supprimer le jeu <span className="text-orange-500 font-extrabold">{ editedVideoGame }</span> de la liste des jeux audités ?</p>
                        <button type="submit" className="submit mt-8 w-full btn bg-red-500 btn-ghost hover:bg-green-300"><FaTrash />Supprimer</button>
                    </form>
                    <p className="py-4 text-gray-700 italic flex justify-end">
                        Appuyez sur la touche ESC ou cliquez sur l'extérieur pour fermer
                    </p>
                </div>
                <form method="dialog" className="modal-backdrop">
                    <button>close</button>
                </form>
            </dialog>
            {toast.message && (
                <div className={"toast"}>
                    <div className={`alert ${toast.type === "success" ? "bg-green-500" : "bg-red-500"}`}>
                        <span className='text-white'>
                            { toast.message }
                        </span>
                    </div>
                </div>
            )}
        </>

    )
}

export default ModalDelete