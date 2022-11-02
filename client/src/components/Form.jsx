import React, { useState } from 'react'

const From = () => {
    const [data, setData] = useState({
        title: '',
        content: ''
    })
    const handleSubmit = async (e) => {
        e.preventDefault()
        const res = await fetch('http://127.0.0.1:8000/api/blog/', {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        })
        const resMessage = await res.json()
        console.log(resMessage)
    }

    const handleChange = (e) => {
        setData(
            {
                ...data,
                [e.target.name]: e.target.value
            }
        )
    }
    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name='title' placeholder='Title' onChange={handleChange} />
            <textarea name="content" id="" cols="30" rows="10" placeholder='Content' onChange={handleChange}></textarea>
            <button type="submit">Add</button>
        </form>
    )
}

export default From