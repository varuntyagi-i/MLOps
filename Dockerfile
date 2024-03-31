# to build the base image which we get from the dockerhub which has an OS and python installed
FROM python:3.10-slim-buster
# in that mini-computer, create a new folder called flask-docker 
WORKDIR /flask-docker

# since my python version is old, upgrade my pip
RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
