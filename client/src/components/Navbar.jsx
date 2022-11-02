import React from 'react'
import { Link, useNavigate } from 'react-router-dom'
const Navbar = () => {
    const navigation = useNavigate()
    return (
        <nav className="App">
            <Link to='/'>Home</Link>
            <Link to='/create'>Add new Blog</Link>
        </nav>
    )
}

export default Navbar