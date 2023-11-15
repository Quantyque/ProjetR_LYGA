import { Videogame } from "@/model/logic/videogame";

interface IVideogameDao {

    fetchVideoGames(): Promise<Videogame[]>;

}

export default IVideogameDao;