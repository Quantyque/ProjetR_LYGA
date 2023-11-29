import { Character } from "./character";

/**
 * Videogame class
 * @author Youri Emmanuel
 * @author Antoine Ricahrd
 */
export class Videogame {

    /**
     * Id  of videogame
     */
    private _id: number;
    /**
     * Name  of videogame
     */
    private _name: string;
    /**
     * Characters  of videogame
     */
    private _characters: Character[];
    /**
     * Image  of videogame
     */
    private _image: string;

    constructor(id: number, name: string, characters: Character[], image: string){
        this._id = id;
        this._name = name;
        this._characters = characters;
        this._image = image;
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
    set name(value: string) {this._name = value}

    /**
     * Gets characters
     */
    get characters():Character[] {return this._characters}
    /**
     * Sets characters
     */
    set characters(value: Character[]) {this._characters = value}

    /**
     * Gets image
     */
    get image():string {return this._image}
    /**
     * Sets image
     */
    set image(value: string) {this._image = value}
};