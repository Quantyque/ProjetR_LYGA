"use client"
import React, { useRef } from 'react'
import Link from 'next/link'
import './register.css'
import IUserDao from '@/model/data/user/IUserDao';
import { UserDao } from '@/model/data/user/UserDao';
import User from '@/model/logic/user';
import { signIn } from 'next-auth/react'


type Props = {
    className?: string
    searchParams?: { [key: string]: string | string[] | undefined}
    error?: string
}

const Register = (props: Props) => {

    const username = useRef("");
    const password = useRef("");
    const confirmPassword = useRef("");

    const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {

        e.preventDefault();

        try {

            const userDao: IUserDao = new UserDao();
            await userDao.createUser(new User(undefined, username.current, undefined, undefined, undefined), password.current, confirmPassword.current);
    
            await signIn('credentials', {

                username: username.current,
                password: password.current,
                redirect: true,
                callbackUrl: "/",

            }).catch((e) => {

                throw e;

            });


        } catch (error) {

            console.error("Erreur lors de la sauvegarde :", error);

        }

    }


    return (
        <div className={props.className}>
            <div style={{ position: 'absolute', height: '92%', right: '0', width: '55%', top: '9.80%', backgroundColor: '#F05959' }}>
                <img src="/images/connexionImg.png" alt="" style={{ position: 'absolute', width: '100%', height: '100%', objectFit: 'cover' }} />
            </div>
            <div id='loginFormContainer' style={{ position: 'absolute', height: '90%', left: '0', width: '45%', top: '10%' }}>
                <div id="loginForm">
                    <h1 id='title'>INSCRIPTION</h1>
                    { props.searchParams?.message && <div className="alert alert-error">{props.searchParams.message}</div> }
                    {!!props.error && <div className="alert alert-error">Authentification failed. Try again.</div>}
                    <form className="login-form" onSubmit={onSubmit}>
                        <input
                            type="text"
                            placeholder="Pseudo"
                            className='input w-full input-error'
                            id='formUsername'
                            onChange={(e) => username.current = e.target.value}
                            required
                        />
                        <input
                            type="password"
                            placeholder="Mot de passe"
                            className='input w-full input-warning'
                            id='formPassword'
                            onChange={(e) => password.current = e.target.value}
                            required
                        />
                        <input
                            type="password"
                            placeholder="Confirmation du mot de passe"
                            className='input w-full input-warning'
                            id='formPassword'
                            onChange={(e) => confirmPassword.current = e.target.value}
                            required
                        />
                        <div id='rememberMe' className="form-control">
                            <label className="label cursor-pointer">
                                <span className="label-text">J'accepte les conditions d'utilisations de PROJET R *</span>
                                <input type="checkbox" className="checkbox" required/>
                            </label>
                        </div>
                        <div id='centerContainer'>
                            <button className='btn btn-wide' id='loginButton' type="submit">
                                S'inscrire
                            </button>
                        </div>
                        <div id='centerContainer'>
                            <p className="message">
                                Déjà un compte ? <Link href="/signin">S'inscrire</Link>
                            </p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Register