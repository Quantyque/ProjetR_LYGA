"use client";

import { ReactNode } from "react";
import { SessionProvider } from "next-auth/react";

/**
 * Interface Props
 * @author Youri Emmanuel
 */
interface Props {
    children: ReactNode;
}

/**
 * Provider
 * @param children
 * @returns session provider
 */
const Providers = ({ children }: Props) => {
    return (
        <SessionProvider>
            {children}
        </SessionProvider>
    );
};

export default Providers;