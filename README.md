# Python Flask Microservices

Install Linux OS packages and dependencies as below
```linux
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install git python3.8 postgresql postgresql-contrib
```

**Setup Project**
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

Create two seperate databases for user and invoice microservies
```inux
sudo -u postgres psql
CREATE DATABASE user_local;
CREATE DATABASE invoice_local;
CREATE USER trellis WITH PASSWORD 'Trellis123';
GRANT ALL PRIVILEGES ON DATABASE user_local TO trellis;
GRANT ALL PRIVILEGES ON DATABASE invoice_local TO trellis;
```

Now, Apply migration in both services.
```inux
cd invoice
flask db upgrade
cd user
flask db upgrade
```

Now, for shell plus
```inux
cd invoice or cd user
flask shell
```
