import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'

import Product from 'components/Product'
import LoadingBox from 'components/LoadingBox'
import { listProducts } from 'actions/listProducts'
import MessageBox from 'components/MessageBox'


export default function HomeScreen() {
  const dispatch = useDispatch()
  const { loading, error, products } = useSelector(state => state.productList)

  useEffect(() => {
    dispatch(listProducts())
  }, [dispatch])

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
          <div className="row center">
            {
              products.map(
                (product) => (
                  <Product key={product._id} product={product} />
                )
              )
            }
          </div>
        )
      }
    </div>
  )
}
