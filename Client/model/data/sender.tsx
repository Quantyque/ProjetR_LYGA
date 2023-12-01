import { API_HOST } from "../constants/constants";

/**
 * Utilisé pour envoyer des informations à la base de données
 */
class Sender {

    /**
     * Hôte API du sender
     */
    private _apiHost: string;

    public constructor() {
        this._apiHost = API_HOST;
    }

    /**
     * Requête GET
     * @param route passage de la requête où elle est faite 
     * @returns Réponse sous format JSON
     */
    public async GET(route: string): Promise<any> {
        const apiEndpoint = this._apiHost + route;
        console.log(apiEndpoint);
        try {
            const response = await fetch(apiEndpoint, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (!response.ok) {
                throw new Error(`GET request failed with status ${response.status}`);
            }

            const result = await response.json();
            return result;
        } catch (error) {
            console.error('GET request failed:', error);
            throw error;
        }
    }

    /**
     * Requête POST
     * @param route passage de la requête où elle est faite 
     * @param data Données changées
     * @returns Réponse sous format JSON
     */
    public async POST(route: string, data: any): Promise<any> {
        const apiEndpoint = this._apiHost + route;

        try {
            const response = await fetch(apiEndpoint, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error(`POST request failed with status ${response.status}`);
            }

            const result = await response.json();
            return result;
        } catch (error) {
            console.error('POST request failed:', error);
            throw error;
        }
    }

    /**
     * Requête UPDATE
     * @param route passage de la requête où elle est faite 
     * @param data Données changées
     * @returns Réponse sous format JSON
     */
    public async UPDATE(route: string, data: any): Promise<any> {
        const apiEndpoint = this._apiHost + route;

        try {
            const response = await fetch(apiEndpoint, {
                method: "PUT",
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error(`UPDATE request failed with status ${response.status}`);
            }

            const result = await response.json();
            return result;
        } catch (error) {
            console.error('UPDATE request failed:', error);
            throw error;
        }
    }

    /**
     * Requête DELETE
     * @param route passage de la requête où elle est faite 
     * @returns Réponse sous format JSON
     */
    public async DELETE(route: string): Promise<any> {
        const apiEndpoint = this._apiHost + route;

        try {
            const response = await fetch(apiEndpoint, {
                method: "DELETE",
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (!response.ok) {
                throw new Error(`DELETE request failed with status ${response.status}`);
            }

            const result = await response.json();
            return result;
        } catch (error) {
            console.error('DELETE request failed:', error);
            throw error;
        }
    }
}

export default Sender;
