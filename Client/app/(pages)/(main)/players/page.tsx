"use client"
import { useEffect, useState } from "react";
import "./players.css";
import { Player } from "@/model/logic/player";
import playerController from "@/controller/playerController";

/**
 * Page de joueurs
 * @returns HTML de la page des joueurs
 * @author Youri Emmanuel
 */
export default function Players(){

    var PlayerController = new playerController();

    const [playerData, setPlayers] = useState<Player[] | null>(null);
    const [searchTerm, setSearchTerm] = useState<string>(''); // Ajout de l'état pour la valeur de la barre de recherche

    const fetchData = async() => {
        try {
            const players = await PlayerController.getAllPlayers();
            setPlayers(players);
        } catch (error) {
          console.error("Error fetching data:", error);
        }
    };

    useEffect(() => {
        fetchData();
    }, []);

    // Fonction pour filtrer les joueurs en fonction de la barre de recherche
    const filteredPlayers = playerData?.filter(player =>
        player.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return(
        <>
        {playerData && (
            <div id="AllContainer">
                <div id="Filters">
                    <div id="SearchText">
                        Barre de recherche
                    </div>
                    <div id="researchBar">
                        <input
                            id="SearchBar"
                            type="text"
                            placeholder="Player's Name"
                            className="input input-bordered w-full max-w-xs"
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)} // Met à jour l'état de la barre de recherche
                        />
                    </div>
                </div>
                <div id="playersMainContainer">
                    {filteredPlayers?.slice(0, 8).map((player, index) => (
                        <div key={index} className="PLAYERS">
                            <div className="avatar rounded-full ring ring-black ring-offset-base-100 testAvatar">
                                <div className="w-28 rounded-full">
                                    <img src={player.images.profile} alt="" />
                                </div>
                            </div>
                            <a className="PlayerName" href={`/profil?playerId=${player.id}`} >{player.name}</a>
                        </div>
                    ))}
                </div>
            </div>
        )}
        </>
    )
}