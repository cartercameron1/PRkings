import './App.css'
import {HashRouter as Router, Routes, Route} from 'react-router-dom'
import { Home } from './Pages/Home'
import { Profile } from './Pages/Profile'

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/home" element={<Home/>}/>
          <Route path="/profile" element={<Profile/>}/>
          <Route/>
          <Route/>
        </Routes>
      </Router>
    </>
  )
}

export default App
