"use client";
import { useSession } from 'next-auth/react';
import { BsPersonFillLock } from 'react-icons/bs';
import { IoGameController } from "react-icons/io5";
import { FaRankingStar } from "react-icons/fa6";
import { FaUserCog } from "react-icons/fa";
import MenuElement from '@/app/components/DashboardsComponents/AdminDashboard/Menu/MenuElement';

export default function AdminDashboardMenuPage() {

  const { data: session } = useSession();

  return (
    <div>
      <div className='border-b-4 border-orange-500 text-5xl mb-2 mx-6 lg:mx-0 mt-2 lg:mt-0 flex flex-col lg:flex-row lg:justify-between items-center'>
        <span className='flex items-center'>
          <div className='mr-2'>
            <img
              src={ session?.user.userPP || "/svg/avatar-default-symbolic.svg" }
              className="rounded-full w-10 h-10 mb-3 mx-auto"
            />
          </div>
          <h1 className='mb-2 lg:mb-4'>
            Bienvenue { session?.user.username ?? 'N/A' }
          </h1>
        </span>
        <p className='mb-2 lg:mb-4 text-xl hidden lg:flex'>
          Panneau d'administration
        </p>
      </div>
      <div className='grid grid-cols-1 lg:grid-cols-2 gap-10 mx-6 lg:mx-0 my-9'>
        <MenuElement href='/admin-dashboard/user-manager' icon={<BsPersonFillLock />} title='Utilisateurs' description="Gérer les utilisateurs de l'application" />
        <MenuElement href='/admin-dashboard/vg-manager' icon={<IoGameController />} title='Jeux audités' description='Gérer les jeux audités de l&apos;application' />
        <MenuElement href='/admin-dashboard/rankings-manager' icon={<FaRankingStar />} title='Classements' description='Gérer les divers classements par jeux audités' />
        <MenuElement href='/admin-dashboard/settings' icon={<FaUserCog />} title='Paramètres / Mon compte' description='Gérer mes préférences et mon profil' />
      </div>
    </div>
  );
}
