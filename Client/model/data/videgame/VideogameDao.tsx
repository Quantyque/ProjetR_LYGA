import { Videogame } from "@/model/logic/videogame";
import { useEffect, useState } from "react";
import IVideogameDao from "./IVideogameDao";
import Sender from "../sender";

export class VideogameDao implements IVideogameDao{

    sender : Sender = new Sender();

    async fetchVideoGames(): Promise<Videogame[]> {

        var Allgames;
        Allgames = this.sender.GET("videogames/all")
        console.log(Allgames)
        return(Allgames);
    }
    
}

