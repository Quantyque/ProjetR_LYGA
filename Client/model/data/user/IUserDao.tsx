import User from '@/model/logic/user';

interface IUserDao {

    /**
     * Retourne un tableau contenant toute la liste des utilisateurs
     * @returns un tableau d'objet user
     */
    fetchUsers(): Promise<User[]>;

    /**
     * Retourne un utilisateur via de son id
     * @param id 
     */
    fetchUserById(id: number): Promise<User>;

    /**
     * Met à jour un utilisateur
     * @param user 
     */
    updateUser(user: User): Promise<User>;

    /**
     * Supprime un utilisateur 
     * @param id 
     */
    deleteUser(id: number): Promise<User>;

}

export default IUserDao;