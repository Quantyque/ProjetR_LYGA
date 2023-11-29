import { Player } from "./player";

/**
 * Game class
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Game {

    /**
     * Id  of game
     */
    private _id: number;
    /**
     * Players  of game
     */
    private _players: Player[];
    /**
     * Winner id of game
     */
    private _winner_id: number;

    constructor(id: number, players: Player[], winner_id: number){
        this._id = id;
        this._players = players;
        this._winner_id = winner_id;
    }

    /**
     * Gets id game
     */
    get id():number {return this._id}
    /**
     * Sets id game
     */
    set id(value: number) {this._id = value}

    /**
     * Gets players game
     */
    get players(): Player[] {return this._players}
    /**
     * Sets players game
     */
    set players(value : Player[]) {this._players = value}

    /**
     * Gets winner id game
     */
    get winner_id():number {return this._winner_id}
    /**
     * Sets winner id game
     */
    set winner_id(value: number) {this._winner_id = value}

};