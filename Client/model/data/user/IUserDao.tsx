import User from '@/model/logic/user';

interface IUserDao {

    /**
     * Créer un utilisateur avec un role
     * @param user 
     */
    createUserWithRole(user: User, password: string, confirm_password: string): Promise<string>;

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
    updateUser(user: User): Promise<string>;

    /**
     * Supprime un utilisateur 
     * @param user 
     */
    deleteUser(user: User): Promise<string>;

    /**
     * Récupère la liste des roles
     */
    fetchRoles(): Promise<string[]>;

}

export default IUserDao;