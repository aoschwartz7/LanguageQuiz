Language Learner's Quiz
--------------------------
This web application uses a Python-Flask framework to create a vocabulary quiz for users. It works with JSON representations of the vocabulary files.

Overview:

In this repository,

uses a JSON representation of German-English and German-Spanish dictionaries to help users learn more introductory German/English/Spanish vocabulary.

The application is made up of the following files:

1) __init__.py - creates Flask instance to start application.
2) routes.py - creates /quizpage URL, starts game, and applies other functions created in wordBank.py to render HTML pages containing german term, user answer, and correct answer.
3) quizPage.html - template to show german word, collect user answer, and two buttons to check answer and view next word.
4) checkAnswer.html - template to show previous german word, user answer, and correct answer, and button to continue.
5) wordBank.py - imports German-English dictionary in startgame function from JSON file; contains helper functions startgame, random_word, and answer.
