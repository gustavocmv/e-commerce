import {
  PRODUCT_DETAILS_FAIL,
  PRODUCT_DETAILS_REQUEST,
  PRODUCT_DETAILS_SUCCESS,

} from "../constants/productConstants"


const initialState = {
  loading: true,
  product: {}
}


export const productDetailsReducer = (state = initialState, { type, payload }) => {
  switch (type) {

    case PRODUCT_DETAILS_REQUEST:
      return {
        loading: true
      }

    case PRODUCT_DETAILS_SUCCESS:
      return {
        loading: false,
        product: payload
      }

    case PRODUCT_DETAILS_FAIL:
      return { 
        loading: false, 
        error: payload
      }

    default:
      return state
  }
}
