"use client";
import React from 'react';
import { AiFillSetting } from 'react-icons/ai';
import { FiLogOut } from 'react-icons/fi';
import { IoGameController } from "react-icons/io5";
import { FaRankingStar } from "react-icons/fa6";
import { BsPersonFillLock } from 'react-icons/bs';
import { FaArrowLeft } from 'react-icons/fa';
import { signOut } from 'next-auth/react';
import SideNavBarElement from '@/app/components/DashboardsComponents/AdminDashboard/Navigation/SideNavBar/SideNavBarElement';
import SideNavbarUserProfile from '@/app/components/DashboardsComponents/AdminDashboard/Navigation/SideNavBar/SideNavbarUserProfile';

const SideNavBar = () => {

  return (
    
    <nav className="fixed border-r-2 border-orange-500 w-20 justify-between hidden lg:flex lg:flex-col h-full">
      <div className="mt-8 mb-10">
        <SideNavbarUserProfile href="/admin-dashboard" title="Menu" />
        <div className="mt-10">
          <ul>
            <li className="mb-6">
              <SideNavBarElement href="/admin-dashboard/user-manager" title="Utilisateurs" icon={<BsPersonFillLock className="h-7 w-7 text-gray-300 mx-auto hover:text-orange-500" />} hoverColor="text-orange-500" />
            </li>
            <li className="mb-6">
              <SideNavBarElement href="/admin-dashboard/vg-manager" title="Jeux audités" icon={<IoGameController className="h-7 w-7 text-gray-300 mx-auto hover:text-orange-500" />} hoverColor="text-orange-500" />
            </li>
            <li className="mb-6">
              <SideNavBarElement href="/admin-dashboard/rankings-manager" title="Classements" icon={<FaRankingStar className="h-7 w-7 text-gray-300 mx-auto hover:text-orange-500" />} hoverColor="text-orange-500" />
            </li>
          </ul>
        </div>
      </div>
      <div className="mb-6">
        <ul>
          <li className='mb-6'>
            <SideNavBarElement href="/home" title="Retour à la page d'accueil" icon={<FaArrowLeft className="h-7 w-7 text-gray-300 mx-auto hover:text-orange-500" />} hoverColor="text-orange-500" />
          </li>
          <li className='mb-6'>
            <SideNavBarElement href="/admin-dashboard/settings" title='Paramètres / Mon compte' icon={<AiFillSetting className="h-7 w-7 text-gray-300 mx-auto hover:text-orange-500" />} hoverColor="text-orange-500" />
          </li>
          <li className='ml-7'>
            <button onClick={() => signOut({ redirect: true, callbackUrl: "/"})} title='Se déconnecter'>
              <span>
                <FiLogOut className="h-7 w-7 text-gray-300 mx-auto hover:text-red-500" />
              </span>
            </button>
          </li>
        </ul>
      </div>
    </nav>

  )
}

export default SideNavBar