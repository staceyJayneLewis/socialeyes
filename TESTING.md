# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files. For the files that require to be logged in I have used the [validate by input](https://validator.w3.org/#validate_by_input) method as any code with jinja will not validate properly if you're copying/pasting into the HTML validator.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsocialeyes-1884ceb59a89.herokuapp.com%2Fhome) | ![screenshot](documentation/html_home.jpg) | No errors to show |
| Login | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsocialeyes-1884ceb59a89.herokuapp.com%2Flogin) | ![screenshot](documentation/html_login.jpg) | No errors |
| Sign Up | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsocialeyes-1884ceb59a89.herokuapp.com%2Fsign_up) | ![screenshot](documentation/html_sign_up.jpg) | No Errors |
| Profile | W3C | ![screenshot](documentation/html_profile.jpg) | No Errors |
| Events | W3C | ![screenshot](documentation/html_events.jpg) | No Errors |
| Add Event | W3C | ![screenshot](documentation/html_add_event.jpg) | No Errors |
| Edit Event | W3C | ![screenshot](documentation/html_edit.jpg) | No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fsocialeyes-1884ceb59a89.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/css.jpg) | Third party tool errors which have all come from materialize or font awesome |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| script.js | ![screenshot](documentation/js.jpg) | Unused variables from external files |


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| app.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/staceyJayneLewis/socialeyes/main/app.py) | ![screenshot](documentation/python-linter.jpg) | No errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Login | Sign Up | Profile | Events | Add Events | Edit Events |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/chrome-home-compat.jpg) | ![screenshot](documentation/chrome-login-compat.jpg) | ![screenshot](documentation/chrome-singup-compat.jpg) | ![screenshot](documentation/chrome-profie-compat.jpg) | ![screenshot](documentation/chrome-events-compat.jpg) | ![screenshot](documentation/chrome-addevents-compat.jpg) | ![screenshot](documentation/chrome-editevents-compat.jpg) | Works as expected |
| Firefox | ![screenshot](documentation/firefox-home.jpg) | ![screenshot](documentation/firefox-login.jpg) | ![screenshot](documentation/firefox-signup.jpg) | ![screenshot](documentation/firefox-profile.jpg) | ![screenshot](documentation/firefox-events.jpg) | ![screenshot](documentation/firefox-addevent.jpg) | ![screenshot](documentation/firefox-edit.jpg) | Works as expected |
| Brave | ![screenshot](documentation/brave-home.jpg) | ![screenshot](documentation/brave-login.jpg) | ![screenshot](documentation/brave-signup.jpg) | ![screenshot](documentation/brave-profile.jpg) | ![screenshot](documentation/brave-events.jpg) | ![screenshot](documentation/brave-add-event.jpg) | ![screenshot](documentation/brave-edit-event.jpg) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Login | Sign up | Profile | Events | Add Events | Edit Event |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive-home.gif) | ![screenshot](documentation/responsive-login.gif) | ![screenshot](documentation/responsive-signup.gif) | ![screenshot](documentation/responsive-profile.gif) | ![screenshot](documentation/responsive-events.gif) | ![screenshot](documentation/responsive-add-events.gif) |![screenshot](documentation/responsive-edit.gif) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet-home.gif) | ![screenshot](documentation/responsive-tablet-login.gif) | ![screenshot](documentation/responsive-tablet-signup.gif) | ![screenshot](documentation/responsive-tablet-profile.gif) | ![screenshot](documentation/responsive-events.gif) | ![screenshot](documentation/responsive-tablet-addevent.gif) |![screenshot](documentation/responsive-tablet-edit.gif) | Works as expected |
| Desktop | ![screenshot](documentation/responsive-desktop-home.gif) | ![screenshot](documentation/responsive-desktop-login.gif) | ![screenshot](documentation/responsive-desktop-signup.gif) | ![screenshot](documentation/responsive-desktop-profile.gif) | ![screenshot](documentation/responsive-desktop-events.gif) | ![screenshot](documentation/responsive-desktop-addevent.gif) | ![screenshot](documentation/responsive-desktop-edit.gif) | Works as expected |
| Google Pixel 7 | ![screenshot](documentation/google-pixel7-home.png) | ![screenshot](documentation/google-pixel7-home2.png) | ![screenshot](documentation/google-pixel7-login.png) | ![screenshot](documentation/google-pixel7-signup.png) | ![screenshot](documentation/google-pixel7-profile.png) | ![screenshot](documentation/google-pixel7-events.png) | ![screenshot](documentation/google-pixel7-addevent.png) | ![screenshot](documentation/google-pixel7-edit.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-mobile-home.jpg) | ![screenshot](documentation/lighthouse-desktop-home.jpg) | Mobile: minor warnigns on mobile from external files(heroku, cdn links) etc, Desktop: PASS |
| Log in | ![screenshot](documentation/lighthouse-mobile-login.jpg) | ![screenshot](documentation/lighthouse-desktop-login.jpg) | Mobile: minor warnigns on mobile from external files(heroku, cdn links) etc, Desktop: PASS |
| Sign up | ![screenshot](documentation/lighthouse-mobile-signup.jpg) | ![screenshot](documentation/lighthouse-desktop-signup.jpg) | Mobile: minor warnigns on mobile from external files(heroku, cdn links) etc, Desktop: PASS |
| Profile | ![screenshot](documentation/lighthouse-mobile-profile.jpg) | ![screenshot](documentation/lighthouse-desktop-profile.jpg) | Mobile: minor warnigns on mobile from external files(heroku, cdn links) etc, Desktop: PASS |
| Events | ![screenshot](documentation/lighthouse-mobile-events.jpg) | ![screenshot](documentation/lighthouse-desktop-events.jpg) | Mobile: minor warnigns on mobile from external files(heroku, cdn links) etc, Desktop: PASS |
| Add Event | ![screenshot](documentation/lighthouse-mobile-addevents.jpg) | ![screenshot](documentation/lighthouse-desktop-addevents.jpg) | Mobile: minor warnigns on mobile from external files(heroku, cdn links) etc, Desktop: PASS |
| Edit Event | ![screenshot](documentation/lighthouse-mobile-edit.jpg) | ![screenshot](documentation/lighthouse-desktop-edit.jpg) | Mobile: minor warnigns on mobile from external files(heroku, cdn links) etc,  Desktop: PASS |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Log in | | | | | |
| | User should not be permitted to submit empty form | Tested the feature by clicking the log in button to see if submits the form with empty inputs | The feature behaved as expected, 'log in' button clicked and prompt came up telling user to fill in event name field | Test concluded and passed | ![screenshot](documentation/defensive-test2.jpg) |
| | User should not be able to log in with incorrect password | Tested the feature by clicking the log in button to see if submits the form with empty inputs | The feature behaved as expected, 'log in' button clicked and prompt came up telling user to fill in event name field | Test concluded and passed | ![screenshot](documentation/defensive-test7.jpg) |
| Sign up | | | | | |
| | User should not be permitted to submit empty form | Tested the feature by clicking the sign up button to see if submits the form with empty inputs | The feature behaved as expected, 'sign up' button clicked and prompt came up telling user to fill in event name field | Test concluded and passed | ![screenshot](documentation/defensive-test3.jpg) |
| | Password must contain letters and numbers and atleast 5-30 characters | Tested the feature by inputting a password shorter than 5 characters and longer than 30 | The feature behaved as expected, prompt shown when password is too long or short | Test concluded and passed | ![screenshot](documentation/defensive-test4.jpg) |
| | Password must match confirm password | Tested the feature by typing in a different password in the confirm password compared to the password field | Feature behaved as expected, flash message of 'passwords do not match, try again' shows on screen if confirm password and password are different | Test concluded and passed | ![screenshot](documentation/defensive-test5.jpg) |
| Profile | | | | | |
| | A user/non-user should not be able to brute force to a different users profile page | I used the URL http://socialeyes-1884ceb59a89.herokuapp.com/profile/staceylewis to test this whilst logged out. | The feature behaved as expected, Flash message displayed 'You must log in to view this page' | Test concluded and passed | ![screenshot](documentation/defensive-test6.jpg) |
| | A user should only be able to see their own created events on their profile page | I created a new user called userA and checked the profile page | Behaved as expected, could not see any events as userA has not created any | Test concluded and passed | ![screenshot](documentation/defensive-test9.jpg) |
| Events | | | | | |
| | A user/non-user should not be able to brute force to the events page | I used the URL http://socialeyes-1884ceb59a89.herokuapp.com/get_events to test this whilst logged out. | The feature behaved as expected, flash message displayed 'You must log in to view this page' | Test concluded and passed | ![screenshot](documentation/defensive-test6.jpg) |
| | Another user should not be able to delete another users events whilst logged in | Tested by logging into the userA user account and visiting the events or profile page | Behaved as expected as for events that are not created by the user in session the 'I'll be attending' button is displayed instead of 'edit' and 'delete' | Test concluded and passed | ![screenshot](documentation/defensive-test8.jpg) |
| Add Event | | | | | |
| | User should not be permitted to submit form | Tested the feature by clicking the add button to see if submits the form with empty inputs | The feature behaved as expected, 'add' button clicked and prompt came up telling user to fill in event name field | Test concluded and passed | ![screenshot](documentation/defensive-test1.jpg) |
| | A user/non-user should not be able to brute force to the add event page | I used the URL http://socialeyes-1884ceb59a89.herokuapp.com/add_events to test this whilst logged out. | The feature behaved as expected, flash message displayed 'You must log in to view this page' | Test concluded and passed | ![screenshot](documentation/defensive-test6.jpg) |
| Edit Page | | | | | |
| | A user/non-user should not be able to brute force to edit an event page | I used the URL http://socialeyes-1884ceb59a89.herokuapp.com/edit_event/654a0c28f29498fdf38f31c0 which is the macmillan event to test this whilst logged out | The feature behaved as expected, flash message displayed 'You must log in to view this page' | Test concluded and passed | ![screenshot](documentation/defensive-test6.jpg) |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to have a 'I'll be attending' button for which events I want to attend, so that I can easily sign up for the event. | ![screenshot](documentation/feature18.jpg) |
| As a new site user, I would like to be able to register for my own account so that I can sign up for events without having to fill in a form each time, as it will already have my details stored. | ![screenshot](documentation/google-pixel7-signup.png) |
| As a new site user, I would like to simply view a list of different events so that I can decide which I prefer. | ![screenshot](documentation/feature6.jpg) |
| As a new site user, I would like to add my own events so that I can advertise any help needed for charities. | ![screenshot](documentation/feature14.jpg) ![screenshot](documentation/mongo-add.jpg) |
| As a new site user, I would like to have simple access to the site's social media pages, so I can contact them or provide feedback if needed. | ![screenshot](documentation/feature7.jpg) |
| As a returning site user, I would like to edit my event I created, so that I can update any details of my event. | ![screenshot](documentation/feature13.jpg) |
| As a returning site user, I would like to have the option to delete my event, so that I can delete my event if necessary and remove the data from the database. | ![screenshot](documentation/feature15.jpg) |
| As a returning site user, I would like to have the option to 'unattend' events, so that I can unattend if i can no longer go to that event. | ![screenshot](documentation/feature19.jpg) |
| As a returning site user, I would like to be able to log in, so that I can view any events I will be attending. | ![screenshot](documentation/google-pixel7-login.png) |
| As a returning site user, I would like to be able to log out, so that I am no longer kept signed in when I leave the site. | ![screenshot](documentation/feature17.jpg) |
| As a site administrator, I should be able to edit events, so that I can update any details of events if needed. | ![screenshot](documentation/feature13.jpg) ![screenshot](documentation/mongo-edit.jpg) |
| As a site administrator, I should be able to delete events, so that I can delete events if the events are postponed or cancelled. | ![screenshot](documentation/feature15.jpg) |
| As a site administrator, I should be able to have my own profile, so that I can see my own events created. | ![screenshot](documentation/google-pixel7-profile.png) |
| As a site administrator, I should be able to add as many events as needed, so that I do not have any limits. | ![screenshot](documentation/feature12.jpg) |

## Bugs

- 404 error on profile page  #1

    ![screenshot](documentation/bug1.png)
    ![screenshot](documentation/bug1-2.png)
    ![screenshot](documentation/bug1-3.png)

    - After some research I discovered that the 404 error codes are generated when a user attempts to access a webpage that does not exist, has been moved, or has a dead or broken link. This made me realise that it was because I did not have an active user session and needed to log in or sign up. In the third screenshot you will see it is now resolved.

- Sign up details not reflecting on mongodb database when I submit the form it does not show any error message and refreshes the sign up form once submitted the details. #2

    ![screenshot](documentation/bug2.png)
    ![screenshot](documentation/bug2-2.png)
    ![screenshot](documentation/bug2-3.png)
    ![screenshot](documentation/bug2-4.png)
    ![screenshot](documentation/bug2-5.png)

    - As you can see in the above I realised the problem was that I needed to add the post method so it can post the information to the connected database.

- jinja2.exceptions.TemplateSyntaxError: unexpected '%' #3

    ![screenshot](documentation/bug3.png)
    ![screenshot](documentation/bug3-2.png)
    ![screenshot](documentation/bug3-3.png)

    - To fix this, After using stackoverflow to help resolve the problem I realised I added double brackets on the if statement block instead of one bracket.

- Edit template not displaying when clicking on the edit button #4
    - There was no error message displaying from python which would tell me the issue however after looking at the URL when clicking on event, it shows the html code in the url which made me realise this was a link issue somewhere.

    ![screenshot](documentation/bug4.png)
    ![screenshot](documentation/bug4-2.png)

    - After realising the issue may be with a link I looked back over my code and noticed that the edit button a href does not include the double brackets. After adding the brackets its works as expected.

- Type Error : 'collection' object is not callable #5

    ![screenshot](documentation/bug5.png)
    ![screenshot](documentation/bug5-2.png)

    - To fix this, I looked on the mongo db website and slack to discover that the update() method that I am using was deprecated and instead on mongo db site (https://www.mongodb.com/docs/manual/reference/method/db.collection.update/) it advises to use the update_one() method however to also use the $set with the dictionary to set the dictionary.

- Text always to the left on buttons and unable to center it #6

    ![screenshot](documentation/bug6.png)
    ![screenshot](documentation/bug6-2.png)

    - To fix this, I checked over my code on the inspect dev tools I noticed I still had a class on there 'icon-right' from when I had originally included icons on the button and forgotten to remove. After removing this class it fixed the bug.

- Rounded class not working when applied to the button with materialise web #8

    ![screenshot](documentation/bug7.png)
    ![screenshot](documentation/bug7-2.png)

    - After research with the help of my mentor I discovered the classes were not working as on the source there is no such class as rounded in Materialize Web css however they were displaying in the github css file. 
    After looking at the materialize github we discovered that Materialize never updated their "Getting Started" information for the CDN links and noticed they have a "beta" release and I was using the alpha release. Soon as I updated the CDN link with the beta version the round class could be applied and worked successfully.

- Navbar img logo doesn't work on the profile page and edit/add event page but works on all other pages. #8

    ![screenshot](documentation/bug8.png)

    - To fix this, I changed the src link to a url_for link instead as I noticed I was using a relative path link in error. 


- Home page arrow button does not work when clicked if user not logged in #9

   ![screenshot](documentation/bug9.png)

   - Whilst using DevTools I checked the caching on my site. When I checked the 'disable cache' box and kept dev tools open I worked as normal.  

- Log in link on the sign up page redirects to the sign up page rather than the log in page #10

   ![screenshot](documentation/bug10.png)

   - I corrected the url as the url_for included the sign up function rather than the log in function.

- When validating the jingja code using HTML validator it says there is a stray div.

   ![screenshot](documentation/bug11.jpg) 

   - Changing the position of the endif to the last line where the end of the for loop closes fixed the problem as its no longer looping over the closing div tags.

## Unfixed Bugs

- On devices smaller than 300px, the page starts to have `overflow-x` scrolling.

     ![screenshot](documentation/unfixed-bug1.jpg)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read particularly on inputs and on the mobile sidebar.
