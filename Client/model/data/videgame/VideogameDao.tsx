import { Videogame } from "@/model/logic/videogame";
import { useEffect, useState } from "react";
import IVideogameDao from "./IVideogameDao";

export class VideogameDao implements IVideogameDao{

    /**
     * 
     * @returns 
     * @author Youri Emmanuel
     */
    fetchVideoGames(): Videogame[] {
        const [games, setGames] = useState<Videogame[]>([]);
    
        useEffect(() => {
            fetch('http://127.0.0.1:5000/videogames/all')
                .then(response => response.json())
                .then(data => setGames(data))
                .catch(error => console.error(error));
        }, []);
        return(games);
    }
    
}

