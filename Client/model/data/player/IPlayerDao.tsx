interface IPlayerDao<player> {

    fetchPlayerByID(id: string): Promise<player>;
    fetchPlayers(): Promise<player[]>;
    
}

export default IPlayerDao;