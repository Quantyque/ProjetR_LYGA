import { Videogame } from "@/model/logic/videogame";

interface IVideogameDao {

    fetchVideoGames(): Videogame[];

}

export default IVideogameDao;