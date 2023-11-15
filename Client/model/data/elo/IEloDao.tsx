import { Elo } from "@/model/logic/elo";

interface IEloDao {

    fetchEloHistoryByPlayerID(id: string): Promise<Elo | null> ;
    
}

export default IEloDao;