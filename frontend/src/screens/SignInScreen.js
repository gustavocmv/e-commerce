import { signIn } from 'actions/userActions'
import LoadingBox from 'components/LoadingBox'
import MessageBox from 'components/MessageBox'
import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link } from 'react-router-dom'

export default function SignInScreen(props) {

  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const redirect = props.location.search ?
    props.location.search.split('=')[1]
    : '/'

  const { loading, user, error } = useSelector(state => state.userSignIn)


  const dispatch = useDispatch()
  const submitHandler = (e) => {
    e.preventDefault();
    dispatch(signIn(email, password))
  }

  useEffect(() => {
    if (user) {
      props.history.push(redirect)
    }
  }, [props.history, redirect, user])



  return (
    <div>
      <form className="form" onSubmit={submitHandler}>
        <div>
          <h1>Sign In</h1>
        </div>
        {loading && <LoadingBox />}
        {error && <MessageBox variant="danger">{error}</MessageBox>}
        <div>
          <label htmlFor="email">Email Address</label>
          <input
            type="email" id="email"
            placeholder="Enter email address"
            required
            onChange={({ target: { value } }) => setEmail(value)}
          >
          </input>
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            type="password" id="password"
            placeholder="Enter password"
            required
            onChange={({ target: { value } }) => setPassword(value)}
          >
          </input>
        </div>
        <div>
          <label />
          <button className="primary" type="submit">
            Sign In
          </button>
        </div>
        <div>
          <label />
          <div>
            New customer? {' '}
            <Link to="/register">Sign Up!</Link>
          </div>
        </div>
      </form>
    </div >
  )
}
