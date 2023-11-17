import { Player } from "@/model/logic/player";

interface IPlayerDao {

    fetchPlayerByID(id: string): Promise<Player | null>;
    fetchPlayers(): Promise<Player[]>;
    
}

export default IPlayerDao;