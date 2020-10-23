# Base image
FROM python:rc-buster

LABEL maintainer="Carlos Navas <dante.maniacs@gmail.com>"

WORKDIR /app

#
# INSTALL DEPENDENCIES IN PYTHON
#
# If you have dependencies in python and you want install them.
# Why don't we copy all files directly and then install the dependencies?
# Because the docker works in layers. If we do everything together
# and we change the files but not the dependencies we would also run
# the dependencies because they will be in the same layer.
#
# COPY requeriments.txt /app
# RUN pip install -r requeriments.txt

# Upgrade pip
RUN pip install --upgrade pip

COPY . /app

CMD ["python", "./app.py"]