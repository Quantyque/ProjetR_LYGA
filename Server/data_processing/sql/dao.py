from data_processing.sql.idatabase import IDatabase
from data_processing.sql.sqlite_database import SQLiteDatabase

class Dao:

    def __init__(self):
        self.__db: IDatabase = SQLiteDatabase()

    @property
    def db(self):
        """
        Retourne la base de données

        Returns:
            IDatabase: Base de données

        Raises:
            None
        """
        return self.__db
    
    @db.setter
    def db(self, db):
        """
        Met à jour la base de données

        Args:
            db (IDatabase): Nouvelle base de données

        Returns:
            None
        """
        self.__db = db