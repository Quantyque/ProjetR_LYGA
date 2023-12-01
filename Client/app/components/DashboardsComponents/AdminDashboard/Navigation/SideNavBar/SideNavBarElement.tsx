import React from 'react'
import Link from 'next/link'
import { ReactNode } from 'react'

interface SideNavBarElementProps {
    href: string;
    title: string;
    icon: ReactNode;
    hoverColor: string;
}

const SideNavBarElement = ({ href, title, icon, hoverColor }: SideNavBarElementProps)  => {
  return (
    <Link href={href} title={ title }>
        <span className={`h-7 w-7 text-gray-300 mx-auto hover:${hoverColor}`}>
            { icon }
        </span>
    </Link>
  )
}

export default SideNavBarElement