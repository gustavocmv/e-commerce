import { createStore, applyMiddleware, compose, combineReducers } from 'redux'
import thunk from 'redux-thunk'

import { productListReducer } from './reducers/productListReducer'
import { productDetailsReducer } from './reducers/productDetailsReducer';
import { cartReducer } from 'reducers/cartReducer';
import { userSignInReducer } from 'reducers/userReducer';

const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

const reducer = combineReducers({
  productList: productListReducer,
  productDetails: productDetailsReducer,
  cart: cartReducer,
  userSignIn: userSignInReducer
})

const initialState = {
  userSignIn: {
    ...(localStorage.getItem('userSignIn')
      ? JSON.parse(localStorage.getItem('userSignIn'))
      : {}
    )
  },
  cart: {
    cartItems: localStorage.getItem('cartItems')
      ? JSON.parse(localStorage.getItem('cartItems'))
      : []
  }
}
const store = createStore(
  reducer,
  initialState,
  composeEnhancer(applyMiddleware(thunk))
)

export default store
