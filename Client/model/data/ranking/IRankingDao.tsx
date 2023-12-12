interface IRankingDao {

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
    autoRefresh(status: boolean, afterDate: Date, beforeDate: Date, videoGameId : number, coordonnees: [number, number], distance: number): Promise<string>;

    /**
     * Effectue une actualisation manuelle du classement.
     * @param afterDate La date après laquelle le classement sera actualisé.
     * @param beforeDate La date avant laquelle le classement sera actualisé.
     * @param videoGameId L'identifiant du jeu vidéo à actualiser.
     * @param coordonnees Les coordonnées du centre de la zone dans laquelle le classement sera actualisé => [latitude, longitude].
     * @param distance La distance en kilomètres à partir du centre de la zone dans laquelle le classement sera actualisé.
     * @returns Une promesse avec le résultat de l'opération.
     */
    manualRefresh(afterDate: Date, beforeDate: Date, videoGameId : number, coordonnees: [number, number], distance: number): Promise<string>;
    
}

export default IRankingDao;