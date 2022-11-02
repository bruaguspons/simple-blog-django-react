import React, { useState } from 'react'
// import reactLogo from './assets/react.svg'
import Blogs from './components/Blogs'
import Form from './components/Form'
import Navbar from './components/Navbar'
import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

function App() {

  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path='/' element={<Blogs />}></Route>
        <Route path='/create' element={<Form />}></Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
