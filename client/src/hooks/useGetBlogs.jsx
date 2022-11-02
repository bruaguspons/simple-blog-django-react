import { useState, useEffect } from "react"
import { deleteService } from "../services/delete.service"



export const useGetBlogs = (pk = '') => {



    const [data, setData] = useState({})
    const [loading, setLoading] = useState(true)

    const getData = async () => {
        const blogs = await fetch(`http://127.0.0.1:8000/api/blog/${pk}`)
        const dataBlogs = await blogs.json()
        setData(dataBlogs)
        setLoading(false)
    }

    useEffect(() => {
        getData()
    }, [pk])
    // useEffect(() => {
    //     fetch(`http://127.0.0.1:8000/api/blog/${pk}`)
    //         .then(data => data.json())
    //         .then(data => {
    //             setData(data)
    //             setLoading(false)
    //         })
    // }, [])

    return { data, loading }
}

