import { CART_ADD_ITEM } from "constants/cartConstants"
import { start } from "pretty-error"

const initialState = {
  cartItems: []
}


export const cartReducer = (state = initialState, { type, payload }) => {
  switch (type) {

    case CART_ADD_ITEM:
      const newItem = payload
      const existItem = state.cartItems.find(
        cartItem => cartItem.product_id === newItem.product_id
      )
      if (existItem) {
        Object.assign(existItem, newItem)
      }
      else {
        state.cartItems.push(newItem)
      }
      return state

    default:
      return state
  }
}
