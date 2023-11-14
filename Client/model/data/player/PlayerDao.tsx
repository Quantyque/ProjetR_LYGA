import { Player } from "@/model/logic/player";
import { useEffect, useState } from "react";

export function fetchPlayers() {
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

export function fetchPlayerByID(id : any){
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