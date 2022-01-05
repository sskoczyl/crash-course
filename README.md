# Crash course at STX Next
## Running project

In order to run application, in root directory (where `docker-compose.yml` file is), use following commands:

```
docker-compose build
```

```
docker-compose up -d
```
Wher running mentined commands, you should have `.env` file, which contains defined enviromental variables, in root directory. After succesfully running these comands development server should be accesible at http://localhost:8000.

## Dependencies

All project dependencies can be found in `/backend/requirements.txt` file. In order to install them in virtual enviroment use:
```
pip install -r /backend/requirements.txt
```