import React from 'react'
import AdminDashboard from '@/app/components/DashboardsComponents/AdminDashboard/AdminDashboard';

export default function AdminDashboardLayout({children,} : {children: React.ReactNode}) 
{
    return (
        <AdminDashboard children={children}/>
    )
}