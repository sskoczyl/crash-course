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
## Migrations
When running the project fresh or after code updates (e.g. new model was added, switching to other branch) there may be need to apply migrations. In order to apply them, after running docker containers, execute following command:
```bash
docker-compose exec backend python manage.py migrate
```

## Tests
In order to run unit tests, after setting up docker containers, run command:
```bash
docker-compose exec backend python manage.py test
```

## Endpoints

After running server following endpoints are available:
* Registration- `/api/v1/accounts/register/`  
    In order to register, send `POST` request, with following data:
    ```json
    {
        "email": "example@mail.com",
        "password": "password123",
        "display_name": "example_name"
    }
    ```
    Password minimal length is 8. Field `display_name` is optional, request does not have to contain it. Default value for `display_name` is `None`, its maximal length is 30.
## Dependencies

All project dependencies can be found in `/backend/requirements.txt` file. In order to install them in virtual enviroment use:
```
pip install -r /backend/requirements.txt
```