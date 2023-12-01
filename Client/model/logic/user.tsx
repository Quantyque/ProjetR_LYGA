class User {
    
    private _id: number | undefined;
    private _username: string;
    private _role: number | undefined;
    private _userPP: string | undefined;
    private _token: string | undefined;
  
    constructor(id: number | undefined, username: string, role: number | undefined, userPP: string | undefined, token: string | undefined) {
      this._id = id;
      this._username = username;
      this._role = role;
      this._userPP = userPP;
      this._token = token;
    }
  
    get id(): number | undefined {
      return this._id;
    }
  
    set id(value: number | undefined) {
      this._id = value;
    }
  
    get username(): string {
      return this._username;
    }
  
    set username(value: string) {
      this._username = value;
    }
  
    get role(): number | undefined {
      return this._role;
    }
  
    set role(value: number | undefined) {
      this._role = value;
    }
  
    get userPP(): string | undefined {
      return this._userPP;
    }
  
    set userPP(value: string |undefined) {
      this._userPP = value;
    }
  
    get token(): string | undefined {
      return this._token;
    }
  
    set token(value: string | undefined) {
      this._token = value;
    }

    public toJSON(): any {
      return {
        id: this._id,
        username: this._username,
        role: this._role,
        userPP: this._userPP,
        token: this._token
      };
    }
    
  }

export default User;