import React from 'react'
import { Link } from 'react-router-dom'
import { round } from 'utils/math'
import Rating from './Rating'


export default function Product(props) {
  const { product } = props
  return (
    <div key={product.id} className="card">
      <Link to={`/product/${product.id}`}>
        <img
          className="medium"
          src={product.image}
          alt={product.name}
        />
      </Link>
      <div className="card-body">
        <Link to={`/product/${product.id}`}>
          <h2>{product.name}</h2>
        </Link>
        <Rating
          rating={product.rating}
          reviews={product.reviews}
        />
        <div className="price">${round(product.price)}</div>
      </div>
    </div>
  )
}
