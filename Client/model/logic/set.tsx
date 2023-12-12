import { Game } from "./game";
import { Player } from "./player";

/**
 * Classe Set
 * @author Youri Emmanuel
 * @author Antoine Richard
 */
export class Set {

    /**
     * Identifiant du set
     */
    private _id: number;
    /**
     * Round du set
     */
    private _round: number;
    /**
     * Identifiant du gagnant du set
     */
    private _winner_id: number;
    /**
     * Joueurs du set
     */
    private _players: Player[];
    /**
     * Numéro d'entrants de l'évènement du set
     */
    private _event_nb_entrants: number;
    /**
     * Date du set
     */
    private _date: number;
    /**
     * Partie du set
     */
    private _game: Game;

    constructor(id: number, round: number, winner_id: number, players: Player[], event_nb_entrants:  number, date: number, game: Game){
        this._id = id;
        this._round = round;
        this._winner_id = winner_id;
        this._players = players;
        this._event_nb_entrants = event_nb_entrants;
        this._date = date;
        this._game = game;
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
     * Obtenir le round
     */
    get round():number {return this._round}
    /**
     * Changer le round
     */
    set round(value: number) {this._round = value}

    /**
     * Obtenir les joueurs
     */
    get players():Player[] {return this._players}
    /**
     * Changer les joueurs
     */
    set players(value : Player[]) {this._players = value}

    /**
     * Obtenir l'identifiant du gagnant
     */
    get winner_id():number {return this._winner_id}
    /**
     * Changer l'identifiant du gagnant
     */
    set winner_id(value: number) {this._winner_id = value}

    /**
     * Obtenir le numéro d'entrants de l'évènement
     */
    get event_nb_entrants():number {return this._event_nb_entrants}
    /**
     * Changer le numéro d'entrants de l'évènement
     */
    set event_nb_entrants(value: number) {this._event_nb_entrants = value}

    /**
     * Obtenir la date
     */
    get date():number {return this._date}
    /**
     * Changer la date
     */
    set date(value: number) {this._date = value}

    /**
     * Obtenir le jeu
     */
    get game():Game {return this._game}
    /**
     * Changer le jeu
     */
    set game(value : Game) {this._game = value}

};