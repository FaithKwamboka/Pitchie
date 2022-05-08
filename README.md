# Pitchie!

## Built By [Faith Kwamboka Okong'o](https://github.com/FaithKwamboka)

## Description
An application that allows users to give their one minute pitches. Upon submission of pitches, other users can give their feedback as well as vote for the best pitch.


## User Stories
User features/behaviours are as below.

As a user I would like to:
* See the pitches other people have posted.
![Pitch_2](https://user-images.githubusercontent.com/100117264/167313894-c8856068-a5f2-4f6f-9499-9b7f3c79e9da.png)

* Submit a pitch in any category.
![Pitch](https://user-images.githubusercontent.com/100117264/167313883-ec6c4125-1cb0-4727-b8eb-3eb32fd5c35b.png)

* Leave a comment upon signing in.
* View the pitches I have created in my profile page.
* Comment on the different pitches and leave feedback.
* To view Pitch Categories


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display pitch categories | **On page load** | List of various categories of pitches |
| Display tabs with  category | **On Tab link click** | Clickable links to open pitches by category |
| Display profile | **Click profile page** | Redirected to a page with your profile |
| Display pitches | **On page load** | Each pitch displays author, title, pitch, date comment tab |
| To add a pitch  | **Click an add pitch** | Redirected to the pitch collection form|


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/FaithKwamboka/Pitchie.git
        $ cd pitchie

## Running the Application
* Creating the virtual environment

        $ python3.8 virtualenv virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py test

## Technologies Used
* Python3.8
* Flask
* CSS

## [License](https://github.com/FaithKwamboka/Pitchie/blob/master/LICENSE)

