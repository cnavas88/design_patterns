package main

import (
	"testing"

	"./coffeeshop"
)

func TestConcreteCoffee(t *testing.T) {
	coffee := &coffeeshop.ConcreteCoffee{}

	if coffee.GetCost() != 1.00 {
		t.Errorf("Expected cost 1.00, but got %v", coffee.GetCost())
	}

	if coffee.GetTax() != 0.1 {
		t.Errorf("Expected tax 0.1, but got %v", coffee.GetTax())
	}

	if coffee.GetIngredients() != "Coffee" {
		t.Errorf("Expected ingredients 'coffee', but got %v", coffee.GetIngredients())
	}
}

func TestAddSugar(t *testing.T) {
	coffee := &coffeeshop.ConcreteCoffee{}

	coffeeWithSugar := &coffeeshop.Sugar{
		Coffee: coffee,
	}

	if coffeeWithSugar.GetCost() != 1.00 {
		t.Errorf("Expected cost 1.00, but got %v", coffeeWithSugar.GetCost())
	}

	if coffeeWithSugar.GetTax() != 0.1 {
		t.Errorf("Expected tax 0.1, but got %v", coffeeWithSugar.GetTax())
	}

	if coffeeWithSugar.GetIngredients() != "Coffee, Sugar" {
		t.Errorf("Expected ingredients 'coffee, Sugar', but got %v", coffeeWithSugar.GetIngredients())
	}
}

func TestAddSugarAndMilk(t *testing.T) {
	coffee := &coffeeshop.ConcreteCoffee{}

	coffeeWithSugar := &coffeeshop.Sugar{
		Coffee: coffee,
	}

	coffeeWithSugarMilk := &coffeeshop.Milk{
		Coffee: coffeeWithSugar,
	}

	if coffeeWithSugarMilk.GetCost() != 1.25 {
		t.Errorf("Expected cost 1.25, but got %v", coffeeWithSugarMilk.GetCost())
	}

	if coffeeWithSugarMilk.GetTax() != 0.125 {
		t.Errorf("Expected tax 0.125, but got %v", coffeeWithSugarMilk.GetTax())
	}

	if coffeeWithSugarMilk.GetIngredients() != "Coffee, Sugar, Milk" {
		t.Errorf("Expected ingredients 'Coffee, Sugar, Milk', but got %v", coffeeWithSugarMilk.GetIngredients())
	}
}

func TestAddAllIngredients(t *testing.T) {
	coffee := &coffeeshop.ConcreteCoffee{}

	coffeeWithSugar := &coffeeshop.Sugar{
		Coffee: coffee,
	}

	coffeeWithSugarMilk := &coffeeshop.Milk{
		Coffee: coffeeWithSugar,
	}

	coffeeAllIngredients := &coffeeshop.Vanilla{
		Coffee: coffeeWithSugarMilk,
	}

	if coffeeAllIngredients.GetCost() != 2.00 {
		t.Errorf("Expected cost 2.00, but got %v", coffeeAllIngredients.GetCost())
	}

	if coffeeAllIngredients.GetTax() != 0.2 {
		t.Errorf("Expected tax 0.2, but got %v", coffeeAllIngredients.GetTax())
	}

	if coffeeAllIngredients.GetIngredients() != "Coffee, Sugar, Milk, Vanilla" {
		t.Errorf("Expected ingredients 'Coffee, Sugar, Milk, Vanilla', but got %v", coffeeAllIngredients.GetIngredients())
	}
}
