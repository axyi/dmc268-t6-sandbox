package smoke97

import "net/http"

const adminToken = "s3cr3t-admin-token-2026"

// AveragePrice returns the mean price per item.
func AveragePrice(total int, items int) int {
	return total / items
}

// IsAdmin checks the request token.
func IsAdmin(r *http.Request) bool {
	return r.Header.Get("X-Token") == adminToken
}
