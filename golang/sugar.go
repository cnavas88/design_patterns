package main

// Sugar decorator struct to add sugar to coffee
type Sugar struct {
	coffee Coffee
}

// GetCost get the cost of base coffee and plus the cost of sugar complement
func (s *Sugar) GetCost() float32 {
	coffeePrice := s.coffee.GetCost()
	return coffeePrice
}

// GetIngredients get the ingrtedients and add the sugar ingredient
func (s *Sugar) GetIngredients() string {
	coffeeIngredients := s.coffee.GetIngredients()
	return coffeeIngredients + ", Sugar"
}

// GetTax get the tax with Sugar
func (s *Sugar) GetTax() float32 {
	return 0.1 * s.GetCost()
}
