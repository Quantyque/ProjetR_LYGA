"use client";
import React, { useState, useEffect } from 'react'
import { IoIosAddCircle } from "react-icons/io";
import { CgClose } from "react-icons/cg";
import { IoMdAddCircle } from "react-icons/io";
import { Videogame } from '@/model/logic/videogame';
import { VideogameDao } from '@/model/data/videogame/VideogameDao';
import IVideogameDao from '@/model/data/videogame/IVideogameDao';
import { useToast } from '@/app/components/Providers/ToastProvider';

interface ModalAddProps {
    classId: string
    isOpen: boolean;
    onClose: () => void;
}

const ModalAdd = ({ classId, isOpen, onClose }: ModalAddProps) => {
  
    const { showToast, toast, hideToast } = useToast();
    const [videoGames, setVideoGames] = useState<Videogame[]>([]);
    const [videoGameToAdd, setVideoGameToAdd] = useState<Videogame>();

    useEffect(() => {

      const fetchData = async () => {
        try {

            const videogameDao : IVideogameDao = new VideogameDao();
            const games = await videogameDao.fetchVideoGames();
            const auditedGames = await videogameDao.fetchAuditedVideoGames();
            const availableGames = games.filter((game) => !auditedGames.some((auditedGame) => auditedGame.id === game.id));
            setVideoGames(availableGames);

        } catch (error) {

          console.error("Error fetching data:", error);

        }
      };
    
      fetchData();

    }, []);

    const handleSave = async (event: React.FormEvent<HTMLFormElement>) => {

        event.preventDefault();
    
        try {

            if (videoGameToAdd) {
                
                const videogameDao : IVideogameDao = new VideogameDao();
                await videogameDao.addVideoGame(videoGameToAdd);
                onClose();
                showToast(`Le jeu ${videoGameToAdd.name} a bien été ajouté`, "success");
                window.location.reload();

            }

        } catch (error) {

            console.error("Error adding data:", error);
            showToast(`Le jeu n'a pas pu être ajouté`, "error");

        }
    };
    

    return (

        <>
            <dialog id={ classId } className="modal" open={ isOpen } onClose={ onClose }>
                <div className="modal-box">
                    <div className='border-b-2 border-orange-500 flex items-center justify-between'>
                            <div className='flex items-center '>
                                <IoMdAddCircle className="mr-2 w-6 h-6" />
                                <h3 className="font-bold text-lg">
                                    Ajouter un jeu
                                </h3>
                            </div>
                            <form method="dialog">
                                <button className='bg-orange-500 hover:bg-orange-600 rounded-md p-3 btn-ghost my-2'><CgClose /></button>
                            </form>
                    </div>
                    <form className='mt-2' onSubmit={ handleSave }>
                        <div className="form-control w-full">
                            <label className="label">
                                <span className="label-text">Jeu à ajouter</span>
                            </label>
                            <select className="select select-bordered" onChange={(e) => {
                                    const selectedGame = videoGames.find((game) => game.id === Number(e.target.value));
                                    setVideoGameToAdd(selectedGame);
                            }}>
                                <option value="">Sélectionner un jeu</option>
                                {videoGames.map((videoGame) => (
                                    <option key={videoGame.id} value={videoGame.id.toString()}>
                                        {videoGame.name}
                                    </option>
                                ))}
                            </select>
                        </div>
                        <button className="submit mt-8 w-full btn bg-green-500 btn-ghost hover:bg-green-300"><IoIosAddCircle />Ajouter</button>
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

export default ModalAdd