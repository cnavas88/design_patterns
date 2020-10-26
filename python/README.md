## How to run python project

Steps:
1. Build docker image: 

```bash
docker build -t NAME_IMAGE .
```

2. Run docker image: 

```bash   
docker run NAME_IMAGE
```

### Execute the tests

The project is configured to run tests automatically when you run docker image. See dockerfile.