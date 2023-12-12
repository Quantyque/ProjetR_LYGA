import { Season } from "@/model/logic/season";
import { SeasonDao } from "@/model/data/season/SeasonDao";
import ISeasonDao from "@/model/data/season/ISeasonDao";

/**
 * Controller des saisons
 * @author Antoine Richard
 */
class seasonController {

    /**
     * Season dao de season controller
     */
    private seasonDao: ISeasonDao;
 
    constructor()  {
        this.seasonDao = new SeasonDao;
    }

    /**
     * Utilise seasonDAO pour obtenir les saisons
     * @returns toutes les saisons
     */
    async getAllSeason(): Promise<Season[]> {
        return await this.seasonDao.fetchAllSeason();
    }
 
}

export default seasonController;