import { useEffect, useState } from "react";
import { Set } from '@/model/logic/set';

export function fetchSetsByIdPlayer(id : any){
  
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