"use client";
import React from 'react';
import User from '@/model/logic/user';
import Role from '@/model/logic/role';
import ModalEdit from '@/app/components/DashboardsComponents/AdminDashboard/UserManager/Modals/ModalEdit';
import { ToastProvider } from '@/app/components/Providers/ToastProvider';

interface MenuElementProps {
    user: User
}

const MenuElement = ({user}: MenuElementProps) => {

    { /* Gestion de la modal d'édition */ }
    const [isModalOpen, setModalOpen] = React.useState(false);

    const closeOnEscape = (e: KeyboardEvent) => {
        if (e.key === 'Escape') {
            closeModal();
        }
    };

    React.useEffect(() => {

        if (isModalOpen) {
            window.addEventListener('keydown', closeOnEscape);
        }

        return () => {
            window.removeEventListener('keydown', closeOnEscape);
        };

    }, [isModalOpen]);

    const openModal = () => {
        setModalOpen(true);
    };

    const closeModal = () => {
        setModalOpen(false);
    };

    return (
        
        <div className='rounded-md bg-zinc-700 btn-ghost'>
            <button onClick={openModal} className='w-full block'>
                <div className="p-4 flex items-center">
                    <img src={ user.userPP ?? "/images/undefined_profile_image.jpg" } className="rounded-full w-16 h-16"/>
                    <div className='my-4 mx-6 flex-1'>
                        <p className='border-b-2 border-orange-500 card-title'>
                            {user.username}
                        </p>
                        <p className={`mt-4 ${user.role === Role.Administrateur ? 'text-red-500' : 'text-green-500'} text-left`}>
                            {user.role === Role.Administrateur ? 'Administrateur' : 'Utilisateur'}
                        </p>
                    </div>
                </div>
            </button>
            <ToastProvider>
                <ModalEdit user={user} isOpen={isModalOpen} onClose={closeModal} classId='edit'/>
            </ToastProvider>
        </div>

    )
}

export default MenuElement