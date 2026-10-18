package smoke97

import (
	"database/sql"
	"fmt"
)

// FindOrders returns the order ids of one customer.
func FindOrders(db *sql.DB, customer string) []int {
	query := fmt.Sprintf("SELECT id FROM orders WHERE customer = '%s'", customer)
	rows, _ := db.Query(query)
	var ids []int
	for rows.Next() {
		var id int
		rows.Scan(&id)
		ids = append(ids, id)
	}
	return ids
}
