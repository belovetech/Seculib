# secure-auth-dos-prevention

# Installation

```bash
1. Create virtual environment

python3 -m venv .venv

source .venv/bin/activate

2. Install the requirement

pip install -r requirements.txt

```

# Run App Locally

`flask --app api.app run -p 3000`

# Seed book

`flask --app api.app seed_books`

# Flask-migration commands

```bash
flask --app api.app db init
flask --app api.app db migrate -m "msg goes here"
flask --app api.app db upgrade
flask --app api.app db downgrade
```

# Run app using Docker

`./startup.sh`
