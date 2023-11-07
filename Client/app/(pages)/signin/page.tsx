import React from 'react'
import Login from '@/app/components/Login/Login'

type Props = {
    searchParams?: Record<"callbackUrl"|"error", string>
}

const SignIn = (props: Props) => {
  return <Login error={props.searchParams?.error}/>
}

export default SignIn