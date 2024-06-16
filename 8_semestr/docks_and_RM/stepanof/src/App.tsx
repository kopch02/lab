import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import { FormPage } from './pages/FormPage'
import { Root } from './pages/Layout'
import { ErrorPage } from './pages/ErrorPage'
import { System } from './pages/System'
import { Order } from './pages/Order'

import './index.css'

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: '/forms',
        element: <FormPage />,
      },
      {
        path: '/system',
        element: <System />,
      },
      {
        path: '/order',
        element: <Order />,
      },
      {
        path: '/*',
        element: <ErrorPage />,
      },
    ],
  },
])

const App = () => {
  return <RouterProvider router={router} />
}

export default App
