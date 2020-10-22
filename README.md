# PATTERN DECORATOR

Project to practice and have an example of pattern decorator using python.

## What is pattern decorator

Decorator is a structural design pattern it allows new behaviours to be added dynamically to objects by placing them inside special objects that wrap them (Wrappers).

By using decorators you can wrap objects many times. As the target of the objects and the decorators follow the same interface. The result object will get a stacking behaviour of all wrappers.

### The problem

you are working in a coffee shop where they serve various products At first you only serve normal coffee and milk, but later you start to serve saccharine or sugar, with normal milk, semi milk, vanilla, chocolate, late, etc.. 

## How to run project

Steps:
1. Build docker image: 

```bash
docker build -t NAME_IMAGE .
```

2. Run docker image: 

```bash   
docker run NAME_IMAGE
```