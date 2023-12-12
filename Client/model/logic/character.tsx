/**
 * Classe Character
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Character {

    /**
     * Identifiant du personnage
     */
    private _id: number;
    /**
     * Nom du personnage
     */
    private _name: string;

    constructor(id: number, name: string){
      this._id = id;
      this._name = name;
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
    set name(value: string) {this._name = value}
};