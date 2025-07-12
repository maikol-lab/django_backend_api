import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className="container">
          <div className="datos">
            <h1>Datos de Python</h1>
            <ul>
              <i className='item-1'></i>
              <i className='item-2'></i>
              <i className='item-3'></i>
              <i className='item-4'></i>
            </ul>
          </div>
      </div>
    </>
  )
}

export default App
