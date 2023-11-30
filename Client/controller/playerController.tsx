import { Player } from "@/model/logic/player";
import { PlayerDao } from "@/model/data/player/PlayerDao";
import IPlayerDao from "@/model/data/player/IPlayerDao";

/**
 * Controller of type Player
 * @author Antoine Richard
 */
class playerController {

    /**
     * Player dao of player controller
     */
    playerDao: IPlayerDao;
 
    constructor()  {
        this.playerDao = new PlayerDao;
    }

    /**
     * Use the playerDao to get player by id
     * @param id id of the player
     * @returns a player by his id
     */
    async getPlayerByID(id: any): Promise<Player | null>{
        return await this.playerDao.fetchPlayerByID(id)
    }

    /**
     * Use the playerDao to get players by season and videogame
     * @param season_id id of the season
     * @param videogame_id id of the videogame
     * @returns players by season and videogame
     */
    async getPlayersBySeasonIDVideogameID(season_id: any, videogame_id: any): Promise<Player[]>{
        
        return await this.playerDao.fetchPlayersBySeasonIDVideogameID(season_id, videogame_id)
    }

    /**
     * Use the playerDao to get all players
     * @returns all players
     */
    async getAllPlayers(): Promise<Player[]>{
        return await this.playerDao.fetchAllPlayers()
    }
 
}

export default playerController;