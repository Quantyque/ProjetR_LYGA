import React, {useRef} from 'react'
import { FaTrash } from "react-icons/fa";
import { CgClose } from "react-icons/cg";
import { TiMinus } from "react-icons/ti";
import { Videogame } from '@/model/logic/videogame';

interface ModalDeleteProps {
    classId: string,
    videoGame: Videogame
}

const ModalDelete = ({ classId, videoGame }: ModalDeleteProps) => {
    
    return (

        <dialog id={ classId } className="modal">
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
                <form className='mt-2'>
                    <p className='mt-8 w-full text-center'>Êtes vous sur de vouloir supprimer le jeu <span className="text-orange-500 font-extrabold">{ videoGame.name }</span> de la liste des jeux audités ?</p>
                    <button className="submit mt-8 w-full btn bg-red-500 btn-ghost hover:bg-green-300"><FaTrash />Supprimer</button>
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

export default ModalDelete