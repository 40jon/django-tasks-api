# Django Tasks API + JS Frontend

A small task manager built with a Django REST API and a vanilla JavaScript frontend.

## Features
- List, create, complete, and delete tasks
- Due dates and overdue flag (`is_overdue`)
- Simple HTML/JS frontend calling the API

## Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venvScriptsactivate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
