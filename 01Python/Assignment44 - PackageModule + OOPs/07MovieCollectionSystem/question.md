'''
Create the following structure:

project/
│
├── models/
│   ├── __init__.py
│   └── movie.py
│
└── main.py

IMPORTANT RULES

1. Create the class inside the `models` package.
2. The class must be written in a separate module.
3. Import the class into `main.py`.
4. Create multiple objects of the class.
5. Store all objects inside a list.
6. Perform operations on the list of objects.
7. Take input from the user wherever required.
8. Do not use dictionaries in place of objects.
9. Do not use database connectivity.
10. Display the output in a proper format.

============================================================
ASSIGNMENT 7 – MOVIE COLLECTION SYSTEM
======================================

Create a `Movie` class inside:

models/movie.py

ATTRIBUTES:

* movie_id
* movie_name
* genre
* rating
* ticket_price

TASKS:

1. Take details of 5 movies from the user.
2. Create Movie objects.
3. Store all objects in a list.
4. Display all movies.
5. Display movies having rating greater than 8.
6. Display all Action movies.
7. Find the highest-rated movie.
8. Search a movie using Movie Id.
9. Calculate average movie rating.
10. Display movies whose ticket price is greater than 300.

SAMPLE DATA:

101 Dangal Drama 8.4 250
102 Jawan Action 7.5 300
103 3Idiots Drama 8.4 200
104 Bahubali Action 8.1 350
105 Pathaan Action 7.0 320

EXPECTED OUTPUT:

Movies with rating greater than 8:

Dangal 8.4
3Idiots 8.4
Bahubali 8.1

Action Movies:

Jawan
Bahubali
Pathaan

Highest Rated Movie:

Dangal 8.4

Movies with ticket price greater than 300:

Bahubali 350
Pathaan 320

Average Movie Rating:

7.88

Search Movie Id: 104

Movie Found:

104 Bahubali Action 8.1 350
'''
