# Instructions

* Open the file, `cereal.csv` and start by skipping the header row. See hints below for this.

* Read through the remaining rows and find the cereals that contain five grams of fiber or more, printing the data from those rows to the terminal.

## Hint

* Everything within the csv is stored as a string and certain rows have a decimal. This means that they will have to be cast to be used.

* You may have to use a string `encode()` method when you are opening and reading the file. This will require you to add a parameter in the `with open()` function. Refer to these stackoverflow to help you to better understand what encoder to use.
1. [Weird character added](https://stackoverflow.com/questions/22974765/weird-characters-added-to-first-column-name-after-reading-a-toad-exported-csv-fi)

2. [Difference between utf-8 and utf-sig](https://stackoverflow.com/questions/57152985/what-is-the-difference-between-utf-8-and-utf-8-sig)

* The `csv.reader` begins reading the csv file at the first row. `next(csv_reader, None)` will skip the header row. Refer to this stackoverflow answer on [how to skip the header](https://stackoverflow.com/a/14257599) for more information.

* Integers in Python are whole numbers and, as such, cannot contain decimals. As such, your numbers containing decimal points will have to be cast as a `float`.

## Bonus

* Try the following again but this time using `cereal_bonus.csv`, which does not include a header.

**Note:** Refer to the encoder hint in the **hint** section above. 
