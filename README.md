**Python Flask Microservices**

Install Linux OS packages and dependencies as below
```linux
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install git python3.8 postgresql postgresql-contrib
```

# Setup Project
Clone project repository in current directory
```inux
git clone https://github.com/maulikpatel4u/flask-microservices.git
```

Create virtual environment
```inux
virtualenv -p python3.8 microservice_env
```

Install requirements.txt for both services.
```inux
pip install -r requirements.txt
```
