import React, { useState, useEffect } from 'react'


import { useGetBlogs } from '../hooks/useGetBlogs'
import { deleteService } from '../services/delete.service'
import deleteBlog from '../utils/deleteBlog'

const Blogs = ({ pk = '' }) => {
    const { data, loading } = useGetBlogs()

    const susbcription$ = deleteService.getSubject()
    useEffect(() => {
        susbcription$.subscribe(id => {
            console.log('funca?')
            dataDelete = data.results.filter(blog => blog.uuid !== id)
            setData({ ...data, results: dataDelete })
        })
        console.log('hola')
    }, [])


    console.log(loading)
    console.log(data.results)

    const handleDelete = async (id) => {
        await deleteBlog(id)
        // const restBlog =
        // setData({ ...data, results: restBlog })
    }
    if (loading) return (<div>loading...</div>)
    return (
        <div>
            {
                (!data.results || Object.keys(data.results).length < 1) ?
                    <div>No Blogs</div>
                    :
                    data.results.map(blog => (

                        <div key={blog.uuid} className="content">
                            <h1>{blog.title}</h1>
                            <h2>{blog.content}</h2>
                            <button onClick={() => handleDelete(blog.uuid)}>Delete</button>
                        </div>
                    ))
            }
        </div>
    )
}

export default Blogs