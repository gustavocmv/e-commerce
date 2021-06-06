import React, { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux';
import { Link } from 'react-router-dom'

import { round } from 'utils/math';
import { getProduct } from 'actions/getProduct';
import LoadingBox from 'components/LoadingBox';
import MessageBox from 'components/MessageBox';
import Rating from 'components/Rating';



export default function ProductScreen(props) {
  const dispatch = useDispatch()
  const productId = props.match.params.id
  const [quantity, setQuantity] = useState(1)
  const { loading, error, product } = useSelector(state => state.productDetails)

  useEffect(() => {
    dispatch(getProduct(productId))
  }, [dispatch, productId])

  const addToCartHandler = () => {
    props.history.push(`/cart/${productId}?quantity=${quantity}`)
  }

  return (
    <div>
      {
        loading ? (
          <LoadingBox />
        ) : error ? (
          <MessageBox variant="danger">
            {error}
          </MessageBox>
        ) : (
          <div>
            <Link to="/">Back to result</Link>
            <div className="row top">
              <div className="col-2">
                <img className="large" src={product.image} alt={product.name} />
              </div>
              <div className="col-1">
                <ul>
                  <li><h1>{product.name}</h1></li>
                  <li><h1>{product.author}</h1></li>
                  <li><Rating rating={product.rating} reviews={product.reviews} /></li>
                  <li>Price: ${round(product.price)}</li>
                  <li>
                    Description:
                    <p>{product.description}</p>
                  </li>
                </ul>
              </div>
              <div className="col-1">
                <div className="card card-body">
                  <ul>
                    <li>
                      <div className="row">
                        <div>Price</div>
                        <div className="price">${round(product.price)}</div>
                      </div>
                    </li>
                    <li>
                      <div className="row">
                        <div>Status</div>
                        <div >
                          {
                            product.stock > 0
                              ? <span className="success">In Stock</span>
                              : <span className="danger">Unavailable</span>
                          }
                        </div>
                      </div>
                    </li>
                    {
                      product.stock > 0 && (
                        <>
                          <li>
                            <div className="row">
                              <div>Quantity</div>
                              <div>
                                <select value={quantity} onChange={e => setQuantity(e.target.value)}>
                                  {
                                    [...Array(product.stock).keys()].map(
                                      x => (
                                        <option key={x + 1} value={x + 1}>
                                          {x + 1}
                                        </option>
                                      )
                                    )
                                  }
                                </select>
                              </div>
                            </div>
                          </li>
                          <li>
                            <button
                              className="primary block"
                              onClick={addToCartHandler}
                            >
                              Add to Cart
                            </button>
                          </li>
                        </>
                      )
                    }
                  </ul>
                </div>
              </div>
            </div>
          </div>
        )
      }
    </div>
  )
}
