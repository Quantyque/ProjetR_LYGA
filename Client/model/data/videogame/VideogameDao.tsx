import { Videogame } from "@/model/logic/videogame";
import IVideogameDao from "./IVideogameDao";
import Sender from "../sender";

export class VideogameDao implements IVideogameDao{

    sender : Sender = new Sender();

    /**
     * Retourne un tableau contenant toute la liste des jeux video
     * @returns un tableau d'objet videogame
     * @author Antoine Richard
     */
    async fetchVideoGames(): Promise<Videogame[]> {

        const allGames = this.sender.GET("videogames/all")
        return allGames;
        
    }

    /**
     * Retourne un tableau contenant toute la liste des jeux video audités
     * @returns un tableau d'objet videogame audités
    */
    async fetchAuditedVideoGames(): Promise<Videogame[]> {

        const allGames = this.sender.GET("videogames/audited")
        return allGames;

    }

    /**
     * Ajoute un jeu video
     * @param videogame jeu video à ajouter
     * @returns un message de confirmation d'ajout du jeu video
    */
    addVideogameToBeAudited(videogame: Videogame): Promise<string> {
            
        const response = this.sender.POST("/videogames/add-audited", {id: videogame.id, name: videogame.name})
        return response;

    }

    /**
     * Supprime un jeu video audités
     * @param id id du jeu video à supprimer
     * @returns un message de confirmation de suppression du jeu video
    */
    async deleteAuditedVideoGame(id: number): Promise<string> {

        const response = this.sender.DELETE("/videogames/delete-audited", { id: id })
        return response;

    }
    
}

