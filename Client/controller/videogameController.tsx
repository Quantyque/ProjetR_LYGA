import { Videogame } from "@/model/logic/videogame";
import { VideogameDao } from "@/model/data/videogame/VideogameDao";
import IVideogameDao from "@/model/data/videogame/IVideogameDao";

/**
 * Controller de type Videogame
 * @author Antoine Richard
 */
class videogameController {

    /**
     * Videogame dao de videogame controller
     */
    videogameDao: IVideogameDao;
 
    constructor()  {
        this.videogameDao = new VideogameDao;
    }

    /**
     * Utilse videogameDao pour obtenir touts les jeux-vidéos
     * @returns touts les juex-vidéos
     */
    async getVideogames(): Promise<Videogame []>{
        return await this.videogameDao.fetchVideoGames()
    }

}

export default videogameController;