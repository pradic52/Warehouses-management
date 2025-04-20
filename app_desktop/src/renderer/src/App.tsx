import Button from 'react-bootstrap/Button'
import 'bootstrap/dist/css/bootstrap.min.css'
import React from 'react'

import x from './routers'

function App(): React.JSX.Element {
  const element = 'hello'
  x()
  return (
    <>
      <Button>Test</Button>
      <h1>Hello Word</h1>
      <div>{element}</div>
    </>
  )
}

export default App
