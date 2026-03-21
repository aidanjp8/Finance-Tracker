import { useReactTable, getCoreRowModel, flexRender } from '@tanstack/react-table'

const columns = [
  { accessorKey: 'date',        header: 'Date' },
  { accessorKey: 'description', header: 'Description' },
  { accessorKey: 'amount',      header: 'Amount', cell: (info) => formatAmount(info.getValue()) },
  { accessorKey: 'category',    header: 'Category' },
]

function formatAmount(amount) {
  if (amount < 0) {
    return <span style={{ color: 'red' }}>{amount}</span>
  } else {
    return <span style={{ color: 'green' }}>+{amount}</span>
  }
}

export default function SimpleTable({ data }) {
  const table = useReactTable({ data, columns, getCoreRowModel: getCoreRowModel() })

  return (
    <table>
      <thead>
        {table.getHeaderGroups().map((hg) => (
          <tr key={hg.id}>
            {hg.headers.map((header) => (
              <th key={header.id}>
                {flexRender(header.column.columnDef.header, header.getContext())}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody>
        {table.getRowModel().rows.map((row) => (
          <tr key={row.id}>
            {row.getVisibleCells().map((cell) => (
              <td key={cell.id}>
                {flexRender(cell.column.columnDef.cell, cell.getContext())}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  )
}