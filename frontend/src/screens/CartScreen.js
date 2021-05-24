import React from 'react'

export default function CartScreen(props) {
  const productId = props.match.params.id
  const quantity = props.location.search 
    ? props.location.search.split('=')[1]
    : 1

  return (
    <div>
      <h1>Cart Screen</h1>
      <p>Add To Card - Product ID: {productId} - Quantity: {quantity}</p>
    </div>
  )
}
