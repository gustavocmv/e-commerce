import Axios from "axios"
import { CART_ADD_ITEM } from "constants/cartConstants"


export const addToCart = (productId, quantity) => async (dispatch, getState) => {
  const { data } = await Axios.get(`/products/${productId}`)
  dispatch({
    type: CART_ADD_ITEM,
    payload: {
      name: data.name,
      image: data.image,
      price: data.price,
      countInStock: data.countInStock,
      product_id: data._id,
      quantity
    }
  })
}


