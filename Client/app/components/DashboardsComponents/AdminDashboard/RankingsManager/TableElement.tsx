"use client";
import React, { useState } from 'react';
import { FiRefreshCw } from "react-icons/fi";
import { Videogame } from '@/model/logic/videogame';

interface TableElementProps {
  videoGame: Videogame,
}

const TableElement = ({ videoGame }: TableElementProps) => {
  const [isChecked, setIsChecked] = useState(false);

  const handleCheckboxChange = () => {
    setIsChecked(!isChecked);
  };

  return (
    <tr className="hover">
      <td className="text-left font-extrabold text-md">{videoGame.name}</td>
        <td className="text-left">
            <label className="cursor-pointer label">
                <span className="text-white">
                    Status:
                    <span className={`ml-2 ${isChecked ? 'text-success' : 'text-red-500'}`}>
                        {isChecked ? 'actif' : 'inactif'}
                    </span>
                </span>
            <input type="checkbox" className="toggle toggle-success" checked={isChecked} onChange={handleCheckboxChange}/>
            </label>
        </td>
        <td className="text-right">
            <button className='btn btn-ghost bg-orange-500 hover:bg-orange-600 m-4'><FiRefreshCw /></button>
        </td>
    </tr>
  );
}

export default TableElement;
