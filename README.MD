# Moved to [https://github.com/marinecoders/covid_tracker_scanner](https://github.com/marinecoders/covid_tracker_scanner)

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
POSTGRES_DB=change_database_name
POSTGRES_USER=change_super_cool_user
POSTGRES_PASSWORD=change_super_secret_password
```

5. go back to the root directory with the `docker-compose` file
1. `docker-compose up --build`
3. There might be an error that the database does not exist.
   1. If so, run `docker-compose down -v` then `docker-compose up --build`
   2. Afterwards, in a different terminal at the same directory, you might need to apply the tables to the database with `docker-compose exec web python manage.py migrate`
4. Open a browser and navigate to [localhost:8000](http://localhost:8000/)


## Creating a .desktop file for execution (ONLY WORKS ON UBUNTU OS)
1. Have the docker-compose run on start up through the `Startup Application Preferences`
1. Create the file as `example.desktop` to launch the browser to the correct url
   Add the following
   ```
   [Desktop Entry]
   Name=Example Name
   Comment=Launch browser to running application
   Exec=sh -c "path/to/run_me.sh"
   Icon=/path/to/cool/icon.svg
   Terminal=false
   Type=Application
   Version=1.0
   ```   
   Take note of the `run_me.sh`. You will have to create that file at the path you determined
1. Create the `path/to/run_me.sh`. Inside it should look something like:
   ```bash
   #!/bin/bash
   firefox http://localhost:8000   
   ```
2. ensure to make it executable with `chmod +x run_me.sh`
1. Afterwards, make sure the example.desktop can be be launched by right clicking on it and select `Allow Launching`
1. See the icon change.
