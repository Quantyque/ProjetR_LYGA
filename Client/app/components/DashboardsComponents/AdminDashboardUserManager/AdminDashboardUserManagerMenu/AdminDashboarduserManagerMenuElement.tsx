import React from 'react'
import Link from 'next/link'
import User from '@/model/logic/user'
import Role from '@/model/logic/role';

interface AdminDashboarduserManagerMenuElementProps {
    href: string,
    user: User
}

const AdminDashboarduserManagerMenuElement = ({href, user}: AdminDashboarduserManagerMenuElementProps) => {

  return (
    
    <Link href={ href } className='rounded-md bg-zinc-700 btn-ghost'>
        <div className="p-4 flex items-center">
            <img src={ user.userPP ?? "/images/undefined_profile_image.jpg" } className="rounded-full w-16 h-16"/>
            <div className='my-4 mx-6 flex-1'>
                <p className='border-b-2 border-orange-500 card-title'>
                    {user.username}
                </p>
                <p className={`mt-4 ${user.role === Role.Administrateur ? 'text-red-500' : 'text-green-500'}`}>
                    {user.role === Role.Administrateur ? 'Administrateur' : 'Utilisateur'}
                </p>
            </div>
        </div>
    </Link>

  )
}

export default AdminDashboarduserManagerMenuElement