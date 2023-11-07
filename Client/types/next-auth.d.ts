import NextAuth from "next-auth/next";

declare module "next-auth"{
    interface Session{
        user: {
            name?: string | null | undefined;
            id: number;
            username: string;
            role: number;
            userPP?: string;
            accessToken: string;
        }
    }
}