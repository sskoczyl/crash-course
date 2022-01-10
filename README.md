# Crash course at STX Next
## Running project

In order to run application, in root directory (where `docker-compose.yml` file is), use following commands:

```
docker-compose build
```

```
docker-compose up -d
```
When running mentioned commands, you should have `.env` file, which contains defined enviromental variables, in root directory. Exampe contents of `.env` are shown in `example_env` file (it contains all enviromental variables used by project).  After succesfully running these comands development server should be accesible at http://localhost:8000. If you want to stop running containers and remove them and any networks that were created, in root folder, run:

```
docker-compose down
```

## Dependencies

All project dependencies can be found in `/backend/requirements.txt` file. In order to install them in virtual enviroment use:
```
pip install -r /backend/requirements.txt
```