# 9.2 Advanced SQL Queries

## Overview

Today's class will introduce students to additional features of the SQL language. Students will dive deeper into queries with aggregates, grouping, and ordering. Today's lesson will also cover subqueries, creating views, and how to combine both features.

## Class Objectives

By the end of today's class, students will be able to:

- Create aggregate queries.
- Create subqueries to explore data further.
- Create views and run subqueries off of them.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* Today's lesson will mostly use imported datasets, so make sure students are comfortable importing data from CSV files. All schemas for the tables will be provided along with the CSV files. Students who don't have this data imported correctly will not be able to follow along with the lesson.

* This lesson will build on what students learned in the previous class, and each activity will combine multiple SQL elements. Students who are new to SQL may struggle a bit, but many of the concepts are similar to those they have learned previously.

* The TAs should be ready to help students who are confused or who have not imported the data correctly.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-09-sql) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Have your TAs refer to the [Time Tracker](TimeTracker.xlsx) to stay on track.

* Lastly, as a reminder these slideshows are for instructor use only - when distributing slides to students, please first export the slides to a PDF file. You may then send out the PDF file.

</details>

<details>
  <summary><strong>Sample Class Video</strong></summary>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a4fa234d-abac-4d50-92f4-aa6901839443)

</details>

- - -

# Class Activities

## 1. Instructor Presentation

| Activity Time:       0:20 |  Elapsed Time:      0:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Welcome Class (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1ECRAKV4eZSiMhGpcyFiSe3-ERb5AjeSaHDAF4WwCGZM/edit?usp=sharing) and welcome the class using slides 1 and 2.

* Explain that today's lesson will provide a more in-depth look at SQL's features. Students will work with imported tables to expand their SQL skills.

</details>

<details>
  <summary><strong>📣 1.2 Instructor Do: Import Data (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1ECRAKV4eZSiMhGpcyFiSe3-ERb5AjeSaHDAF4WwCGZM/edit?usp=sharing) and use slides 3-5 to assist you to present this chapter.

* **Files:**

  * [schema.sql](Activities/01-Evr_Import_Data/Resources/schema.sql)

  * [Data CSVs](Activities/01-Evr_Import_Data/Resources)

* Explain to the class that today's activities will require a few tables to be imported into a database. The data is taken from a popular [MySQL Database](https://dev.mysql.com/doc/sakila/en/). There is [another database](https://github.com/devrimgunduz/pagila) that is similar to Sakila, but it is instead using PostgreSQL. There are two options for doing so, if any students run into issues with the schema option, direction them to the CSV option.

* Compress the Resources folder and send it out to the class. This folder contains everything students need in order to upload the data.

#### Schema option

* Together, walk through the following steps:

  * From pgAdmin, create a database named `rental_db`.

  * Open the Query Tool for the newly created `rental_db`.

  * Copy [pagila-schema.sql](Activities/01-Evr_Import_Data/Resources/pagila-schema.sql) and run the code to create the needed tables.

  * Copy [pagila-insert-data.sql](Activities/01-Evr_Import_Data/Resources/pagila-insert-data.sql). **Note:** this will take a few minutes due to the amount of data. As long as no errors pop up the data will be uploaded.

* If any students have issues uploading data this way have the follow the CSV option.

#### CSV option

* Together, walk through the following steps:

  * From pgAdmin, create a database named `rental_db`.

  * Open the Query Tool for the newly created `rental_db`.

  * Copy [schema.sql](Activities/01-Evr_Import_Data/Resources/schema.sql) and run the code to create the needed tables.

  * Right-click the **actor** table on the right-hand side, and then select **Import/Export**.

  * Import `actor.csv`.

  * Run `SELECT * FROM actor LIMIT 100;` to confirm that the import was successful.

    Optional: Right-click the **actor** table and view the first 100 rows to check that the data was imported correctly.

  * Have the class repeat this process for the remaining tables.

* While the data is being uploaded the TAs should walk around the classroom to assist students with the database upload.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3aGtTP7)</sub>

- - -

## 2. Gregarious Aggregates

| Activity Time:       0:30 |  Elapsed Time:      0:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Aggregate Functions, Aliases, and Grouping (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1ECRAKV4eZSiMhGpcyFiSe3-ERb5AjeSaHDAF4WwCGZM/edit?usp=sharing) and use slides 6-8 to review the following:

  * Similar to aggregates in Pandas, aggregate functions allow calculations on a set of values and return a singular value. (Slide 4)

  * Some of most commonly used aggregates are `Avg`, `COUNT`, `MIN`, `MAX`, and `SUM`. (Slide 4)

  * Aggregates are often combined with `GROUP BY`, `HAVING`, and `SELECT`. (Slide 5)

* **File:** [aggregates.sql](Activities/02-Ins_Aggregates/Solved/aggregates.sql)

* Select the `rental_db` database in pgAdmin and open a Query window.

* Run `SELECT * FROM film;` and count the number of rows.

* Run `SELECT COUNT(film_id) FROM film;` and explain the following:

  * Using `COUNT()` is an easier way to count the rows.

  * The `COUNT()` function is an aggregate.

  ![Count](Images/Count.png)

* Now that the number of `film_id` entries has been counted, it's easy to see a total of 1,000 films.

* Point out that the name of the field returned is `count bigint`, which doesn't describe the column accurately. Postgres has a way to change the column names and make them more descriptive.

* Run the following:

  ```sql
  SELECT COUNT(film_id) AS "Total films"
  FROM film;
  ```

* Explain the following:

  * `AS 'Total films'` is a technique called *aliasing*.

  * Aliasing creates an `alias`, or a new name for the column.

  * Using an alias does not change the table or the database in any way. Aliasing is only a measure of convenience, used to view a column or to create shortcuts for columns or other data.

  ![Total](Images/Total.png)

* The `COUNT()` function is great to see the number of movies, but it isn't informative enough when searching for the number of specific ratings, like G or PG-13. This is where `GROUP BY` comes into play.

* Run the following code:

  ```sql
  SELECT rating, COUNT(film_id) AS "Total films"
  FROM film
  GROUP BY rating;
  ```

* Explain the following:

  * The `GROUP BY` method will first group by the column indicated.

  * Aggregates are used to get the values for any columns not included in the `GROUP BY` clause.

  * Here, the `COUNT()` function will count the `film_id` for each `rating`.

  ![Ratings](Images/Ratings.png)

* Explain that we can aggregate data in other ways besides counting. For example, *sum*, *average*, *min*, and *max* are all valid aggregate functions to apply to the data.

* Ask the class how to query the average rental period for *all* movies. To demonstrate, run the following query:

  ```sql
  SELECT AVG(rental_duration)
  FROM film;
  ```

* To demonstrate how to add an alias to the `AVG()` function, run the following:

  ```sql
  SELECT AVG(rental_duration) AS "Average rental period"
  FROM film;
  ```

* Put it all together by running the following query, showing how to `GROUP BY` rental duration, get the average `rental_rate`, and give it an alias.

  ```sql
  SELECT  rental_duration, AVG(rental_rate) AS "Average rental rate"
  FROM film
  GROUP BY rental_duration;
  ```

  ![Aggregate1](Images/Aggregate1.png)

* Ask a student to explain the query.

  * Movies that can be rented for three days cost an average of $2.82 to rent, movies that can be rented for four days cost an average of $2.97 to rent, and so on.

* SQL can also return the rows that contain the minimum values and maximum values in a column using `MIN()` and `MAX()` respectively.

```sql
  -- Find the rows with the minimum rental rate
  SELECT  rental_duration, MIN(rental_rate) AS "Min rental rate"
  FROM film
  GROUP BY rental_duration;

  -- Find the rows with the maximum rental rate
  SELECT  rental_duration, MAX(rental_rate) AS "Max rental rate"
  FROM film
  GROUP BY rental_duration;
```

* Mention that these aggregate functions calculate and retrieve data, but they do not *alter* the data. That is, they do not modify the database.

* Explain that there are many other aggregate functions students can research. Send out [Postgres functions](https://www.tutorialspoint.com/postgresql/postgresql_useful_functions.htm) to the class for future reference.

</details>

<details>
  <summary><strong>✏️ 2.2 Student Do: Gregarious Aggregates (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1ECRAKV4eZSiMhGpcyFiSe3-ERb5AjeSaHDAF4WwCGZM/edit?usp=sharing) and use slides 9 and 10 to go over this activity, students will practice writing queries with aggregate functions, with grouping, and with using aliases.

* **File:** [gregarious_aggregates.sql](Activities/03-Stu_GregariousAggregates/Unsolved/gregarious_aggregates.sql)

* **Instructions:** [README.md](Activities/03-Stu_GregariousAggregates/README.md)

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Gregarious Aggregates (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1ECRAKV4eZSiMhGpcyFiSe3-ERb5AjeSaHDAF4WwCGZM/edit?usp=sharing) and use slide 11 to review the activity.

* **File**: [gregarious_aggregates.sql](Activities/03-Stu_GregariousAggregates/Solved/gregarious_aggregates.sql)

* Review the solution in pgAdmin and explain the following:

  * Postgres uses double quotes for table and column names, and single quotes for string constants.

  * `GROUP BY` is similar to the `groupby` operation in Pandas.

  * `SELECT` without aggregates can only choose the columns in the `GROUP BY` clause.

* Answer any questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3bPAaZ2)</sub>

- - -

## 3. Movies Ordered By

| Activity Time:       0:30 |  Elapsed Time:      1:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: Order By Aggregates (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1ECRAKV4eZSiMhGpcyFiSe3-ERb5AjeSaHDAF4WwCGZM/edit?usp=sharing) and use slides 12-14 to demonstrate this module.

* **File:** [order_by_aggregates.sql](Activities/04-Ins_Order_By/Solved/order_by_aggregates.sql)

* Explain that aggregate functions return the results in a random order. This can be tough when trying to find the top or bottom numerical results.

* Open pgAdmin and explain the following:

  * Postgres has a function called `ORDER BY` that will solve this issue. `ORDER BY` is added toward the end of a query, and by default will sort the results by ascending values.

  ```sql
  SELECT rental_rate, AVG(length) AS "avg length"
  FROM film
  GROUP BY rental_rate
  ORDER BY "avg length";
  ```

  * Postgres will add a lot of numbers after the decimal. To reduce the numbers after the decimal, use `ROUND()`. This takes the parameters `ROUND(<value>, <number of decimal places>)`, which rounds the value down to the specified number of decimal places.

  ```sql
  SELECT rental_rate, ROUND(AVG(length),2) AS "avg length"
  FROM film
  GROUP BY rental_rate
  ORDER BY "avg length";
  ```

  * The `ORDER BY` statement can organize by descending values by adding `DESC`.

  ```sql
  SELECT rental_rate, ROUND(AVG(length),2) AS "avg length"
  FROM film
  GROUP BY rental_rate
  ORDER BY "avg length" DESC;
  ```

  * Top results can also be taken by limiting the amount returned using `LIMIT`.

  ```sql
  SELECT rental_rate, ROUND(AVG(length),2) AS "avg length"
  FROM film
  GROUP BY rental_rate
  ORDER BY "avg length" DESC
  LIMIT 5;
  ```

* Answer any questions before moving on.

</details>

<details>
  <summary><strong>✏️ 3.2 Student Do: Movies Ordered By (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1ECRAKV4eZSiMhGpcyFiSe3-ERb5AjeSaHDAF4WwCGZM/edit?usp=sharing) and use slides 15 and 16 to go over this activity, you will use `ORDER BY` in combination with other SQL methods to query and order the tables.

**Instructions:** [README.md](Activities/05-Stu_Order_By/README.md)

</details>

<details>
  <summary><strong>⭐ 3.3 Review Movies Ordered By (5 mins)</strong></summary>

* **File:** [movies_ordered_by.sql](Activities/05-Stu_Order_By/Solved/movies_ordered_by.sql)

* Open the [slideshow](https://docs.google.com/presentation/d/1ECRAKV4eZSiMhGpcyFiSe3-ERb5AjeSaHDAF4WwCGZM/edit?usp=sharing) and use slide 16 to review the activity.

* Open pgAdmin and walk through the solution, highlighting the following:

  * The `actor` table is grouped by `first_name`, with an aggregate taking the count, and then given an alias of `actor count`. The query is then ordered in descending order by the count.

  * The `ROUND` function is used to limit the results to two decimal places.

  * `LIMIT 10` is added to the end of the query to return the top 10 results.

  * For the bonus, a `JOIN` is needed to combine the `country` and `city` tables. The return of the join can then be grouped and aggregated. The result is sorted by the count of countries in descending order.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2X79Ipm)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:35  |
|---------------------------|---------------------------|

- - -

## 4. Subqueries

| Activity Time:       0:30 |  Elapsed Time:      2:05  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: Introduction to Subqueries (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1oxzeWN6YPC01Ylt8avZ78tEdXnbVRfmidvu8fWp0xJw) and use slides 19 and 20 to begin the discussion of subqueries. Explain that a *subquery* is nested inside a larger query.

* **File:** [subqueries.sql](Activities/06-Ins_Subqueries/Solved/subqueries.sql)

* Explain that there is often more than one way of accomplishing a task in SQL.

* For example, suppose we want to view the inventory of a film called *Early Home*. One way to do this is to run several queries in succession. In the first query, we would search by the title and obtain its `film_id` number.

  ```sql
  SELECT title, film_id
  FROM film
  WHERE title = 'EARLY HOME';
  ```

  * The `film_id` is 268. We can use this information to search for data in the `inventory` table:

  ```sql
  SELECT *
  FROM inventory
  WHERE film_id = 268;
  ```

  ![Subquery](Images/subquery.png)

  * There are two copies of this movie—as indicated by two separate `inventory_id` numbers—both located in store number 2.

* At this point, ask the class whether it might be possible to join these two queries into a single query. Then run the following query:

  ```sql
  SELECT i.inventory_id, i.film_id, i.store_id
  FROM inventory i
  JOIN film f
  ON (i.film_id = f.film_id)
  WHERE f.title = 'EARLY HOME';
  ```

* The class should now begin to feel more comfortable with joins. Explain that we can retrieve the same information in a different way, using a tool called a subquery. Type the following query:

  ```sql
  SELECT *
  FROM inventory
  WHERE film_id IN
  (
    SELECT film_id
    FROM film
    WHERE title = 'EARLY HOME'
  );
  ```

* It may look a bit confusing or intimidating at first. Start with the inner query:

  ```sql
  SELECT film_id
  FROM film
  WHERE title = 'EARLY HOME';
  ```

  * This query will return a `film_id` of 268.

  * The next (outer) query is now querying from the results of the inner query.

  * A helpful way to think about this is that the inner query is creating a one-time temporary table, and the outer query is selecting from that temporary table.

* To confirm the result is correct, plug 268 (the result of the subquery) into the parentheses to replace the subquery.

  ```sql
  SELECT *
  FROM inventory
  WHERE film_id IN (268);
  ```

* This will get the same result as the previous join.

  ![subquery](Images/subquery.png)

* We have simplified the query by first running the nested subquery, and then plugging the results into the outer query.

* Explain that Postgres doesn't necessarily run code in that order; it helps us to reduce subqueries to basic queries as building blocks.

* Send out this [link](https://sqlbolt.com/lesson/select_queries_order_of_execution), which explains the order of execution in SQL queries.

* Mention that although we can often accomplish the same task with joins and subqueries, joins tend to be faster.

* Note that `SELECT *` was used in this activity. While this is fine for exploration, in production code, it is standard practice to specify the fields.

* Answer any questions before moving on.

</details>

<details>
  <summary><strong>✏️ 4.2 Student Do: Subqueries (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1oxzeWN6YPC01Ylt8avZ78tEdXnbVRfmidvu8fWp0xJw) and use slides 21 and 22 to give directions to this activity, students will practice creating subqueries.

**Instructions:** [README.md](Activities/07-Stu_Subqueries/README.md)

</details>

<details>
  <summary><strong>⭐ 4.3 Review: Subqueries (5 mins)</strong></summary>

* **File:** [stu_subqueries.sql](Activities/07-Stu_Subqueries/Solved/stu_subqueries.sql)

* Open the [slideshow](https://docs.google.com/presentation/d/1oxzeWN6YPC01Ylt8avZ78tEdXnbVRfmidvu8fWp0xJw) and use slide 23 to review the activity.

* Review the solution in pgAdmin and explain the following:

  * In the first query, we're seeking the name and ID number of cities from a given list:

  ```sql
  SELECT city, city_id
  FROM city
  WHERE city IN ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes');
  ```

  * The second query is a subquery to select the `district`.

  * This query will select the `district` where `city_id` is in the results from the first query.

  ```sql
  SELECT district
  FROM address
  WHERE city_id IN
  (
    SELECT city_id
    FROM city
    WHERE city IN ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes')
  );
  ```

  * Because `district` is not available in the `city` table, we had to use the `city_id` from the `city` table. The `city_id` will now allow a connection between `district` and `city`.

  * The bonus adds another level of subqueries. It requires querying information from the `city` table, with which the `address` table is queried. That information is then used to query the `customer` table.

  ```sql
  SELECT first_name, last_name
  FROM customer cus
  WHERE address_id IN
  (
    SELECT address_id
    FROM address a
    WHERE city_id IN
    (
      SELECT city_id
      FROM city
      WHERE city LIKE 'Q%'
    )
  );
  ```

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2yrRowV)</sub>

- - -

## 5. A View with a Roomful of Queries

| Activity Time:       0:30 |  Elapsed Time:      2:35  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 5.1 Instructor Do: Create Views (Slides 12–14) (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1oxzeWN6YPC01Ylt8avZ78tEdXnbVRfmidvu8fWp0xJw) and use slides 24 and 25 to begin the discussion of views. Explain that a *view* in SQL is a virtual table that can be created from a single table, multiple tables, or another view.

* **File:** [create_views.sql](Activities/08-Ins_Create_Views/Solved/create_views.sql)

* This activity will be a pleasant interlude from some of the heavy lifting we have been doing in Postgres. It is not crucial, so feel free to tweak the length and content as you deem appropriate.

* Up to this point, we have seen relatively long queries, especially when they involve joins and subqueries. There is a way to save a long query under a name and run that name as a shortcut.

* Send out the following query and ask the students run it:

  ````sql
  SELECT s.store_id, SUM(amount) AS Gross
  FROM payment AS p
    JOIN rental AS r
    ON (p.rental_id = r.rental_id)
      JOIN inventory AS i
      ON (i.inventory_id = r.inventory_id)
        JOIN store AS s
        ON (s.store_id = i.store_id)
        GROUP BY s.store_id;
  ````

* The query is used to monitor the total sales from each store, which is something a company executive would want to look up often. Notice that an alias is used to narrow table names down to a single letter. Instead of having to type this query, we can store it under a `view`:

  ```sql
  CREATE VIEW total_sales AS
  SELECT s.store_id, SUM(amount) AS Gross
  FROM payment AS p
  JOIN rental AS r
  ON (p.rental_id = r.rental_id)
    JOIN inventory AS i
    ON (i.inventory_id = r.inventory_id)
      JOIN store AS s
      ON (s.store_id = i.store_id)
      GROUP BY s.store_id;
  ```

* Point out that the query is identical to the one above, except for the first line:

  ```sql
  CREATE VIEW total_sales AS
  ```

* A `view` is created under the name `total_sales`. Created views can be found on the left sidebar in pgAdmin.

  ![views](Images/views.png)

* The rest of the query follows `AS`.

* Run the query. To execute this view, type the following:

  ```sql
  SELECT *
  FROM total_sales;
  ```

* Simple! Ask a student to guess how we might delete a view.

  ```sql
  DROP VIEW total_sales;
  ```

* For the remainder of the activity, have students create and drop their views.

</details>

<details>
  <summary><strong>👥 5.2 Partner Do: A View with a Roomful of Queries (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1oxzeWN6YPC01Ylt8avZ78tEdXnbVRfmidvu8fWp0xJw) and use slides 26 and 27 to explain this activity, students will pair up and practice their join and subquery skills, as well as build out a view.

  * **Instructions:** [README.md](Activities/09-Stu_View_Room_Queries/README.md)

  * **Image:** [subquery.png](Images/subquery.png)

</details>

<details>
  <summary><strong>⭐ 5.3 Review: a View with a Roomful of Queries (5 mins)</strong></summary>

* **File**: [roomful_of_queries.sql](Activities/09-Stu_View_Room_Queries/Solved/roomful_of_queries.sql)

* Open the [slideshow](https://docs.google.com/presentation/d/1oxzeWN6YPC01Ylt8avZ78tEdXnbVRfmidvu8fWp0xJw) and use slide 28 to review the activity.

* Review the code and explain the following:

  * Two pieces of information are required in the query: (1) the title of a film and (2) the number of copies of the title in the system.

  ```sql
  SELECT title,
  (SELECT COUNT(inventory.film_id)
    FROM inventory
    WHERE film.film_id = inventory.film_id ) AS "Number of Copies"
  FROM film;
  ```

  * Add `CREATE VIEW title_count AS` before the above query to create a view for the results.

  * The newly created table view, `title_count`, can now be queried to find which titles have 7 copies in the inventory.

  ```sql
  SELECT title, "Number of Copies"
  FROM title_count
  WHERE "Number of Copies" = 7;
  ```

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2UYaHWq)</sub>

- - -

## 6. Mine the Subquery

| Activity Time:       0:25 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 6.1 Instructor Do: Revisit Subqueries (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1oxzeWN6YPC01Ylt8avZ78tEdXnbVRfmidvu8fWp0xJw) and use slides 29 and 30 to assist you with this chapter.

* **Files**:

  * [revisit_subqueries.sql](Activities/10-Ins_Revist_Subquery/Solved/revisit_subqueries.sql)

  * [Pagila ERD](http://www.postgresqltutorial.com/postgresql-sample-database/)

* Up to this point, the subqueries we've seen have been relatively straightforward. In this activity, we will look at more complicated examples, but tell students not to worry. We can perform complexly nested subqueries using the same principles that we've learned so far.

* We begin with a question: how many people have rented the film *Blanket Beverly*?

* To answer this question systematically, we must first identify the tables needed for our query. To help with this process, an entity relationship diagram (ERD) is used.

* Send out the [ERD](http://www.postgresqltutorial.com/postgresql-sample-database/) link to the class. Tell students to scroll down to the **DVD Rental ER Model**, and then explain the following:

  * An ERD shows the connections between the tables.

  * The schema makes it easier to identify the tables we need as well as the keys we will use to link our subqueries.

  * We will dive deeper into these in the next lesson.

* Tell students that we will need to start with the table `customer` and end with the table `film`, since we are counting how many customers have rented this specific film.

* Ask the class which tables and keys will serve as the intermediaries, or bridges, between these two tables. Then explain the following:

  * Start with the `customer` table and examine its keys. A good place to look is the primary key, which in this table is `customer_id`.

  * The `customer` table has a relationship with the `payment` table, which also contains the `customer_id`.

* Begin a class discussion to determine how to formulate the rest of the subquery using the ERD. One solution could be the following:

  * Connect the `payment` table with the `rental` table using the key `rental_id`, which these tables have in common.

  * Connect to the `inventory` table using the key `inventory_id`.

  * Connect the `film` table using the key `film_id`, which it has in common with the `inventory` table.

  * In the last subquery, query the film title, BLANKET BEVERLY.

* The sample query would be as follows:

  ```sql
  SELECT COUNT(*)
  FROM customer
  WHERE customer_id IN
  (
    SELECT customer_id
    FROM payment
    WHERE rental_id IN
  (
    SELECT rental_id
    FROM rental
    WHERE inventory_id IN
    (
      SELECT inventory_id
      FROM inventory
      WHERE film_id IN
      (
        SELECT film_id
        FROM film
        WHERE title = 'BLANKET BEVERLY'
      )
    )
  )
  );
  ```

* `COUNT(*)` will count the number of rows, similar to how `SELECT *` will select all rows. The asterisk indicates *all*.

* Run the query, which will return that 12 people have rented this film.

* Explain that there are often multiple ways to find this result through different table relationships.

* Answer any questions before moving on.

</details>

<details>
  <summary><strong>✏️ 6.2 Student Do: Mine the Subquery (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1oxzeWN6YPC01Ylt8avZ78tEdXnbVRfmidvu8fWp0xJw) and use slides 31 and 32 to go over this activity, students will continue to practice subqueries. Students can either work individually or in pairs.

**Instructions:** [README.md](Activities/11-Stu_Mine_the_Subquery/README.md)

</details>

<details>
  <summary><strong>⭐ 6.3 Review: Mine the Subquery (5 mins)</strong></summary>

* **File**: [mine_the_subquery.sql](Activities/11-Stu_Mine_the_Subquery/Solved/mine_the_subquery.sql)

* Open the [slideshow](https://docs.google.com/presentation/d/1oxzeWN6YPC01Ylt8avZ78tEdXnbVRfmidvu8fWp0xJw) and use slide 33 to review the activity.

* Review the solution to the activity and answer any questions that students have.

* A possible solution to the first problem is as follows:

  ```sql
  SELECT first_name, last_name
  FROM actor
  WHERE actor_id IN
  (
    SELECT actor_id
    FROM film_actor
    WHERE film_id IN
    (
      SELECT film_id
      FROM film
      WHERE title = 'ALTER VICTORY'
    )
  );
  ```

  * It is recommended that you start with the most specific piece of information and work your way up. In this case, the innermost subquery retrieves the `film_id` of the given film title.

  * This information is used to retrieve the `actor_id`, which is then used to extract the names of the actors who appear in the film.

* A possible solution to the second problem is as follows:

  ```sql
  SELECT title
  FROM film
  WHERE film_id
  IN (
    SELECT film_id
      FROM inventory
      WHERE inventory_id
      IN (
          SELECT inventory_id
          FROM rental
          WHERE staff_id
          IN (
                SELECT staff_id
                FROM staff
                WHERE last_name = 'Stephens' AND first_name = 'Jon'
              )
          )
    );
  ```

  * Similar to the first problem, the query begins with the most specific piece of information and works its way up.

  * The employee name is used to query the `staff_id`.

  * The `staff_id` is used to retrieve the `inventory_id` from rentals.

  * The `inventory_id` is used to retrieve the `film_id`, which is then used to retrieve the relevant film titles.

* Answer any questions before ending class.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/39F66O4)</sub>

- - -

### End Class

- - -

## References

Oracle Corporation. (2019). Sakila Sample Database. Edited by Devrim Gündüz into Pagila. [Sakila Sample Database](https://github.com/devrimgunduz/pagila)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
