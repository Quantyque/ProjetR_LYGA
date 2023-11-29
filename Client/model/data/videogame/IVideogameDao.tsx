import { Videogame } from "@/model/logic/videogame";

interface IVideogameDao {

    /**
    * Retourne un tableau contenant toute la liste des jeux video
    * @returns un tableau d'objet videogame
    * @author Antoine Richard
    */
    fetchVideoGames(): Promise<Videogame[]>;

}

export default IVideogameDao;