import { Videogame } from "@/model/logic/videogame";
import { useEffect, useState } from "react";
import IVideogameDao from "./IVideogameDao";
import Sender from "../sender";

export class VideogameDao implements IVideogameDao{

    sender : Sender = new Sender();

    /**
     * Retourne un tableau contenant toute la liste des jeux video
     * @returns un tableau d'objet videogame
     * @author Antoine Richard
     */
    async fetchVideoGames(): Promise<Videogame[]> {

        var Allgames;
        Allgames = this.sender.GET("videogames/all")
        console.log(Allgames)
        return(Allgames);
    }

    /**
     * Retourne un tableau contenant toute la liste des jeux video audités
     * @returns un tableau d'objet videogame audités
    */
    async fetchAuditedVideoGames(): Promise<Videogame[]> {

        var Allgames;
        Allgames = this.sender.GET("videogames/audited")
        return(Allgames);

    }
    
}

