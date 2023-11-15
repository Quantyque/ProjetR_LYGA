import { useEffect, useState } from "react";
import { Set } from '@/model/logic/set';
import ISetDao from "./ISetDao";


export class SetDao implements ISetDao{

  /**
   * Retourne les dernier sets réalisé par le joueur dans ses dernier tournois
   * @param id : Id du joueur
   * @returns Les 3 dernier Sets réaliser par le joueur dans un tableau
   */
  fetchSetsByIdPlayer(id : any): Set | null{
    
    const [playerSet, setPlayerSet] = useState<Set | null>(null);

        useEffect(() => {
          fetch('http://127.0.0.1:5000/sets/player/', {
              method: "POST", 
              headers: {
                "Content-Type": "application/json",
                // 'Content-Type': 'application/x-www-form-urlencoded',
              },
              body: JSON.stringify(id), // body data type must match "Content-Type" header
            })
              .then(response => response.json())
              .then(data => setPlayerSet(data))
              .catch(error => console.error(error));
      }, []);
      return(playerSet);  
  }
}