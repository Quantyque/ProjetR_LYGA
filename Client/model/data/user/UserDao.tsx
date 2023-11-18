import User from "@/model/logic/user";
import { useEffect, useState } from "react";
import IUserDao from "@/model/data/user/IUserDao";
import Sender from "@/model/data/sender";

export class UserDao implements IUserDao{

    sender : Sender = new Sender();

    /**
     * Retourne un tableau contenant toute la liste des utilisateurs
     * @returns un tableau d'objet user
     */
    async fetchUsers(): Promise<User[]> {
        var Allusers;
        Allusers = this.sender.GET("user/get-all")
        return(Allusers);
    }

    /**
     * Retourne un utilisateur via de son id
     * @param id 
     */
    async fetchUserById(id: number): Promise<User> {
        var user;
        user = this.sender.POST("user/get-by-id", id)
        console.log(user)
        return(user);
    }

    /**
     * Met à jour un utilisateur
     * @param user 
     */
    async updateUser(user: User): Promise<User> {
        this.sender.UPDATE("user/update", user)
        return(user);
    }

    /**
     * Supprime un utilisateur 
     * @param id 
     */
    async deleteUser(id: number): Promise<User> {
        var user;
        user = this.sender.DELETE("user/delete", id)
        return(user);
    }
    
}