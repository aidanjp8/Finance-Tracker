import { useState } from 'react'
import './App.css'
import SimpleTable from './TransactionalTable'
import AddTransactionForm from './AddTransactionForm'

function App() {
  const [transactions, setTransactions] = useState([
  { id: 1, date: '2026-03-13', description: 'SAFEWAY #1463', amount: -53.31, category: 'Food' },
  { id: 2, date: '2026-03-13', description: 'SPOTIFY',       amount: -9.99,  category: 'Entertainment' },
])
  
  function handleAdd(newTransaction) {
    setTransactions([...transactions, newTransaction])
  }
  
  return (
    <div>
      <h1>Finance Tracker</h1>
      <AddTransactionForm onAdd={handleAdd} />
      <SimpleTable data={transactions} />
    </div>
  )
}

export default App