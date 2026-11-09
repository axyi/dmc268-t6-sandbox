package store

// ApplyDiscount returns the order total after a percentage discount.
func ApplyDiscount(o Order, percent int) int {
	off := o.TotalCents * percent / 100
	return o.TotalCents - off
}
