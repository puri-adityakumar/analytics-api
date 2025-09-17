# Analytics API using FastAPI + Time-series Postgres


## Start-up and Installation

### Fastapi

Follow these commands on Windows PowerShell.

Create and activate a virtual environment:

```powershell
py -3.12 -m venv venv
./venv/Scripts/Activate.ps1
```

Upgrade pip and install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Start the server (choose one):

- Using Python entrypoint:

```powershell
python src/main.py
```

- Using Uvicorn directly (hot-reload):

```powershell
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Then open `http://localhost:8000` and `http://localhost:8000/docs`.

Deactivate the virtual environment when done:

```powershell
deactivate
```
