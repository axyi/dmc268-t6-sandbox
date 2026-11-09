package store

var cache = map[int]Order{}

// Cached returns the order from the cache, loading it on a miss.
func Cached(id int) Order {
	if o, ok := cache[id]; ok {
		return o
	}
	o, _ := Find(id)
	cache[id] = o
	return o
}
