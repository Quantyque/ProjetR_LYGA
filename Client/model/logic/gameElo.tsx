/**
 * Classe GameElo
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class GameElo {

    /**
     * Label de l'Élo du jeu
     */
    private _label: string;
    /**
     * Données de l'Élo du jeu
     */
    private _data: number[];
    /**
     * Couleur de la bordure de l'Élo du jeu
     */
    private _borderColor: string;
    /**
     * Couleur de l'arrière-plan de l'Élo du jeu
     */
    private _backgroundColor: string;

    constructor(label: string, data: number[], borderColor: string, backgroundColor: string){
        this._label = label;
        this._data = data;
        this._borderColor = borderColor;
        this._backgroundColor = backgroundColor;
    }

    /**
     * Obtenir le label
     */
    get label():string {return this._label}
    /**
     * Changer le label
     */
    set label(value : string) {this._label = value}

    /**
     * Obtenir les données
     */
    get data():number[] {return this._data}
    /**
     * Changer les données
     */
    set data(value: number[]) {this._data = value}

    /**
     * Obtenir la couleur de la bordure
     */
    get borderColor():string {return this._borderColor}
    /**
     * Changer la couleur de la bordure
     */
    set borderColor(value: string) {this._borderColor = value}

    /**
     * Obtenir la couleur de l'arrière-plan
     */
    get backgroundColor():string {return this._backgroundColor}
    /**
     * Changer la couleur de l'arrière-plan
     */
    set backgroundColor(value: string) {this._backgroundColor = value}
};