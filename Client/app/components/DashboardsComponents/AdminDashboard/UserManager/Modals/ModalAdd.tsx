import React from 'react'
import Role from '@/model/logic/role'
import { IoIosAddCircle } from "react-icons/io";
import { FaUserPlus } from "react-icons/fa";import { CgClose } from "react-icons/cg";

interface ModalAddProps {
    classId: string
}


const ModalAdd = ({ classId }: ModalAddProps) => {
    
  return (

    <dialog id={ classId } className="modal">
        <div className="modal-box">
            <div className='border-b-2 border-orange-500 flex items-center justify-between'>
                    <div className='flex items-center '>
                        <FaUserPlus className="mr-2 w-6 h-6" />
                        <h3 className="font-bold text-lg">
                            Ajouter un utilisateur
                        </h3>
                    </div>
                    <form method="dialog">
                        <button className='bg-orange-500 hover:bg-orange-600 rounded-md p-3 btn-ghost my-2'><CgClose /></button>
                    </form>
            </div>
            <form className='mt-2'>
                <div className="form-control w-full">
                    <label className="label">
                        <span className="label-text">Nom</span>
                    </label>
                    <input type="text" placeholder="Nom du compte" className="input input-bordered w-full" />
                </div>
                <div className="form-control w-full">
                    <label className="label">
                        <span className="label-text">Role</span>
                    </label>
                    <select className="select select-bordered">
                        <option value={Role.Utilisateur}>Utilisateur</option>
                        <option value={Role.Administrateur}>Administrateur</option>
                    </select>
                </div>
                <div className="form-control w-full">
                    <label className="label">
                        <span className="label-text">Mot de passe</span>
                    </label>
                    <input type="password" placeholder="Mot de passe..." className="input input-bordered w-full" />
                </div>
                <div className="form-control w-full">
                    <label className="label">
                        <span className="label-text">Confirmation du mot de passe</span>
                    </label>
                    <input type="password" placeholder="Confirmation du mot de passe..." className="input input-bordered w-full" />
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