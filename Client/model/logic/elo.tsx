import { Videogame } from "./videogame";

export type Elo = {
    id: number,
    score: number,
    videogame: Videogame
};

export type GameElo = {
    label: string;
    data: number[];
    borderColor: string;
    backgroundColor: string;
};