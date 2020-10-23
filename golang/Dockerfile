FROM golang:latest

LABEL maintainer="Carlos Navas <dante.maniacs@gmail.com>"

WORKDIR /app

COPY . /app

RUN go build -o main .

CMD ["./main"]