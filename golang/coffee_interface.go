package main

// CoffeeInterface is the interface all struct will implement
type CoffeeInterface interface {
	GetCost() float32
	GetIngredients() string
}
