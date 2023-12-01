import { Season } from "@/model/logic/season";
import { SeasonDao } from "@/model/data/season/SeasonDao";
import ISeasonDao from "@/model/data/season/ISeasonDao";

/**
 * Controller of type Season
 * @author Antoine Richard
 */
class seasonController {

    /**
     * Season dao of season controller
     */
    seasonDao: ISeasonDao;
 
    constructor()  {
        this.seasonDao = new SeasonDao;
    }

    /**
     * Use the seasonDAO to get the datas
     * @returns the all seasons
     */
    async getAllSeason(): Promise<Season[]> {
        return await this.seasonDao.fetchAllSeason();
    }
 
}

export default seasonController;