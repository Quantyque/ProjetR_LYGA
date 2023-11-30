import { Set } from "@/model/logic/set";
import { SetDao } from "@/model/data/set/SetDao";
import ISetDao from "@/model/data/set/ISetDao";

/**
 * Controller of type Set
 * @author Antoine Richard
 */
class setController {

    /**
     * Set dao of set controller
     */
    setDao: ISetDao;
 
    constructor()  {
        this.setDao = new SetDao;
    }

    /**
     * Use the setDao to get set by id of player
     * @param id id of the player
     * @returns a set by id player
     */
    async getSetByID(id: string): Promise<Set | null>{
        return await this.setDao.fetchSetsByIdPlayer(id)
    }

}

export default setController;