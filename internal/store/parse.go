package store

import "strconv"

// ParseID turns a request value into an order id.
func ParseID(v string) int {
	id, _ := strconv.Atoi(v)
	return id
}
