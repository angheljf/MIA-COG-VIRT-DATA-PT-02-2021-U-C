# 18.1: R We There Yet

## Overview

Today's class will be a relatively short, but an impactful introduction to R. Despite some substantial differences, it shares many similarities with Python. By the end of the lesson, students will be able to leverage their knowledge of Python and pandas into revisiting data analysis tasks they performed in the fourth week, this time in R.

## Class Objectives

* Students will learn the basics of R syntax.
* Students will learn the fundamental R data types.
* Students will gain familiarity with RStudio.
* Students will learn how to create tibbles.
* Students will be able to manipulate data in tibbles.
* Students will be able to compare and contrast the features of Python and R.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* There is a fair amount of overlap between R and Python. Be sure to highlight the similarities as you go through the lesson. This will help students acclimate to the superficial syntactical differences.

* Navigating the file and directory structure in RStudio is a potential logistical hangup for some students. If students appear to be confused on this topic, feel free to emphasize the graphical interface over the command line. The TAs should be ready to help students.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-18-r) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Lastly, as a reminder these slideshows are for instructor use only - when distributing slides to students, please first export the slides to a PDF file. You may then send out the PDF file.

</details>

<details>
  <summary><strong>Sample Class Video</strong></summary>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=10118634-59bc-4f77-899c-aa6a0013930f)

</details>

- - -

# Class Activities

## 1. Introduction to R

| Activity Time:       0:15 |  Elapsed Time:      0:15  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Introduction to R (0:05)</strong></summary>

* R is a language used for data analysis, statistics, and machine learning, more popular in academia than Python.

* Whether Python or R is better than the other is debatable. However, R offers compelling features, including piping and ease of plotting. Other benefits of R include speed, specialized statistical packages, as well as great visualization libraries.

</details>

<details>
  <summary><strong>✏️ 1.2 Students Do: Install RStudio (0:10)</strong></summary>

* **File:** [prework.R](Activities/00_Stu_Installation/Solved/prework.R)

* RStudio is an Integrated Development Environment, which includes all the tools required to program in R.

* In this activity, students will install R, RStudio and several packages.

* Direct students to the download page for their respective operating system: [R for Mac OSX](https://cran.r-project.org/bin/macosx/) or [R for Windows](https://cran.r-project.org/bin/windows/base/).

* Direct students to the [RStudio download page](https://www.rstudio.com/products/rstudio/download/#download) and instruct them to download the RStudio installer for their respective operating system.

* Note, students may already have RStudio installed via Anaconda. But they may not have R itself installed and will need to install it via one of the links above.

* Once R and RStudio are installed, have students open the application.

* Next, they will install the packages that will be used for this week's activities. Send out the `prework.R` file and demonstrate opening the file in RStudio with `File > Open File...`. Alternatively, students can open R files by using `CTRL + click` (Apple) or `right-click` (Windows) and selecting RStudio. Students can also use the built-in file browser in RStudio to find and open files.

* Once the file is open within RStudio, students will install the listed packages. There are several ways to run the installation commands in a batch. One is to highlight all the lines in the text editor pane and click on the `Run` button. Another is to press `Ctrl+Shift+Enter` (`Cmd+Shift+Enter` on Macs).

  ![Images/RStudio1.png](Images/RStudio1.png)

* If students should run into error messages with any of the packages, they can type `install.packages(<"package-name">)` in the Console. For example, if an error message with the `tidyverse` package is returned, we would type `install.packages("tidyverse")` in the console.

  - Send out [this link to R keyboard shortcuts](https://support.rstudio.com/hc/en-us/articles/200711853-Keyboard-Shortcuts).

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3e3Cr4z)</sub>

- - -

## 2. We R in Junior High Again

| Activity Time:       0:30 |  Elapsed Time:      0:45  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Basics of R Syntax (0:10)</strong></summary>

* **Directory:** [Activities/01_Ins_RBasics](Activities/01_Ins_RBasics/Solved)

* Walk through the code with the class. Much of the basic syntax bears resemblance to those we have seen in Python and JavaScript. Little of what is covered today should be completely unfamiliar.

* Consult [Activities/01_Ins_RBasics/01_Ins_R_Basics.nb.html](Activities/01_Ins_RBasics/Solved/01_Ins_R_Basics.nb.html) for the complete code, but here is a more complete explanation.

* In R, like Python, we can assign values to variables without specifying the data type. Unlike Python, however, the left-pointing arrow `<-` is used to accomplish this task, in which the value on the right is assigned to the variable on the left. Semantically, it is probably more accurate than the equality symbol. The equality symbol can be used, and is used in certain cases, as we will see. For simple assignment operations, however, `<-` is preferred.

  ```R
  a <- 3
  b < 3.1415
  c <- "This is a string"
  d <- "Yet another string"
  e <- TRUE
  f <- FALSE
  g <- T
  h <- F
  ```

  * Tip: the keyboard shortcut for the assignment operator is `Option-Hyphen` in Macs, and `Alt-Hyphen` in PCs.

* Like Python lists, an R **vector** can hold multiple items. Unlike Python lists, however, a vector must hold items of the same type:

  ```R
  disney_characters <- c("mickey", "minnie", "donald", "goofy")
  presidents <- c("washington", "adams", "jefferson")
  numbers_vector <- c(1, 3, 5, 7, 9, 11)
  ```

  * Even a single item can be a vector, however.

* **This point is extremely important**: R data structures are indexed at one, whereas Python and JavaScript arrays are indexed at zero. In this example, `presidents[1]` returns the first item from the vector, `"washington"`, whereas in Python or JavaScript, `"adams"` would be returned.

* As seen above, vectors are created using the `c()`, or concatenate, function. We can combine two vectors into a single vector with the same operation:

  ```R
  combined_vector <- c(disney_characters, presidents)
  ```

* A for-loop in R is similar to that in Python and JavaScript:

  ```R
  for (x in combined_vector){
      print(x)
  }
  ```

* We can likewise create a vector of integers using the colon operator (`:`) and the `length` function, and even perform operations on them en masse:

  ```R
  numeric_vector <- 1:length(combined_vector)
  squared_vector <- numeric_vector**2
  ```


* An `if` statement works much the same way in R as it does in Python:

  ```R
  for (prez in presidents){
      if (nchar(prez) > 5){
          next
      }
      else {
        print(prez)
      }
  }
  ```

  * `nchar()` returns the number of characters in a string. `next` stops the current loop iteration and starts a new iteration from the beginning.

* Whereas R vectors can only contain a single data type, a list in R can contain multiple data times.

  ```R
  random_list <- list("movies"=c("Star Wars", "Titanic", "Avatar"),
  						  "states"=c("California", "Oklahoma", "Texas", "Virginia"),
  						  "coins"=c("penny", "dime", "nickel", "quarter"),
  						  "first_presidents"=presidents,
  						  "nums"=c(1,2,3,4,5),
  						  "bools"=c(T,F,T,T,T,F)
  						  )
  ```

  * We can use the bracket notation to access an item in a list:

  ```R
  random_list["states"]
  ```

  * Or a dollar sign to accomplish the same task:

  ```R
  random_list$coins
  ```

* We can verify that `random_list` is indeed a list with `typeof()`:

  ```R
  typeof(random_list)
  ```

</details>

<details>
  <summary><strong>✏️ 2.2 Students Do: We R in Junior High Again (0:15)</strong></summary>

* **Directory:** [Activities/02_Stu_RBasics](Activities/02_Stu_RBasics)

* In this activity, students will practice the basics of R syntax. They will create vectors, use for-loops, use if/else statements, identify substrings of strings, and create functions.

</details>

<details>
  <summary><strong>⭐ 2.3 Review: We R in Junior High Again (0:05)</strong></summary>

* **Directory:** [Activities/02_Stu_RBasics](Activities/02_Stu_RBasics/Solved)

* Go over the solution with the class and answer any questions.

* In Part I, students were required to research how to access the current date. This can be done with [`Sys.Date()`](https://www.rdocumentation.org/packages/base/versions/3.5.1/topics/Sys.time).

* In Part II, students were required to research how to generate a pseudo-random sample of three numbers from 1 through 33. This is accomplished with [`sample(33, 3)`](https://www.rdocumentation.org/packages/base/versions/3.5.1/topics/sample).

  * The first argument is the range of numbers, i.e. from 1 through 33. We can also specify the range thus: `sample(1:33,3)`.
  * The second argument is the number of pseudo-randomly generated numbers to return.

* In Part III, students were required to research how to access a substring of a string. We can do so with [`substr(student, 2, 2)`](https://www.rdocumentation.org/packages/base/versions/3.5.1/topics/substr):

  * The first argument is the string. In this case, `student` stands for the name of each student in the for-loop.
  * The second and third arguments denote the start and end points of the substring. In other words, here we begin at the second letter, and also end our substring at the second letter, returning only the second letter. Additionally, `substr(student, 2, 4)` would return a substring of three letters, from the second through the fourth letter.

* Now would be a good time to introduce [R Markdown](https://rmarkdown.rstudio.com/index.html) for students that did not take the initiative to look into it on their own as it will be used in subsequent activities.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2V5jqGk)</sub>

- - -

## 3. Vectors and Pipes & File Structure Navigation

| Activity Time:       0:30 |  Elapsed Time:      1:15  |
|---------------------------|---------------------------|

<details>
  <summary><strong>🎉 3.1 Everyone Do: Vectors and Pipes (0:10)</strong></summary>

* **Directory:** [Activities/03_Ins_Vectors](Activities/03_Ins_Vectors/Solved)

* In this activity, we will go over how to work with vectors and to run statistical summaries. As you go over each block of code, encourage students to follow along.

* Give special emphasis to the following observations:

  * Just as an array can be used to index a Series in pandas, a vector in R can be paired up as names for another vector using the [names()](https://www.rdocumentation.org/packages/base/versions/3.5.1/topics/names) function.

  * [`summary()`](https://www.rdocumentation.org/packages/base/versions/3.5.1/topics/summary) provides a statistical summary of a data set. We can store the results of `summary()` in a vector and access features of the summary.

  * We can use the familiar square brackets to index elements in a vector.

* Explain that the pipe operator (`%>%`) is a nifty feature that can improve workflow in R. Demonstrate the following example:

  * `summary(precipitation)` is used to obtain a summary of the `precipitation` vector.

  * The same result can be obtained by using the pipe operator: `precipitation %>% summary()`.

  * This means to take what's on the **left** (`precipitation` vector), and perform the operation on the **right** (the `summary()` function).

  * In mathematics, this is equivalent to `f(g(x))`, or `(f ◦ g)(x)`.

  * In computer science, this is equivalent to a Terminal command such as `ps -ax | grep <application name>`

  * The keyboard shortcut for the pipe operator, `%>%`, is `Cmd` + `Shift` + `M` in Macs, and `Ctrl` + `Shift` + `M` in Windows.

  * While the usefulness of the pipe operator may not be immediately obvious, it becomes more apparent in a sequence of multiple operations.

  * R ships with a [stats package](https://www.rdocumentation.org/packages/stats/versions/3.5.1). Here we are using [`sd()`](https://www.rdocumentation.org/packages/stats/versions/3.5.1/topics/sd) to calculate the standard deviation of `precipitation`.

</details>

<details>
  <summary><strong>📣 3.2 Instructor Do: File Structure Navigation (0:10)</strong></summary>

* **Directory:** [Activities/04_Ins_Navigation](Activities/04_Ins_Navigation/Solved)

* **File:** [Activities/04_Ins_Navigation/Solved/data.csv](Activities/04_Ins_Navigation/Solved/data.csv)

* In order to work with external data files, such as CSV files, students will need to familiarize themselves with file structure navigation in R. File structure navigation in R shares some similarities to that in Unix-based environments.

* In R, the command to display the current directory is `getwd()`

  * To accomplish the same task in Terminal or Git Bash, one would type `pwd`.

* To display the contents of the current directory, type `dir()`

  * This is the equivalent of `ls` in Unix-flavored environments.

* To change the directory, enter `setwd()`.

  * This is the equivalent of `cd` in Unix.

* A simpler way to set the working directory in RStudio is to select the `Files` panel, then use either the `up` arrow icons to move up a directory or click on a directory name to navigate into it. Under the `More` menu (designated by the gear icon), select `Set As Working Directory`:

  ![Images/setwd.png](Images/setwd.png)

* Navigate to the directory for this activity, and load the `data.csv` file:

  ![Images/read_csv.png](Images/read_csv.png)

* Inform students that to run a cell of code in an Rmd file, they can click on the green play button, or press `Ctrl+Shift+Enter` (`Cmd+Shift+Enter` in Macs).

* Here are some additional command for students to reference, but they are not required to learn them:

  * To create a directory called "data_science" one would enter `dir.create("data_science")`

  * To create a file: `file.create("my_first.R")`

  * To determine whether a file exists: `file.exists()`

  * Obtain additional info on a file: `file.info()`

  * Rename a file: `file.rename(file1, file2)`

  * To copy a file: `file.copy()`

* Finally, send out the R files and `data.csv` to the class. They will need them for the next activity.

</details>

<details>
  <summary><strong>👥 3.3 Partners Do: Discussion (0:10)</strong></summary

* In this activity, students will pair up with a partner. Each partner will ensure that his or her partner is able to load `data.csv` in RStudio.

  * The `tidyverse` package is required for the `read_csv()` function. Technically, only the `readr` package, which comes with `tidyverse`, is required, but we use `tidyverse` here for convenience.

  * Students may ask about the difference between `read_csv()` and `read.csv()`, if the latter comes up as an auto-complete option. Inform them that the `read_csv()` is more efficient, and is the de facto standard for reading CSV files in R now.

* Students will also discuss the syntax of R, comparing and contrasting it with those of Python and JavaScript. Which features are similar, and which are different from those Python and JavaScript? Among the topics to discuss are:

  * Assignment operator used to assign a variable
  * Declaring a function
  * Basic data structures
  * Concatenating a string
  * Logical operators (they will have to research on logical operators in R)
  * If/Else statements

* Bring the class back and call on students to summarize points from their discussion. Answer any questions about R syntax or file structure navigation.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3e2Z4Ge)</sub>

- - -

## 4. Back to School

| Activity Time:       0:35 |  Elapsed Time:      1:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: DataFrames in R (0:10)</strong></summary>

* **Directory:** [Activities/05_Ins_Tibble](Activities/05_Ins_Tibble/Solved)

* For our purposes, a `tibble` (a word play on "table"), is a data frame.

* Tibbles in R are similar to DataFrames in pandas: data are organized by rows and columns, and allow operations for computation and data-wrangling. However, there are some compelling aspects of R, such as piping, which we will discuss later.

* `tibbles.html` provides a complete walk-through of the code, but here are some additional details.

* `library(tidyverse)`: `tidyverse` is a collection of data science-oriented packages.

  * Tibbles are not available in standard R, but are enabled by `tidyverse` and are generally superior to R's standard data frame.
  * The `library()` function loads this package.

* `data(diamonds, package='ggplot2')`: the `data()` function loads data sources. `diamonds` is a sample data set that comes with `ggplot2`, a plotting package for R.

* As this is an important point, be sure to take the time to emphasize it: Unlike other languages that we have encountered so far, R allows the use of periods/dots in regular variable names:

  ```R
  total.volume2 <- mutate(diamonds, total.volume=(x*y*z))
  ```

  * `total.volume2` does not refer to a `volume2` property of `total` object. It is simply a variable name. It is equivalent to `total_volume2`, for example.


* The `mutate()` function adds a new columnar variable to the tibble.

  ![Images/mutate.png](Images/mutate.png)

  * Note that, in the `Rmd` file, it may be necessary to click on the arrow to reveal more columns of a tibble.

</details>

<details>
  <summary><strong>✏️ 4.2 Students Do: Back to School (0:20)</strong></summary>

* **Files:** [Activities/06_Stu_Tibble](Activities/06_Stu_Tibble)

* This activity will revisit the PySchool homework assignment from the fourth week: this time in R!

* Students will perform some of the same data operations they ran in the homework assignment, including the following:

  * A list of all schools
  * Calculate the total count of schools
  * Calculate the total number of students
  * Calculate the average reading and math scores
  * Calculate the percentage of students with passing reading scores, i.e. over 70%.
  * Calculate the percentage of students with passing math scores, i.e. over 70%.
  * Calculate the overall passing rate, i.e. the average of math and reading passing percentages

</details>

<details>
  <summary><strong>⭐ 4.3 Review: Back to School (0:05)</strong></summary>

* **Files:** [Activities/06_Stu_Tibble](Activities/06_Stu_Tibble/Solved)

* Go over the most salient aspects of this activity, which include the following bullet points.

* We first load `tidyverse` with `library(tidyverse)`, then use `read_csv()` to load an external CSV file.

* `head()` and `tail()` can be used to preview the tibble.

* `unique()` is used to display the unique entries across a column.

* `summarize()` provides a basic statistical summary.

* `filter()` can be used to filter rows.

* `group_by()` can be used to perform aggregate calculations, such as mean and sum.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2JQXrNW)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      2:05  |
|---------------------------|---------------------------|

- - -

## 5. Project 2 Group Work

| Activity Time:       0:55 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 5.1 Students Do: Project 2 Group Work (0:55)</strong></summary>

* Open up the [Project 2 Requirements](https://drive.google.com/open?id=1nDfFo_eU0e3HXbqDYbA9YZ-YR_wHaQgH-8PXvmuj45w) slideshow and explain to the students the requirements and schedule for Project 2

  * The remainder of class is dedicated to Project 2 - the students should be selecting a topic, finding a potential data set and working on their 1-page proposals.

</details>

- - -

## References

Mockaroo, LLC. (2021). Realistic Data Generator. [https://www.mockaroo.com/](https://www.mockaroo.com/)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
