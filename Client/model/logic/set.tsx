import { Game } from "./game";
import { Player } from "./player";

/**
 * Set class
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Set {

    /**
     * Id  of set
     */
    private _id: number;
    /**
     * Round  of set
     */
    private _round: number;
    /**
     * Winner id of set
     */
    private _winner_id: number;
    /**
     * Players  of set
     */
    private _players: Player[];
    /**
     * Event nb entrants of set
     */
    private _event_nb_entrants: number;
    /**
     * Date  of set
     */
    private _date: number;
    /**
     * Game  of set
     */
    private _game: Game;

    constructor(id: number, round: number, winner_id: number, players: Player[], event_nb_entrants:  number, date: number, game: Game){
        this._id = id;
        this._round = round;
        this._winner_id = winner_id;
        this._players = players;
        this._event_nb_entrants = event_nb_entrants;
        this._date = date;
        this._game = game;
    }

    /**
     * Gets id set
     */
    get id():number {return this._id}
    /**
     * Sets id set
     */
    set id(value: number) {this._id = value}

    /**
     * Gets round set
     */
    get round():number {return this._round}
    /**
     * Sets round set
     */
    set round(value: number) {this._round = value}

    /**
     * Gets players set
     */
    get players():Player[] {return this._players}
    /**
     * Sets players set
     */
    set players(value : Player[]) {this._players = value}

    /**
     * Gets winner id set
     */
    get winner_id():number {return this._winner_id}
    /**
     * Sets winner id set
     */
    set winner_id(value: number) {this._winner_id = value}

    /**
     * Gets event nb entrants set
     */
    get event_nb_entrants():number {return this._event_nb_entrants}
    /**
     * Sets event nb entrants set
     */
    set event_nb_entrants(value: number) {this._event_nb_entrants = value}

    /**
     * Gets date set
     */
    get date():number {return this._date}
    /**
     * Sets date set
     */
    set date(value: number) {this._date = value}

    /**
     * Gets game set
     */
    get game():Game {return this._game}
    
    set game(value : Game) {this._game = value}

};