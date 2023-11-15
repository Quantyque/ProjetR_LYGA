import { Elo } from "@/model/logic/elo";
import { useEffect, useState } from "react";
import IEloDao from "./IEloDao";
import Sender from "../sender";

export class EloDao implements IEloDao {

  sender : Sender = new Sender();

  /**
   * récupère l'historique du joueur grâce à l'id du joueur mis en paramètre
   * @param id : id du joueur
   * @returns Un tableau contenant les élos précedents du joueur
   * @author Youri Emmanuel
   */   
  async fetchEloHistoryByPlayerID(id: any): Promise<Elo | null> {

    var playerEloHistory : Promise<Elo | null>;

    playerEloHistory = this.sender.POST("elo/get-history", id)
    console.log(playerEloHistory)
    return playerEloHistory;
  }
}
