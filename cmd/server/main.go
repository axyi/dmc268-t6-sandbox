package main

import (
	"fmt"

	"example.com/sandbox/internal/store"
)

func describe(id int) string {
	order, ok := store.Find(id)
	if !ok {
		return "missing"
	}
	return fmt.Sprintf("order %d: %d cents", order.ID, order.TotalCents)
}

func main() {
	fmt.Println(describe(1))
}
