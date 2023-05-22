#! /bin/bash

python manage.py migrate
python manage.py database_seed
