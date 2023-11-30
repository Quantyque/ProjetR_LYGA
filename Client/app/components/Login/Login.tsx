"use client"
import React, { useRef, useState } from 'react'
import './login.css'
import { signIn } from 'next-auth/react'

type Props = {
    className?: string
    searchParams?: { [key: string]: string | string[] | undefined}
    error?: string
}

const Login = (props: Props) => {

    const username = useRef("")
    const password = useRef("")

    const [loading, setLoading] = useState(false);

    const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {

        e.preventDefault()

        setLoading(true);

        await signIn('credentials', {
            username: username.current,
            password: password.current,
            callbackUrl: '/home'
        }).finally(() => {  setLoading(false); })

    }

    return (
        <div className={props.className}>
            <div style={{ position: 'absolute', height: '92%', right: '0', width: '55%', top: '9.85%', backgroundColor: '#F05959' }}>
                <img src="/images/connexionImg.png" alt="" style={{ position: 'absolute', width: '100%', height: '100%', objectFit: 'cover' }} />
            </div>
            <div id='loginFormContainer' style={{ position: 'absolute', height: '90%', left: '0', width: '45%', top: '10%' }}>
                <div id="loginForm">
                    <h1 id='title'>CONNEXION</h1>
                    { props.searchParams?.message && <div className="alert alert-error">{props.searchParams.message}</div> }
                    {!!props.error && <div className="alert alert-error">Authentification failed. Try again.</div>}
                    {loading ? (
                        <div className="loading loading-spinner loading-lg ml-[190px] mt-[95px]"></div>
                    ) : (
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
                        <div id='rememberMe' className="form-control">
                            <label className="label cursor-pointer">
                                <span className="label-text">Rester connecté</span>
                                <input type="checkbox" className="checkbox" />
                            </label>
                        </div>
                        <div id='centerContainer'>
                            <button className='btn btn-wide' id='loginButton' type="submit">
                                Se connecter
                            </button>
                        </div>
                        <div id='centerContainer'>
                            <p className="message">
                                Pas encore inscrit ? <a href="/register">S'inscrire</a>
                            </p>
                        </div>
                    </form>
                    )}
                </div>
            </div>
        </div>
    )
}

export default Login