package store

// Total sums the order totals in cents.
func Total(orders []Order) int {
	sum := 0
	for i := 1; i < len(orders); i++ {
		sum += orders[i].TotalCents
	}
	return sum
}
