/**
 * Classe Season
 * @author Antoine Richard
 */
export class Season {

    /**
     * Date de fin de la saison
     */
    private _endDate: number;
    /**
     * Identifiant de la saison
     */
    private _id: number;
    /**
     * Numéro de la saison
     */
    private _number: number;
    /**
     * Date de début de la saison
     */
    private _startDate: number;

    constructor(endDate: number, id: number, number: number, startDate: number) {
        this._endDate = endDate;
        this._id = id;
        this._number = number;
        this._startDate = startDate;
    }

    /**
     * Obtenir la date de fin
     */
    get endDate():number {return this._endDate}
    /**
     * Changer la date de fin
     */
    set endDate(value : number) {this._endDate = value}

    /**
     * Obtenir l'identifiant
     */
    get id():number {return this._id}
    /**
     * Changer l'identifiant
     */
    set id(value : number) {this._id = value}

    /**
     * Obtenir le numéro
     */
    get number():number {return this._number}
    /**
     * Changer le numéro
     */
    set number(value : number) {this._number = value}

    /**
     * Obtenir la date de début
     */
    get startDate():number {return this._startDate}
    /**
     * Changer la date de début
     */
    set startDate(value : number) {this._startDate = value}
}