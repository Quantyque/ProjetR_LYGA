/**
 * Season class
 * @author Antoine Richard
 */
export class Season {

    /**
     * End date of season
     */
    private _endDate: number;
    /**
     * Id  of season
     */
    private _id: number;
    /**
     * Number  of season
     */
    private _number: number;
    /**
     * Start date of season
     */
    private _startDate: number;

    constructor(endDate: number, id: number, number: number, startDate: number) {
        this._endDate = endDate;
        this._id = id;
        this._number = number;
        this._startDate = startDate;
    }

    /**
     * Gets end date
     */
    get endDate():number {return this._endDate}
    /**
     * Sets end date
     */
    set endDate(value : number) {this._endDate = value}

    /**
     * Gets id
     */
    get id():number {return this._id}
    /**
     * Sets id
     */
    set id(value : number) {this._id = value}

    /**
     * Gets number
     */
    get number():number {return this._number}
    /**
     * Sets number
     */
    set number(value : number) {this._number = value}

    /**
     * Gets start date
     */
    get startDate():number {return this._startDate}
    /**
     * Sets start date
     */
    set startDate(value : number) {this._startDate = value}
}