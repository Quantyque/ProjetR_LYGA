import React from 'react'
import { AiFillSetting } from 'react-icons/ai';
import AdminInformations from '@/app/components/DashboardsComponents/AdminDashboard/Settings/AdminInformations/AdminInformations';
import AppSettings from '@/app/components/DashboardsComponents/AdminDashboard/Settings/AppSettings/AppSettings';

const UserSettingsPage = () => {

  return (

    <div>
      <div className='border-b-4 border-orange-500 text-5xl mb-2 mx-6 lg:mx-0 mt-2 lg:mt-0 flex flex-col lg:flex-row items-center'>
        <span>
          <AiFillSetting className="mb-2 mr-2" />
        </span>
        <h1 className='mb-2 lg:mb-4'>Paramètres / Mon compte</h1>
      </div>
      <div>
        <AdminInformations />
      </div>
      <div>
        <AppSettings />
      </div>
    </div>
    
  )
}

export default UserSettingsPage