import { API_HOST } from "../constants/constants";

/**
 * Use to send informations to Database
 */
class Sender {

    /**
     * Api host of sender
     */
    private _apiHost: string;

    public constructor() {
        this._apiHost = API_HOST;
    }

    /**
     * GET query
     * @param route path where the query is done
     * @returns JSON format response
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
     * POST query
     * @param route path where the query is done
     * @param data data changed
     * @returns JSON format response
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
     * UPDATE query
     * @param route path where the query is done
     * @param data data changed
     * @returns JSON format response
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
     * DELETE query
     * @param route path where the query is done
     * @returns JSON format response
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
