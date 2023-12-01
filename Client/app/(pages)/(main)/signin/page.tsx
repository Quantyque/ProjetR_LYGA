import React from 'react'
import Login from '@/app/components/Login/Login'

/**
 * Type Props
 * @author Youri Emmanuel
 */
type Props = {
    searchParams?: Record<"callbackUrl"|"error", string>
}

/**
 * Méthode s'enregistrer
 * @param props
 * @returns erreur si les paramètres de recherches sont érronés
 * @author Youri Emmanuel
 */
const SignIn = (props: Props) => {
  return <Login error={props.searchParams?.error}/>
}

export default SignIn