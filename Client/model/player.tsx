import { Character } from "./character";
import { Elo } from "./elo";

type EloDictionary = { [key: number]: Elo };

export type Player = {
    id: number,
    name: string,
    prefix: string,
    character: Character,
    elos: EloDictionary,
    images: { [key: string]: string },
    externals_urls: { [key: string]: string },
    isDisqualified: boolean,
    bio:string
};