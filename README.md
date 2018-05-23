# SIMBION - Sistem Informasi Beasiswa Universitas Application
Tugas Akhir Basis Data

## Tech Stack
- Django
- PostgreSQL
- Bootstrap 4
- HTML / CSS


## Installation & Getting Started
```
virtualenv venv
source venv/bin/activate
pip install requirements.txt
python3 manage.py runserver
```

## Deploying in ITF Server
- ```ssh user.sso@kawung.cs.ui.ac.id```
- ```ssh http://152.118.25.3```
```
git clone https://gitlab.com/naufal.ihsan/simbion
python3 manage.py migrate
python3 manage.py runserver
```
- Running forever: edit settings.py and overwrite the default database configuration to production config
- Run ```nohup python3 manage.py runserver & > logs.txt```

### About Us
**Kelompok C06**
- Naufal Ihsan P
- M Yusuf Sholeh
- M Jihad Rinaldi
