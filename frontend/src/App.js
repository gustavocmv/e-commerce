import { signOut } from 'actions/userActions'
import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { BrowserRouter, Link, Route } from 'react-router-dom'
import CartScreen from 'screens/CartScreen'
import HomeScreen from 'screens/HomeScreen'
import ProductScreen from 'screens/ProductScreen'
import SignInScreen from 'screens/SignInScreen'
import TestScreen from 'screens/TestScreen'

function App() {

  const cart = useSelector(state => state.cart)
  const user = useSelector(state => state.userSignIn.user)

  const dispatch = useDispatch()
  const signOutHandler = () => {
    dispatch(signOut())
  }

  return (
    <BrowserRouter>
      <div className="grid-container">
        <header className="row">
          <div>
            <Link className="brand" to="/">Livraria do IVE</Link>
          </div>
          <div>
            <Link to="/cart">
              Cart {
                cart.cartItems.length > 0 && (
                  <span className="badge">{cart.cartItems.length}</span>
                )
              }
            </Link>
            {
              user ? (
                <div className="dropdown">
                  <Link to="#">
                    {user.name} <i className="fa fa-caret-down"></i> {' '}
                  </Link>
                  <ul className="dropdown-content">
                    <Link to="signout" onClick={signOutHandler}>Sign Out</Link>
                  </ul>
                </div>
              ) : (
                <Link to="/signin">Sign In</Link>
              )
            }
          </div>
        </header>
        <main>
          <Route path="/" component={HomeScreen} exact />
          <Route path="/product/:id" component={ProductScreen} />
          <Route path="/cart/:id?" component={CartScreen} />
          <Route path="/signin" component={SignInScreen} />
          <Route path="/test/" component={TestScreen} />
        </main>
        <footer className="row center">
          All rights reserved.
        </footer>
      </div>
    </BrowserRouter >
  )
}

export default App
