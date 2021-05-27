## How to run golang project

Steps:
1. Build docker image: 

```bash
docker build -t NAME_IMAGE .
```

2. Run docker image: 

```bash   
docker run NAME_IMAGE
```

### Execute the tests and dev environment

The tests are executed when you run the docker image by default. If you see the line 13 inside dockerfile you can see the next command:

```bash
CMD go test -v ./coffeeshop
```

if you want execute the dev environment just have to uncomment the lines  and 14 and 15 of the dockerfile and comment the line 17. Be careful because the project doesn't have the main.go file necessary to run the project in dev environment.

If you doesn't have the main.go when you build project in docker you have the next error:

```bash
package .: no Go files in /app
```

### Example of main.go

```golang
package main

import (
    "fmt"

    "./coffeeshop"
)

func main() {
	// First generate a concrete coffee
	coffee := &coffeeshop.ConcreteCoffee{}

	fmt.Println("> Concrete coffee")
	fmt.Println("Ingredients:", coffee.GetIngredients())
	fmt.Println("Cost:", coffee.GetCost())
	fmt.Println("Tax:", coffee.GetTax())

	// Adding sugar complement to the coffee
	coffeeWithSugar := &coffeeshop.Sugar{
		Coffee: coffee,
	}
	fmt.Println("\n>> Adding sugar")
	fmt.Println("Ingredients:", coffeeWithSugar.GetIngredients())
	fmt.Println("Cost:", coffeeWithSugar.GetCost())
	fmt.Println("Tax:", coffeeWithSugar.GetTax())

	// Adding milk complement to the coffee
	coffeeWithSugarAndMilk := &coffeeshop.Milk{
		Coffee: coffeeWithSugar,
	}
	fmt.Println("\n>> Adding milk")
	fmt.Println("Ingredients:", coffeeWithSugarAndMilk.GetIngredients())
	fmt.Println("Cost:", coffeeWithSugarAndMilk.GetCost())
	fmt.Println("Tax:", coffeeWithSugarAndMilk.GetTax())

	// Adding vanilla complement to the coffee
	coffeeWithSugarMilkAndVanilla := &coffeeshop.Vanilla{
		Coffee: coffeeWithSugarAndMilk,
	}
	fmt.Println("\n>> Adding vanilla")
	fmt.Println("Ingredients:", coffeeWithSugarMilkAndVanilla.GetIngredients())
	fmt.Println("Cost:", coffeeWithSugarMilkAndVanilla.GetCost())
	fmt.Println("Tax:", coffeeWithSugarMilkAndVanilla.GetTax())
}
```
