# backend_python_prueba
INSTRUCTIONS

* Open a terminal within the project
* In the app.py file change the path where the JSON file will be saved in the best and last functions
* Save changes
* Run the command python app.py to start the Flask server
* In the browser type: localhost: 4000 to see the details of the routes

PATHS OF PROYECTS

The project runs on 127.0.0.1:4000 or localhost: 4000

The provided paths of ben to be typed in the browser bar

Regarding the service of obtaining the 20 best and latest podcasts, the path where the file will be created within the project must be established

JSON data was used as source

Service to search podcast by artist name (artistName)
    path: / podcast / artist name
    Some names you can try:
        iHeartRadio
        Joe rogan
        Armchair Umbrella
    For the service of saving the top 20 in a JSON
    path: / best20 - Create a file inside the project folder
    To replace the top 20 podcasts with the bottom 20 in a JSON file
    path: / last20 - Replaces the content of the created archive of the top 20 podcasts
    To delete podcast by artist name (artistName)
    path: / podcastdel / artist name>

Using a SQLite3 database called: podcast.db

  Service that lists the twenty podcasts in the database
    path: / podcastdb - They are listed in JSON format

DESCRIPTION OF APP.PY
    
The app.py file is the initial file this needs to be executed in order to start the services, within it the following routes were established:

* first route - (/) shows the HTML page with the details of the routes this route makes use of the content in the static and templates folders to work.
* second path - (/podcast) used to test server response
* third path - (/podcast/<string:name>) is to search for a podcast by artist name
* fourth path - (/best20) create a JSON file with the top 20 podcasts
* fifth path - (/last20) replace the top 20 with the last top 20 podcasts in the same file
* sixth path - (/podcastdel) remove a podcast by artist name
* seventh path - (/podcastdb) lists the 20 podcasts from a SQLite3 database, said database is in the project: database / podcast.db
