import Link from "next/link"

const Logo = () => {
    return (
        <Link href='/'>
            <img src="/logo.png" width={54} height={54} alt="" />
        </Link>
    )
}

export default Logo