# secure-auth-dos-prevention

# Installation

```bash
1. Create virtual environment

python3 -m venv .venv

2. Install the requirement

pip install -r requirements.txt

```

# Run App

`flask run --debug`

# Monitoring tools

`ab -n 1000 -c 10 http://127.0.0.1:5000/unprotected`
