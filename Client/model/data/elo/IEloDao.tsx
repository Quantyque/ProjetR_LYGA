interface IEloDao<elo> {

    fetchEloHistoryByPlayerID(id: string): Promise<elo>;
    
}

export default IEloDao;