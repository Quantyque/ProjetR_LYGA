import { Set } from "@/model/logic/set";

interface ISetDao {

    fetchSetsByIdPlayer(id: string): Set | null;
    
}

export default ISetDao;