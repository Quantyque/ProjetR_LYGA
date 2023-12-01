import React, { useState } from 'react'
import Role from '@/model/logic/role'
import { IoIosAddCircle } from "react-icons/io";
import { FaUserPlus } from "react-icons/fa";import { CgClose } from "react-icons/cg";
import User from '@/model/logic/user';
import { useToast } from '@/app/components/Providers/ToastProvider';
import userController from '@/controller/userControllers';

interface ModalAddProps {
    classId: string
    isOpen: boolean;
    onClose: () => void;
}


const ModalAdd = ({ classId, isOpen, onClose }: ModalAddProps) => {

    const { showToast, toast, hideToast } = useToast();
    const [username, setUsername] = useState('');
    const [role, setRole] = useState(Role.Utilisateur);
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    
    const handleSave = async (e: React.FormEvent<HTMLFormElement>) => {
        
            e.preventDefault();

            try {
    
                const userCtrl: userController = new userController();
                await userCtrl.createUserWithRole(new User(undefined, username, role, undefined, undefined), password, confirmPassword);
                onClose();
                showToast("L'utilisateur a été ajouté", "success");
                window.location.reload();
    
            } catch (error) {
    
                console.error("Erreur lors de la sauvegarde :", error);
                showToast("Erreur lors de l'ajout de l'utilisateur", "error");
    
            }

    }

    
    return (

        <>
            <dialog id={ classId } className="modal" open={ isOpen } onClose={ onClose } >
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
                    <form className="mt-2" onSubmit={ handleSave }>
                        <div className="form-control w-full">
                            <label className="label">
                                <span className="label-text">
                                    Nom
                                </span>
                            </label>
                            <input type="text" placeholder="Nom du compte" className="input input-bordered w-full" value={username} onChange={(e) => setUsername(e.target.value)}/>
                        </div>
                        <div className="form-control w-full">
                            <label className="label">
                                <span className="label-text">Role</span>
                            </label>
                            <select className="select select-bordered" value={role} onChange={(e) => setRole(Number(e.target.value))}>
                                <option value={Role.Utilisateur}>Utilisateur</option>
                                <option value={Role.Administrateur}>Administrateur</option>
                            </select>
                        </div>
                        <div className="form-control w-full">
                            <label className="label">
                                <span className="label-text">
                                    Mot de passe
                                </span>
                            </label>
                            <input type="password" placeholder="Mot de passe..." className="input input-bordered w-full" value={password} onChange={(e) => setPassword(e.target.value)} />
                        </div>
                        <div className="form-control w-full">
                            <label className="label">
                                <span className="label-text">
                                    Confirmation du mot de passe
                                </span>
                            </label>
                            <input type="password" placeholder="Confirmation du mot de passe..." className="input input-bordered w-full" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)}/>
                        </div>
                        <button className="submit mt-8 w-full btn bg-green-500 btn-ghost hover:bg-green-300">
                            <IoIosAddCircle /> 
                            Ajouter
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

export default ModalAdd