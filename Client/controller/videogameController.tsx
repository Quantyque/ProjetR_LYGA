import { Videogame } from "@/model/logic/videogame";
import { VideogameDao } from "@/model/data/videogame/VideogameDao";
import IVideogameDao from "@/model/data/videogame/IVideogameDao";

/**
 * Controller of type Videogame
 * @author Antoine Richard
 */
class videogameController {

    /**
     * Videogame dao of videogame controller
     */
    videogameDao: IVideogameDao;
 
    constructor()  {
        this.videogameDao = new VideogameDao;
    }

    /**
     * Use the videogameDao to get videogames
     * @returns all videogames
     */
    async getVideogames(): Promise<Videogame []>{
        return await this.videogameDao.fetchVideoGames()
    }

}

export default videogameController;