import React from 'react';
import AdminPanelSideNavBar from '@/app/components/DashboardsComponents/AdminDashboardBase/AdminDashboardSideNavBar/AdminDashboardSideNavBar';
//import AdminDashboardBottomNavBar from '@/app/components/DashboardsComponents/AdminDashboardBase/AdminDashboardBottomNavBar/AdminDashboardBottomNavBar';

type AdminPanelSideNavBarProps = {
    children: React.ReactNode
}

const AdminDashboard = (props: AdminPanelSideNavBarProps) => {

    return (

        <div className="flex flex-row h-full">

            {/* Navbar LG + */}
            <AdminPanelSideNavBar />

            {/* Page content */}
            <div className="py-4 lg:ml-32 lg:mr-16 text-white  h-screen w-screen">
                {props.children}
            </div>

            {/* Navbar LG - */}
            {/*<AdminDashboardBottomNavBar />*/}

        </div>
        
    )
}

export default AdminDashboard