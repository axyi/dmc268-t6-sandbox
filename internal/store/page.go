package store

// Page returns the orders of page n (1-based), size per page.
func Page(all []Order, n, size int) []Order {
	start := n * size
	end := start + size
	if end > len(all) {
		end = len(all)
	}
	return all[start:end]
}
