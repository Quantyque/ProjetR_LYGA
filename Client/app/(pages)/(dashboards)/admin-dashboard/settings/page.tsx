"use client";
import React from 'react'
import { AiFillSetting } from 'react-icons/ai';
import { FaUser } from "react-icons/fa";
import { useSession } from 'next-auth/react';
import { MdEdit } from "react-icons/md";

const UserSettingsPage = () => {

  const { data: session } = useSession();

  return (

    <div>
      <div className='border-b-4 border-orange-500 text-5xl mb-2 mx-6 lg:mx-0 mt-2 lg:mt-0 flex flex-col lg:flex-row items-center'>
        <span>
          <AiFillSetting className="mb-2 mr-2" />
        </span>
        <h1 className='mb-2 lg:mb-4'>Paramètres / Mon compte</h1>
      </div>
      <div>
        <div className='my-4 mx-6 lg:mx-0 flex items-center border-b-2 border-white w-full'>
          <FaUser className="mr-2 text-white w-8 h-8 mb-2" />
          <p className='text-xl mb-2'>Mes informations</p>
        </div>
        <div>
          <table className="table">
            <tbody>
              <tr className="hover">
                <td className="font-bold">Nom du compte</td>
                <td>
                  <p>{ session?.user.username ?? "N/A" }</p>
                </td>
              </tr>
              <tr className="hover">
                <td className="font-bold">Role</td>
                <td>
                  <p>{session?.user.role ?? "N/A"}</p>
                </td>
              </tr>
              <tr className="hover">
                <td className="font-bold">Avatar</td>
                <td>
                  <img
                    src={session?.user.userPP || "/images/undefined_profile_image.jpg"}
                    className="rounded-full w-10 h-10"
                  />
                </td>
              </tr>
            </tbody>
          </table>
          <button className='btn btn-ghost bg-orange-500 hover:bg-orange-600 my-4 ml-4'><MdEdit />Modifier</button>
        </div>
      </div>
    </div>
    
  )
}

export default UserSettingsPage