import React from 'react'
import Link from 'next/link'

interface MenuElementProps {
    href: string,
    icon: React.ReactNode,
    title: string,
    description: string,
}

const MenuElement = ({href, icon, title, description}: MenuElementProps) => {
  return (

    <Link href={ href } className='rounded-md bg-zinc-700 btn-ghost'>
        <div className="p-4">
            <div className='my-4 mx-4'>
                <p className='border-b-2 border-orange-500 card-title'>
                { icon }{ title }
                </p>
                <p className='mt-4'>
                { description }
                </p>
            </div>
        </div>
    </Link>
    
  )
}

export default MenuElement