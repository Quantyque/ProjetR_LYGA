import { Elo } from "@/model/logic/elo";
import { EloDao } from "@/model/data/elo/EloDao";
import IEloDao from "@/model/data/elo/IEloDao";

/**
 * Controller of type Elo
 * @author Antoine Richard
 */
class eloController {

    /**
     * Elo dao of elo controller
     */
    eloDao: IEloDao;
 
    constructor()  {
        this.eloDao = new EloDao;
    }

    /**
     * Use the eloDAO to get the datas
     * @param id id of the player
     * @returns the elo of the id player
     */
    async getEloHistoryByPlayerID(id: any): Promise<Elo | null> {
        return await this.eloDao.fetchEloHistoryByPlayerID(id)
    }
 
}

export default eloController;