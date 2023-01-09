# Pleroma to Yukimochi relay migration tool

Simply place the jsonld of the relay you'd like to move into the base directory.
Running `pleroma-2-yukimochi.py` will take that database the convert it to a json backup for Yukimochi, placed in the file `new-yuki.json`.
You can then import that database into Yukimochi by running `relay control config import --json ~/new-yuki.json`