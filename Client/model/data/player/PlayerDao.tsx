import { Player } from "@/model/logic/player";
import { useEffect, useState } from "react";
import IPlayerDao from "./IPlayerDao";



export class PlayerDao implements IPlayerDao{

  /**
   * Récupère toute les informations d'un joueur grâce à son id
   * @param id : Id du joueur à récupérer
   * @returns Les informations du joueur récupérer
   * @author Youri Emmanuel
   */  
  fetchPlayerByID(id : any): Player | null{
    const [playerData, setPlayerData] = useState<Player | null>(null);

        useEffect(() => {
          fetch('http://127.0.0.1:5000/player/infos', {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
                // 'Content-Type': 'application/x-www-form-urlencoded',
              },
              body: JSON.stringify(id), // body data type must match "Content-Type" header
            })
              .then(response => response.json())
              .then(data => setPlayerData(data))
              .catch(error => console.error(error));
      }, []);
      return(playerData);
  }

  /**
   * Récupère toute les informations de tout les joueurs présent dans la DB
   * @returns Les informations de tout les joueurs dans un tableau d'informations
   * @author Youri Emmanuel
   */  
  fetchPlayers() : Player[]{
    const [players, setPlayers] = useState<Player[]>([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/player/all_ranked', {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              // 'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: JSON.stringify({"videogame_id":1386}), // body data type must match "Content-Type" header
          })
            .then(response => response.json())
            .then(data => setPlayers(data))
            .catch(error => console.error(error));
    }, []);
    return(players);
  }
}
