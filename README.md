Install Linux OS packages and dependencies as below

sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install git python3.8 postgresql postgresql-contrib

Setup Project

Clone project repository in current directory

git clone https://github.com/maulikpatel4u/flask-microservices.git

Create virtual environment

virtualenv -p python3.8 microservice_env

Install requirements.txt for both services.

pip install -r requirements.txt
