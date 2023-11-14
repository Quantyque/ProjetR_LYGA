interface IVideogameDao<videogame> {

    fetchVideoGames(): Promise<videogame[]>;

}

export default IVideogameDao;