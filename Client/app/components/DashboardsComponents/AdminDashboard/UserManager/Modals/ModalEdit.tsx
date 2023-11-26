"use client";
import React, { useRef } from 'react';
import Role from '@/model/logic/role';
import User from '@/model/logic/user';
import { MdEdit } from "react-icons/md";
import { FaSave } from "react-icons/fa";
import { FaUser, FaUserMinus, FaTrash } from "react-icons/fa";
import { CgClose } from "react-icons/cg";

interface ModalEditProps {
    user: User
    classId: string
}

const ModalEdit = ({ user, classId }: ModalEditProps) => {

    const username = useRef(user.username)
    const role = useRef("")

    return (

        <dialog id={ classId } className="modal">
            <div className="modal-box">
                <div className='border-b-2 border-orange-500 flex items-center justify-between'>
                    <div className='flex items-center '>
                        <FaUser className="mr-2 w-6 h-6" />
                        <h3 className="font-bold text-lg">
                            Utilisateur <span className='text-orange-500'>{ user.username }</span>
                        </h3>
                    </div>
                    <form method="dialog">
                        <button className='bg-orange-500 hover:bg-orange-600 rounded-md p-3 btn-ghost my-2'><CgClose /></button>
                    </form>
                </div>
                <div className='flex items-center border-b-2 border-gray-200 mt-4'>
                    <MdEdit className="mr-1"/>
                    <h3 className="font-bold text-sm">
                        Modifier l'utilisateur
                    </h3>
                </div>
                <form className='mt-2'>
                    <div className="form-control w-full">
                        <label className="label">
                            <span className="label-text">Nom</span>
                        </label>
                        <input type="text" placeholder="Nom du compte" value={ user.username } className="input input-bordered w-full" onChange={(e) => username.current = e.target.value}/>
                    </div>
                    <div className="form-control w-full mt-2">
                        <label className="label">
                            <span className="label-text">Role</span>
                        </label>
                        <select className="select select-bordered" value={user.role} onChange={(e) => role.current = e.target.value}>
                            <option value={Role.Utilisateur}>Utilisateur</option>
                            <option value={Role.Administrateur}>Administrateur</option>
                        </select>
                    </div>
                    <button className="submit btn w-full mt-8 mb-8 bg-orange-500 btn-ghost hover:bg-orange-600"><FaSave />Enregistrer</button>
                </form>
                <div className='flex items-center border-b-2 border-gray-200 mt-4'>
                    <FaUserMinus className="mr-1"/>
                    <h3 className="font-bold text-sm">
                    Supprimer l'utilisateur
                    </h3>
                </div>
                <button className="submit btn bg-red-600 btn-ghost hover:bg-red-800 mt-8 w-full"><FaTrash />Supprimer l'utilisateur</button>
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

export default ModalEdit