# [SOCIALEYES](https://socialeyes-1884ceb59a89.herokuapp.com)

The aim of Socialeyes is to promote events that encourage people of all ages to socialize face to face through their interests/hobbies or charities to help improve mental health and conquer loneliness. This platform will give the space for users to have the ability to see upcoming events that may be of interest and to click 'I'll be attending' to sign up for events or they can add their own event if they want to. 

The second aim is to give fundraising events/charities a platform where they can share any events or needs that could help them out for users who may have a little spare time. The event coordinators will have the ability to add, update and delete events.

https://ui.dev/amiresponsive?url=https://socialeyes-1884ceb59a89.herokuapp.com

![screenshot](documentation/mockup.jpg)

Below you can see the charts I created to visualise the flow of the website and any error messages or actions needed depending on the user interaction. You can see on the charts I have worked out what data needs to be collected or added to the database depending on user interaction and what error messages need to be put in place incase of an unexpected/incorrect response.

<details>
<summary> Click here to see the flow charts </summary><br>

Data Collection
- ![screenshot](documentation/database-data-collection.jpg)

Events
- ![screenshot](documentation/user-authentication.jpg)

</details>


## UX

Socialeyes is created as a simple interactive website, making it user-friendly and simple to use as it has a wide age range of target audience. The website has been designed in a standard hierarchial tree structure so that the users does not to to click more than 3 times to get to their destination. This standard structure design means it can also be easily developed further in the future and has the potential to add many more features to it without the site looking overcrowded. It's a smooth journey to achieve what users are looking for with simple forms depending on what they need to do such as sign up or log in. 
The sign up form has only 4 inputs and log in has just 2 and both of which have a big blue highlighted button making it noticable for everyone to see using the hover button. To help the users further content hinting has also been implemented in the design to show users can scroll down for more content.
The purpose of the app is to encourage users of all ages and therefore some users may not be tech savvy which is why the site has a very basic approach which also keeps users on the website as if they are overloaded with information or a complex looking form it will lose the users attention. The type of site is also a site which users can or will be returning to as frequent as they want and so a simple design layout means it is easier to add new features accordingly for the admin. The branding was designed by myself by using speech marks as a respresentation of eyes followed by the brand name so that it is keeping to the convention of simplicity but it is also memorable so users will recognise the brand and boost it's popularity.

### Colour Scheme

The colour scheme of Socialeyes is a mix of contrasting colours which was influenced from the illustration I chose for the homepage. The colours work well together even though they are all completely different colours and this can symbolise the objective of the app, which is to bring different people from different backgrounds together. 
Also, according to colour psychology orange and blue both symbolise social communication, so these are the two I will carry out throughout the colour theme of the website.

- `#17268a` used as part of the logo.
- `#000000` used for primary text and logo.
- `#FFFFFF` used for primary highlights.
- `#17268a` used for secondary highlights.

I used [coolors.co](https://coolors.co/ffdfdb-f96d4d-17268a-ffb740-000000) to generate my colour palette which was also influnced by the illustration colours.

![screenshot](documentation/coolors.jpg)


### Typography

I have used Google fonts to help with the styles of the fonts used in the website.

- [Comfortaa](https://fonts.google.com/specimen/Comfortaa) was used for the primary headers and titles.

- [Poppins](https://fonts.google.com/specimen/Poppins) was used the logo branding and any secondary text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories

### New Site Users

- As a new site user, I would like to 'like' which events I want to attend, so that I can sign up for the event.
- As a new site user, I would like to like to be able to register for my own account so that I can sign up for events without having to fill in a form each time as it will already have my details stored.
- As a new site user, I would like to simply view a list of different events so that I can decide which I prefer.
- As a new site user, I would like to add my own events so that I can advertise any help needed for charities.
- As a new site user, I would like have simple access to the sites social media pages so I can contact for help if needed or provide feedback.

### Returning Site Users

- As a returning site user, I would like to edit, so that I can so that I can update any details of my event.
- As a returning site user, I would like to delete, so that I can delete my event if necessary.
- As a returning site user, I would like to have the option to unattend events, so that I can unattend if i can no longer go to that event.
- As a returning site user, I would like to login, so that I can view any events I will be attending.
- As a returning site user, I would like to log out, so that I am no longer kept signed in if I leave the site.

### Site Admin

- As a site administrator, I should be able to edit events, so that I can update any details of events if needed.
- As a site administrator, I should be able to delete events, so that I can delete events if the events are postponed or cancelled.
- As a site administrator, I should be able to have my own profile, so that I can see my own events created.
- As a site administrator, I should be able to add as many events as needed, so that I do not have any limits.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

<details>
<summary> Click here to see the Wireframes </summary>

Home
- ![screenshot](documentation/wireframes/home.png)

Events
- ![screenshot](documentation/wireframes/events.png)

Login
- ![screenshot](documentation/wireframes/login.png)

Sign up
- ![screenshot](documentation/wireframes/sign_up.png)

Profile
- ![screenshot](documentation/wireframes/profile.png)

Add/Edit Event
- ![screenshot](documentation/wireframes/add_edit_event.png)
</details>


## Features

### Existing Features

- **Navbar**

The navbar background colour has been blended into the colour of the callout section for the website design so it becomes part of the design of the page. For easier navigaition and readibility for the user the navbar is responsive and has a collapsable white side navbar for smaller devices up to tablet size devices. The navbar feature is essential for users to navigate through each page of the site and it is a feature the users will always depend on to achieve what they want to do or see on the site. 

![screenshot](documentation/feature1.jpg)
![screenshot](documentation/feature1-mobile.jpg)

- **Logo**

    - The logo sits within the navbar and following standard website conventions the logo is another way the user can 'click' their way back to the homepage for even simpler use of the site or app. The logo was designed by myself to represent the eyes in the word socialeyes by using ""speech marks as the concept is about socialising and communication between one another.
    I've used the shade of blue that's used within the hero image so the brand flows nicely into the design of the site.
    A logo increases brand awareness and recognition as the brand grows and people may even make a judgement based on how the logo makes them feel, which is one of the main values to having it on the website. 

![screenshot](documentation/feature2.jpg)

- **Callout header**

    - The callout header includes a header with the company slogan to capture the audiences attention along with a short description of the company's philosophy. If the user is not logged in it will also include log in or sign up buttons to make it easier for users to find what they want to do without having to look far. 

![screenshot](documentation/feature3.jpg)

- **Arrow Button**

    - An animated arrow displays on the home page to show users that you can scroll down to view more or click the arrow so it automatically jumps to the next section of the page. The use of animation clearly shows users that it is clickable.

![screenshot](documentation/feature4.jpg)

- **Hero Image**

    - The hero image is for aesthetic to make the website look visually appealing but to also demonstrate visually the purpose of the website at first glance. The hero image is a colourful illustration of people communicating amongst one another and each person looks visually different, which as I mentioned previous in the colour scheme section that the colours work well together even though they are all completely different colours and it is a good way to symbolise the objective of the app, which is to bring different people from different backgrounds together.
    The value a good designed site can bring is a good impression and returning customers due to its memorable design, and so the effective use of colour and imagery is important for first impressions.

![screenshot](documentation/feature5.jpg)

- **Cards**

    - Simple cards designed to display the events on the upcoming events section on the homepage but also for the events and profile page. Each card has details of the events name, description, location, date and time with an 'I'll be attending' button on each event for users to sign up to the event. If the users create their own event they instead will be shown the edit or delete button as it is their own event they do not need to be shown the option to attend.

![screenshot](documentation/feature6.jpg)

- **Footer**

    - The footer holds the links to social media pages which can increase following on social media or direct users to contact information if they have any queries or feedback. As common conventions I used the social media symbols through font awesome to respresent each social media brand as many are familiar with the icons. Each social media icon is black with the blue colour used throughout the site to highlight the icon on hover affect so that they stand out against the background colour of the footer which is the same colour as the hero image and navbar so it works with the flow of the design. 

![screenshot](documentation/feature7.jpg)


- **Login/Sign up Header/Events**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature8.jpg)

- **Login form**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature9.jpg)

- **Sign Up Form**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature10.jpg)

- **Login/Sign up link**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature11.jpg)

- **Profile Card**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature12.jpg)

- **Edit Event**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature13.jpg)

- **Add Event**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature14.jpg)

- **Delete Event**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature15.jpg)


- **Back to top arrow**

    - The link is very useful for returning users back to the top of the site page especially for mobile users as if there are many results displayed users would have to scroll all the way back up to the top of the page if they wanted to return to the start of the page. The value this adds will be keeping users on the site page as they will not get frustrated and leave the site if they have numerous results to scroll through to go back up the page.

![screenshot](documentation/feature16.jpg)


- **log out modal**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature17.jpg)


### Future Features

- Location filter #1
    - Users are shown events based on their location.
- Add 'Attending' button #2
    - Users are able to 'Attending' events they are interested in attending to show the event creator they are interested but also to add to the users profile as a reminder.
- Filter upcoming events by date #3
    - The ability to filter events by the closest dates on the upcoming events panel
- Attendee counter #4
    - Display how many people have said they are attending based on how many users have clicked 'attending'.
- Search filter
    - Users are able to search for events depending on what they want, such as 'duration of event' or 'charity event' etc.

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Materialize Web](https://materializeweb.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Flask](https://flask.palletsprojects.com) used as the Python framework for the site.
- [MongoDB](https://www.mongodb.com) used as the non-relational database management with Flask.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.

## Database Design

My project uses a non-relational database with MongoDB, and therefore the database architecture
doesn't have actual relationships like a relational database would.

My database is called **socialeyes**.

It contains 2 collections:

- **events**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | event_name | String | |
    | event_description | String | |
    | event_date | String | |
    | event_location | String | |
    | event_time | String | |
    | created_by | String | selected from the *users* collection |

- **users**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | username | String | |
    | password | String | uses Secure Hash Algorithm (SHA) |

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://socialeyes-1884ceb59a89.herokuapp.com).

### MongoDB Non-Relational Database

This project uses [MongoDB](https://www.mongodb.com) for the Non-Relational Database.

To obtain your own MongoDB Database URI, sign-up on their site, then follow these steps:

- The name of the database on MongoDB should be called **insert-your-database-name-here**.
- The collection(s) needed for this database should be **insert-your-collection-names-here**.
- Click on the **Cluster** name created for the project.
- Click on the **Connect** button.
- Click **Connect Your Application**.
- Copy the connection string, and replace `password` with your own password (also remove the angle-brackets).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `IP` | 0.0.0.0 |
| `MONGO_DBNAME` | user's own value |
| `MONGO_URI` | user's own value |
| `PORT` | 5000 |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: python app.py > Procfile`
- *replace **app.py** with the name of your primary Flask app name; the one at the root-level*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

If you are using SQLAlchemy for your project, you need to create a local PostgreSQL database.
In this example, the example database name is **db-name**.

```shell
workspace (branch) $ set_pg
workspace (branch) $ psql

... connection to postgres ...

postgres=# CREATE DATABASE db-name;
CREATE DATABASE
postgres=# \c db-name;
You are now connected to database "db-name" as user "foobar".
db-name=# \q
```

Once that database is created, you must migrate the database changes from your models.py file.
This example uses **app-name** for the name of the primary Flask application.

```shell
workspace (branch) $ python3

... connection to Python CLI ...

>>> from app-name import db
>>> db.create_all()
>>> exit()
```

To confirm that the database table(s) have been created, you can use the following:

```shell
workspace (branch) $ psql -d db-name

... connection to postgres ...

postgres=# \dt

	List of relations
Schema | Name | Type | Owner
-------+------+------+--------
public | blah1 | table | foobar
public | blah2 | table | foobar
public | blah3 | table | foobar

db-name=# \q
```

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps, plus a few extras.

Sample `env.py` file:

```python
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("MONGO_DBNAME", "user's own value")
os.environ.setdefault("MONGO_URI", "user's own value")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DB_URL", "user's own value")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
```

If using Flask-Migrate, make sure to include the following steps as well.

During the course of development, it became necessary to update the PostgreSQL data models.
In order to do this, [Flask-Migrate](https://flask-migrate.readthedocs.io) was used.

- `pip3 install Flask-Migrate`
- Import the newly installed package on your main `__init__.py` file:
	- `from flask_migrate import Migrate`
- Define **Migrate** in the same file after **app** and **db** are defined:
	- `migrate = Migrate(app, db)`
- Initiate the migration changes in the terminal:

```shell
workspace (branch) $ flask db init

	... generating migrations ...

workspace (branch) $ set_pg
workspace (branch) $ flask db migrate -m "Add a commit message for this migration"

	... migrating changes ...

workspace (branch) $ flask db upgrade

	... updating database ...
```

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/staceyJayneLewis/socialeyes) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git shell or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/staceyJayneLewis/socialeyes.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/staceyJayneLewis/socialeyes)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/staceyJayneLewis/socialeyes)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

No differences found on local and deployed site.

## Credits

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Dev to](https://dev.to/nehalahmadkhan/how-to-make-footer-stick-to-bottom-of-web-page-3i14) | footer | How to get a sticky footer if not enough content |
| [w3schools](https://www.w3schools.com/howto/howto_css_center-vertical.asp) | page header, edit and add page | used snippet of code to help align content vertically and horizontally. b0

### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [iStock](https://www.istockphoto.com) | Home page | hero image | hero image background (purchased the image as it was not free) |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |


### Acknowledgements
- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my partner William and my daughter Maeva, for believing in me, and allowing me to share my time to learn coding and make this transition into software development.


