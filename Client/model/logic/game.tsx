import { Player } from "./player";

/**
 * Classe Game
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Game {

    /**
     * Identifiant de la partie
     */
    private _id: number;
    /**
     * Joueurs de la partie
     */
    private _players: Player[];
    /**
     * Identifiant du gagnant de la partie
     */
    private _winner_id: number;

    constructor(id: number, players: Player[], winner_id: number){
        this._id = id;
        this._players = players;
        this._winner_id = winner_id;
    }

    /**
     * Obtenir l'identifiant
     */
    get id():number {return this._id}
    /**
     * Changer l'identifiant
     */
    set id(value: number) {this._id = value}

    /**
     * Obtenir les joueurs
     */
    get players(): Player[] {return this._players}
    /**
     * Changer les joueurs
     */
    set players(value : Player[]) {this._players = value}

    /**
     * Obtenir l'identifiant du gagnant
     */
    get winner_id():number {return this._winner_id}
    /**
     * Changer l'identifiant du gagnant
     */
    set winner_id(value: number) {this._winner_id = value}

};