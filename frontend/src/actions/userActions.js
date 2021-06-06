import { USER_SIGNIN_FAIL, USER_SIGNIN_RESQUEST, USER_SIGNIN_SUCCESS, USER_SIGNOUT } from "constants/userConstants"
import Axios from "axios"


export const signIn = (email, password) => async (dispatch) => {
  dispatch({
    type: USER_SIGNIN_RESQUEST,
    payload: { email, password }
  })
  try {
    let formData = new FormData();
    formData.append('grant_type', 'password')
    formData.append('username', email)
    formData.append('password', password)


    let access_token = (await Axios.post(
      "/login/access-token",
      formData,
      { "Content-Type": "multipart/form-data" },
    )).data.access_token

    let user = (await Axios.get(
      "/users/me",
      { headers: { "Authorization": `Bearer ${access_token}` } }
    )).data

    let data = { user, access_token }

    dispatch({ type: USER_SIGNIN_SUCCESS, payload: data })
    localStorage.setItem("userSignIn", JSON.stringify(data))

  } catch (error) {
    dispatch({
      type: USER_SIGNIN_FAIL,
      payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message
    })
  }
}

export const signOut = () => async (dispatch) => {
  localStorage.removeItem('userInfo')
  localStorage.removeItem('cartItems')
  dispatch({ type: USER_SIGNOUT })
}