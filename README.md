# PATTERN DECORATOR

Project to practice and have an example of pattern decorator using python.

## What is pattern decorator

Decorator is a structural design pattern it allows new behaviours to be added dynamically to objects by placing them inside special objects that wrap them (Wrappers).

By using decorators you can wrap objects many times. As the target of the objects and the decorators follow the same interface. The result object will get a stacking behaviour of all wrappers.

### The problem

you are working in a coffee shop where they serve various products At first you only serve normal coffee and milk, but later you start to serve saccharine or sugar, with normal milk, semi milk, vanilla, chocolate, late, etc.. 

### Solution

when we have to alter the funcionality of an object. The first it comes in my mind is extend a class. However, the 
inheritance has several important limitations.

1. The inheritance is static. We can't alter the funcionality of an exist object during execution time. Only can replace the whole object by other created from a different subclass.

2. Subclases just can have a father class. In the majority lenguages, the inheritance doesn't allow to a class inherit behaviours of several classes at the same time.

To solve this problem we can use the pattern decorator (Wrapper). The wrapper implements the same interface as the wrapped object. This is why, from the customer's perspective, these objects are identical.

The solution is in 2 languages: Golang and Python.