import { Character } from "./character";

/**
 * Classe Videogame
 * @author Youri Emmanuel
 * @author Antoine Ricahrd
 */
export class Videogame {

    /**
     * Identifiant du jeu-vidéo
     */
    private _id: number;
    /**
     * Nom du jeu-vidéo
     */
    private _name: string;
    /**
     * Personnages du jeu-vidéo
     */
    private _characters: Character[];
    /**
     * Image du jeu-vidéo
     */
    private _image: string;

    constructor(id: number, name: string, characters: Character[], image: string){
        this._id = id;
        this._name = name;
        this._characters = characters;
        this._image = image;
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

    /**
     * Obtenir les joueurs
     */
    get characters():Character[] {return this._characters}
    /**
     * Changer les joueurs
     */
    set characters(value: Character[]) {this._characters = value}

    /**
     * Obtenir l'image
     */
    get image():string {return this._image}
    /**
     * Changer l'image
     */
    set image(value: string) {this._image = value}
};