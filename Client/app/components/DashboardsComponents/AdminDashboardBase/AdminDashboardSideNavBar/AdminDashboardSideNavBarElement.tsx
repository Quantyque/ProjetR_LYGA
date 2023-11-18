import React from 'react'
import Link from 'next/link'
import { ReactNode } from 'react'

interface AdminDashboardSideNavBarElementProps {
    href: string;
    title: string;
    icon: ReactNode;
    hoverColor: string;
}

const AdminDashboardSideNavBarElement = ({ href, title, icon, hoverColor }: AdminDashboardSideNavBarElementProps)  => {
  return (
    <Link href={href} title={ title }>
        <span className={`h-7 w-7 text-gray-300 mx-auto hover:${hoverColor}`}>
            { icon }
        </span>
    </Link>
  )
}

export default AdminDashboardSideNavBarElement