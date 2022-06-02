# Django_Courses_Store


## Make a website for selling courses to users. This website will display the courses for users, then a user can display the details of the course and decide to buy it or add a review . 

### Courses Store website should have the following models :

#### Course :
- title
- description
- duration (how many days it will take)
- price
- image
- online (is it online or offline , boolean)
- start_date
- user (use the User from Django auth models)


#### Review :
- rating
- comment
- course (the course to be reviewed)
- user (use the User from Django auth models)


#### Order :
- course (the course to order)
- user (the user who ordered the course)
- date (when was the order)
- totalprice (the course price + tax)


### The website should have the following pages :

#### Home page
This will show the main page in the website with a list of courses for the users to buy.


#### Course Detail Page
- This page will show the detail of a course (when a user clicks on the course) . 
-  this page will display all the reviews abouth this course , and allow the users to add new reviews (only logged in user can add review). 
- A buy button , to buy the course and add it to the orders.


#### Orders Page
- This page will display the courses that are bougth by the user and date of purchase. 


#### Register Page
- This page will allow new users to register.


#### Login Page
- This page will be used to login users.



#### Add Course Page
- Thie page will be used to let the users add new courses . NOTE: Only user who has permission to add a course will be able to add a course .



#### Use Bootstrap or similar library for styling.


#### Bonus (not required):
- Only user who bought a course can add a review.
- Add filtering to the home page so a user can filter by price, online or offline .
- Add search to the home page to search for a course. 





















