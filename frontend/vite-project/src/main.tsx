import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import './index.css'
import App from './App.tsx'
import Regist from './pages/regist.tsx'

const router = createBrowserRouter([{
  path: '/',
  element: <App />,
  errorElement: <h1>404 NOT FOUND</h1>
},
{
  path: '/register',
  element: <Regist />,
  errorElement: <h1>404 NOT FOUND</h1>
}])

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
