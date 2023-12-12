import { Character } from "./character";
import { Elo } from "./elo";

/**
 * Classe Player
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Player {

    /**
     * Identifiant du joueur
     */
    private _id: number;
    /**
     * Nom du joueur
     */
    private _name: string;
    /**
     * Date du joueur
     */
    private _date: string;
    /**
     * Préfix du joueur
     */
    private _prefix: string;
    /**
     * Personnages du joueur
     */
    private _characters: Character[];
    /**
     * Élos du joueur
     */
    private _elos: {[key: number]: Elo};
    /**
     * Images du joueur
     */
    private _images: {[key: string]: string}
    /**
     * URL externes du joueur
     */
    private _externals_urls: {[key: string]: string}
    /**
     * Détermine si le joueur est disqualifié
     */
    private _isDisqualified: boolean;
    /**
     * Biographie du joueur
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
    get name():string {return this._name}
    /**
     * Changer le nom
     */
    set name(value :  string) {this._name = value}

    /**
     * Obtenir la date
     */
    get date(): string {return this._date}
    /**
     * Changer la date
     */
    set date(value : string) {this._date = value}

    /**
     * Obtenir préfix
     */
    get prefix():string {return this._prefix}
    /**
     * Changer préfix
     */
    set prefix(value : string) {this._prefix = value}

    /**
     * Obtenir les joueurs
     */
    get characters():Character[] {return this._characters}
    /**
     * Changer les joueurs
     */
    set characters(value : Character[]) {this._characters = value}

    /**
     * Obtenir l'élo
     */
    get elos():{[key: number]: Elo} {return this._elos}
    /**
     * Changer l'élo
     */
    set elos(value : {[key: number]: Elo}) {this._elos = value}

    /**
     * Obtenir les images
     */
    get images(): {[key: string]: string} {return this._images}
    /**
     * Changer les images
     */
    set images(value : {[key: string]: string}) {this._images = value}

    /**
     * Obtenir les URL externes
     */
    get externals_urls(): {[key: string]: string} {return this._externals_urls}
    /**
     * Changer les URL externes
     */
    set externals_urls(value : {[key: string]: string}) {this._externals_urls = value}

    /**
     * Obtenir la disqualification
     */
    get isDisqualified(): boolean {return this._isDisqualified}
    /**
     * Changer la disqualification
     */
    set isDisqualified(value : boolean) {this._isDisqualified = value}

    /**
     * Obtenir la biographie
     */
    get bio():string {return this._bio}
    /**
     * Changer la biographie
     */
    set bio(value : string) {this._bio = value}

};