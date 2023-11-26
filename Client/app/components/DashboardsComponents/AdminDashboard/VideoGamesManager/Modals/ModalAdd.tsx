"use client";
import React, { useState, useEffect } from 'react'
import { IoIosAddCircle } from "react-icons/io";
import { CgClose } from "react-icons/cg";
import { IoMdAddCircle } from "react-icons/io";
import { Videogame } from '@/model/logic/videogame';
import { VideogameDao } from '@/model/data/videgame/VideogameDao';
import IVideogameDao from '@/model/data/videgame/IVideogameDao';

interface ModalAddProps {
    classId: string
}

const ModalAdd = ({ classId }: ModalAddProps) => {

    const videogameDao : IVideogameDao = new VideogameDao();
  
    const [videoGames, setVideoGame] = useState<Videogame[]>([]);
  
    useEffect(() => {

      const fetchData = async () => {
        try {

          const games = await videogameDao.fetchVideoGames();
          setVideoGame(games);

        } catch (error) {

          console.error("Error fetching data:", error);

        }
      };
    
      fetchData();

    }, []);

    return (

        <dialog id={ classId } className="modal">
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
                <form className='mt-2'>
                    <div className="form-control w-full">
                        <label className="label">
                            <span className="label-text">Jeu à ajouter</span>
                        </label>
                        <select className="select select-bordered">
                            {videoGames.map((videoGame) => (
                                <option key={videoGame.id} value={videoGame.id}>
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

    )
}

export default ModalAdd