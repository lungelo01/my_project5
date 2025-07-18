
# Django capstone project

This is a Django-based web application built as part of the Capstone Project. It includes a virtual environment setup, Sphinx documentation, and a Docker container for easier deployment.

## Authors

- [@Lungelo](https://www.github.com/lungelo01)

## Tech Stack
**client:** HTML, CSS, BOOTSTRAP
**Server:** python, django, 

## Setup instruction 
install python 

```bash
  python3 -m venv venv
```

for local development set up a virtual environment and activate it 

for windows:

```bash
  myworld\Scripts\activate.bat
```

for Unix or MacOS:

```bash
  source myworld/bin/activate
```

install django on your computer

```bash
  python -m pip install Django
```

install dependencies

```bash
  pip install -r requirements.txt
```

set up environment variables

```bash
  OPENAI_API_KEY=your_api_key_here
```

run the application

```bash
  python app.py
```

## setup docker

install docker

clone the repository

```bash
  https://github.com/lungelo01/my_project5
  cd fictional_band
```

create a .env file

```bash
  OPENAI_API_KEY=your_api_key_here
```

build the docker image

```bash
  docker build -t fictional_band
```

run the docker container 

```bash
  docker run --env-file .env -p 8000:8000 fictional_band
```

access the application by navigating to http://localhost:8000 in your web browse
## Running Tests

To run tests, run the following command

```bash
  python manage.py runserver
```

## Support

For support, email Lungelo@gmail.com 

## Run Locally

Clone the project

```bash
  git clone https://github.com/lungelo01/myProject
```

run with virtual environment

```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    "# consolidation_project_consolidation" 
```
