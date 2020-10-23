import coffeeshop

# First we generate a concrete coffee.
myCoffee = coffeeshop.Concrete_Coffee()

print('> Concrete Coffee')
print('Ingredients: '   + myCoffee.get_ingredients())  
print('Cost: '          + str(myCoffee.get_cost())) 
print('Sales tax: '     + str(myCoffee.get_tax()))

# Adding milk to my coffee
myCoffee = coffeeshop.Milk(myCoffee)
print('\n>> Concrete Coffee with milk')
print('Ingredients: '   + myCoffee.get_ingredients())  
print('Cost: '          + str(myCoffee.get_cost())) 
print('Sales tax: '     + str(myCoffee.get_tax()))

# Adding sugar to my coffee
myCoffee = coffeeshop.Sugar(myCoffee)
print('\n>> Concrete Coffee with milk and sugar')
print('Ingredients: '   + myCoffee.get_ingredients())  
print('Cost: '          + str(myCoffee.get_cost())) 
print('Sales tax: '     + str(myCoffee.get_tax()))

# Adding vanilla to my coffee
myCoffee = coffeeshop.Vanilla(myCoffee)
print('\n>> Now I want a vanilla in my coffee:')
print('Ingredients: '   + myCoffee.get_ingredients())  
print('Cost: '          + str(myCoffee.get_cost())) 
print('Sales tax: '     + str(myCoffee.get_tax()))
