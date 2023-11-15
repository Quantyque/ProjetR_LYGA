import { Set } from "@/model/logic/set";

interface ISetDao {

    fetchSetsByIdPlayer(id: string): Promise<Set | null>;
    
}

export default ISetDao;