import Axios from "axios"
import { CART_ADD_ITEM, CART_CLEAN, CART_REMOVE_ITEM } from "constants/cartConstants"

const updateCartItemsLocalStorage = (getState) =>
  localStorage.setItem('cartItems', JSON.stringify(getState().cart.cartItems))


export const addToCart = (productId, quantity) => async (dispatch, getState) => {
  const { data } = await Axios.get(`/products/${productId}`)
  dispatch({
    type: CART_ADD_ITEM,
    payload: {
      name: data.name,
      image: data.image,
      price: data.price,
      stock: data.stock,
      product_id: data.id,
      quantity
    }
  })
  updateCartItemsLocalStorage(getState)
}


export const removeFromCart = (productId) => async (dispatch, getState) => {
  dispatch({
    type: CART_REMOVE_ITEM,
    payload: {
      productId
    }
  })
  updateCartItemsLocalStorage(getState)
}

export const clearCart = () => async (dispatch, getState) => {
  dispatch({
    type: CART_CLEAN,
    payload: null
  })
  updateCartItemsLocalStorage(getState)
}
