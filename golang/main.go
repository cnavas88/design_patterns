package main

import "fmt"

func main() {
	// First generate a concrete coffee
	coffee := &ConcreteCoffee{}

	fmt.Println("> Concrete coffee")
	fmt.Println("Ingredients:", coffee.GetIngredients())
	fmt.Println("Cost:", coffee.GetCost())
	fmt.Println("Tax:", coffee.GetTax())

	// Adding sugar complement to coffee
	coffeeWithSugar := Sugar{
		coffee: coffee,
	}
	fmt.Println("\n>> Adding sugar")
	fmt.Println("Ingredients:", coffeeWithSugar.GetIngredients())
	fmt.Println("Cost:", coffeeWithSugar.GetCost())
	fmt.Println("Tax:", coffeeWithSugar.GetTax())
}
