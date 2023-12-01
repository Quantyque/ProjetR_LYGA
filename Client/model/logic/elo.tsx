import { Videogame } from "./videogame";

/**
 * Classe Elo
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Elo {

    /**
     * Identifiant de l'Élo
     */
    private _id: number;
    /**
     * Score de l'Élo
     */
    private _score: number;
    /**
     * Jeu-vidéo de l'Élo
     */
    private _videogame: Videogame;

    constructor(id: number, score: number, videogame:Videogame){
        this._id = id;
        this._score = score;
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
     * Obtenir le score
     */
    get score():number {return this._score}
    /**
     * Changer le score
     */
    set score(value: number) {this._score = value}

    /**
     * Obtenir le jeu-vidéo
     */
    get videogame():Videogame {return this._videogame}
    /**
     * Changerle jeu-vidéo
     */
    set videogame(value : Videogame) {this._videogame = value}

};