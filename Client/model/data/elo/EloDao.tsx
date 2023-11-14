import { Elo } from "@/model/logic/elo";
import { useEffect, useState } from "react";


/**
 * récupère l'historique du joueur grâce à l'id mis en paramètre
 * @param id id du joueur
 * @returns l'historique de l'elo du joueur
 * @author Youri Emmanuel
 */
export function fetchEloHistoryByPlayerID(id : any){
  
    const [playerEloHistory, setPlayerEloHistory] = useState<Elo | null>(null);
  
    useEffect(() => {
        fetch('http://127.0.0.1:5000/elo/get-history', {
            method: "POST", // GET, POST, PUT, DELETE, etc.
            headers: {
            "Content-Type": "application/json",
            // 'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: JSON.stringify(id), // body data type must match "Content-Type" header
        })
            .then(response => response.json())
            .then(data => setPlayerEloHistory(data))
            .catch(error => console.error(error));
    }, []);
    console.log(playerEloHistory)
    return(playerEloHistory);
}