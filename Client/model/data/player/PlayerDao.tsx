import { Player } from "@/model/logic/player";
import { useEffect, useState } from "react";
import IPlayerDao from "./IPlayerDao";
import Sender from "../sender";



export class PlayerDao implements IPlayerDao{

  sender : Sender = new Sender();
  
  /**
   * Récupère toute les informations d'un joueur grâce à son id
   * @param id : Id du joueur à récupérer
   * @returns Les informations du joueur récupérer
   * @author Youri Emmanuel
   */  
  async fetchPlayerByID(id : any): Promise<Player | null>{

    var playerFetched;
    playerFetched = this.sender.POST("player/infos", id)
    console.log(playerFetched)
    return(playerFetched);

  }

  /**
   * Récupère toute les informations de tout les joueurs présent dans la DB
   * @returns Les informations de tout les joueurs dans un tableau d'informations
   * @author Youri Emmanuel
   */  
  async fetchPlayers() : Promise<Player[]>{
    
    var players;
    const requestBody = {
      "videogame_id": 1386,
    };
    players = this.sender.POST("player/all_ranked",requestBody)
    console.log(players)
    return(players);
  }
}
