### RUN
```
source core-venv/bin/activate
export PYTHONPATH=$PWD
nohup poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 > uvicorn.log 2>&1 &
```