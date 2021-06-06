import React, { useState } from 'react'
import axios from 'axios'

export default function TestScreen() {

  const [valueA, setValueA] = useState(1)
  const [valueB, setValueB] = useState(2)

  // const []

  const { data } = axios.get(`/calc-sum?a=${valueA}&b=${valueB}`)

  console.log(data)

  return (
    <div>
      <h1>A</h1>
      <select
        value={valueA}
        onChange={e => setValueA(e.target.value)}
      >
        <option key={1} value={1}>1</option>
        <option key={2} value={2}>2</option>
        <option key={3} value={3}>3</option>
      </select >
      <h1>B</h1>
      <select
        value={valueB}
        onChange={e => setValueB(e.target.value)}
      >
        <option key={1} value={1}>1</option>
        <option key={2} value={2}>2</option>
        <option key={3} value={3}>3</option>
      </select >
      <div>
        {axios.get(`/calc-sum?a=${valueA}&b=${valueB}`).data}
      </div>
    </div>
  )
}
