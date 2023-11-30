"use client";
import React, { useState } from 'react';
import { FiRefreshCw } from "react-icons/fi";
import { Videogame } from '@/model/logic/videogame';
import { FaMapMarkedAlt } from "react-icons/fa";
import MapElement from './MapElement';

interface TableElementProps {
  videoGame: Videogame,
}

const TableElement = ({ videoGame }: TableElementProps) => {

  const [isChecked, setIsChecked] = useState(false);
  const [showMap, setShowMap] = useState(false);
  const [coordinates, setCoordinates] = useState("");

  const handleCheckboxChange = () => {
    setIsChecked(!isChecked);
  };

  const handleMapButtonClick = () => {
    setShowMap(!showMap);
  };
  
  const updateCoordinates = (lat: number, lng: number) => {
    setCoordinates(`${lat}, ${lng}`);
  };

  return (
    <>
      <tr className="hover">
        <td className="text-left font-extrabold text-md">{videoGame.name}</td>
        <td>
          <input className='input input-bordered' type="date" id="start" name="tournaments-start" />
        </td>
        <td>
          <input className='input input-bordered' type="date" id="start" name="tournaments-end" />
        </td>
        <td className="flex items-center">
          <input type="text" id="coordinates" name="coordinates" placeholder="Latitude, Longitude" className="input input-bordered w-full max-w-xs" value={ coordinates } />
          <button className='btn btn-ghost bg-zinc-500 hover:bg-zinc-500 m-4' onClick={ handleMapButtonClick }><FaMapMarkedAlt /></button>
        </td>
        <td>
          <input type="number" placeholder="Distance (km)" className="input input-bordered w-full max-w-xs" />
        </td>
        <td className="">
          <label className="cursor-pointer label">
            <span className="text-white">
              Status:
              <span className={`ml-2 ${isChecked ? 'text-success' : 'text-red-500'}`}>
                {isChecked ? 'actif' : 'inactif'}
              </span>
            </span>
            <input type="checkbox" className="toggle toggle-success" checked={isChecked} onChange={ handleCheckboxChange } />
          </label>
        </td>
        <td>
          <button className='btn btn-ghost bg-orange-500 hover:bg-orange-600 m-4'><FiRefreshCw /></button>
        </td>
      </tr>
      {showMap && (
        <tr>
          <td colSpan={8}>
            <MapElement onMapClick={updateCoordinates}/>
          </td>
        </tr>
      )}
    </>
  );
}

export default TableElement;

