# Character Sheet
This repository contains the source code for a basic character sheet for PROJECT: Tempestus - a tactical RPG set in WH40k lore.

# Usage

The character sheet is meant to be used with the [Roll20](https://roll20.net/welcome) system for enjoying RPG games online. It is a developer's hope that once an appropriate stage of development is reached, the character sheet will be pulled into the [Roll20 Character Sheets Repository](https://github.com/Roll20/roll20-character-sheets). P:T fork of the Roll20 Character Sheets Repository is not yet created, as all assets in that repository amount to over 1.2GB (at the moment of writing). 

In the mean time, the character sheet is meant to be downloaded and used through Custom Sheet Sandbox (a Pro feature of the Roll20 system).


# Development

- Lists of inputs for select fields are in `tools\data`
- Build.py uses Jinja `templates`
- Adding new features to html is recommended in `tools\templates`
- Sandbox testing is best done on files from `static` or `release`

