# Movie Trailer

Open `fresh_tomatoes.html` to view the generated site. To add or edit movies, open `movies.json` and edit as you see fit. Then run `$ python entertainment_center.py` to generate and view the movies site.

# First review

The reviewer who failed this project on the first go round complained of two violations of PEP8.

> The Python style guide suggests that the maximum length of a line should be restricted to 79 characters. The init method is longer than 79 characters. I encourage you to write the parameters in two lines such that the second line begins from the same column as self.

Fixed.

> According to the python style guide there should be exactly two blank lines before a function and a class name. I recommend you to add one more blank line before the function's name to enhance readability.

Fixed.

But okay, seriously? It's not in the rubric that "Code must not emit errors when checked against PEP8." If that's the standard, then it should be in the rubric. If that's not the standard, then that should be clarified.

PEP8 complains a lot about fresh_tomatoes.py, so I moved all the templates to their own files.

# Rubric

## Functionality

> Student includes additional information about their favorite movies (actors, release date, etc) or personalizes their page with additional HTML or CSS features.

I added a rating field. The page now displays the rating and plot, and I tweaked the entry animation.

> Page is dynamically generated from a Python data structure.

Yep. Pulling info from a JSON file.

> Page is error free.

Done and done.

## Code Quality

> Code is ready for personal review and neatly formatted.

Sure? Kunal wrote almost all this code. I just added the Movie class and the JSON loader.



## Comments

> Comments are present.

Sure. Most are by Kunal, but I added a few.

> Comments effectively explain longer code procedures.

Are you sure this isn't just the recycled PFwP rubric? Yep. I added a few comments.

## Documentation

> A README file is included.

You're reading it.

> README file includes details of all the steps required to successfully run the application.

See above!

