package main

// Milk decorator struct to add milk to coffee
type Milk struct {
	coffee Coffee
}

// GetCost get the cost of base coffee and plus the cost of milk complement
func (m *Milk) GetCost() float32 {
	coffeePrice := m.coffee.GetCost()
	return coffeePrice + 0.25
}

// GetIngredients get the ingrtedients and add the milk ingredient
func (m *Milk) GetIngredients() string {
	coffeeIngredients := m.coffee.GetIngredients()
	return coffeeIngredients + ", Milk"
}

// GetTax get the tax with milk
func (m *Milk) GetTax() float32 {
	return 0.1 * m.GetCost()
}
