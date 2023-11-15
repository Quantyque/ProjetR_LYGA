import { Player } from "@/model/logic/player";

interface IPlayerDao {

    fetchPlayerByID(id: string): Player | null;
    fetchPlayers(): Player[];
    
}

export default IPlayerDao;