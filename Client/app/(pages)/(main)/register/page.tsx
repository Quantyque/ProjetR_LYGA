import React from 'react'
import Register from '@/app/components/RegisterComponents/Register';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Projet R | Register',
  description: 'Register page',
}

const RegisterPage = () => {
  return (
    <Register />
  )
}

export default RegisterPage