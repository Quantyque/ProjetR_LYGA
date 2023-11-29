import { Set } from "./set";
import { Videogame } from "./videogame";

/**
 * Event class
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Event {

    /**
     * Id  of event
     */
    private _id: number;
    /**
     * Name  of event
     */
    private _name: string;
    /**
     * Num entrants of event
     */
    private _num_entrants: number;
    /**
     * Sets  of event
     */
    private _sets: Set[];
    /**
     * Videogame  of event
     */
    private _videogame: Videogame;

    constructor(id:number, name:string, num_entrants: number, sets: Set[], videogame: Videogame){
        this._id = id;
        this._name = name;
        this._num_entrants = num_entrants;
        this._sets = sets;
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
     * Gets name
     */
    get name():string {return this._name}
    /**
     * Sets name
     */
    set name(value : string) {this._name = value}

    /**
     * Gets num entrants
     */
    get num_entrants():number {return this._num_entrants}
    /**
     * Sets num entrants
     */
    set num_entrants(value : number) {this._num_entrants = value}

    /**
     * Gets sets
     */
    get sets():Set[] {return this._sets}
    /**
     * Sets sets
     */
    set sets(value : Set[]) {this._sets = value}

    /**
     * Gets videogame
     */
    get videogame():Videogame {return this._videogame}
    /**
     * Sets videogame
     */
    set videogame(value : Videogame) {this._videogame = value}

};