import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
// import Go from './Go'
import Chatbot from './Chatbot'

function App() {
//   const [count, setCount] = useState(0)

  return (
    <>
      <h1>Welcome to the Support Chat</h1>
      <Chatbot />
    </>
  )
}

export default App
