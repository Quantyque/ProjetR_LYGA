import { Event } from "./event";

export type Tournament = {
    id: number,
    name: string,
    winner_id: string,
    owner: string,
    lat:number,
    lng:number,
    events:[Event]
};