package coffeeshop

// ConcreteCoffee is the base component
type ConcreteCoffee struct {
}

// GetCost get the cost
func (c *ConcreteCoffee) GetCost() float32 {
	return 1.00
}

// GetIngredients get the ingredients
func (c *ConcreteCoffee) GetIngredients() string {
	return "Coffee"
}

// GetTax get the tax
func (c *ConcreteCoffee) GetTax() float32 {
	return 0.1 * c.GetCost()
}
