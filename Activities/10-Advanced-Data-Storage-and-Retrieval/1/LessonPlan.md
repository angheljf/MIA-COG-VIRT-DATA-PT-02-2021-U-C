# 10.1 Introduction to SQLAlchemy

## Overview

Today's lesson will introduce students to the SQLAlchemy library for Python.

## Class Objectives

* Students will  be able to connect to a SQL database using SQLAlchemy
* Students will learn to perform basic SQL queries using engine.execute()
* Students will learn how to create Python classes and objects
* Students will  be able to create, read, update, and delete data from a SQL database using SQLAlchemy's ORM

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* This first day on SQLAlchemy includes a lot of material students will need for the homework whilst day two includes more complex activities for the class to practice on. As such, feel free to mix up the timing/activities for these two lessons so as to ensure students feel comfortable with the SQLAlchemy library and are having an enjoyable experience.

* If SQLAlchemy is not running on a student's computer, simply have them `conda install -c anaconda sqlalchemy` within their terminal/GitBash.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#Unit-10-advanced-data-storage-and-retrieval) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

</details>

<details>
  <summary><strong>Sample Class Video</strong></summary>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=12880620-a753-4da5-bc76-aa6d00f7814e)

</details>

- - -

# Class Activities

## 1. Intro to SQLAlchemy

| Activity Time:       0:10 |  Elapsed Time:      0:10  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Welcome the Class (0:00)</strong></summary>

* Welcome the class back to another fun-filled week of SQL. This week, the class will use Python to interact with SQL databases.

* Open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 1 and 2 to welcome the class. Be sure to cover the following:

* Explain that this week's class will combine what we learned last week using SQL and combining it with our favorite programming language - Python!

* Explain to the students what the class objectives are for today:

  * Connect to a SQL database with SQLAlchemy.

  * Perform a SQL query with SQLAlchemy.

  * Create Python classes and objects.

  * Use a Python class to model a SQL table.


</details>

<details>
  <strong><summary>👥 1.2 Partners Do: Looking Into SQLAlchemy (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 3-5 to cover the next activity. Be sure to cover the following:

* Before diving into SQLAlchemy as a class, have students break into groups of two or three and research the following questions...

  * What is an ORM?

  * What are the benefits to using an ORM?

  * What are some of the disadvantages to using an ORM?

* After 3 minutes, have the students come back together to answer the questions above.

  * Some of the advantages to using an ORM for SQL databases include:

    * Being able to work across different SQL dialects using the same basic Python query.

    * Being able to create command line interfaces that allow users to construct SQL queries without having to know the language.

</details>

<details>
  <summary><strong>📣 1.3 Instructor Do: Introduction to SQLAlchemy (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 6-9 to accompany this activity. Be sure to cover the following talking points:

* Explain that SQLAlchemy is a Python library designed to work with SQL databases.

  * SQLAlchemy bridges the differences in the various dialects of SQL.

  * This means that a single Python script that uses SQLAlchemy can perform the same query across the different SQL dialects, such as PostgreSQL, SQLite, and MySQL.

* Send out the link to the [SQLAlchemy](https://www.sqlalchemy.org/features.html) features page, and tell the students they can refer to this page if they are interested in just how flexible and robust `SQLAlchemy` can be.

* Explain that SQLAlchemy is able to query a SQL database with SQL or Python:

  * The first query is a simple select all query: `SELECT * FROM icecreamstore;`

  * The second queries a database called `BaseballPlayer` that is imported into Python.

  * `player.name_given` uses the dot notation. We will return to what this means and how it is used in our discussion of Python classes and SQLAlchemy ORM.

* Finally, explain that an ORM can also provide greater security against malicious queries such as SQL injections. Feel free to send a [link](https://www.w3schools.com/sql/sql_injection.asp) on injections, but do not dwell on the topic.

* Send the class the link to the [SQLAlchemy Documentation](http://docs.sqlalchemy.org/en/latest/dialects).

  * The page lists SQL dialects that are compatible with SQLAlchemy.

  * To the left side of the page, students can find the complete documentation of the SQLAlchemy library.

  * Students should consult this documentation to clarify any questions they may have before consulting the instructional team. They should be able to fix any number of bugs they encounter this way.

</details>

- - -

## 2. Ice Cream Connection

| Activity Time:       0:30 |  Elapsed Time:      0:40  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.2 Instructor Do: Building a SQLAlchemy Connection (0:10)</strong></summary>

* You may open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 10-12 to accompany the beginning of this activity. Otherwise, be sure to cover the following:

* Let the class know that, for the purposes of today's class, they will only be working with SQLite databases.

  * SQLite is a SQL dialect that shares much the same syntax as PostgreSQL but that it is entirely serverless.

  * How can a database be serverless? Well, SQLite reads and writes directly to ordinary disk files which can in-turn be stored on a computer's hard drive. This makes it amazingly easy to perform tests with and share between users.

  * If any students do not have SQLite installed, have them run `conda install -c anaconda sqlite` within their Terminal/GitBash.

* Once everyone has installed SQLite, open up [01-Ins_BasicSQL_Connection](Activities/01-Ins_BasicSQL_Connection/Solved/Read_Census_Data.ipynb) within Jupyter Notebook and go through the code with the class.

  * In order to use SQLAlchemy, certain modules from the library must be imported. For example, to create a connection to a SQL database, the `create_engine` module will need to be imported.

  * After importing in all of the necessary libraries/modules, the connection engine can finally be created using the `create_engine()` method from earlier and passing a connection string into it.

    ```python
    engine = create_engine(f"sqlite:///{database_path}")
    ```

  * Connection strings can also include the database username, password, or database name. Students can refer to the SQLAlchemy documentation to determine how to connect to other databases, but today's class will focus on sqlite.

* Once a connection engine has been created, developers can then use `engine.execute()` to run SQL commands from their Python script. Simply pass the code to run into the method as a string and SQLAlchemy will pass the request onto the database.

  * For example, to collect all of the data stored within a table on a database, simply pass `SELECT * FROM <Tablename>` into the `engine.execute()` method.

    ![Engine Execute](Images/01-Connections_Execute.png)

  * Point out how the data being returned in [01-Ins_BasicSQL_Connection](Activities/01-Ins_BasicSQL_Connection/Solved/Read_Census_Data.ipynb) is stored within a variable and then looped through so as to print out the rows from `Census_Data`.

* Answer whatever questions the class may have before moving onto the next activity.

</details>

<details>
  <summary><strong>✏️ 2.2 Students Do: Ice Cream Connection (0:15)</strong></summary>

* **Files**:

  * [02-Stu_IceCreamConnection/IceCreamConnector.ipynb](Activities/02-Stu_IceCreamConnection/Unsolved/IceCreamConnector.ipynb)

  * [02-Stu_IceCreamConnection/Resources/icecreamstore.csv](Activities/02-Stu_IceCreamConnection/Resources/icecreamstore.csv)

* **Instructions**: [02-Stu_IceCreamConnection/README.md](Activities/02-Stu_IceCreamConnection/README.md)

* In this activity, students will be creating a new database and connection to it using SQLAlchemy. They will then read the data in with `engine.execute()`.

* You may open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 13-15 to accompany this activity.

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Ice Cream Connection (0:05)</strong></summary>

* Open up [02-Stu_IceCreamConnection](Activities/02-Stu_IceCreamConnection/Solved/IceCreamConnector.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, answering whatever questions students may have.

* Make sure to hit upon the following points...

    ![Ice Cream Code](Images/02-IceCreamConnect_Code.png)

  * The queries being used by `engine.execute()` are using plain SQL.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2JzeR1C)</sub>

- - -

## 3. Read All the SQL

| Activity Time:       0:25 |  Elapsed Time:      1:05  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: SQLAlchemy and Pandas (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 16-19 to accompany the beginning of this activity. Be sure to cover the following:

  * One of the most impressive aspects of SQLAlchemy is how it integrates with Pandas.

  * After creating the engine and connection to our SQL database, we can use Pandas to query the database and store the records in a DataFrame.

* Open up [03-Ins_ReadSQL](Activities/03-Ins_ReadSQL/Solved/SQLIntoPandas.ipynb) within Jupyter Notebook in order to show the class how this can be accomplished.

  * Through creating a connection to a database using SQLAlchemy, Pandas can use that engine to pull data directly into a dataframe with the `pd.read_sql()` method.

  * When using the `pd.read_sql()` method, a query string and a connection variable must be passed through. The query string is the same as those written for SQL while the connection variable can be declared using `engine.connect()`.

    ```python
    data = pd.read_sql("SELECT * FROM Census_Data", conn)
    ```

  * Although SQL can always be used for basic analysis, it is often easier to use pandas for exploratory analysis and data wrangling.

* Answer whatever questions the class may have before continuing onto the next activity.

</details>

<details>
  <summary><strong>✏️ 3.2 Students Do: Read All the SQL (0:10)</strong></summary>

* **Files**:

  * [04-Stu_ReadAllTheSQLs/Census_Data.csv](Activities/04-Stu_ReadAllTheSQLs/Resources/Census_Data.csv)

  * [04-Stu_ReadAllTheSQLs/zip_census.csv](Activities/04-Stu_ReadAllTheSQLs/Resources/zip_census.csv)

  * [04-Stu_ReadAllTheSQLs/Read_All_The_SQLs.ipynb](Activities/04-Stu_ReadAllTheSQLs/Unsolved/Read_All_The_SQLs.ipynb)

* **Instructions**: [04-Stu_ReadAllTheSQLs/README.md](Activities/04-Stu_ReadAllTheSQLs/README.md)

* Students will now query an external server using Pandas and SQLAlchemy as they work to create new dataframes based on US census data.

* You may open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 20-22 to accompany this activity.

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Read All the SQL (0:05)</strong></summary>

* Open up [04-Stu_ReadAllTheSQLs](Activities/04-Stu_ReadAllTheSQLs/Solved/Read_All_The_SQLs.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, answering whatever questions students may have.

</details>

<details>
  <summary><strong>📣 3.4 Instructor Do: Preview SQLAlchemy with Classes (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 23-25 to accompany the beginning of this activity. Be sure to cover the following:

* So far the class has been using SQLAlchemy in ways that make it work in similar fashion to SQL. It takes in strings of SQL code and then performs some tasks based upon that. This, however, is not how it is used in most cases.

* Classes are essentially blueprints for Python objects. In other words, they allow developers to create organized variables with keys, values, and methods on the fly.

* In the case of SQLAlchemy, we can use classes to make a table blueprint and update the SQL schema.

* Open up [05-Ins_Preview_SQL_Alchemy](Activities/05-Ins_Preview_SQL_Alchemy/Solved/Alchemy.ipynb) within an IDE and show the class how differently this code looks in comparison to those scripts they wrote previously.

  * The first thing that should stand out as different to students are the two classes near the top of the application.

  * It is not terribly important for students to understand what these classes mean at the moment. Once the class reconvenes after break, students will be diving much deeper into creating/using classes.

  * What is important is for students to understand that SQLAlchemy uses Python classes as its primary means to communicate and make changes to SQL databases. This is what makes SQLAlchemy an ORM as it uses objects to map changes to SQL tables/databases.

* Let the class know that it is normal to feel intimidated by SQLAlchemy at first. Thankfully this class will be taking a deep look into how the library functions and the whole team will be right there beside them as they become masters of this ORM.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/347qdU1)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:20  |
|---------------------------|---------------------------|

- - -

## 4. Surfer Class

| Activity Time:       0:30 |  Elapsed Time:      1:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: A Schooling on Classes (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 27-29 to accompany the beginning of this activity. Be sure to cover the following:

* Once everyone has returned from their break, let the class know that they will now be given a crash course in object oriented programming.

  * Object oriented programming (OOP) is a style of coding based around the concept of "objects". These objects may contain data, often known as attributes, and functions, often known as methods.

  * Python is a class-based programming language. This means that objects can be created according to user-created blueprints, thus allowing developers to rapidly create objects of similar structure/purpose but with differing values.

* Open up [06-Ins_Classes](Activities/06-Ins_Classes/Solved/Dog.ipynb) within an IDE and go through the code line-by-line.

  * To define a class in Python, developers simply have to type `class <ClassName>():`

  * The line `def __init__(self):` is a special method called a "class constructor" that Python calls every time a new instance of the class is created.

  * The parameters declared within `__init__` - excluding "self" - must be passed whenever the developer wishes to create a new instance of the class. This is because each object's values will be defined by these parameters.

    ![Declaring Classes](Images/06-Classes_Declare.png)

  * Creating an instance of a class is quite simple. Simply call the class using the class name and pass in whatever arguments its `__init__` method accepts.

  * Users can then access the object's attributes using dot operators with the object. So, in order to call the `name` attribute of an object, one would use `object.name`

    ![Class Instances](Images/06-Classes_Instance.png)

* Go over this code one more time with the class, answering whatever questions students may have. Once everyone is comfortable with Python classes, move onto the next activity.

</details>

<details>
  <summary><strong>✏️ 4.2 Students Do: Surfer Class (0:15)</strong></summary>

* **Files**: [07-Stu_Surfer_Class/Surfer.ipynb](Activities/07-Stu_Surfer_Class/Unsolved/Surfer.ipynb)

* **Instructions**: [07-Stu_Surfer_Class/README.md](Activities/07-Stu_Surfer_Class/README.md)

* Students will now work on creating their own classes in Python. More specifically, they will be creating a "Surfer" class which will be used more throughout today's lesson.

  ![Surfer Class Output](Images/07-SurferClass_Output.png)

* You may open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 30-32 to accompany this activity.

</details>

<details>
  <summary><strong>⭐ 4.3 Review: Surfer Class (0:05)</strong></summary>

* Open up [07-Stu_Surfer_Class](Activities/07-Stu_Surfer_Class/Solved/Surfer.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, answering whatever questions students may have.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2JDJWBq)</sub>

- - -

## 5. Surfer Class Extended

| Activity Time:       0:20 |  Elapsed Time:      2:10  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 5.1 Instructor Do: A Method to The Classes (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 33-35 to accompany the beginning of this activity. Be sure to cover the following:

* Creating and attaching methods to Python classes is also fairly easy to accomplish, thus allowing developers to attach regularly used functions to objects of similar types.

  * Adding methods to a class is very similar to the `__init__` method discussed earlier. Simply define the function using `def`, provide it with a name, and then pass a list of parameters - including self - into the parentheses that follow.

  * To run the method in code, simply call upon the instance of an object created and then, using dot notation, reference the method. For example: `doggy.printHello()` would run the `printHello()` method for the `doggy` object.

* Open up [08-Ins_Classes_With_Methods](Activities/08-Ins_Classes_With_Methods/Solved/Classes_With_Methods.ipynb) within an IDE and go through the code line-by-line, answering whatever questions students may have.

  * The `boast()` method contained within the `Expert` class takes in another object as a parameter and then prints out some statements based upon its contents.

    ![Class Methods](Images/08-ClassMethods_Code.png)

* Answer whatever questions students may have before moving onto the next activity.

</details>

<details>
  <summary><strong>✏️ 5.2 Students Do: Surfer Class Extended (0:10)</strong></summary>

* **File**: [09-Stu_Surfer_Class_Extended/Surfer_Extended.ipynb](Activities/09-Stu_Surfer_Class_Extended/Unsolved/Surfer_Extended.ipynb)

* **Instructions**: [09-Stu_Surfer_Class_Extended/README.md](Activities/09-Stu_Surfer_Class_Extended/README.md)

* The class will now be reworking their Surfer script from earlier as they add in some methods to perform some specific tasks.

  ![Surfer Methods Output](Images/09-SurferMethods_Output.png)

* You may open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 36-38 to accompany this activity.

</details>

<details>
  <summary><strong>⭐ 5.3 Review: Surfer Class Extended (0:05)</strong></summary>

* Open up [09-Stu_Surfer_Class_Extended](Activities/09-Stu_Surfer_Class_Extended/Solved/Surfer_Extended.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, answering whatever questions students may have.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2JEbzdn)</sub>

- - -

## 6. Surfing SQL

| Activity Time:       0:50 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>🎉 6.1 Everyone Do: Back to the SQL (0:20)</strong></summary>

* You may open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 39 and 40 to accompany the beginning of this activity.

* Now that everyone has a firm grasp on how to create and use Python classes, it is time to dive back into SQLAlchemy and its class-based methodology.

* For the purposes of this activity, start out with a blank Python script and have the class follow along. By the end of the activity, everyone should have code that looks that stored in [10-Ins_SQL_Alchemy_Revisited](Activities/10-Ins_SQL_Alchemy_Revisited/Solved/Alchemy_Annotated.ipynb).

* As with most Python code that uses external libraries, the first step is to import in the modules desired.

  * `create_engine` allows SQLAlchemy to create connections to SQL databases.

  * `declarative_base` allows SQLAlchemy to convert the classes created in Python to SQL tables.

  * The different datatypes used in SQL must also be imported into Python from SQLAlchemy. These datatypes are then used when creating class fields so as to state what datatypes each column in the SQL table should contain.

    ```python
    # Dependencies
    # ----------------------------------
    # Imports the method used for connecting to DBs
    from sqlalchemy import create_engine

    # Imports the methods needed to abstract classes into tables
    from sqlalchemy.ext.declarative import declarative_base

    # Allow us to declare column types
    from sqlalchemy import Column, Integer, String, Float
    ```

* The classes created using SQLAlchemy's "Base" class will serve as the anchor points for SQL tables.

  * When creating classes to be used with SQLAlchemy, a `__tablename__` field must be declared and provided with the name of a table. If the table exists, any new objects created will be added into the existing table. If the table does not yet exist, a new table will be created based upon the class' fields.

  * Each field of a SQLAlchemy class must be declared as a column and the datatype of the field must also be provided.

  * A primary key can also be set by using the `primary_key` value and setting it to either True or False.

    ```python
    # Sets an object to utilize the default declarative base in SQL Alchemy
    Base = declarative_base()

    # Creates Classes which will serve as the anchor points for our Tables
    class Dog(Base):
        __tablename__ = 'dog'
        id = Column(Integer, primary_key=True)
        name = Column(String(255))
        color = Column(String(255))
        age = Column(Integer)

    class Cat(Base):
        __tablename__ = 'cat'
        id = Column(Integer, primary_key=True)
        name = Column(String(255))
        color = Column(String(255))
        age = Column(Integer)
    ```

  * Creating instances of SQLAlchemy classes functions almost identically to creating regular Python objects. It is not necessary to declare fields explicitly within the constructor but this is common practice.

    ```python
    # Calls the Pet Constructors to create "Dog" and "Cat" objects
    dog = Dog(name='Rex', color='Brown', age=4)
    cat = Cat(name='Felix', color='Gray', age=7)
    ```

* After the SQLAlchemy classes have been made, they can be created on the SQL database by creating a connection engine and then calling `Base.metadata.create_all(engine)`

  * The `create_all` looks through the Python script and checks if the classes declared exist within the database being connected to. If they do not yet exist, the tables will be created at this time.

    ```python
    # Create Database Connection
    # ----------------------------------
    # Creates a connection to our DB
    engine = create_engine("sqlite:///pets.sqlite")
    conn = engine.connect()

    # Create a "Metadata" Layer That Abstracts our SQL Database
    # ----------------------------------
    # Create (if not already in existence) the tables associated with our classes.
    Base.metadata.create_all(engine)
    ```

* SQLAlchemy functions much like Git does in how new rows of data can be added/changed within a SQL table.

  * A SQLAlchemy session is created using the `Session` module and bound to the connection engine.

  * New rows of data can then be staged by creating a new instance of a SQLAlchemy class and passing them into `session.add()` as a parameter.

  * When all of the changes desired have been made, simply use `session.commit()` to push them up to the database.

    ```python
    # Session is a temporary binding to our DB
    from sqlalchemy.orm import Session
    session = Session(bind=engine)

    # Add Records to the Appropriate DB
    # ----------------------------------
    # Use the SQL ALchemy methods to run simple "INSERT" statements using the classes and objects
    session.add(dog)
    session.add(cat)
    session.commit()
    ```

* Run through the code as many times as needed so as to ensure that the class fully understands how to use SQLAlchemy to add new data/tables to a SQL database.

  * Feel free to point out how simple it is to collect all of the data from a SQL table using SQLAlchemy as well.

  * Simply use `session.query()` and pass the class/table to query in as a parameter. The returned data can then be looped through and printed to the terminal.

    ```python
    # Perform a simple query of the database
    dog_list = session.query(Dog)
    for doggy in dog_list:
        print(doggy.name)

    cat_list = session.query(Cat)
    for kitty in cat_list:
        print(kitty.name)
    ```

* When the class seems comfortable with the script they have just written, go through it one final time and have them describe to you what each line does. Upon reaching the end of the script, feel free to move onto the next activity.

</details>

<details>
  <summary><strong>✏️ 6.2 Students Do: Surfing SQL (0:20)</strong></summary>

* **Files**: [11-Stu_Surfer_SQL/Surfer_SQL.ipynb](Activities/11-Stu_Surfer_SQL/Unsolved/Surfer_SQL.ipynb)

* **Instructions**: [11-Stu_Surfer_SQL/README.md](Activities/11-Stu_Surfer_SQL/README.md)

* Students will now test their SQLAlchemy skills as they attempt to turn their Surfer class from earlier into a new table on a SQL database whilst also creating a new Board class.

* You may open the [slideshow](https://docs.google.com/presentation/d/1h8PkezJoa70IwaygZVO-SMTXovB1frZlC3udsL3zlIQ) and use slides 36-38 to accompany this activity.

</details>

<details>
  <summary><strong>⭐ 6.3 Review: Surfing SQL (0:10)</strong></summary>

* Open up [11-Stu_Surfer_SQL](Activities/11-Stu_Surfer_SQL/Solved/Surfer_SQL.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, answering whatever questions students may have.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3aG39hN)</sub>

- - -

## References

U.S. Department of Commerce Bureau of the Census. (2019) ACS 1-Year Estimates-Public Use Microdata Sample. [https://data.census.gov/mdat/#/](https://data.census.gov/mdat/#/)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
