import { useState } from 'react'

function AddTransactionForm({ onAdd }) {
  const [form, setForm] = useState({
    date: '', description: '', amount: '', category: ''
  })

  function handleSubmit() {
    onAdd(form)
    setForm({ date: '', description: '', amount: '', category: '' })
  }

  return (
    <div>
      <input placeholder="Date"        value={form.date}        onChange={e => setForm({...form, date: e.target.value})} />
      <input placeholder="Description" value={form.description} onChange={e => setForm({...form, description: e.target.value})} />
      <input placeholder="Amount"      value={form.amount}      onChange={e => setForm({...form, amount: e.target.value})} />
      <input placeholder="Category"    value={form.category}    onChange={e => setForm({...form, category: e.target.value})} />
      <button onClick={handleSubmit}>Add</button>
    </div>
  )
}

export default AddTransactionForm