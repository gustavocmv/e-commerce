import { addToCart, clearCart, removeFromCart } from 'actions/cartActions'
import MessageBox from 'components/MessageBox'
import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link } from 'react-router-dom'

export default function CartScreen(props) {
  const productId = props.match.params.id
  const quantity = props.location.search
    ? props.location.search.split('=')[1]
    : 1
  const { cartItems } = useSelector(state => state.cart)

  const dispatch = useDispatch()
  useEffect(() => {
    if (productId) {
      dispatch(addToCart(productId, quantity))
    }
  }, [dispatch, productId, quantity])

  const removeFromCartHandler = (id) => {
    dispatch(removeFromCart(id))
  }

  const checkoutHandler = () => {
    props.history.push('/signin?redirect=shipping')
  }

  return (
    <div>
      <div className="row top">
        <div className="col-2">
          <h1>Shopping Cart</h1>
          {cartItems.length === 0
            ? (
              <MessageBox>
                Cart is Empty. <Link to="/">Go Shopping</Link>
              </MessageBox>
            ) : (
              <ul>
                {
                  cartItems.map((item) => (
                    <li key={item.product_id}>
                      <div className="row">
                        <img src={item.image} alt={item.name} className="small" />
                        <div className="min-30">
                          <Link to={`/product/${item.product_id}`}>{item.name}</Link>
                        </div>
                        <div>
                          <select
                            value={item.quantity}
                            onChange={e =>
                              dispatch(
                                addToCart(item.product_id, Number(e.target.value))
                              )
                            }
                          >
                            {[...Array(item.countInStock).keys()].map(x => (
                              <option key={x + 1} value={x + 1}>
                                {x + 1}
                              </option>
                            ))}
                          </select>
                        </div>
                        <div>$ {item.price}</div>
                        <div>
                          <button
                            onClick={() => removeFromCartHandler(item.product_id)}
                          >
                            Delete
                      </button>
                        </div>
                      </div>
                    </li>
                  ))
                }
              </ul>
            )


          }
        </div>
        <div className="col-1">
          <div className="card card-body">
            <ul>
              <li>
                <h2>
                  Subtotal ({cartItems.reduce((a, c) => (a + c.quantity), 0)} items) : $ {cartItems.reduce((a, c) => (a + c.price * c.quantity), 0)}
                </h2>
              </li>
              <li>
                <button
                  type="button"
                  onClick={checkoutHandler}
                  className="primary block"
                  disabled={cartItems.length === 0}
                >
                  Proceed to Checkout
              </button>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div>
        <button
          className="block"
          onClick={() => dispatch(clearCart())}
        >
          Clear Cart
        </button>
      </div>
    </div>
  )
}
