package main

import "fmt"

func main() {
	// First generate a concrete coffee
	coffee := &ConcreteCoffee{}

	fmt.Println("> Concrete coffee")
	fmt.Println("Ingredients:", coffee.GetIngredients())
	fmt.Println("Cost:", coffee.GetCost())
	fmt.Println("Tax:", coffee.GetTax())
}
