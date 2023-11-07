import './Navbar.css';
import { BsChevronDown } from 'react-icons/bs';
import UserNavMenu from "./UserNavMenu"


export default function Navbar() {

    return (
        <>
        <div
            id="navbar"
            className={`navbar bg-base-100`}>         
                    <div className="flex-1" >

                        <a id="TitleNavbar" className="btn btn-ghost normal-case text-white text-xl" href='/home' >
                            <img src="/projetR.svg" width={"32"} height={"32"} className='mr-2' alt="" />
                            PROJET R
                            <div className="badge badge-neutral ml-1">V1.0 Alpha</div>
                        </a>
                        <div className="dropdown" id='menuNavigation'>
                        <label tabIndex={0} className="btn m-1 btn-ghost" id='menuNavigationTitle'>Menu <BsChevronDown/></label>
                        <ul tabIndex={0} className="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52">
                            <li><a href='./community'>Community</a></li>
                            <li><a href='./tournaments'>Tournaments</a></li>
                            <li><a href='./players'>Players</a></li>
                            <li><a href='./ranking'>Ranking</a></li>
                            <li><a href='./guides'>Guides</a></li>
                        </ul>
                    </div>
                    </div>

                    <div className="flex-none gap-2">
                        <div className="form-control">
                            <input type="text" placeholder="Search" className="input input-bordered w-24 md:w-auto" />
                        </div>
                        <UserNavMenu/>
                    </div>
                </div>
            </>
        )
}
