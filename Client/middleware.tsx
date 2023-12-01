import { withAuth } from "next-auth/middleware"
import { NextResponse } from "next/server"

export default withAuth(
  function middleware(req){

    if (req.nextUrl.pathname.startsWith("/admin-dashboard") && req.nextauth.token?.role !== 1) {
      return NextResponse.rewrite(new URL("/signin?message=Access denied !", req.url))
    };

  },
  {
    callbacks: {

      authorized: ({ token }) => !!token, // If you return falsey, the user will be redirected to the login page

    }
  }
)

export const config = {
  matcher: ["/admin-dashboard/:path*"]
}


