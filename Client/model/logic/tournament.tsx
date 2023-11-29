import { Event } from "./event";

/**
 * Tournament class
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Tournament {

    /**
     * Id  of tournament
     */
    private _id: number;
    /**
     * Name  of tournament
     */
    private _name: string;
    /**
     * Winner id of tournament
     */
    private _winner_id: number;
    /**
     * Owner  of tournament
     */
    private _owner: string;
    /**
     * Lat  of tournament
     */
    private _lat: number;
    /**
     * Lng  of tournament
     */
    private _lng: number;
    /**
     * Events  of tournament
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
     * Gets id tournament
     */
    get id():number {return this._id}
    /**
     * Sets id tournament
     */
    set id(value : number) {this._id = value}

    /**
     * Gets name tournament
     */
    get name(): string {return this._name}
    /**
     * Sets name tournament
     */
    set name(value : string) {this._name = value}

    /**
     * Gets winner id tournament
     */
    get winner_id(): number {return this._winner_id}
    /**
     * Sets winner id tournament
     */
    set winner_id(value : number) {this._winner_id = value}

    /**
     * Gets owner tournament
     */
    get owner(): string {return this._owner}
    /**
     * Sets owner tournament
     */
    set owner(value : string) {this._owner = value}

    /**
     * Gets lat tournament
     */
    get lat():number {return this._lat}
    /**
     * Sets lat tournament
     */
    set lat(value : number) {this._lat = value}

    /**
     * Gets lng tournament
     */
    get lng():number {return this._lng}
    /**
     * Sets lng tournament
     */
    set lng(value : number) {this._lng = value}

    /**
     * Gets events tournament
     */
    get events():Event[] {return this._events}
    /**
     * Sets events tournament
     */
    set events(value : Event[]) {this._events = value}

};