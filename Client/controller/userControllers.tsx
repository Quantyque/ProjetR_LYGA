import User from "@/model/logic/user";
import IUserDao from "@/model/data/user/IUserDao";
import { UserDao } from "@/model/data/user/UserDao";

/**
 * Controller des utilisateurs
 */
class userController {

    private userDao: IUserDao;

    constructor()  {
        this.userDao = new UserDao;
    }

    /**
     * Utilse userDao pour ajouter un utilisateur avec un role
     * @param user utilisateur à ajouter
     * @returns message de confirmation d'ajout de l'utilisateur
     */
    async createUserWithRole(user: User, password: string, confirm_password: string): Promise<string>{
        return await this.userDao.createUserWithRole(user, password, confirm_password)
    }

    /**
     * Utilse userDao pour ajouter un utilisateur
     * @param user utilisateur à ajouter
     * @returns message de confirmation d'ajout de l'utilisateur
     */
    async createUser(user: User, password: string, confirm_password: string): Promise<string>{
        return await this.userDao.createUser(user, password, confirm_password)
    }

    /**
     * Utilse userDao pour obtenir touts les utilisateurs
     * @returns touts les utilisateurs
     */
    async getUsers(): Promise<User []>{
        return await this.userDao.fetchUsers()
    }

    /**
     * Utilse userDao pour obtenir un utilisateur via de son id
     * @param id id de l'utilisateur à obtenir
     * @returns un utilisateur
     */
    async getUserById(id: number): Promise<User>{
        return await this.userDao.fetchUserById(id)
    }

    /**
     * Utilse userDao pour mettre à jour un utilisateur
     * @param user utilisateur à mettre à jour
     * @returns message de confirmation de mise à jour de l'utilisateur
     */
    async updateUser(user: User): Promise<string>{
        return await this.userDao.updateUser(user)
    }

    /**
     * Utilse userDao pour supprimer un utilisateur audités
     * @param id id de l'utilisateur à supprimer
     * @returns message de confirmation de suppression de l'utilisateur
     */
    async deleteUser(user: User): Promise<string>{
        return await this.userDao.deleteUser(user)
    }

    /**
     * Récupère la liste des roles
     * @returns Promise<string[]> : liste des roles
     */
    async getRoles(): Promise<string[]> {
        return await this.userDao.fetchRoles()
    }

}

export default userController;