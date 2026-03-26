import * as React from 'react'
import { PieChart } from '@mui/x-charts/PieChart'
import Typography from '@mui/material/Typography'
import Box from '@mui/material/Box'

export default function Charts({ data }) {
  // Group transactions by category and sum amounts
  const summary = {}
  data.forEach(t => {
    if (t.amount < 0) {  // only show expenses
      const cat = t.category || 'Uncategorized'
      summary[cat] = (summary[cat] || 0) + Math.abs(t.amount)
    }
  })

  // Format for MUI PieChart
  const chartData = Object.entries(summary).map(([label, value], id) => ({
    id,
    label,
    value: parseFloat(value.toFixed(2))
  }))

  if (chartData.length === 0) {
    return <Typography>No data to display</Typography>
  }

  return (
    <Box sx={{ width: '100%', mt: 4 }}>
      <Typography variant="h6">Spending by Category</Typography>
      <PieChart
        series={[{
          data: chartData,
          valueFormatter: (item) => `$${item.value}`
        }]}
        width={500}
        height={300}
      />
    </Box>
  )
}