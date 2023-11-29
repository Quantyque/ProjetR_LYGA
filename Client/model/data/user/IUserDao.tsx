import User from '@/model/logic/user';

interface IUserDao {

    /**
     * Créer un utilisateur avec un role
     * @param Promise<string> : message de confirmation de création
     */
    createUserWithRole(user: User, password: string, confirm_password: string): Promise<string>;

    /**
     * Retourne un tableau contenant toute la liste des utilisateurs
     * @returns Promise<User[]> : un tableau d'objet user
     */
    fetchUsers(): Promise<User[]>;

    /**
     * Retourne un utilisateur via de son id
     * @param id 
     * @returns Promise<User> : un utilisateur
     */
    fetchUserById(id: number): Promise<User>;

    /**
     * Met à jour un utilisateur
     * @param user 
     * @returns Promise<string> : message de confirmation de mise à jour
     */
    updateUser(user: User): Promise<string>;

    /**
     * Supprime un utilisateur 
     * @param user 
     * @returns Promise<string> : message de confirmation de suppression
     */
    deleteUser(user: User): Promise<string>;

    /**
     * Récupère la liste des roles
     * @returns Promise<string[]> : liste des roles
     */
    fetchRoles(): Promise<string[]>;

}

export default IUserDao;