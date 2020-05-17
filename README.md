Pressie
================

Thankyou for visiting my project Pressie, a wishlist website designed to help people buy meaningful gifts for their loved ones. 

This project remains in development at this time. As a submission for Code Institute's third milestone project the CRUD (Create, Read, Update, Delete) functionality has been added while other features remain yet to be completed.

[View Pressie](https://mypressie.herokuapp.com/)

Please feel free to read through this Readme and browse my project, if you have any questions or suggestions head to my Github contact details or <a href="geminerald.github.io/geminerals">my website</a>. 

## Contents:

* UX 
    * Project Goals
    * Target Audience Goals
    * Site Owner Goals
    * User Requirements and Expectations
    * Design Choices 
        * Fonts
        * Colours
        * Styling
* Wireframes
* Features 
    * Current Features
    * Features in Development
    * Features that will be developed in the future
* Technologies Used 
* Testing 
* Bugs 
* Deployment 
* Credits 


## Notes for Assessors:

* This project is designed to primarily showcase CRUD functionality in Python and MongoDB. There are features that are not yet fully operational. 

## UX (User Experience) 
### Project Goals
The goal of this project is to help users find meaningful gifts for people they care about or "Finding gifts they care about for the people you care about".
The project is aimed toward people who either struggle to know what to get someone for a present or people who find that too often they get unwanted gifts which are then regifted or not enjoyed. 
The website needs to be visually appealing and simple enough to allow and encourage use for all ages and technological abilities.

#### User Stories:

As a user I expect: 
    
 * A website that serves as an online wishlist to be able to share with their friends and family.
 * Simple and consistent theme and styles throughout to encourage engagement and provide a good user experience across generations.
 * A website that allows one to quickly and easily locate gifts that someone actually wants.
 * Ensure no duplication of gifts purchased.
 * Easily share a wishlist. 
 * Do everything possible to ensure that a gift will be purchased before being removed from a wishlist.
 * Interact across all devices of all sizes.

#### User Goals:

##### Mr Smith: 
<em>"I want to be able to locate gifts for my loved ones without having to ask them."</em>

##### Mr Jones: 
<em>"I want to be able to share my choice of gifts with my loved ones without it being awkward."</em>

##### Mr Brown: 
<em>"I want to be able to access websites easily and quickly"</em>

##### Mr Adeolokun: 
<em>"I want to be able to share my choices with my loved ones without compromising my security or personal information"</em>

##### Mr Wong: 
<em>"As a user I want to be able to quickly grasp what I want from a website and have clear instructions throughout. "</em>


#### Site Owner Current Goals:
* Provide a great service for people looking for gifts.


#### Site Owner Future Goals:
* Offer a premium (paid) service which would allow for greater specification, ranking gifts in order etc. etc.
* Direct users towards specific websites such as Amazon, Groupon etc. with a view to taking a referral fee per click.
* Sell ad space on wishlist creation page to give the buyer ideas for what they may want based on their web use.
* Add Premium Links to View Wishlist page so that buyers can be directed to a specific shop for a fee
* Add a feature that checks for other places to buy an item apart from the one provided and advises the buyer if they could get the gift cheaper elsewhere. 
* Collect data on what gifts are popular to assist future projects.

## User Requirements and Expectations:
##### Requirements:
* Create an online wishlist of meaningful gifts.
* Navigate the website using the navigation elements.
* Be able to easily access the wishlist of someone.
* Content displayed in a simple and consistent manner throughout.
* Be directed to somewhere that their chosen gift can be purchased.
* Personal Information is kept secure.
* Every effort made to ensure that wishlists are accurate at all times.

##### Expectations:
* Easy wishlist creation.
* Content is visually appealing, clear and informative.
* Ability to locate someone's list and quickly select item of choice.
* Navigation elements work as designed and are clear and intuitive. 
* Website is fully responsive across all devices and navigation elements etc. alter as required.
* Wishlists are fully configurable and editable.


## Design Choices: 

The theme of this project is gift giving, as a result the design is themed around being upbeat and positive. The Colour theme was taken from <a href="https://visme.co/blog/website-color-schemes/">Visme</a>

One key issue throughout this project is the fact that this website will often be used to bridge a generational gap. At times of gift giving it would be usual for people to buy gifts for someone in a different generation and it would often be more difficult to do so compared to someone in one's own generation. 

As a result of this the project had to be developed with simplicity to the forefront and had to be equally so across all devices as there is a marked difference in device use based on age ranges. <a href="https://www.klarna.com/knowledge/articles/should-you-think-mobile-first-or-mobile-only/">This</a> research shows the differing device use across ages and so it is very possible that a list will be written on one device and read on another.

##### Fonts: 
I chose the font <a href="https://fonts.google.com/specimen/Roboto">Roboto</a> as it a very simple style which is easily readable and not in any way distracting. The content is there to facilitate the creation of lists and assist in getting the right gift at the right time and not to provide a distraction.

##### Colours:

* The colour theme is based across a blue spectrum which encourages positivity and calmness.
* The submit buttons are orange to keep the contrast high and the theme of positivity throughout as orange is a colour associated with action.
* Dark blue was used instead of black for text and similar elements as this colour is softer and therefore more in keeping with the theme.


##### Styling: 


* Elements were given rounder corners to soften the look of the project and ensure that it kept the feeling of being a simlpe "app style" site.

* The site is designed and styled so there are relatively few moving parts. These are all central and intuitive and all instructions are designed to be easy to grasp and intuitive.

* These choices are made to cater to the wide variety of users - unlike many projects there is no single "target demographic" and this needs simplicity baked into the style to allow for a universal feel.


## Wireframes: 
I built the wireframes for this project using <a href="https://balsamiq.com/">Balsamiq mockups</a>. To view my mockups please visit my mockup <a href="https://github.com/geminerald/pressie/tree/master/wireframes">here.</a>

## Features: 

* Login/ Authentication system.
* Wishlist creator
* Ability to add items to wishlists and edit wishlists at any time.
* Ability to find a wishlist easily yet keep it secure.
* Logout system to clear the session for security of Authentication

## Technologies Used: 

### Languages:

* <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>
* <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a>
* <a href="https://www.w3schools.com/js/">JavaScript</a>
* <a href="https://www.json.org/json-en.html">JSON</a>
* <a href="https://www.python.org/">Python</a>


### Tools & Libraries:

* <a href="https://palletsprojects.com/p/flask/">Flask</a>
* <a href="https://jquery.com/">jQuery</a>
* <a href="https://git-scm.com/">Git</a>
* <a href="https://materializecss.com/">Materialize</a>

## Testing: 

##### Test Overview: 

Testing was conducted on an ongoing basis throughout development. 

As each feature was added it was thoroughly tested and each feature that it interacted with was also tested to ensure that they were not affected.

Testing of new components was tested before each commit.

##### Testing Against the User Goals:

* A website that serves as an online wishlist to be able to share with their friends and family.
 - The website does store wishlists on a database which will be able to be securely accessed by a third party.
* Simple and consistent theme and styles throughout to encourage engagement and provide a good user experience across generations.
 - The design is kept simple and consistent with relatively few elements on each page.
* A website that allows one to quickly and easily locate gifts that someone actually wants.
 - The finder function returns the specific wishlist with just one piece of input.
* Ensure no duplication of gifts purchased.
 - This feature remains in delveopment at this time. 
* Easily share a wishlist. 
 - Users will only need to provide their phone number (or another number of their choice) to direct people to their wishlist. 
* Do everything possible to ensure that a gift will be purchased before being removed from a wishlist.
 - This feature remains in delveopment at this time. . 
* Interact across all devices of all sizes.
 - Testing was conducted across different screen sized at each deployment push to ensure responsiveness. The nav bar was updated towards the end of the project to aid responsiveness.

### Overall:

<strong>Responsiveness - </strong>
* <strong>Plan</strong> : Responsiveness is important in this project as the system needs to function seamlessly across all devices due to the generational differences in device use.
* <strong>Implementation</strong> : Materialize and Bootstrap are used for CSS and JavaScript elements and also comes with built in responsive classes.
* <strong>Result</strong> : The site does transform seamlessly across different sizes of device and the theme and functionality is consistent across all platforms. 
* <strong>Verdict</strong> : The site is responsive and a user should not be slowed down on any device. 

<strong>Design -</strong>
* <strong>Plan</strong> : 
* <strong>Implementation</strong> : 
* <strong>Result</strong> : 
* <strong>Verdict</strong> :

### Features:

#### Current Features

* Create account (with secure password storage)
* Create wishlist
* Edit wishlist
* Add items to wishlist
* Delete wishlist
* View existing wishlists

#### Features in Development

* Search for a wishlist
* Additional wishlist options and updated functionality - such as ability to order wishlists etc.
* Password reset functionality


#### Potential Future Features

* Ads on wishlist page to assist users in deciding what to add to their wishlist and generate revenue.
* Sponsored links on view wishlist page to provide different options for where to purchase the gift and generate revenue.
* Functionality to search major retailers and if an item is available for cheaper than the link provided by the person who creates the wishlist it can direct people there.


## Bugs: 

#### Bugs During Development:

Overview:

<strong>Invalid Email Throwing Incorrect Error</strong>:
* <strong>Bug</strong> : When an invalid email was entered to the email field the error message was displayed in the Password input area.
* <strong>Fix</strong> :  The issue was resolved in forms.py - the email validation logic was applied to password field in error.
* <strong>Verdict</strong> : Bug Effectively Squashed!

<strong>Registration Form Fields Error</strong>:
* <strong>Bug</strong> : The Registration form was pushing incorrect info to the database. 
* <strong>Fix</strong> :  The form fields were corrected and the labels updated to match the correct information that was to be updated to the DB.
* <strong>Verdict</strong> : Bug Effectively Squashed!


<strong>Delete Item Redirect</strong>:
* <strong>Bug</strong> : Upon clicking on Delete Item on the View Wishlist page the redirect to the wishlist page would not show the items in the wishlist and would have sensitive information in the URL
* <strong>Fix</strong> :  The information passed into the redirect on the Delete Wishlist function in app.py was updated and a typo removed so it now redirects with the correct information passed in.
* <strong>Verdict</strong> : Bug Effectively Squashed!

#### Known Bugs:

Here is a list of known bugs that exist on the site: 

<strong>Finder not finding</strong>:
* <strong>Bug</strong> : The finder function is not currently returning the correct wishlist page. 
* <strong>Fix</strong> :  TBC. Have tried changing type of objects and how they are accessed.
* <strong>Verdict</strong> : Fix efforts are ongoing

<strong>My List Logic</strong>:
* <strong>Bug</strong> : The view wishlist page needs to show different options if the current user is the list owner. Currently this is non functional.
* <strong>Fix</strong> :  TBC. Have tried input boolean values based on user but this creates further issues with the CSS not displaying correctly.
* <strong>Verdict</strong> : Fix efforts are ongoing

## Deployment: 

This project was deployed via Heroku. For full details on deployment with Heroku you can view their documentation <a href="https://devcenter.heroku.com/articles/git">here</a>

### In Summary:

* A repository was created on GitHub and the code was comitted and pushed there throughout development. 
* A repository was created on Heroku and the code was then pushed to Heroku as follows once development was sufficiently advanced.
* First - Login to Heroku using the Command Line Interface (CLI) command: $ heroku login
* Then deployed using the heroku commands:

$ git add .
$ git commit -am "make it better"
$ git push heroku master

* Config vars were then set in Heroku for linking to the DB, the Secret Key, the IP and PORT.

## Closing Notes:

This project remains a work in progress. I intend to use and improve it myself and I sincerely believe that with time, development and effort it could have useful real world application.

I would like to thank everyone who helped me on this project and detail their specific assistance but to do so would fill the entirety of GitHub.

Special thanks to my mentor at Code Institute Simen who gave me the encouragement and real world feedback I needed to know how to accomplish this. He believed in me far more than I did. 

I would also like to especially thank the tutors at Code Institute for their seemingly endless patience. They are while(true) willing to help.

Also a special mention for all the people who helped me without knowing it on Stack Overflow and similar servies and everyone at Nescafe without whom this would not have been possible.

## Credits: 

* 