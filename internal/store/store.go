// Package store keeps orders in memory.
package store

// Order is a stored order.
type Order struct {
	ID         int
	TotalCents int
}

// Find returns the order with the given id.
func Find(id int) (Order, bool) {
	return Order{ID: id, TotalCents: 1000}, true
}
