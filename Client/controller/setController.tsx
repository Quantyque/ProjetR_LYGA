import { Set } from "@/model/logic/set";
import { SetDao } from "@/model/data/set/SetDao";
import ISetDao from "@/model/data/set/ISetDao";

/**
 * Controller de type Set
 * @author Antoine Richard
 */
class setController {

    /**
     * Set dao de set controller
     */
    setDao: ISetDao;
 
    constructor()  {
        this.setDao = new SetDao;
    }

    /**
     * Utilse setDao pour obtenir un set par l'identifiant d'un joueur
     * @param id identifiant du joueur
     * @returns un set par joueur
     */
    async getSetByID(id: any, page:any): Promise<Set | null>{
        return await this.setDao.fetchSetsByIdPlayer(id,page)
    }

}

export default setController;