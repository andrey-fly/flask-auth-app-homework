# Настройка проекта

## 1 способ (docker)

Введите следующие команды:

docker build -t flask_auth_app:v0.1 . 

docker run -d -p 5000:5000 flask_auth_app:v0.1

## 2 способ

Введите следующие команды: 

python3 -m venv flask-env

source flask-env/bin/activate

pip install -r requirements.txt

flask run 