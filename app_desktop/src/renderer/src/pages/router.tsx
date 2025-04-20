import { JSX } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

export function AppRoutes(): JSX.Element {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<h1>test</h1>} />
      </Routes>
    </Router>
  )
}
