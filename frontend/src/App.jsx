import './App.css'
import {HashRouter as Router, Routes, Route} from 'react-router-dom'
import { Home } from './Pages/Home'

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route/>
          <Route/>
          <Route/>
        </Routes>
      </Router>
    </>
  )
}

export default App
