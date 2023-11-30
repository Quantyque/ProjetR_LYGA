import IRankingDao from "@/model/data/ranking/IRankingDao";
import Sender from "@/model/data/sender";


export class SetDao implements IRankingDao{

    sender : Sender = new Sender();

    /**
     * Convertit une date en timestamp unix.
     * @param date La date à convertir.
     * @returns Le timestamp unix.
     */
    private dateToUnixTimestamp(date: Date): number {

        return Math.round(date.getTime() / 1000);
        
    }


    /**
     * Active ou désactive l'actualisation automatique du classement.
     * @param status true pour activer, false pour désactiver.
     * @param afterDate La date après laquelle le classement sera actualisé.
     * @param beforeDate La date avant laquelle le classement sera actualisé.
     * @param videoGameId L'identifiant du jeu vidéo à actualiser.
     * @param coordonnees Les coordonnées du centre de la zone dans laquelle le classement sera actualisé => [latitude, longitude].
     * @param distance La distance en kilomètres à partir du centre de la zone dans laquelle le classement sera actualisé.
     * @returns Une promesse avec le résultat de l'opération.
     */
    async autoRefresh(status: boolean, afterDate: Date, beforeDate: Date, videoGameId : number, coordonnees: [number, number], distance: number): Promise<string>{

        const result = await this.sender.POST("/rankings/parameters/auto-refresh", 
        {

            activate: status, 
            afterDate: this.dateToUnixTimestamp(afterDate),
            beforeDate: this.dateToUnixTimestamp(beforeDate),
            videogameId: videoGameId,
            coordonnees: coordonnees.join(', '),
            distance: `${distance}km`

        });

        return result;

    }

    /**
     * Effectue une actualisation manuelle du classement.
     * @param afterDate La date après laquelle le classement sera actualisé.
     * @param beforeDate La date avant laquelle le classement sera actualisé.
     * @param videoGameId L'identifiant du jeu vidéo à actualiser.
     * @param coordonnees Les coordonnées du centre de la zone dans laquelle le classement sera actualisé => [latitude, longitude].
     * @param distance La distance en kilomètres à partir du centre de la zone dans laquelle le classement sera actualisé.
     * @returns Une promesse avec le résultat de l'opération.
     */
    async manualRefresh(afterDate: Date, beforeDate: Date, videoGameId : number, coordonnees: [number, number], distance: number): Promise<string>{

        const result = await this.sender.POST("/rankings/update", 
        {

            afterDate: this.dateToUnixTimestamp(afterDate),
            beforeDate: this.dateToUnixTimestamp(beforeDate),
            videogameId: videoGameId,
            coordonnees: coordonnees.join(', '),
            distance: `${distance}km` 

        });

        return result;

    }
}