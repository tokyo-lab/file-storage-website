# url-shortener

# Python virtual enviornment set up

Python 3 comes with a virtual enviornment module built-in called 'venv'. There's no need to download anything. Just jump in and create a vm

1- In terminal navigate to the project folder

2 - To create a virtual enviornment. In this example calling it 'urlshort':

    python3 -m venv urlshort_venv

3 - Activate the virtual enviornment by sourcing the activate script in its bin directory

    source urlshort_venv/bin/activate

4 - To deactivate the virtual enviornment, just type 'deactivate':

    deactivate

5 - In .gitignore file, you may want to add the virtual enviornment folder as 'venv/' is not picking the folder up.

6 - To delete, just delete the virtual enviornment folder from the project directory

# Using Flask

The flask command is installed by Flask, not your application; it must be told where to find your application in order to use it. The FLASK_APP environment variable is used to specify how to load the application.

Unix Bash (Linux, Mac, etc.):

    export FLASK_APP=hello
    flask run

To switch Flask to the development environment and enable debug mode, set FLASK_ENV:

    export FLASK_ENV=development
    flask run

# To run the app

Be on the top project directory (url-shortener), start the venv

    source urlshort_venv/bin/activate

In terminal set the FLASK_APP as follow:

    export FLASK_APP=urlshort

Next, set the FLASK_ENV:

    LASK_ENV=development

Run the flask app

    flask run
