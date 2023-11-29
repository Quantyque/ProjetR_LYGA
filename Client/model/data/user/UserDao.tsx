import User from "@/model/logic/user";
import IUserDao from "@/model/data/user/IUserDao";
import Sender from "@/model/data/sender";

export class UserDao implements IUserDao{

    sender : Sender = new Sender();

    /**
     * Créer un utilisateur avec un role
     * @param Promise<string> : message de confirmation de création
     */
    async createUserWithRole(user: User, password: string, confirm_password: string): Promise<string> {
        const result = await this.sender.POST("user/admin-register", { ...user.toJSON(), password, confirm_password })
        return result;
    }

    /**
     * Retourne un tableau contenant toute la liste des utilisateurs
     * @returns un tableau d'objet user
     */
    async fetchUsers(): Promise<User[]> {
        const allUsers = await this.sender.GET("user/get-all")
        return(allUsers);
    }

    /**
     * Retourne un utilisateur via de son id
     * @param id 
     * @returns Promise<User> : un utilisateur
     */
    async fetchUserById(id: number): Promise<User> {
        const user = await this.sender.POST("user/get-by-id", id)
        return(user);
    }

    /**
     * Met à jour un utilisateur
     * @param user 
     * @returns Promise<string> : message de confirmation de mise à jour
     */
    async updateUser(user: User): Promise<string> {
        const result = await this.sender.UPDATE("user/update", user.toJSON())
        return result;
    }

    /**
     * Supprime un utilisateur 
     * @param user 
     * @returns Promise<string> : message de confirmation de suppression
     */
    async deleteUser(user: User): Promise<string> {
        const result = await this.sender.DELETE("user/delete", user.toJSON())
        return result;
    }

    /**
     * Récupère la liste des roles
     * @returns Promise<string[]> : liste des roles
     */
    async fetchRoles(): Promise<string[]> {
        const roles = await this.sender.GET("user/get-roles")
        return(roles);
    }
    
}