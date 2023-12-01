import { useEffect, useState } from "react";
import { Season } from '@/model/logic/season';
import ISeasonDao from "./ISeasonDao";
import Sender from "../sender";


export class SeasonDao implements ISeasonDao{

  sender : Sender = new Sender();
  
    async fetchAllSeason(): Promise<Season[]> {

    var season;
    season = this.sender.GET("season/all")
    console.log(season)
    return(season);
  }
}