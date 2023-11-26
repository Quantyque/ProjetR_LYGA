"use client";
import React from 'react';
import User from '@/model/logic/user';
import Role from '@/model/logic/role';
import ModalEdit from '@/app/components/DashboardsComponents/AdminDashboard/UserManager/Modals/ModalEdit';

interface MenuElementProps {
    user: User
}

const MenuElement = ({user}: MenuElementProps) => {

    return (
        
        <div className='rounded-md bg-zinc-700 btn-ghost'>
            <button onClick={() => (document.getElementById('edit') as HTMLDialogElement)?.showModal()} className='w-full block'>
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
            <ModalEdit user={user} classId='edit'/>
        </div>

    )
}

export default MenuElement