import { Elo } from "@/model/logic/elo";
import { EloDao } from "@/model/data/elo/EloDao";
import IEloDao from "@/model/data/elo/IEloDao";

/**
 * Controller des elo
 * @author Antoine Richard
 */
class eloController {

    /**
     * Elo dao de elo controller
     */
    private eloDao: IEloDao;
 
    constructor()  {
        this.eloDao = new EloDao;
    }

    /**
     * Utilise eloDAO pour obtenir les données
     * @param id identifiant du joueur
     * @returns l'elo du joueur
     */
    async getEloHistoryByPlayerID(id: any): Promise<Elo | null> {
        return await this.eloDao.fetchEloHistoryByPlayerID(id)
    }
 
}

export default eloController;