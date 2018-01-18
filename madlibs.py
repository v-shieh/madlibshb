"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

PEOPLE = ['Balloonicorn', 'Seed.py', 'Boolean', 'Obscenicorn', 'Henry',
          'Leslie', 'Meggie', 'Katie', 'Maggie', 'Rachel']

COLORS = ['papaya whip', 'mauve', 'cerulean blue', 'lavender',
          'mint', 'scarlet', 'burnt sienna']

ANIMALS = ['giraffe', 'beluga whale', 'penguin', 'python',
           'kitten', 'lion', 'platypus', 'aardvark']


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Show madlib form to user."""
    play_game = request.args.get("play-game")

    if play_game == "yes":
        return render_template("game.html",
                               people=PEOPLE,
                               colors=COLORS,
                               animals=ANIMALS)
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Displays finished madlib."""

    person = request.args.get('person')
    color = request.args.get('color')
    noun = request.args.get('noun')
    adjective = request.args.get('adjective')
    animals = request.args.getlist('animals')
    concatenated_str = ""

    # if list length is 0; animal = 'unicorn'
    # if list length is 1; animal = animals[0]

    # while len(list) > 0
    # Go through list, concatenate what we're popping from end
    # Then concatenate ", "
    # when list is 1, we concatenate ", and "
    # pop and concatenate last item

    if len(animals) == 0:
        animal = "unicorn"
    if len(animals) == 1:
        animal = animals.pop()
    while len(animals) > 0:

        for animal in animals:

            if len(animals) == 1:
                concatenated_str = concatenated_str + "and " + animals.pop()
            else:
                concatenated_str = concatenated_str + animals.pop() + ", "

    return render_template("madlibs.html",
                           person=person,
                           color=color,
                           noun=noun,
                           adjective=adjective,
                           animals=concatenated_str)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
