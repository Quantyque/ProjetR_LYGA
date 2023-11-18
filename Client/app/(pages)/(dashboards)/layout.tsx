export default function DashboardLayout({
    children,
  } : {
    children: React.ReactNode
  }) {
    return (
      <body className="bg-[#1d232a]">
        {children}
      </body>
    )
}