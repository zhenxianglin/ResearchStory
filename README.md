# Group 19: Research Stories
## **Introduction**
Documenting impact of research is needed for various reasons including evaluating research impact, motivating young researchers, and sharing knowledge in general. The goal of this project is to develop an online software service to identify research stories and make them available for general audience on a dedicated video channel.
Our potential users are those who want to share and fin novel and interesting research papaers, as well as long term impact of research.
<br></br>
## **Catalogue**

- [Environment Preparation](#Environment-Preparation)
- [How to start](#How-to-start)
- [Feature Instruction](#Feature-Instruction)

<br></br>
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
<br></br>
## **How to start**
After the preparation of environment, you can run the server.
We have provided an Amazon AWS database.
<br></br>
If you want to use it, you can run the server directly by
```sh
$ python manage.py runserver 8000
```
<br></br>
If you want to use your own database, you need to change the argument DATABASE in [ResearchStory/settings.py](https://github.com/blastxiaol/ResearchStory/blob/front-end/ResearchStory/settings.py#L125) and set your own database.
Then, you need to migrate you database by
```sh
$ python manage.py migrate
```
At last, you can start the server by
```sh
$ python manage.py runserver 8000
```
<br></br>
## **Feature Instruction**
We also deploy the website. Its url is [https://researchstory-19.herokuapp.com/](https://researchstory-19.herokuapp.com/)
<br></br>
Input url can open the website. Here is the front-page of the website.
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/1.png)
<br></br>
As a user, first need to register an account. Click the “username” button(top-right), then choose [“Register"](https://researchstory-19.herokuapp.com/Users/register/) to go to register page. If the user already has an account, then choose [“Login”](https://researchstory-19.herokuapp.com/Users/login/) to go to login page. Here are register and login pages. 
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/2.png)
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/3.png)
<br></br>
After logging in, if this is a researcher user, [“Add story”](https://researchstory-19.herokuapp.com/story/upload/) button will be shown on the navigation bar. A common user cannot see this button. As a researcher user, click the “Add story” button to go to upload story page. Researcher can input their research story content, and add a front-page of their story. Here is the upload story page.
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/4.png)
<br></br>
After the researcher user uploading a story, maybe we want to look at the story. whatever a user’s type are, researcher or common user, even just a visitor who does not have an account, anyone can browse or search stories. Click the [“Story”](https://researchstory-19.herokuapp.com/story/) button on the navigation bar, all stories are shown on the page. We also can click the “Research area” button that next to “Story” and choose a category such as [“Computer Science”](https://researchstory-19.herokuapp.com/story/category=ComputerScience), or click a category that below to the navigation bar, to look at the stories belong to a specific category. Furthermore, we can ask the stories to order by created time or views. Just click [“Latest Stories”](https://researchstory-19.herokuapp.com/story/category=ALL_sort_by=time_title=_all) or [“Most Viewed”](https://researchstory-19.herokuapp.com/story/category=ALL_sort_by=hot_title=_all) button so that can achieve requirements. The following picture shows engineering stories sorted by views.
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/5.png)
<br></br>
Search bar also can be used by anyone. Type the keywords can search the corresponding stories. Or click [“Advanced Search”](https://researchstory-19.herokuapp.com/story/advancedSearch=T) button to choose more conditions so that achieve more refined search. Here is the advanced search alert.
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/6.png)
<br></br>
To have a look at a story, click the [story title](https://researchstory-19.herokuapp.com/story/story_id=73). We can browse the story content and watch the corresponding video. Here is a story content page.
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/7.png)
<br></br>
A user(researcher or common user) can post comments below a story, and others can reply comments. Here are comment area and reply box.
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/8.png)
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/9.png)
<br></br>
If We are interested in the research story, we can book an interview about the researcher of the story, click the black button [“welcome to make interview appointment with Researcher”](https://researchstory-19.herokuapp.com/new_interview/73) to go to the booking page. Then a interview summary will be shown on the day of booking. Here are booking page and summary page.
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/10.png)
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/11.png)
<br></br>
Similar to interview, if users want to have a meeting with public, click [“meeting”](https://researchstory-19.herokuapp.com/meeting/) button on the navigation bar, and click [“Add A New Meeting”](https://researchstory-19.herokuapp.com/meeting/new_meeting) button so that they can book a meeting, then the meeting summary will be shown on the meeting page. The difference between meeting and interview is that only one incoming interview summary about a research story will be shown on the story page, even there are many interviews, while all incoming meeting summaries will be shown on the meeting page. Both meetings and interviews will take place in Teams. Here are booking meeting page and meeting summary page.
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/12.png)
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/13.png)
<br></br>
Besides uploading research story, users also can upload videos. Click [“Video”](https://researchstory-19.herokuapp.com/video_list/) button, user can look at all videos. To click a specific [video title](https://researchstory-19.herokuapp.com/video_list/5/), user can watch a video and post or reply comments. User also can upload their video, click [“upload a new interview video meeting”](https://researchstory-19.herokuapp.com/new_video/) can achieve uploading. Here are video page, a specific video page and the uploading page.
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/14.png)
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/15.png)
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/16.png)
<br></br>
Users who logged in can discuss in Forum. Click [“Forum”](https://researchstory-19.herokuapp.com/forum/) button on the navigation bar, all threads will be shown on the page. click a [thread title](https://researchstory-19.herokuapp.com/forum/forum_id=8) can browse the thread content and users can post any comments or reply others. Here are forum page and a specific thread page.
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/17.png)
<br></br>
![](https://github.com/blastxiaol/ResearchStory/blob/front-end/readme_img/18.png)
<br></br>
