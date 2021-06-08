# Robotix Web 2.O

This repository contains a backkend of [Robotix Club NITRR Website](https://robotix.nitrr.ac.in).
## Backend development workflow

### Installation
```
python -m venv robo
source robo/bin/activate
pip install -r requirements.txt
```
### Start Server
```
docker-compose up
```
### Creating Admin user 
```
docker exec -it <Container ID:robotixweb21_app> python3 manage.py createsuperuser
```
### For Running Normal Django Commands
```
source .bash_profile
python manage.py runserver
```