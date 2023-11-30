"use client";
import React, { useState } from 'react';
import { FiRefreshCw } from "react-icons/fi";
import { Videogame } from '@/model/logic/videogame';
import { FaMapMarkedAlt } from "react-icons/fa";
import IRankingDao from '@/model/data/ranking/IRankingDao';
import { SetDao } from '@/model/data/ranking/RankingDao';
import MapElement from './MapElement';

interface TableElementProps {
  videoGame: Videogame,
}

const TableElement = ({ videoGame }: TableElementProps) => {

  const [isChecked, setIsChecked] = useState(false);
  const [showMap, setShowMap] = useState(false);
  const [coordinates, setCoordinates] = useState("");

  const handleManualRefreshButtonClick = async () => {

    try {

      const startDate = (document.getElementById('start') as HTMLInputElement)?.value;
      const endDate = (document.getElementById('end') as HTMLInputElement)?.value;
      const coordinatesInput = (document.getElementById('coordinates') as HTMLInputElement)?.value;
      const distanceInput = (document.getElementById('distance') as HTMLInputElement)?.value;
  
      console.log({startDate : startDate, endDate: endDate, coordinatesInput: coordinatesInput, distanceInput: distanceInput, videoGameId: videoGame.id});
  
      if (startDate && endDate && coordinatesInput && distanceInput) {

        const coordinates = coordinatesInput.split(',').map(coord => parseFloat(coord.trim()));
  
        if (coordinates.length === 2 && !isNaN(coordinates[0]) && !isNaN(coordinates[1])) {

          const coordinatesToSend: [number, number] = [coordinates[0], coordinates[1]];
          const distance = parseFloat(distanceInput);
  
          const rankingDao: IRankingDao = new SetDao();
          await rankingDao.manualRefresh(new Date(startDate), new Date(endDate), videoGame.id, coordinatesToSend, distance);
  
          window.location.reload();

        } else {

          console.error("Le format des coordonnées est incorrect.");

        }
      } else {

        console.error("Veuillez remplir tous les champs nécessaires.");

      }
    } catch (error) {

      console.error("Erreur lors de la sauvegarde :", error);

    }

  };
  

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
          <input className='input input-bordered' type="date" id="start" name="tournaments-start" required />
        </td>
        <td>
          <input className='input input-bordered' type="date" id="end" name="tournaments-end" required />
        </td>
        <td className="flex items-center">
          <input type="text" id="coordinates" name="coordinates" placeholder="Latitude, Longitude" className="input input-bordered w-full max-w-xs" value={ coordinates } required />
          <button className='btn btn-ghost bg-zinc-500 hover:bg-zinc-500 m-4' onClick={ handleMapButtonClick }><FaMapMarkedAlt /></button>
        </td>
        <td>
          <input type="number" placeholder="Distance (km)" id='distance' name="distance" className="input input-bordered w-full max-w-xs" />
        </td>
        <td className="">
          <label className="cursor-pointer label">
            <span className="text-white">
              Status:
              <span className={`ml-2 ${isChecked ? 'text-success' : 'text-red-500'}`}>
                {isChecked ? 'actif' : 'inactif'}
              </span>
            </span>
            <input type="checkbox" className="toggle toggle-success" checked={isChecked} onChange={ handleCheckboxChange }/>
          </label>
        </td>
        <td>
          <button className='btn btn-ghost bg-orange-500 hover:bg-orange-600 m-4' onClick={ handleManualRefreshButtonClick }><FiRefreshCw /></button>
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

