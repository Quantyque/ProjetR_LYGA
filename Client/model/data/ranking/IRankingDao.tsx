interface IRankingDao {

    /**
     * Activates or deactivates the automatic refresh of the ranking.
     * @param status true to activate, false to deactivate.*
     * @returns a promise with the result of the operation.
     */
    autoRefresh(status: boolean, videoGameId: number): Promise<string>;

    /**
     * Do a manual refresh of a ranking.
     * @param videoGameId the id of the video game to refresh.
     * @returns a promise with the result of the operation.
     */
    manualRefresh(videoGameId : number): Promise<string>;
    
}

export default IRankingDao;