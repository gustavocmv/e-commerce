import { CART_ADD_ITEM, CART_CLEAN, CART_REMOVE_ITEM } from "constants/cartConstants"


const initialState = {
  cartItems: []
}


export const cartReducer = (state = initialState, { type, payload }) => {
  switch (type) {
    case CART_ADD_ITEM:
      const existItem = state.cartItems.find(
        cartItem => cartItem.product_id === payload.product_id
      )
      if (existItem) {
        Object.assign(existItem, payload)
      }
      else {
        state.cartItems.push(payload)
      }
      return { ...state }

    case CART_REMOVE_ITEM:
      state.cartItems = state.cartItems.filter(
        cartItem => cartItem.product_id !== payload.productId
      )
      return { ...state }

    case CART_CLEAN:
      state.cartItems = []
      return { ...state }

    default:
      return state
  }
}
