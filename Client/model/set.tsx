import { Game } from "./game";
import { Player } from "./player";

export type Set = {
    id: number,
    round: number,
    winner_id: number,
    players: [Player],
    event_nb_entrants:number,
    date:number,
    game:Game
};