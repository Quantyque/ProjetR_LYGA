import { Player } from "./player";

export type Game = {
    id: number,
    player: [Player],
    winner_id: number
};