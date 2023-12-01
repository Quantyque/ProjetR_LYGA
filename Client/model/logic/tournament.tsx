import { Event } from "./event";

/**
 * Classe Tournament
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Tournament {

    /**
     * Identifiant du tournois
     */
    private _id: number;
    /**
     * Nom du tournois
     */
    private _name: string;
    /**
     * Identifiant du gagant du tournois
     */
    private _winner_id: number;
    /**
     * Propriétaire du tournois
     */
    private _owner: string;
    /**
     * Lat du tournois
     */
    private _lat: number;
    /**
     * Lng du tournois
     */
    private _lng: number;
    /**
     * Évènements du tournois
     */
    private _events: Event[];

    constructor(id: number, name: string, winner_id: number, owner: string, lat: number, lng : number, events : Event[]){
        this._id = id;
        this._name = name;
        this._winner_id = winner_id;
        this._owner = owner;
        this._lat = lat;
        this._lng = lng;
        this._events = events;
    }

    /**
     * Obtenir l'identifiant
     */
    get id():number {return this._id}
    /**
     * Changer l'identifiant
     */
    set id(value : number) {this._id = value}

    /**
     * Obtenir le nom
     */
    get name(): string {return this._name}
    /**
     * Changer le nom
     */
    set name(value : string) {this._name = value}

    /**
     * Obtenir l'identifant du gagnant
     */
    get winner_id(): number {return this._winner_id}
    /**
     * Changer l'identifant du gagnant
     */
    set winner_id(value : number) {this._winner_id = value}

    /**
     * Obtenir le propriétaire
     */
    get owner(): string {return this._owner}
    /**
     * Changer le propriétaire
     */
    set owner(value : string) {this._owner = value}

    /**
     * Obtenir le lat
     */
    get lat():number {return this._lat}
    /**
     * Changer le lat
     */
    set lat(value : number) {this._lat = value}

    /**
     * Obtenir le lng
     */
    get lng():number {return this._lng}
    /**
     * Changer le lng
     */
    set lng(value : number) {this._lng = value}

    /**
     * Obtenir les évènements
     */
    get events():Event[] {return this._events}
    /**
     * Changer les évènements
     */
    set events(value : Event[]) {this._events = value}

};