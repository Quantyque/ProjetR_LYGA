import { Player } from "@/model/logic/player";

interface IPlayerDao {

    /**
    * Récupère toute les informations d'un joueur grâce à son id
    * @param id : Id du joueur à récupérer
    * @returns Les informations du joueur récupérer
    * @author Youri Emmanuel
    */
    fetchPlayerByID(id: string): Promise<Player | null>;

    /**
    * Récupère toute les informations de tout les joueurs présent dans la DB
    * @param season_id id of the season
    * @param videogame_id id of the videogame
    * @returns Les informations de tout les joueurs dans un tableau d'informations
    * @author Youri Emmanuel
    */  
    fetchPlayers(season_id: any, videogame_id: any): Promise<Player[]>;
    
}

export default IPlayerDao;