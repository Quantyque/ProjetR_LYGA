interface ISetDao<set> {

    fetchSetsByIdPlayer(id: string): Promise<set>;
    
}

export default ISetDao;