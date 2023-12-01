import { Player } from "@/model/logic/player";
import { PlayerDao } from "@/model/data/player/PlayerDao";
import IPlayerDao from "@/model/data/player/IPlayerDao";

/**
 * Controller de type Player
 * @author Antoine Richard
 */
class playerController {

    /**
     * Player dao de player controller
     */
    playerDao: IPlayerDao;
 
    constructor()  {
        this.playerDao = new PlayerDao;
    }

    /**
     * Utilise playerDao pour avoir un joueur par son identifiant
     * @param id identifiant du joueur
     * @returns un joueur par son identifiant
     */
    async getPlayerByID(id: any): Promise<Player | null>{
        return await this.playerDao.fetchPlayerByID(id)
    }

    /**
     * Utilise playerDao pour avoir des joueurs par saison et pas jeu-vidéo
     * @param season_id identifiant de la saison
     * @param videogame_id identifiant du jeu-vidéo
     * @returns les joueurs par saison et par jeu-vidéo
     */
    async getPlayersBySeasonIDVideogameID(season_id: any, videogame_id: any): Promise<Player[]>{
        
        return await this.playerDao.fetchPlayersBySeasonIDVideogameID(season_id, videogame_id)
    }

    /**
     * Utilise playerDao pour avoir tout les joueurs
     * @returns tout les joueurs
     */
    async getAllPlayers(): Promise<Player[]>{
        return await this.playerDao.fetchAllPlayers()
    }
 
}

export default playerController;