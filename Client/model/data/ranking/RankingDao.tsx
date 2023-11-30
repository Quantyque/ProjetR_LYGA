import IRankingDao from "@/model/data/ranking/IRankingDao";
import Sender from "@/model/data/sender";


export class SetDao implements IRankingDao{

  sender : Sender = new Sender();

    /**
     * Activates or deactivates the automatic refresh of the ranking.
     * @param status true to activate, false to deactivate.*
     * @returns a promise with the result of the operation.
     */
    async autoRefresh(status: boolean, videoGameId: number): Promise<string>{

        const result = await this.sender.POST("http://localhost:8080/api/ranking/autorefresh", {activate: status, id: videoGameId});
        return result;

    }

    /**
     * Do a manual refresh of a ranking.
     * @param videoGameId the id of the video game to refresh.
     * @returns a promise with the result of the operation.
     */
    async manualRefresh(videoGameId : number): Promise<string>{

        const result = await this.sender.POST("http://localhost:8080/api/ranking/manualrefresh", {id: videoGameId});
        return result;

    }
}