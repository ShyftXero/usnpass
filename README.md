# usnpass
uShallNotPass - password complexity/strength/whatever checker

### Requirements
* flask
* flask-wtf
* flask-bootstrap
* john.txt from   https://wiki.skullsecurity.org/Passwords (or any dictionary...)


### Features
* Statistically weed out passwords with the top 20 most common bi, tri, and quad-grams (these are indicators of english words meaning it awards points for not looking like a word.)
* completely arbitrary scoring system.
* potentially inaccurate results that are not tied to reality in any way.
* mangler is somewhat interesting.



