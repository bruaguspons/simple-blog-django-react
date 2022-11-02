import { deleteService } from "../services/delete.service"

const deleteBlog = async (pk) => {
    const resuBlog = await fetch(`http://127.0.0.1:8000/api/blog/${pk}`, {
        method: 'DELETE',
    })
    if (resuBlog.status === 200) {
        deleteService.setSubject(true)
    }
}

export default deleteBlog