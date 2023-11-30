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
    * Récupère les joueurs d'une saison et d'un jeu
    * @param season_id id of the season
    * @param videogame_id id of the videogame
    * @returns Les informations de tout les joueurs dans un tableau d'informations
    * @author Youri Emmanuel
    */  
    fetchPlayersBySeasonIDVideogameID(season_id: any, videogame_id: any): Promise<Player[]>;
    
    /**
     * Récupère toute les informations de tout les joueurs présent dans la DB
     * @returns Les informations de tout les joueurs dans un tableau d'informations
     * @author Antoine Richard
     */
    fetchAllPlayers(): Promise<Player[]>;
}

export default IPlayerDao;