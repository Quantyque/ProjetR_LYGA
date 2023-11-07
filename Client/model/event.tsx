import { Set } from "./set";
import { Videogame } from "./videogame";

export type Event = {
    id: number,
    name: string,
    num_entrants: number,
    set: [Set],
    videogame: Videogame
};