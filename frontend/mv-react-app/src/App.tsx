import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './Layout';
import Sierra from './pages/Sierra';
import Home from './pages/Home';
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="sierra" element={<Sierra />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App
