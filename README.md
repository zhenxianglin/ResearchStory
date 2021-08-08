# Group 19: Research Stories
## **Introduction**
Documenting impact of research is needed for various reasons including evaluating research impact, motivating young researchers, and sharing knowledge in general. The goal of this project is to develop an online software service to identify research stories and make them available for general audience on a dedicated video channel.
<br><br/>
## **Environment Preparation**
This project is based on python 3.7.4.
It has prepared virtual environment. 
If you want to use virtual environment, you can
```sh
$ source venv/bin/activate
```
All packets we use are listed in requirements.txt.
If you want to your own environment, you should install the packets as follows:
```sh
$ pip install -r requirements.txt
```
<br><br/>
## **How to start**
After the preparation of environment, you can run the server.
We have provided an Amazon AWS database.
<br><br/>
If you want to use it, you can run the server directly by
```sh
$ python manage.py runserver 8000
```
<br><br/>
If you want to use your own database, you need to change the argument DATABASE in [ResearchStory/settings.py](https://github.com/blastxiaol/ResearchStory/blob/front-end/ResearchStory/settings.py#L125) and set your own database.
Then, you need to migrate you database by
```sh
$ python manage.py migrate
```
At last, you can start the server by
```sh
$ python manage.py runserver 8000
```
