FROM golang:latest

LABEL maintainer="Carlos Navas <dante.maniacs@gmail.com>"

# Set the current directory inside the container
WORKDIR /app

COPY . .

# Build the go app
RUN go build -o .

CMD go test -v ./coffeeshop