"use client"
import React, { useRef } from 'react'
import Link from 'next/link'
import './register.css'
import { signIn } from 'next-auth/react'

type Props = {
    className?: string
    searchParams?: { [key: string]: string | string[] | undefined}
    error?: string
}

const Register = (props: Props) => {

    const username = useRef("")
    const password = useRef("")
    const confirmPassword = useRef("")

    const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {

        e.preventDefault()

    }

    return (
        <div className={props.className}>
            <div style={{ position: 'absolute', height: '92%', right: '0', width: '55%', top: '9.80%', backgroundColor: '#F05959' }}>
                <img src="/images/connexionImg.png" alt="" style={{ position: 'absolute', width: '100%', height: '100%', objectFit: 'cover' }} />
            </div>
            <div id='loginFormContainer' style={{ position: 'absolute', height: '90%', left: '0', width: '45%', top: '10%' }}>
                <div id="loginForm">
                    <h1 id='title'>LOGIN</h1>
                    { props.searchParams?.message && <div className="alert alert-error">{props.searchParams.message}</div> }
                    {!!props.error && <div className="alert alert-error">Authentification failed. Try again.</div>}
                    <form className="login-form" onSubmit={onSubmit}>
                        <input
                            type="text"
                            placeholder="Username"
                            className='input w-full input-error'
                            id='formUsername'
                            onChange={(e) => username.current = e.target.value}
                        />
                        <input
                            type="password"
                            placeholder="Password"
                            className='input w-full input-warning'
                            id='formPassword'
                            onChange={(e) => password.current = e.target.value}
                        />
                        <input
                            type="password"
                            placeholder="Password"
                            className='input w-full input-warning'
                            id='formPassword'
                            onChange={(e) => confirmPassword.current = e.target.value}
                        />
                        <div id='rememberMe' className="form-control">
                            <label className="label cursor-pointer">
                                <span className="label-text">Remember me</span>
                                <input type="checkbox" className="checkbox" />
                            </label>
                        </div>
                        <div id='centerContainer'>
                            <button className='btn btn-wide' id='loginButton' type="submit">
                                Connect
                            </button>
                        </div>
                        <div id='centerContainer'>
                            <p className="message">
                                Not registered? <a href="#">Create an account</a>
                            </p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Register