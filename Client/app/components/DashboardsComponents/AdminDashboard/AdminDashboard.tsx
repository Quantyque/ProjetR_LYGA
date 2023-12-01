import React from 'react';
import SideNavBar from '@/app/components/DashboardsComponents/AdminDashboard/Navigation/SideNavBar/SideNavBar';

type AdminPanelSideNavBarProps = {
    children: React.ReactNode
}

const AdminDashboard = (props: AdminPanelSideNavBarProps) => {

    return (

        <div className="flex flex-row h-full">

            {/* Navbar LG + */}
            <SideNavBar />

            {/* Page content */}
            <div className="py-4 lg:ml-32 lg:mr-16 text-white  h-screen w-screen">
                {props.children}
            </div>

        </div>
        
    )
}

export default AdminDashboard