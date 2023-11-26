"use client";
import React, { useEffect, useState, Suspense, lazy  } from 'react'
import { BsPersonFillLock } from 'react-icons/bs';
import ModalAdd from '@/app/components/DashboardsComponents/AdminDashboard/UserManager/Modals/ModalAdd';
import IUserDao from '@/model/data/user/IUserDao';
import { UserDao } from '@/model/data/user/UserDao';
import User from '@/model/logic/user';
import Role from '@/model/logic/role';
import { MdCancel } from "react-icons/md";
import { IoIosAddCircle } from "react-icons/io";

const MenuElement = lazy(() =>
  import('@/app/components/DashboardsComponents/AdminDashboard/UserManager/MenuElement')
);

export default function UserManagerPage() {

  const [users, setUsers] = useState<User[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedRole, setSelectedRole] = useState<number | null>(null);
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('asc');

  {/* Recuperation des utilisateurs */}
  useEffect(() => {
    const fetchData = async () => {
      try {
        const userDao: IUserDao = new UserDao();
        const response = await userDao.fetchUsers();
        setUsers(
          response.map(
            (data) =>
              new User(data.id, data.username, data.role, data.userPP, undefined)
          )
        );
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  {/* Filtres */}
  const filteredUsers = users
    .filter((user) => {
      const searchTermLowerCase: string = searchTerm.toLowerCase();
      const isUsernameMatch = user.username.toLowerCase().includes(searchTermLowerCase);
      const isRoleMatch = selectedRole === null || user.role === selectedRole;

      return isUsernameMatch && isRoleMatch;
    })
    .sort((a, b) => {
      if (sortOrder === 'asc') {
        return a.username.localeCompare(b.username);
      } else {
        return b.username.localeCompare(a.username);
      }
    });

  {/* Reinitialisation des filtres */}
  const resetFilters = () => {
    setSearchTerm('');
    setSelectedRole(null);
    setSortOrder('asc');
  };

  return (

    <div>
      <div className='border-b-4 border-orange-500 text-5xl mb-2 mx-6 lg:mx-0 mt-2 lg:mt-0 flex flex-col lg:flex-row items-center'>
        <span>
          <BsPersonFillLock className="mb-2 mr-2" />
        </span>
        <h1 className='mb-2 lg:mb-4'>Gestionnaire des utilisateurs</h1>
      </div>
      <div className='my-4 mx-6 lg:mx-0 flex justify-between items-center'>
        <div>
          <input type='text' placeholder='Rechercher par nom' value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)} className='p-2 border border-gray-300 rounded-md'/>
          <select value={selectedRole === null ? '' : selectedRole.toString()} onChange={(e) => setSelectedRole(e.target.value === '' ? null : parseInt(e.target.value, 10))} className='ml-2 p-2 border border-gray-300 rounded-md'>
            <option value=''>Tous les rôles</option>
            <option value={Role.Utilisateur}>Utilisateur</option>
            <option value={Role.Administrateur}>Administrateur</option>
          </select>
          <select value={sortOrder} onChange={(e) => setSortOrder(e.target.value as 'asc' | 'desc')} className='ml-2 p-2 border border-gray-300 rounded-md'>
            <option value='asc'>Tri croissant</option>
            <option value='desc'>Tri décroissant</option>
          </select>
          <button onClick={resetFilters} className='ml-2 p-2 rounded-md border border-gray-300 hover:bg-zinc-700'>
            <span className='flex items-center'>
              <MdCancel className="mr-2" /> Réinitialiser les filtres
            </span>
          </button>
        </div>
        <div>
          <button className='ml-2 p-2 rounded-md bg-green-500 hover:bg-green-300' onClick={() => (document.getElementById('add') as HTMLDialogElement)?.showModal()}>
            <span className='flex items-center'>
              <IoIosAddCircle className="mr-2"/> Ajouter
            </span>
          </button>
          <ModalAdd classId='add'/>
        </div>
      </div>
      <div className='grid grid-cols-1 xl:grid-cols-4 gap-10 mx-6 lg:mx-0 my-9'>
        <Suspense fallback={
          <div className="h-screen flex items-center justify-center">
              <div className="fixed top-0 left-0 w-full h-full bg-opacity-70 flex items-center justify-center">
                  <span className="loading loading-spinner w-[100px] h-[100px]"></span>
              </div>
          </div>
        }>
          {filteredUsers.map((user) => (
            <MenuElement key={user.id} user={user}/>
          ))}
        </Suspense>
      </div>
    </div>

  );
}
