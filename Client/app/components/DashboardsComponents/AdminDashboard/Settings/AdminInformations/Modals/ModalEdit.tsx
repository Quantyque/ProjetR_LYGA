import React, { useState, useEffect } from 'react'
import User from '@/model/logic/user'
import { MdEdit } from "react-icons/md";
import { FaSave } from "react-icons/fa";
import { FaUser } from "react-icons/fa";
import { CgClose } from "react-icons/cg";
import IUserDao from '@/model/data/user/IUserDao';
import { UserDao } from '@/model/data/user/UserDao';
import Role from '@/model/logic/role';
import { useToast } from '@/app/components/Providers/ToastProvider';
import { signOut } from 'next-auth/react';

interface ModalEditProps {
    user: User
    classId: string
    isOpen: boolean;
    onClose: () => void;
}

const ModalEdit = ({ user, classId, isOpen, onClose }: ModalEditProps) => {

    const [editedUsername, setEditedUsername] = useState(user.username);
    const [editedRole, setEditedRole] = useState(user.role);
    const { showToast, toast, hideToast } = useToast();

    useEffect(() => {

        setEditedUsername(user.username);
        setEditedRole(user.role);

    }, [user]);
    
    const handleSave = async (e: React.FormEvent<HTMLFormElement>) => {

        e.preventDefault();

        try {

            const userDao: IUserDao = new UserDao();
            await userDao.updateUser(new User(user.id, editedUsername, editedRole, user.userPP, undefined));
            onClose();
            showToast("L'utilisateur a été mis à jour", "success");
            signOut({
                callbackUrl: '/signin'
            });
            window.location.reload();

        } catch (error) {

            console.error("Erreur lors de la sauvegarde :", error);
            showToast("Erreur lors de la sauvegarde de l'utilisateur", "error");

        }
        
    };

    return (

        <>
            <dialog id={classId} className="modal" open={ isOpen } onClose={ onClose }>
                <div className="modal-box">
                    <div className='border-b-2 border-orange-500 flex items-center justify-between'>
                        <div className='flex items-center '>
                            <FaUser className="mr-2 w-6 h-6" />
                            <h3 className="font-bold text-lg">
                                Utilisateur <span className='text-orange-500'>{user.username}</span>
                            </h3>
                        </div>
                    <form method="dialog">
                        <button className='bg-orange-500 hover:bg-orange-600 rounded-md p-3 btn-ghost my-2'><CgClose /></button>
                    </form>
                    </div>
                    <div className='flex items-center border-b-2 border-gray-200 mt-4'>
                        <MdEdit className="mr-1" />
                        <h3 className="font-bold text-sm">
                            Modifier l'utilisateur
                        </h3>
                    </div>
                    <form className='mt-2' onSubmit={ handleSave }>
                        <div className="form-control w-full">
                            <label className="label">
                            <span className="label-text">Nom</span>
                            </label>
                            <input type="text" placeholder="Nom du compte" value={editedUsername} className="input input-bordered w-full" onChange={(e) => setEditedUsername(e.target.value)}/>
                        </div>
                        <div className="form-control w-full mt-2">
                            <label className="label">
                                <span className="label-text">Role</span>
                            </label>
                            <select className="select select-bordered" value={editedRole} onChange={(e) => setEditedRole(Number(e.target.value))}>
                                <option value={Role.Utilisateur}>Utilisateur</option>
                                <option value={Role.Administrateur}>Administrateur</option>
                            </select>
                        </div>
                        <button className="submit btn w-full mt-8 mb-8 bg-orange-500 btn-ghost hover:bg-orange-600" type='submit'>
                            <FaSave /> Enregistrer
                        </button>
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

export default ModalEdit