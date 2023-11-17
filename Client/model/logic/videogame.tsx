import { Character } from "./character";

export type Videogame = {
    id: number,
    name: string,
    characters: Character[],
    images:string[]
};