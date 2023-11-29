import { Player } from "@/model/logic/player";
import { useEffect, useState } from "react";
import IPlayerDao from "./IPlayerDao";
import Sender from "../sender";

export class PlayerDao implements IPlayerDao{

  sender : Sender = new Sender();
    
  async fetchPlayerByID(id : any): Promise<Player | null>{

    var playerFetched;
    playerFetched = this.sender.POST("player/infos", id)
    console.log(playerFetched)
    return(playerFetched);

  }

  async fetchPlayersBySeasonIDVideogameID(season_id: any, videogame_id: any) : Promise<Player[]>{
    
    var players;
    const requestBody = {
      "season_id":season_id,
      "videogame_id": videogame_id,
    };
    players = this.sender.POST("player/all_ranked",requestBody)
    console.log(players)
    return(players);
  }

  async fetchAllPlayers(): Promise<Player[]>{

    var players;
    players = this.sender.GET("player/all")
    console.log(players)
    return(players);
  }
}
