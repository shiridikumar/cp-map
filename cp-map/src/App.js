import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react'
import {
  BrowserRouter,
  Routes,
  Route,
  createBrowserRouter,
} from "react-router-dom";
import Signin from './components/SIgnin';
import Dashboard from './components/Dashboard';
import SignUp from './components/Signup';

function App() {
  
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          
          <Route exact path="/" element={<Signin />} />
          <Route exact path="/dashboard" element={<Dashboard />} />
          <Route exact path="/signup" element={<SignUp />} />

        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
