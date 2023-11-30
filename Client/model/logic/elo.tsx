import { Videogame } from "./videogame";

/**
 * Elo class
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Elo {

    /**
     * Id  of elo
     */
    private _id: number;
    /**
     * Score  of elo
     */
    private _score: number;
    /**
     * Videogame  of elo
     */
    private _videogame: Videogame;

    constructor(id: number, score: number, videogame:Videogame){
        this._id = id;
        this._score = score;
        this._videogame = videogame;
    }

    /**
     * Gets id
     */
    get id():number {return this._id}
    /**
     * Sets id
     */
    set id(value: number) {this._id = value}

    /**
     * Gets score
     */
    get score():number {return this._score}
    /**
     * Sets score
     */
    set score(value: number) {this._score = value}

    /**
     * Gets videogame
     */
    get videogame():Videogame {return this._videogame}
    /**
     * Sets videogame
     */
    set videogame(value : Videogame) {this._videogame = value}

};