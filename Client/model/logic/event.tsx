import { Set } from "./set";
import { Videogame } from "./videogame";

/**
 * Classe Event
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Event {

    /**
     * Identifiant d'un évènement
     */
    private _id: number;
    /**
     * Nom d'un évènement
     */
    private _name: string;
    /**
     * Numéro d'entrants d'un évènement
     */
    private _num_entrants: number;
    /**
     * Changer d'un évènement
     */
    private _sets: Set[];
    /**
     * Jeu-vidéo d'un évènement
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
     * Obtenir l'identifiant
     */
    get id():number {return this._id}
    /**
     * Changer l'identifiant
     */
    set id(value: number) {this._id = value}

    /**
     * Obtenir le nom
     */
    get name():string {return this._name}
    /**
     * Changer le nom
     */
    set name(value : string) {this._name = value}

    /**
     * Obtenir le numéro d'enrants
     */
    get num_entrants():number {return this._num_entrants}
    /**
     * Changer le numéro d'enrants
     */
    set num_entrants(value : number) {this._num_entrants = value}

    /**
     * Obtenir les sets
     */
    get sets():Set[] {return this._sets}
    /**
     * Changer les sets
     */
    set sets(value : Set[]) {this._sets = value}

    /**
     * Obtenir le jeu-vidéo
     */
    get videogame():Videogame {return this._videogame}
    /**
     * Changer le jeu-vidéo
     */
    set videogame(value : Videogame) {this._videogame = value}

};