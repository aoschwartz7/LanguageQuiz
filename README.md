Language Learner's Vocab Quiz
--------------------------
This web application uses a Python-Flask framework to create a vocabulary quiz for users. It works with JSON representations of vocabulary files which can be created in the app.

### Table of Contents
1. [Overview](#overview)
2. [Walkthrough](#walkthrough)
3. [How to run it](#howtorunit)
4. [How it works](#howitworks)

### Overview <a name="overview"></a>

This app guides a user to create or select existing flashcard decks that they can use in a simple quiz. The quiz is structured to show user a term, have them provide the definition, and tell them if they are correct before proceeding to the next term. This quiz can be played using both localhost and Terminal.

### Walkthrough <a name="walkthrough"></a>

![alt text](/READMEimages/image1.png)
Welcome Page where user can select to either create new flashcards or start a quiz with existing flashcard sets.

![](/READMEimages/image2.PNG)
If user chooses to create new flashcards, they can select an existing folder or create a new one where they will store their flashcards.

![](/READMEimages/image3.PNG)
Allow user to create new flashcards until the set is complete, then redirect user back to Welcome Page.

![](/READMEimages/image1.PNG)
User can now choose to continue to the quiz.

![](/READMEimages/image4.PNG)
User picks a folder containing flashcards.

![](/READMEimages/image5.PNG)
User picks a flashcard set.

![](/READMEimages/image6.PNG)
Quiz the user with randomized terms from the flashcard set. User can then check their answer or skip to the next word.

![](/READMEimages/image7.PNG)
If user decides to check their answer, tell them if they're correct. If not, show correct answer.


### How to run it <a name="howtorunit"></a>

1) Install Python [link]
2) Install Flask [link]
3) Download this repository [link]
4) In Terminal change directory to /VocabQuiz
5) To play the game in Terminal, type this into the command line:
   $ python quizFunctions.py
6) To play the game using the GUI, activate the Flask virtual environment and run Flask:
   $ cd venv
   $ source bin/activate
   $ cd ..
   $ flask run
7) Open web browser and type this into address bar: http://localhost:5000/
8) To stop running the game:
   $ ctrl + c
   $ deactivate (deactivates virtual environment)

### How it works <a name="howitworks"></a>

The application is made up of the following files:

1) __init__.py - imports Flask, creates app instance, then imports routes from routes.py.
2) routes.py - contains all route decorators, imports Python functions from quizFunctions.py, and uses request methods to show and submit client-server data.
3) base.html - this is the base template that extends across all templates to keep the style uniform.
4) style.css - contains custom CSS for the template.
5) HTML templates
