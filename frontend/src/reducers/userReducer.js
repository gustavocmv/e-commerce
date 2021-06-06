import { USER_SIGNIN_FAIL, USER_SIGNIN_RESQUEST, USER_SIGNIN_SUCCESS, USER_SIGNOUT } from "constants/userConstants"

const initialState = {

}

export const userSignInReducer = (state = initialState, { type, payload }) => {
  switch (type) {

    case USER_SIGNIN_RESQUEST:
      return { loading: true }

    case USER_SIGNIN_SUCCESS:
      return { loading: false, ...payload }

    case USER_SIGNIN_FAIL:
      return { loading: false, error: payload }

    case USER_SIGNOUT:
      return {}

    default:
      return state
  }
}
