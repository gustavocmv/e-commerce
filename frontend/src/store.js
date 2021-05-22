import { createStore, applyMiddleware, compose, combineReducers} from 'redux'
import thunk from 'redux-thunk'

import { productListReducer } from './reducers/productListReducer'
import { productDetailsReducer } from './reducers/productDetailsReducer';

const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

const reducer = combineReducers({
  productList: productListReducer,
  productDetails: productDetailsReducer
})

const initialState = {}
const store = createStore(
  reducer,
  initialState,
  composeEnhancer(applyMiddleware(thunk)))

export default store
