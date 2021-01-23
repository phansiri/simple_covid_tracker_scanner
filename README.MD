# Simple Covid Tracker with CAC scanner

## Set Up
1. `git clone https://github.com/phansiri/simple_covid_tracker_scanner.git`
2. `cd simple_covid_tracker_scanner`
3. Create `.env` in the `covid_project` directory with something like:
```.env
DJ_SECRET_KEY=super-secret-key
DJ_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] 0.0.0.0
DJ_DEBUG=True
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=change_database_name
SQL_USER=change_super_cool_user
SQL_PASSWORD=change_super_secret_password
SQL_HOST=db
SQL_PORT=5432
```
4. Create `.env.db` in the `covid_project` directory with something like:

```.env
POSTGRES_DB=hange_database_name
POSTGRES_USER=change_super_cool_user
POSTGRES_PASSWORD=change_super_secret_password
```

5. go back to the root directory with the `docker-compose` file
1. `docker-compose up --build`
3. There might be an error that the database does not exist.
   1. If so, run `docker-compose down -v` then `docker-compose up --build`
   2. Afterwards, in a different terminal at the same directory, you might need to apply the tables to the database with `docker-compose exec web python manage.py migrate`
4. Open a browser and navigate to `[localhost:](http://localhost:8000/)`