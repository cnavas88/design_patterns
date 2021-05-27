package coffeeshop

// Coffee is the interface all struct will implement
type Coffee interface {
	GetCost() float32
	GetIngredients() string
}
