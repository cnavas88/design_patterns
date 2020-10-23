package main

import "fmt"

func main() {
	// First generate a concrete coffee
	coffee := &ConcreteCoffee{}

	fmt.Println("> Concrete coffee")
	fmt.Println("Ingredients:", coffee.GetIngredients())
	fmt.Println("Cost:", coffee.GetCost())
	fmt.Println("Tax:", coffee.GetTax())

	// Adding sugar complement to the coffee
	coffeeWithSugar := &Sugar{
		coffee: coffee,
	}
	fmt.Println("\n>> Adding sugar")
	fmt.Println("Ingredients:", coffeeWithSugar.GetIngredients())
	fmt.Println("Cost:", coffeeWithSugar.GetCost())
	fmt.Println("Tax:", coffeeWithSugar.GetTax())

	// Adding milk complement to the coffee
	coffeeWithSugarAndMilk := &Milk{
		coffee: coffeeWithSugar,
	}
	fmt.Println("\n>> Adding milk")
	fmt.Println("Ingredients:", coffeeWithSugarAndMilk.GetIngredients())
	fmt.Println("Cost:", coffeeWithSugarAndMilk.GetCost())
	fmt.Println("Tax:", coffeeWithSugarAndMilk.GetTax())

	// Adding vanilla complement to the coffee
	coffeeWithSugarMilkAndVanilla := &Vanilla{
		coffee: coffeeWithSugarAndMilk,
	}
	fmt.Println("\n>> Adding vanilla")
	fmt.Println("Ingredients:", coffeeWithSugarMilkAndVanilla.GetIngredients())
	fmt.Println("Cost:", coffeeWithSugarMilkAndVanilla.GetCost())
	fmt.Println("Tax:", coffeeWithSugarMilkAndVanilla.GetTax())
}
