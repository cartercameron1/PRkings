import './App.css'
import {HashRouter as Router, Routes, Route} from 'react-router-dom'
import { Home } from './Pages/Home'
import { Profile } from './Pages/Profile'
import { SubmitLift } from './Pages/SubmitLift'

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route path="/profile" element={<Profile/>}/>
          <Route path="/submit_lift" element={<SubmitLift/>}/>
          <Route/>
        </Routes>
      </Router>
    </>
  )
}

export default App
