import { useState } from 'react'

const CATEGORIES = [
  'Food',
  'Transport',
  'Entertainment',
  'Shopping',
  'Groceries',
  'Utilities',
  'Rent',
  'Debts/Payments',
  'Subscriptions',
  'Uncategorized'
]

function AddTransactionForm({ onAdd }) {
  const [form, setForm] = useState({
    date: '', description: '', amount: '', category: ''
  })
  const [search, setSearch] = useState('')
  const [showDropdown, setShowDropdown] = useState(false)

  // Filter categories based on what user types
  const filtered = CATEGORIES.filter(cat =>
    cat.toLowerCase().includes(search.toLowerCase())
  )

  function handleCategorySelect(cat) {
    setForm({ ...form, category: cat })
    setSearch(cat)       // show selected value in the input
    setShowDropdown(false) // close dropdown
  }

  function handleSubmit() {
    onAdd(form)
    setForm({ date: '', description: '', amount: '', category: '' })
    setSearch('')
  }

  return (
    <div>
      <input
        placeholder="Date"
        value={form.date}
        onChange={e => setForm({ ...form, date: e.target.value })}
      />
      <input
        placeholder="Description"
        value={form.description}
        onChange={e => setForm({ ...form, description: e.target.value })}
      />
      <input
        placeholder="Amount"
        value={form.amount}
        onChange={e => setForm({ ...form, amount: e.target.value })}
      />

      {/* Searchable category dropdown */}
      <div style={{ position: 'relative', display: 'inline-block' }}>
        <input
          placeholder="Search category..."
          value={search}
          onChange={e => {
            setSearch(e.target.value)
            setShowDropdown(true)
          }}
          onFocus={() => setShowDropdown(true)}
        />
        {showDropdown && (
          <ul style={{
            position: 'absolute',
            background: 'white',
            border: '1px solid #ccc',
            listStyle: 'none',
            margin: 0,
            padding: 0,
            width: '100%',
            zIndex: 10
          }}>
            {filtered.map(cat => (
  <li
    key={cat}
    onClick={() => handleCategorySelect(cat)}
    onMouseEnter={e => e.target.style.backgroundColor = '#f0f0f0'}
    onMouseLeave={e => e.target.style.backgroundColor = 'white'}
    style={{ 
      padding: '6px 10px', 
      cursor: 'pointer',
      color: 'black',
      backgroundColor: 'white'
    }}
  >
    {cat}
  </li>
))}
            {filtered.length === 0 && (
              <li style={{ padding: '6px 10px', color: 'gray' }}>No match</li>
            )}
          </ul>
        )}
      </div>

      <button onClick={handleSubmit}>Add</button>
    </div>
  )
}

export default AddTransactionForm