import { Videogame } from "@/model/logic/videogame";

interface IVideogameDao {

    /**
     * Retourne un tableau contenant toute la liste des jeux video
     * @returns un tableau d'objet videogame
     * @author Antoine Richard
    */
    fetchVideoGames(): Promise<Videogame[]>;

    /**
     * Retourne un tableau contenant toute la liste des jeux video audités
     * @returns un tableau d'objet videogame audités
    */
    fetchAuditedVideoGames(): Promise<Videogame[]>;

    /**
     * Ajoute un jeu video
     * @param videogame jeu video à ajouter
     * @returns un message de confirmation d'ajout du jeu video
    */
    addVideogameToBeAudited(videogame: Videogame): Promise<string>;

    /**
     * Supprime un jeu video audités
     * @param id id du jeu video à supprimer
     * @returns un message de confirmation de suppression du jeu video
    */
    deleteAuditedVideoGame(id: number): Promise<string>;

}

export default IVideogameDao;