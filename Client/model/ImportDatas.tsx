import { Player } from './player';
import { Videogame } from './videogame';
import { Set } from './set';
import React, { useEffect, useState } from 'react';
import { Elo } from './elo';

export function fetchPlayers() {
    const [players, setPlayers] = useState<Player[]>([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/player/all_ranked', {
            method: "POST", // GET, POST, PUT, DELETE, etc.
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

export function fetchVideoGames() {
  const [games, setGames] = useState<Videogame[]>([]);

  useEffect(() => {
      fetch('http://127.0.0.1:5000/videogames/all')
          .then(response => response.json())
          .then(data => setGames(data))
          .catch(error => console.error(error));
  }, []);
  return(games);
}

export function fetchPlayerByID(id : any){
  const [playerData, setPlayerData] = useState<Player | null>(null);

      useEffect(() => {
        fetch('http://127.0.0.1:5000/player/infos', {
            method: "POST", // GET, POST, PUT, DELETE, etc.
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

export function fetchSetsByIdPlayer(id : any){
  
  const [playerSet, setPlayerSet] = useState<Set | null>(null);

      useEffect(() => {
        fetch('http://127.0.0.1:5000/sets/player/', {
            method: "POST", // GET, POST, PUT, DELETE, etc.
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