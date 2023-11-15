import sqlite3
from typing import Optional
from data_processing.sql.idatabase import IDatabase

class SQLiteDatabase(IDatabase):
    """
    Implémentation de la base de données SQLite
    """
    
    def __init__(self):
        self.db_file = "database.db"
        self.connection = None
        self.cursor = None

    def exec_request(self, req: str, params: Optional[tuple] = None, data_fetch_one: Optional[bool] = False) -> Optional[list]:
        """
        Exécute une requête SQL.

        Args:
            req (str): La requête SQL.
            params (tuple, optional): Les paramètres de la requête. Defaults to None.
            data_fetch_one (bool, optional): True si on veut récupérer un seul élément, False sinon. Defaults to False.

        Returns:
            list, optional: La liste des résultats de la requête.

        Raises:
            Exception: Si la requête échoue.
        """
        try:
            #Connexion à la base de données
            self.connection = sqlite3.connect(self.db_file, check_same_thread=False, timeout=1)
            with self.connection:
                self.cursor = self.connection.cursor()

                result = []
                # Exécution de la requête
                if params is not None:
                    self.cursor.execute(req, params)
                else:
                    self.cursor.execute(req)
                # Récupération du résultat
                if data_fetch_one:
                    result = self.cursor.fetchone()
                else:
                    result = self.cursor.fetchall()
                    
                return result

        except Exception as e:
            raise Exception(str(e))

        finally:
            # Fermeture de la connexion
            self.connection.commit()
            if self.cursor is not None:
                self.cursor.close()
            if self.connection is not None:
                self.connection.close()
