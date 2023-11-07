"use client"
import { signIn, signOut, useSession } from "next-auth/react"

function UserNavMenu() {

    const { data: session } = useSession()

    if (session && session.user) {
        return (
            <div className="dropdown dropdown-end">
                <label tabIndex={0} className="btn btn-ghost btn-circle avatar">
                    <div className="w-10 rounded-full">
                        <img alt="" src={ session.user.userPP ?? "images/undefined_profile_image.jpg"} />
                    </div>
                </label>
                <ul tabIndex={0} className="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
                    <li>
                        <a href='#' className="text-orange-500">{"Bienvenue " + session.user.username}</a>
                    </li>
                    <li><a href='profil'>Profil</a></li>
                    <li><a>Settings</a></li>
                    {session.user.role === 1 && <li><a href='admin-panel'>Admin panel</a></li>}
                    <li><button onClick={() => signOut()}>
                        Logout
                        </button>
                    </li>
                </ul>
            </div>
        )
    } 
    else {
        return (
            <div className="dropdown dropdown-end">
                <label tabIndex={0} className="btn btn-ghost btn-circle avatar">
                    <div className="w-10 rounded-full">
                        <img alt="" src={"images/undefined_profile_image.jpg"} />
                    </div>
                </label>
                <ul tabIndex={0} className="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
                    <li><button onClick={() => signIn()}>
                        Login
                        </button>
                    </li>
                </ul>
            </div>
        )
    }
}

export default UserNavMenu