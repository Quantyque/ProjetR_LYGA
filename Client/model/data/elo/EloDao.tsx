import { Elo } from "@/model/logic/elo";
import { useEffect, useState } from "react";
import IEloDao from "./IEloDao";
import Sender from "../sender";

export class EloDao implements IEloDao {

  sender : Sender = new Sender();

  async fetchEloHistoryByPlayerID(id: any): Promise<Elo | null> {

    var playerEloHistory : Promise<Elo | null>;

    playerEloHistory = this.sender.POST("elo/get-history", id)
    console.log(playerEloHistory)
    return playerEloHistory;
  }
}
