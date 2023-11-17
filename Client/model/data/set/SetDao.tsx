import { useEffect, useState } from "react";
import { Set } from '@/model/logic/set';
import ISetDao from "./ISetDao";
import Sender from "../sender";


export class SetDao implements ISetDao{

  sender : Sender = new Sender();

  /**
   * Retourne les dernier sets réalisé par le joueur dans ses dernier tournois
   * @param id : Id du joueur
   * @returns Les 3 dernier Sets réaliser par le joueur dans un tableau
   * @author Youri Emmanuel
   */
  async fetchSetsByIdPlayer(id: any): Promise<Set | null> {

    var LastsetsPlayed;
    LastsetsPlayed = this.sender.POST("sets/player/", id)
    console.log(LastsetsPlayed)
    return(LastsetsPlayed);
  }
}