# Prediction Engine

> **Note**: If the model doesn't work. Prepare a new model [copying the notebook from here](https://colab.research.google.com/drive/1WaNfQf6xdVP3LoEJmfs5hwW1u9GDxgKE?usp=sharing).

## Installation Instructions

### Setup a virtualenv

```bash
python3 -m venv venv
```

### Activate virtualenv

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application
### Development Environment

```bash
flask run
```

### Production (for deployment)

```bash
gunicorn main:app
```
