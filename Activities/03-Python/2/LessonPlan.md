# 3.2 Reading, Writing, and Pyrithmetic

## Overview

During today's class, the class will be diving further into reading and writing data from/to external CSV files. They will also dive into Python dictionaries, zipping lists, and functions.

## Class Objectives

* Students should feel confident reading data into Python from CSV files.

* Students should feel confident writing data from Python into CSV files.

* Students should know how to zip two lists together and know when this is helpful.

* Students should understand well how to create and use Python functions.

## Instructor Prep

<details>
    <summary><strong>Instructor Notes</strong></summary>

* Today is a challenging but immensely useful class that pertains directly to the homework. Nevertheless, today should be a fun class due to the number of engaging activities students will have access to. There will be some frustrations and hurdles to overcome, but so long as the class trudges through the challenges they will come out all the stronger.

* The first half of today's class is far more relevant to this week's homework than the latter half. As such, feel free to provide students with additional time so they are able to sufficiently complete the activities.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-03-python) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Have your TAs refer to the [Time Tracker](TimeTracker.xlsx) to stay on track.

* When the lesson plan calls for files to be sent to students there are a few ways to do so. For the first couple of weeks it may be easiest to use Slack, but as the files and directories get more complex you may look to try alternate methods such as pushing and pulling from GitHub/GitLab and sending out the link, using a file storage like google drive, or zipping up files and continuing to Slack out. Please use whatever method you find most comfortable for sending files out to students.

</details>

<details>
    <summary><strong>Sample Class Video</strong></summary>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9df023fb-da39-4fe2-a322-aa71017341ec)

</details>

- - -

# Class Activities

## 1. Welcome & Python Check-Up

| Activity Time:       0:20 |  Elapsed Time:      0:20  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 1.1 Instructor Do: Welcome Class (0:05)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 1 - 2 to facilitate your welcome to the class while covering the following points:

* Welcome students to today's class and reassure them that, even though this stuff is tough, practice makes perfect. The more they work with Python, the more sense it will make.

</details>

<details>
    <summary><strong>✏️ 1.2 Students Do: Python Check-Up (0:10)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 3 - 6.

* Since last class introduced quite a lot of new material, today's lesson will start with a quick warmup activity to get the Python juices flowing!

* Run [01-Stu_QuickCheckup/quick_check_up.py](Activities/01-Stu_QuickCheckup/Solved/quick_check_up.py) within the terminal so that students can see what they are making before sending out the starter file and instructions.

![Check Up Solved](Images/01-CheckUp_Solved.gif)

* **File:**

  * [01-Stu_QuickCheckup/quick_check_up.py](Activities/01-Stu_QuickCheckup/Unsolved/quick_check_up.py)

* **Instructions:**

  * Create a simple Python command line application. Upon running, the application should:

    * Print "Hello User!"

    * Then ask: "What is your name? "

    * Then respond: "Hello <user's name>"

    * Then ask: "What is your age? "

    * Then respond: "Awww... you're just a baby!" or "Ah... A well traveled soul are ye." depending on the user's age.

* **Hints:**

  * Remember to cast your variables!

</details>

<details>
    <summary><strong>⭐ 1.3 Review: Python Check-Up (0:05)</strong></summary>

* Send out [01-Stu_QuickCheckup/quick_check_up.py](Activities/01-Stu_QuickCheckup/Solved/quick_check_up.py) and go over the code with the class, answering any questions students may have regarding the activity.

* Key points to cover during the discussion of this code:

  * The `name` variable is being set to whatever the user inputs as their response to the question "What is your name?"

  * Since the `age` variable is taken in as a string when inputted, it has to be cast as an integer when run through the conditionals.

  ![Check Up Code](Images/01-CheckUp_Code.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3aOFwnj)</sub>

- - -

## 2. Kid in a Candy Store - Python Loops Recap

| Activity Time:       0:25 |  Elapsed Time:      0:45  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 2.1 Instructor Do: Loop Recap (0:05)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 7 - 10.

* Open up [02-Ins_SimpleLoops/simple_loops.py](Activities/02-Ins_SimpleLoops/Solved/simple_loops.py) within the editor to refresh the class on how to create basic loops.

* You may want to have the students inspect the code and discuss it with the people around them before running each for loop separately.

  * A For loop will loop through a range of numbers, the letters in a string, or the elements within a list one at a time.

  ![Simple For Loop - Numbers](Images/02-SimpleLoops_0to9.gif)

  * A While loop will loop through the code contained inside of it until some condition is met.

  ![Simple While Loop - Merry-Go-Round](Images/02-SimpleLoops_MerryGoRound.gif)

* Answer whatever questions the class may have regarding loops before moving onto the next activity.

</details>

<details>
    <summary><strong>✏️ 2.2 Students Do: Kid in a Candy Store - Loop Recap (0:15)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 11 - 13.

* Each student is being placed in the role of a kid going with their parents to the supermarket. After pestering their parents for a while, they finally are allowed to pick out some candy to take home.

![Kid In Candy Store](Images/03-KidInCandyStore_Solved.gif)

* Open up the [03-Stu_KidInCandyStore-LoopsRecap/kid_in_candy_store.py](Activities/03-Stu_KidInCandyStore-LoopsRecap/Solved/kid_in_candy_store.py) within the terminal and run through the application to show students how it functions.

* **Files:**

  * [KidInCandyStore_Unsolved.py](Activities/03-Stu_KidInCandyStore-LoopsRecap/Unsolved/kid_in_candy_store.py)

* **Instructions:**

  * Create a loop that prints all of the candies in the store to the terminal with their index stored in brackets beside them.

    * For example: `"[0] Snickers"`

  * Create a loop that runs for a number of times as determined by the variable `allowance`.

    * For example: If allowance is equal to five, the loop should run five times.

  * Each time this second loop runs, take in a user's input - preferably a number - and then add the candy with a matching index to the variable `candy_cart`.

    * For example: If the user enters "0" as their input, "Snickers" should be added into the `candy_cart` list.

  * Use another loop to print all of the candies selected to the terminal.

* **Bonus:**

  * Create a version of the same code which allows a user to select as much candy as they want up until they say they do not want any more.

</details>

<details>
    <summary><strong>⭐ 2.3 Review: Kid in a Candy Store (0:05)</strong></summary>

* Send out the [03-Stu_KidInCandyStore-LoopsRecap/kid_in_candy_store.py](Activities/03-Stu_KidInCandyStore-LoopsRecap/Solved/kid_in_candy_store.py) of the previous activity and go over the code with the class, answering whatever questions they may have.

* Key points to cover in the discussion of this code:

  * There are three For loops being used in this activity. One to print out the original candy list. A second to collect all of the candy choices the user has. And a third to print the final list of choices to the screen.

  * When adding candies into the `candy_cart` list, the `selection` variable has to be cast as an integer since all inputs are naturally set as strings.

  * In order to solve the bonus, we would simply use a While loop instead of a For loop, asking after each selection whether the user would like to make another selection. If they ever answer anything other than "Yes", the loop will stop.

    ```python
    # The list of candies to print to the screen
    candy_list = [
        "Snickers",
        "Kit Kat",
        "Sour Patch Kids",
        "Juicy Fruit",
        "Swedish Fish",
        "Skittles",
        "Hershey Bar",
        "Starbursts",
        "M&Ms"
    ]

    # The amount of candy the user will be allowed to choose
    allowance = 5

    # The list used to store all of the candies selected inside of
    candy_cart = []

    # Print all of the candies to the screen and their index in brackets
    for candy in candy_list:
        print(f'[{(candy_list.index(candy))}] {candy}')

    # Another option to run the for loop involves Python's enumerate method
    # This method obtains both the index and the value of an item during a for loop
    # for index, candy in candy_list:
    #     print(index, candy)

    # Run through a loop which allows the user to choose which candies to take home with them
    print("Which candy would you like to bring home?")
    for x in range(allowance):
        selected = input("Input the number of the candy you want: ")

        # Add the candy at the index chosen to the candy_cart list
        candy_cart.append(candy_list[int(selected)])

    # Loop through the candy_cart to say what candies were brought home
    print("I brought home with me...")
    for candy in candy_cart:
        print(candy)
    ```

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2wWjpwk)</sub>

- - -

## 3. House of Pies - Advanced Python Loops

| Activity Time:       0:30 |  Elapsed Time:      1:15  |
|---------------------------|---------------------------|

<details>
    <summary><strong>✏️ 3.1 Students Do: House of Pies - Advanced Loops (0:20)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 14 - 17.

* From one form of sweets to another. In this activity, the class will be constructing an order form that will display a list of pies and then prompt users to make a selection. It will continue to prompt for selections until the user decides to terminate the process.

* This activity comes in three parts: an easy version that is very much like the previous activity and a hard version which is very challenging. Encourage students to try their luck on the hardest version if they are feeling confident.

![House of Pies](Images/04-HouseOfPies_Solved.gif)

* Open up the [04-Stu_HouseOfPies-AdvancedLoops/Solved/house_of_pies_bonus.py](Activities/04-Stu_HouseOfPies-AdvancedLoops/Solved/house_of_pies_bonus.py) within the terminal and run through the application to show students how it functions.

* **Instructions:**

  * **Part 1**

    * Create an order form that will display a list of pies to the user in the following way:

    ```
    Welcome to the House of Pies! Here are our pies:

    ---------------------------------------------------------------------
    (1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak
    ```

    * Then prompt the user to select which pie they'd like to order via number.

    * Immediately after, follow the order with `Great! We'll have that <PIE NAME> right out for you` and then ask if they would like to make another order. If so, repeat the process.

    * Once the user is done purchasing pies, print the total number of pies ordered.

  * **Part 2 (Very Challenging!)**

    * Modify the application once again, this time conclude the user's purchases by listing out the total pie count broken by _each_ pie.

    ```
    You purchased:
    0 Pecan
    0 Apple Crisp
    0 Bean
    2 Banoffee
    0 Black Bun
    0 Blueberry
    0 Buko
    0 Burek
    0 Tamale
    1 Steak
    ```

</details>

<details>
    <summary><strong> ⭐ 3.2 Review: House of Pies (0:10)</strong></summary>

* Send out the [04-Stu_HouseOfPies-AdvancedLoops/house_of_pies_bonus.py](Activities/04-Stu_HouseOfPies-AdvancedLoops/Solved/house_of_pies_bonus.py) of the previous activity and go over the code with the class, answering whatever questions they may have.

* Important points to touch upon during this discussion:

  * Since the GUI for the application starts with 1, the user's input must be subtracted by 1 one when referencing the pie's actual index. This is because all indices start at 0 naturally.

  * The primary loop being used is a While loop that is constantly checking whether the user's response to the question `Would you like to make another purchase?` ever changes from `y`

  * The means by which the total number of pies is calculated in the original solution is by determining the length of the `pie_purchases` array.

  * Within the bonus, the means by which the code is keeping track of how many pie purchases are being made for each type of pie is by having a second list that corresponds to the first filled with 0 values. Every time a pie is chosen, therefore, the code adds one to the index of the `pie_purchases` list that is equal to that of the original `pie_list`.

    ```python
    # While we are still shopping...
    while shopping == "y":

        # Show pie selection prompt
        print("---------------------------------------------------------------------")
        print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
              " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
              " (9) Tamale, (10) Steak ")

        pie_choice = input("Which would you like? ")

        # Get index of the pie from the selected number
        choice_index = int(pie_choice) - 1

        # Add pie to the pie list by finding the matching index and adding one to its value
        pie_purchases[choice_index] += 1

        print("------------------------------------------------------------------------")

        # Inform the customer of the pie purchase
        print("Great! We'll have that " + pie_list[choice_index] + " right out for you.")

        # Provide exit option
        shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

    # Once the pie list is complete
    print("------------------------------------------------------------------------")

    # Count instances of each pie
    print("You purchased: ")

    # Loop through the full pie list
    for pie_index in range(len(pie_list)):
        pie_count = str(pie_purchases[pie_index])
        pie_name = str(pie_list[pie_index])

        # Gather the count of each pie in the pie list and print them alongside the pies
        print(pie_count + " " + pie_name)
    ```

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2UUpzoJ)</sub>

- - -

## 4. Module Playground

| Activity Time:       0:20 |  Elapsed Time:      1:35  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 4.1 Instructor Do: Reading Text Files (0:05)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 18 - 21.

* Another function of Python is that it is capable of reading data in from external text files and then performing some tasks on it.

* Open up [05-Ins_BasicRead/read_file.py](Activities/05-Ins_BasicRead/Solved/read_file.py) and [05-Ins_BasicRead/Resources/input.txt](Activities/05-Ins_BasicRead/Resources/input.txt), going over the syntax and purpose of the code contained within.

  * When dealing with external files, Python requires very precise directions on what path to follow to reach the desired file. As such, if the desired file is stored within a sub-folder called "Resources", the path needed would be "Resources/FileName.txt".

  * It is critical to note that different operating systems use different paths to locate files. For example: Windows machines will often use forward slashes to separate folders while Mac devices will use backslashes.

  ![File Path](Images/05-BasicRead_FilePath.png)

  * The `with` statement is simply saying that, for as long as we are dealing with the code within the following block, save the text variable. Once the code block has completed, the text variable will be "cleaned up" and removed to save memory.

  * `open(<File Path>, <Read/Write>)` is the function Python uses in order to open up and work with external text files. By specifying either `'r'`, `'w'`, or `'rw'`, users can use the `open()` function to either read from a text file, write to a text file, or perform both operations in the code block that follows it.

  * `text.read()` parses the data that is read in by the `open()` function and converts it into a string type. If this function was not used all that would be printed to the screen would be an unhelpful text wrapper object.

  ![With Open](Images/05-BasicRead_Open.png)

</details>

<details>
    <summary><strong>📣 4.2 Instructor Do: Introduction to Modules (0:05)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 22 - 27.

* While Python includes many built-in functions, sometimes coders have to bring in external modules in order to perform specific tasks.

  * If a coder wanted a random number generator for a dice game they were making, for example, they would most likely want to use the `random` module instead of having to create the code from scratch.

* Importing modules into Python is actually very simple. All that is required is for the module to be installed and for the user to import the module into their code.

  * All of the modules for today come packaged with Python, so there is no need to install anything new.

* Open up [06-Ins_Modules/imports.py](Activities/06-Ins_Modules/Solved/imports.py) within your editor and show the class how to import modules into their code.

  * The `string` module contains many helpful constants and methods which pertain to strings. For example, users can use `string.ascii_letters` and Python will instantly grab a reference to every ascii character.

  ![Ascii Gif](Images/06-Modules_String.gif)
  ![String Module](Images/06-Modules_String.png)

  * The `random` module does exactly what one might expect, it allows Python to randomly select values from set ranges, lists, or even strings.

  ![Random Module](Images/06-Modules_Random.gif)
  ![Random Module](Images/06-Modules_Random.png)

</details>

<details>
    <summary><strong>✏️ 4.3 Students Do: Module Playground (0:05)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 28 - 30.

* There are tons of built-in modules for Python and there is no possible way that a single class could cover all of them. For the time being, however, provide students with the opportunity to look through some of Python's modules and play around with them.

* The class will come back together after a couple of minutes to discuss some of the modules that were uncovered before moving on.

* **Links:**

  * [List of Built-In Python Modules](https://docs.python.org/3/py-modindex.html)

</details>

<details>
    <summary><strong>⭐ 4.4 Review: Module Playground  (0:05)</strong></summary>

* Call the class back together and ask if there were any modules in particular that folks found useful. Have those students that answer stand and discuss the module that they found and how it could be used.

* If no one offers up any modules that they found, feel free to call upon some random students to encourage engagement.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/342m3Nh)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:50  |
|---------------------------|---------------------------|

- - -

## 5. Reading Netflix

| Activity Time:       0:30 |  Elapsed Time:      2:20  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 5.1 Instructor Do: Reading In CSV Files (0:10)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 32 - 39.

* While reading in text files can be useful in some circumstances, it is more likely within the data industry to run across files known as CSV files.

  * CSV stands for **Comma** **Separated** **Values** and is essentially a table that has been converted into text format with each row and column being separated by specified symbols.

  * More often than not each row is located on a new line and each column is separated by a comma. Seems simple enough since this is why the file type is called Comma Separated Values.

    ![Example CSV](Images/07-ReadCSV_ExampleFile.png)

* Python has a module called `csv` which allows its users to easily pull in data from external CSV files and perform some operations upon them.

* Open up [07-ReadCSV](Activities/08-Ins_ReadCSV/Solved/read_csv.py) within the editor and go over the code contained within with the class.

  * The first major piece of code to point out is the importing and usages of the `os` module. This module allows Python programmers to very easily create dynamic paths to external files that function across different operating systems.

  ![OS Path](Images/07-ReadCSV_OSPath.png)

  * Instead of `text.read()`, this new code instead utilizes `csv.reader()` to translate the object being opened by Python. It is critical to note the `delimiter=','` parameter being used as this tells Python that each comma within the CSV should be seen as moving into a new column for a row.

  * Reiterate to students that the reading of the file must be done within `with open()` statement.  Outside of that block of code, the variable `csvreader` will not be useful because the file will be closed when the `with open()` block ends. In a later example, students will see that one option for working with the data outside of `with open()` is to append it to a list.

    ![Read CSV Code](Images/07-ReadCSV_ReadCode.png)

  * The code then loops through each row of the CSV and prints out the contents. Make sure to point out how each value is being shown as a string and how all of the rows are lists.

    ![Read CSV Run](Images/07-ReadCSV_ReadRun.gif)

</details>

<details>
    <summary><strong>✏️ 5.2 Students Do: Reading Netflix (0:15)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 40 - 42.

* In this activity, students will be provided with a CSV file containing data taken from Netflix. They will then create an application which searches through the data for a specific movie/show and returns the name, rating, and review score for it.

  ![Read NetFlix](Images/08-ReadNetFlix_Grease.gif)

* After opening up the [09-Stu_ReadNetFlixCSV/netflix.py](Activities/09-Stu_ReadNetFlixCSV/Solved/netflix.py) of this activity in order to show students how their application should function, send out the following file and instructions.

* **File:**

  * [Netflix_Ratings.csv](Activities/09-Stu_ReadNetFlixCSV/Resources/netflix_ratings.csv)

* **Instructions:**

  * Prompt the user for what video they are looking for.

  * Search through the `netflix_ratings.csv` to find the user's video.

  * If the CSV contains the user's video then print out the title, what it is rated and the current user ratings.

    * For example: `'Grease is rated PG with a rating of 86'`

* **Bonus:**

  * You may have noticed that there is more than one listing for some videos.

  * Edit your code to have the title, the rating and user rating printed out only once.

  * Set a variable to `False` to check if we found the video.

  * In the `for loop` change the variable to confirm that the video is found.

  * Insert a `break` statement into the `for loop` to stop the loop when the **first** movie is found. See the [documentation](https://docs.python.org/3.6/reference/simple_stmts.html#break) for additional info.

  * If the CSV does not contain the user's video then print out a message telling them that their video could not be found.

</details>

<details>
    <summary><strong>⭐ 5.3 Review: Reading Netflix (0:05)</strong></summary>

* Send out the [09-Stu_ReadNetFlixCSV/netflix.py](Activities/09-Stu_ReadNetFlixCSV/Solved/netflix.py) of the previous activity and go over the code with the class, answering whatever questions they may have.

* Important topics to cover when discussing this activity:

  * Before doing anything else, Python imports both the `os` and `csv` modules for use later on. It is common practice to import all modules at the start of an application.

  * When opening up the CSV file, the code dictates that each new line in the file should be viewed as a new line of data to be read in.

  ![New Line](Images/08-ReadNetFlix_Newline.png)

  * When reading the CSV file, the delimiter is set to `","` to ensure Python splits up the data into the proper columns whenever a comma is found.

  * The code loops through each row, searching for the row whose first value - index 0 - is equal to that of the search term entered.

  * The rating of a video is at the index of 1 and the review score is located at the index of 5. For the bonus the `break` statement is added to end the loop once a movie is found.

  ![NetFlix Read](Images/08-ReadNetFlix_Read.png)

  * The way in which the bonus operates is fairly simple. First a variable is created that stores the value `False`. If a video matching the user's search is discovered then this value is set to `True`. After the code loops through all of the data stored within the CSV, if the value is still equal to `False` then the apology message is printed to the screen.

  ![Apology Screen](Images/08-ReadNetFlix_Apology.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2R3DYh2)</sub>

- - -

## 6. Udemy Zip

| Activity Time:       0:40 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 6.1 Instructor Do: Writing CSV Files (0:05)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 43 - 46.

* Not only can python read data in from CSV files, it is also wholly capable of writing data into CSV files as well.

  * While this may not seem handy at first, it allows Python users to very easily modify and/or create datasets based upon previous data.

* Open up [10-Ins_WriteCSV/write.py](Activities/10-Ins_WriteCSV/Solved/write.py) within the editor and go through the code with the class, explaining each line as you go along.

  * The syntax for writing into a CSV file is thankfully very similar to that used to read data in from an external file.

  * First, the code references the path that will point into the CSV file the user would like to write to.

  * Next, the `with open()` statement is used once more but with one significant difference. Instead of the parameter `'r'` being passed and directing Python to read a file, the parameter `'w'` is passed instead to inform Python to write to the file.

  * Instead of `csv.reader()`, `csv.writer()` is used to once again inform Python that this application will be writing code into an external CSV file.

  * To write a new row into a CSV file, simply use the `csv.writerow(<DATA LIST>)` function and pass in an array of data as the parameter.

  ![Write CSV](Images/09-WriteCSV_Code.png)

* Run the code and then open up the new CSV file create to show students that the application was successful.

</details>

<details>
    <summary><strong>📣 6.2 Instructor Do: Zipping Lists (0:05)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 47 - 50.

* While it is possible to write new rows of data into a CSV file using a bunch of `csv.writerow()` statements, Python users can far more efficiently write data into a new CSV file by using the `zip()` function.

  * `zip()` takes in a series of lists as its parameters and joins them together into a stack.

* Open up [10-Zip](Activities/11-Ins_Zip/Solved/zipper.py) within the editor and go through the code with the class, explaining each line as you go.

  * This application has three lists, all of which pertain to each other and are of the same length. By zipping these lists together, there is now a single joined list whose indexes reference all three of the lists inside.

  * Zipped listed are turned into iterator objects which are similar to tuples, but once they are iterated over they are empty.  This means each zipped object can only be used once.  For example, you can write the zipped object to a CSV or print to the terminal, but not both.

  ![Zip Run](Images/10-Zip_Run.png)
  ![Zip Code](Images/10-Zip_Code.png)

</details>

<details>
    <summary><strong>✏️ 6.3 Students Do: Udemy Zip (0:20)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 51 - 53.

* Now that students have a decent idea on how to write/read data to/from CSV files, they will now take a large dataset from Udemy, clean it up, and create a new CSV file that is far easier to comprehend.

![Clean CSV](Images/11-UdemyZip_CleanCSV.png)

* After comparing the [12-Stu_UdemyZip/Resources/web_starter.csv](Activities/12-Stu_UdemyZip/Resources/web_starter.csv) to the [12-Stu_UdemyZip/Solved/web_final.csv](Activities/12-Stu_UdemyZip/Solved/web_final.csv) of this activity in order to show students how their application should function, send out the following file and instructions.

* **File:**

  * [WebDevelopment.csv](Activities/12-Stu_UdemyZip/Resources/web_starter.csv)

* **Instructions:**

  * Create a Python application that reads the data on Udemy Web Development offerings.

  * Then store the contents of the Title, Price, Subscriber Count, Number of Reviews, and Course Length into Python Lists.

  * Then zip these lists together into a single tuple.

  * Finally, write the contents of your extracted data into a CSV. Make sure to include the titles of these columns in your CSV.

* **Notes:**

  * As, with many datasets, the file does not include the header line. Use the below as a guide on the columns: "id,title,url,isPaid,price,numSubscribers,numReviews,numPublishedLectures,instructionalLevel,contentInfo,publishedTime"

* **Bonus:**

  * Find the percent of subscribers that have also left a review on the course. Include this in your final output.

  * Parse the string associated with course length, such that we store it as an integer instead of a string. (i.e. "4 hours" should be converted to 4).

</details>

<details>
    <summary><strong>⭐ 6.4 Review: Udemy Zip Review (0:05)</strong></summary>

* Open up and send out the [12-Stu_UdemyZip/web_solved.py](Activities/12-Stu_UdemyZip/Solved/web_solved.py) of the previous activity and go over the code line by line with the class, answering whatever questions they may have.

* Key points to cover during this discussion:

  * There are six empty lists created at the start of this application, all of which will be used to hold specific data taken from within the original CSV and ultimately be zipped together before being written to a new CSV file.

  * For every new row read in from the original CSV file, new data is appended into the lists from earlier. In the cases of `percent` and `length`, the data is being altered before being placed into their respective list.

  ![Udemy Reading](Images/11-UdemyZip_Reading.png)

  * Once all data has been read, the lists are zipped together and written into a new CSV file with a header row being written in beforehand.

  ![Udemy Writing](Images/11-UdemyZip_Writing.png)

</details>

<details>
    <summary><strong>📣 6.5 Instructor Do: Introduction to Functions (0:05)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1Mu-qvYd0BMbh0u02WSFc9LPl_lyeu99Qpa8UjBZKX1g) and use slides 54 - 57.

* Within the field of coding there is a popular acronym - DRY - which many coders live by. It stands for **D**on't **R**epeat **Y**ourself** and essentially states that code should avoid having similar/repeating lines whenever possible.

* One of the best ways to prevent repetition is through the liberal usage of Python functions.

  * A function is a block of organized, reusable code that is used to perform a single, related action. In other words, functions are placeable blocks of code that perform a specific action.

* Open up [13-Ins_Functions/functions.py](Activities/13-Ins_Functions/Solved/functions.py) within the editor and run through the code line-by-line with your class.

  * To create a new function, simply use `def <Function Name>():` and then place the code that you would like to run within the block underneath it.

  * In order to run the code stored within a function, the function itself must be called within the program. Functions will never run unless called upon.

    ```python
    def print_hello():
      print(f"Hello!")

    print_hello()
    ```

  * Functions that take in parameters can also be created by simply adding a variable into the parentheses of the function's definition. This allows specific data to be passed into the function for usage.

    ```python
    def print_name(name):
        print("Hello " + name + "!")

    print_name("Bob Smith")
    ```

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3431dgy)</sub>

- - -

## References

Willden, C. (2017, June 11). 1000 Netflix shows. [https://www.kaggle.com/chasewillden/netflix-shows](https://www.kaggle.com/chasewillden/netflix-shows)

Willden, C. (2017, July 07). Web development courses from Udemy. [https://data.world/chasewillden/web-development-courses-from-udemy](https://data.world/chasewillden/web-development-courses-from-udemy)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
