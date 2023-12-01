"use client";
import React from 'react'
import { FaUser } from "react-icons/fa";
import { useSession } from 'next-auth/react';
import { MdEdit } from "react-icons/md";
import Role from '@/model/logic/role';
import ModalEdit from '@/app/components/DashboardsComponents/AdminDashboard/Settings/AdminInformations/Modals/ModalEdit';
import User from '@/model/logic/user';
import { ToastProvider } from '@/app/components/Providers/ToastProvider';

const AdminInformations = () => {

    const { data: session } = useSession();

    const [isModalAddOpen, setModalAddOpen] = React.useState(false);

    const closeOnEscape = (e: KeyboardEvent) => {

        if (e.key === 'Escape') {

            closeAddModal();

        }

    };

    React.useEffect(() => {

        if (isModalAddOpen) {

            window.addEventListener('keydown', closeOnEscape);

        }

        return () => {

            window.removeEventListener('keydown', closeOnEscape);

        };

    }, [isModalAddOpen]);

    const openAddModal = () => {
  
      setModalAddOpen(true);
  
    };
  
    const closeAddModal = () => {
  
      setModalAddOpen(false);
  
    };

    return (
        <>
            <div className='my-4 mx-6 lg:mx-0 flex items-center border-b-2 border-white w-full'>
                <FaUser className="mr-2 text-white w-8 h-8 mb-2" />
                <p className='text-xl mb-2'>Mes informations</p>
            </div>
            <div>
                <table className="table">
                    <tbody>
                    <tr className="hover">
                        <td className="font-bold">Nom du compte</td>
                        <td>
                            <p>{ session?.user.username ?? "N/A" }</p>
                        </td>
                    </tr>
                    <tr className="hover">
                        <td className="font-bold">Role</td>
                        <td>
                            <p>{session?.user.role === Role.Administrateur ? 'Administrateur' : 'Utilisateur' ?? "N/A"}</p>
                        </td>
                    </tr>
                    <tr className="hover">
                        <td className="font-bold">Avatar</td>
                        <td>
                            <img
                                src={session?.user.userPP || "/images/undefined_profile_image.jpg"}
                                className="rounded-full w-10 h-10"
                            />
                        </td>
                    </tr>
                    </tbody>
                </table>
                <button className='btn btn-ghost bg-orange-500 hover:bg-orange-600 my-4 ml-4' onClick={ openAddModal }><MdEdit />Modifier</button>
                <ToastProvider>
                    <ModalEdit user={ new User(session?.user.id, session?.user.username ?? "N/A", session?.user.role, session?.user.userPP, undefined) } isOpen={isModalAddOpen} onClose={ closeAddModal } classId='add' />
                </ToastProvider>
            </div>
        </>
    )
}

export default AdminInformations