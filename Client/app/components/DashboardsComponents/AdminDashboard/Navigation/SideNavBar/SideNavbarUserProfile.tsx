"use client";
import React from 'react'
import Link from 'next/link'
import { useSession } from 'next-auth/react';

interface SideNavbarUserProfileProps {
    href: string;
    title: string;
}

const SideNavbarUserProfile = ({href, title}: SideNavbarUserProfileProps) => {

    const { data: session } = useSession();

    return (
        <Link href={ href } title={ title }>
            <img
            src={ session?.user.userPP || "/images/undefined_profile_image.jpg" }
            className="rounded-full w-10 h-10 mb-3 mx-auto"
            />
        </Link>
    )
}

export default SideNavbarUserProfile