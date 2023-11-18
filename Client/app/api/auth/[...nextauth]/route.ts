import NextAuth, { NextAuthOptions } from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';
import jwt, { JwtPayload } from 'jsonwebtoken';

const authOptions: NextAuthOptions = {
    providers: [
        CredentialsProvider({
            name: 'credentials',
            credentials: {
                username: { label: "Username", type: "text", placeholder: "Username" },
                password: { label: "Password", type: "password" }
            },
            async authorize(credentials, req) {
                console.log(credentials);
            
                try {
                    const res = await fetch('http://127.0.0.1:5000/user/login', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ 
                            username: credentials?.username, 
                            password: credentials?.password 
                        }),
                    });
            
                    if (!res.ok) {

                        throw new Error(`HTTP error! Status: ${res.status}`);
                        
                    }
            
                    const user = await res.json();
                    const payload = jwt.decode(user.authorization) as JwtPayload;
            
                    if (user) {

                        return user;

                    } else {

                        return null;

                    }

                } catch (err) {

                    console.log(err);
                    return null;

                }
            }
            
        }),
    ],
    callbacks: {

        async jwt({ token, user }) {
            return { ...token, ...user };
        },

        async session({ session, token, user }) {
            session.user = token as any;
            return session;
        }

    },
    pages: {
        signIn: '/signin',
    }
}

const handler = NextAuth(authOptions);
export { handler as GET, handler as POST };