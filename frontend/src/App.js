import React from 'react'
import { BrowserRouter, Route } from 'react-router-dom'
import CartScreen from 'screens/CartScreen'
import HomeScreen from 'screens/HomeScreen'
import ProductScreen from 'screens/ProductScreen'

function App() {
  return (
    <BrowserRouter>
      <div className="grid-container">
        <header className="row">
          <div>
            <a className="brand" href="/">Livraria do IVE</a>
          </div>
          <div>
            <a href="/cart">Cart</a>
            <a href="/sigin">Sign In</a>
          </div>
        </header>
        <main>
          <Route path="/" component={HomeScreen} exact />
          <Route path="/product/:id" component={ProductScreen} />
          <Route path="/cart/:id?" component={CartScreen} />
        </main>
        <footer className="row center">
          All rights reserved.
        </footer>
      </div>
    </BrowserRouter>
  )
}

export default App
