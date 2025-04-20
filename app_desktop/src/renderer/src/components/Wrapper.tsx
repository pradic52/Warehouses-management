import { WrapperProps } from '@globaltype/component/index'
import { ToastContainer } from 'react-toastify'
import NavBar from './NavBar'
import { JSX } from 'react'

function Wrapper({ children }: WrapperProps): JSX.Element {
  console.log(children)
  return (
    <div>
      <NavBar></NavBar>
      <ToastContainer
        position="top-right"
        autoClose={9000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        pauseOnHover
        draggable
      />
    </div>
  )
}

export default Wrapper
