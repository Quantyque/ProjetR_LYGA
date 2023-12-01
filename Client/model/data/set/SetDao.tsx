import { useEffect, useState } from "react";
import { Set } from '@/model/logic/set';
import ISetDao from "./ISetDao";
import Sender from "../sender";


export class SetDao implements ISetDao{

  sender : Sender = new Sender();
  
  async fetchSetsByIdPlayer(id: any, page: any): Promise<Set | null> {

    var LastsetsPlayed;
    LastsetsPlayed = this.sender.POST("sets/player", { ...id, ...page })
    console.log(LastsetsPlayed)
    return(LastsetsPlayed);
  }
}