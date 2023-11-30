import { useEffect, useState } from "react";
import { Set } from '@/model/logic/set';
import ISetDao from "./ISetDao";
import Sender from "../sender";


export class SetDao implements ISetDao{

  sender : Sender = new Sender();
  
  async fetchSetsByIdPlayer(id: any): Promise<Set | null> {

    var LastsetsPlayed;
    LastsetsPlayed = this.sender.POST("sets/player/", id)
    console.log(LastsetsPlayed)
    return(LastsetsPlayed);
  }
}