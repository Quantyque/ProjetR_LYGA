import { Videogame } from "@/model/logic/videogame";
import { VideogameDao } from "@/model/data/videogame/VideogameDao";
import IVideogameDao from "@/model/data/videogame/IVideogameDao";

/**
 * Controller des jeux-vidéos
 * @author Antoine Richard
 */
class videogameController {

    /**
     * Videogame dao de videogame controller
     */
    private videogameDao: IVideogameDao;
 
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

    /**
     * Utilse videogameDao pour obtenir touts les jeux-vidéos audités
     * @returns touts les juex-vidéos audités
     */
    async getAuditedVideogames(): Promise<Videogame []>{
        return await this.videogameDao.fetchAuditedVideoGames()
    }

    /**
     * Utilse videogameDao pour ajouter un jeu-vidéo
     * @param videogame jeu-vidéo à ajouter
     * @returns message de confirmation d'ajout du jeu-vidéo
     */
    async addVideogameToBeAudited(videogame: Videogame): Promise<string>{
        return await this.videogameDao.addVideogameToBeAudited(videogame)
    }

    /**
     * Utilse videogameDao pour supprimer un jeu-vidéo audités
     * @param id id du jeu-vidéo à supprimer
     * @returns message de confirmation de suppression du jeu-vidéo
     */
    async deleteAuditedVideogame(id: number): Promise<string>{
        return await this.videogameDao.deleteAuditedVideoGame(id)
    }

}

export default videogameController;