/**
 * Game Elo class
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class GameElo {

    /**
     * Label  of game elo
     */
    private _label: string;
    /**
     * Data  of game elo
     */
    private _data: number[];
    /**
     * Border color of game elo
     */
    private _borderColor: string;
    /**
     * Background color of game elo
     */
    private _backgroundColor: string;

    constructor(label: string, data: number[], borderColor: string, backgroundColor: string){
        this._label = label;
        this._data = data;
        this._borderColor = borderColor;
        this._backgroundColor = backgroundColor;
    }

    /**
     * Gets label
     */
    get label():string {return this._label}
    /**
     * Sets label
     */
    set label(value : string) {this._label = value}

    /**
     * Gets data
     */
    get data():number[] {return this._data}
    /**
     * Sets data
     */
    set data(value: number[]) {this._data = value}

    /**
     * Gets border color
     */
    get borderColor():string {return this._borderColor}
    /**
     * Sets border color
     */
    set borderColor(value: string) {this._borderColor = value}

    /**
     * Gets background color
     */
    get backgroundColor():string {return this._backgroundColor}
    /**
     * Sets background color
     */
    set backgroundColor(value: string) {this._backgroundColor = value}
};