import NextAuth, { NextAuthOptions } from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';
import jwt, { JwtPayload } from 'jsonwebtoken';

/**
 * Next authentification options
 * @author Youri Emmanuel
 */
const authOptions: NextAuthOptions = {
    providers: [
        CredentialsProvider({
            name: 'credentials',
            credentials: {
                username: { label: "Username", type: "text", placeholder: "Username" },
                password: { label: "Password", type: "password" }
            },
            async authorize(credentials, req) {

                const res = await fetch('http://localhost:5000/user/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ 
                        username: credentials?.username, 
                        password: credentials?.password 
                    }),
                });

                const user = await res.json();
                const payload = jwt.decode(user.authorization) as JwtPayload;

                if (user) {

                    return user;

                } else {

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