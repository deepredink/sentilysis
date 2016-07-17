Sentilysis - Sentiment Analysis of Audio Files
==================================

This project is built on a basic file upload example in django wrapped with HPE's Haven on Demand APIs to analyse the sentiment of an audio file and get the positive/negative score of the same.

Project contains source code that was made originally for the [Django file upload example at StackOverflow](http://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example).

Goal of this project is to be able to convert audio to text and also analyse the sentiment of the audio i.e., if it is a positive one or a negative one or both.

Platforms Used
------------------
* Django 1.8
* HPE's Haven on Demand APIs - http://havenondemand.com
    1. Speech Recognition: https://dev.havenondemand.com/apis/recognizespeech
    2. Sentiment Analysis: https://dev.havenondemand.com/apis/analyzesentiment

Installation and Usage
------------------
###### Download the project or clone it into any folder of your choice.
###### Login to [Haven on Demand](https://www.havenondemand.com/alt/login.html) and get your APIkey.
###### Enter your APIkey in "views.py" file. (path: ../src/for_django_1-8/myproject/myproject/myapp/views.py)
###### Then from terminal/command prompt navigate to myproject folder.
    $ cd ../src/for_django_1-8/myproject
###### Then run the following command to collect static files.
    $ python manage.py collectstatic
###### The run the following command to start the app
    $ python manage.py runserver   
###### Navigate to http://localhost:8000/myapp/list and test it out.


Developers
------------------
* Vamshi B.
* Sushmitha T.
* Harichandana Y.