FROM python:3.13-slim

# set the working directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy the src to the folder
COPY ./app /code/app