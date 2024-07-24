# -*- coding: utf-8 -*-
"""Pokemon API Challenge (Spring 2024)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R09OTdTJWdllfsvQ9bfNog6vOqz486Gr

# Background

Pokemon is a popular video game and cartoon show.

For this API Challenge, we will explore the capabilities of the Poke API, which provides access to Pokemon game data:
  + https://pokeapi.co/
  + https://pokeapi.co/docs/v2

> "This is a full RESTful API linked to an extensive database detailing everything about the Pokémon main game series. We've covered everything from Pokémon to Berry Flavors."
"""

from IPython.display import Image, Audio, display

display(Image(url="https://pokeapi.co/static/pokeapi_256.3fa72200.png"))

display(Image(url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"))
Audio(url="https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/25.ogg")

"""# Challenges

Our goal is to build a pokemon information lookup tool, to help pokemon trainers make data-driven decisions when battling and raising their pokemon.

Basic Requirements:

  + In Part 1, we will fetch and display a list of all pokemon characters.

  + In Part 2, we will ask the user to choose their favorite pokemon from the list, and ensure they chose a valid name.
  
  + In Part 3, we will fetch and display information about the user's favorite pokemon.

Further Exploration:

  + In Part 4, we will loop through all the pokemon and gather information about each, and save this data to a CSV file for later.

  + In Part 5, we will save this data about all Pokemon to Google Sheets (see [example sheet](https://docs.google.com/spreadsheets/d/1WhswYl9OJWJ4V0WaM_GceljIknCx6vUdOo2JDbMYBlQ/edit?usp=sharing)).

## Part 1 (List All Pokemon)

Goal: Display a list of pokemon from the first generation games.

a) Fetch a list of first generation pokemon from the API. Use a single request only.

> NOTE: first generation pokemon are the first 151 provided by the API

> HINT: explore the `limit` and `offset` URL parameters of the pokemon list endpoint (https://pokeapi.co/api/v2/pokemon)


b) Store the list of Pokemon in a variable called `first_gen`.

c) Display a count of the number of Pokemon in the list (i.e. `151`).

d) Loop through the pokemon and print the name of each, formatted as title case (i.e. starting with "Bulbasaur" and ending with "Mew").
"""













"""## Part 2 (Lookup Pokemon)

Goal: Prompt the user to input their favorite pokemon, and perform validations to ensure they input a valid name.

a) Prompt the user to input the name of their favorite Pokemon, based on the list of names displayed in Part 1.

b) Store their favorite Pokemon name in a variable called `fav_name`.

c) Lookup the favorite pokemon name from the list of Pokemon obtained in Part 1. Perform validations such that if the user types a valid name, the program will display the name and URL of the matching Pokemon (i.e. ` 'snorlax'`, `'https://pokeapi.co/api/v2/pokemon/143/'`). Otherwise if they mistype the Pokemon name, the program should display a message like "OOPS, invalid name, please try again."

> CHALLENGE: optionally perform this validation step within a loop that will allow the user to continuously try again until they finally input a valid name.
"""





"""## Part 3 (Get Pokemon Info)

Goal: Fetch detailed information about the user's favorite Pokemon inputted in Part 2.

> HINT: see https://pokeapi.co/docs/v2#pokemon-section

Using data from the Poke API, address the following challenges:

a) Display the following information about the selected Pokemon:

   + Name (i.e. `"Snorlax"`)
   + Height (i.e. `21`), presumably this is in feet
   + Weight (i.e. `4600`), presumably this is in lbs
   + Base Experience (i.e. `189`)


b) Display a thumbnail image of the Pokemon, for example using its "front default sprite".

c) Play an audio of the Pokemon's cry, using its "latest cry".


d) Display additional information about the selected Pokemon:
   + Types, formatted as a simple list of strings (i.e. `['Normal']`)
   + Abilities, formatted as a simple list of strings (i.e. `['Immunity', 'Thick-Fat', 'Gluttony']`)
   + Items, formatted as a simple list of strings (i.e. `['Chesto-Berry', 'Leftovers']`)


e) Display the Pokemon's stats, including:

  +  HP (i.e. `160`)
  + Attack (i.e. `110`)
  + Defense (i.e. `65`)
  + Special Attack (i.e. `65`)
  + Special Defense (i.e. `110`)
  + Speed (i.e. `30`).
"""

















"""## Part 4 (Pokemon Database)

Motivation: Everytime we fetch data about a pokemon, we are making a network request, which takes time. How about if we go through a one time process where we collect data for all the pokemon and store it somewhere for easier reference?

Goal: loop through all the first generation pokemon and collect data about each, and store all the data in a single CSV file.

a) Loop through each Pokemon in the `first_gen` list, and print the name and URL for each.

b) Within the loop, make a request for data about each pokemon, using the provided URL.

c) Within the loop, create a simple dictionary of information for each Pokemon (to simplify the super nested structure and only keep the data we care about). Also "collect" this simplified dictionary for later, into a list called `db`.


d) When your loop finishes, print the number of items in the `db` list, as well as the first item.

...

e) Pass the list of dictionaries (`db`) to the pandas `DataFrame` class constructor, to initialize a new instance of the dataframe datatype, using the Pokemon data we collected.

f) Display the number of rows in the dataframe, as well as the first few records.

g) Save the dataframe to a CSV file called "first_gen_pokemon.csv".
"""







"""Code for parts E, F, and G:"""

# from pandas import DataFrame
#
# df = DataFrame(db)
# print(len(df))
# df.head()

# df.to_csv("first_gen_pokemon.csv", index=False)

"""## Part 5 (Google Sheets Database)

Stretch Goal: In addition to storing the Pokemon database to CSV file, also write the data to Google Sheets (like this [example](https://docs.google.com/spreadsheets/d/1WhswYl9OJWJ4V0WaM_GceljIknCx6vUdOo2JDbMYBlQ/edit#gid=788962999)).

Setup: Create a new google sheet document, and note it's identifier (i.e. `GOOGLE_SHEETS_DOCUMENT_ID`). Create a new sheet within this document called "gen-1".

References:

  + https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/gspread.md

a) Use some boilerplate Google Colab authentication code to login with your Google Account.

b) Set the `GOOGLE_SHEETS_DOCUMENT_ID` to reference the identifier to the document you set up.

c) Install the `gspread` package via pip, as necessary, and use it to access the document provided by the `GOOGLE_SHEETS_DOCUMENT_ID`. Verify by printing a list of the sheet names that currently exist in this document.

d) Finally, write the dataframe data to the "gen-1" sheet.


> NOTE: when trying to write data to the sheet, if any columns have list values (for types, held items, abilities, etc.), that will trigger an error. To work around this error, we can use an approach like this to convert each column of lists to a column of comma separated strings instead:
>
>  `df["types"] = df["types"].str.join(", ")`.
>
> These new columns of comma separated strings can be written to the sheet without error.
"""

# df["types"] = df["types"].str.join(", ")
# df["held_items"] = df["held_items"].str.join(", ")
# df["abilities"] = df["abilities"].str.join(", ")
# df.head()

# %%capture
# !pip install gspread



GOOGLE_SHEETS_DOCUMENT_ID = "..."








