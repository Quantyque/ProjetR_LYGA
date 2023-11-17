import { Character } from "./character";
import { Elo } from "./elo";

type EloDictionary = { [key: number]: Elo };

export type Player = {
    id: number,
    name: string,
    date:string,
    prefix: string,
    character: {    
        id: number | null;
        name: string | null;
    },
    elos: EloDictionary,
    images: { [key: string]: string },
    externals_urls: { [key: string]: string },
    isDisqualified: boolean,
    bio:string
};