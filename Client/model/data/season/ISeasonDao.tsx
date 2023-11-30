import { Season } from "@/model/logic/season";

interface ISeasonDao {

    /**
    * Retourne les saisons
    * @returns Les 3 dernier Sets réaliser par le joueur dans un tableau
    * @author Antoine Richard
    */
    fetchAllSeason(): Promise<Season[]>;
    
}

export default ISeasonDao;