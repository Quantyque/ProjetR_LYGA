import { Elo } from "@/model/logic/elo";

interface IEloDao {

    fetchEloHistoryByPlayerID(id: string): Elo | null;
    
}

export default IEloDao;