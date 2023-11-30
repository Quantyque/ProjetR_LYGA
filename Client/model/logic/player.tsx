import { Character } from "./character";
import { Elo } from "./elo";

/**
 * Player class
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Player {

    /**
     * Id  of player
     */
    private _id: number;
    /**
     * Name  of player
     */
    private _name: string;
    /**
     * Date  of player
     */
    private _date: string;
    /**
     * Prefix  of player
     */
    private _prefix: string;
    /**
     * Characters  of player
     */
    private _characters: Character[];
    /**
     * Elos  of player
     */
    private _elos: {[key: number]: Elo};
    /**
     * Images  of player
     */
    private _images: {[key: string]: string}
    /**
     * Externals urls of player
     */
    private _externals_urls: {[key: string]: string}
    /**
     * Determines whether disqualified is
     */
    private _isDisqualified: boolean;
    /**
     * Bio  of player
     */
    private _bio: string;

    constructor(id: number,
                name: string,
                date: string,
                prefix: string, 
                characters: Character[],
                elos: {[key: number]: Elo},
                images :{[key: string]: string},
                externals_urls: {[key: string]: string},
                isDisqualified: boolean,
                bio: string){

                this._id = id;
                this._name = name;
                this._date = date;
                this._prefix = prefix;
                this._characters = characters;
                this._elos = elos;
                this._images = images;
                this._externals_urls = externals_urls;
                this._isDisqualified = isDisqualified;
                this._bio = bio;
            }

    /**
     * Gets id player
     */
    get id():number {return this._id}
    /**
     * Sets id player
     */
    set id(value : number) {this._id = value}

    /**
     * Gets name player
     */
    get name():string {return this._name}
    /**
     * Sets name player
     */
    set name(value :  string) {this._name = value}

    /**
     * Gets date player
     */
    get date(): string {return this._date}
    /**
     * Sets date player
     */
    set date(value : string) {this._date = value}

    /**
     * Gets prefix player
     */
    get prefix():string {return this._prefix}
    /**
     * Sets prefix player
     */
    set prefix(value : string) {this._prefix = value}

    /**
     * Gets characters player
     */
    get characters():Character[] {return this._characters}
    /**
     * Sets characters player
     */
    set characters(value : Character[]) {this._characters = value}

    /**
     * Gets elo player
     */
    get elos():{[key: number]: Elo} {return this._elos}
    /**
     * Sets elo player
     */
    set elos(value : {[key: number]: Elo}) {this._elos = value}

    /**
     * Gets images player
     */
    get images(): {[key: string]: string} {return this._images}
    /**
     * Sets images player
     */
    set images(value : {[key: string]: string}) {this._images = value}

    /**
     * Gets externals urls player
     */
    get externals_urls(): {[key: string]: string} {return this._externals_urls}
    /**
     * Sets externals urls player
     */
    set externals_urls(value : {[key: string]: string}) {this._externals_urls = value}

    /**
     * Gets whether is disqualified player
     */
    get isDisqualified(): boolean {return this._isDisqualified}
    /**
     * Sets whether is disqualified player
     */
    set isDisqualified(value : boolean) {this._isDisqualified = value}

    /**
     * Gets bio player
     */
    get bio():string {return this._bio}
    /**
     * Sets bio player
     */
    set bio(value : string) {this._bio = value}

};