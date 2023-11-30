/**
 * Character class
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Character {

    /**
     * Id  of character
     */
    private _id: number;
    /**
     * Name  of character
     */
    private _name: string;

    constructor(id: number, name: string){
      this._id = id;
      this._name = name;
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
};