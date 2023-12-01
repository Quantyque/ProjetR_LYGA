import { Set } from "@/model/logic/set";

interface ISetDao {

    /**
    * Retourne les dernier sets réalisé par le joueur dans ses dernier tournois
    * @param id : Id du joueur
    * @returns Les 3 dernier Sets réaliser par le joueur dans un tableau
    * @author Youri Emmanuel
    */
    fetchSetsByIdPlayer(id: string, page: number): Promise<Set | null>;
    
}

export default ISetDao;