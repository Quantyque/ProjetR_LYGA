import { Elo } from "@/model/logic/elo";

interface IEloDao {

    /**
    * récupère l'historique du joueur grâce à l'id du joueur mis en paramètre
    * @param id : id du joueur
    * @returns Un tableau contenant les élos précedents du joueur
    * @author Youri Emmanuel
    */   
    fetchEloHistoryByPlayerID(id: string): Promise<Elo | null> ;
    
}

export default IEloDao;