# 2.2 Fundamentals of Programming Using Visual Basic: Day 2

## Overview

In today's class, students will learn to use basic for-loops and nested for-loops in conjunction with conditionals to complete common coding challenges in VBA.

## Class Objectives

* Students will understand the basic syntax of a VBA for loop
* Students will understand how to utilize for-loops in conjunction with conditionals to direct logic flow
* Students will understand the value of a nested for-loop and gain basic proficiency in their use
* Students will refine their fundamental coding skills (syntax recollection, pattern recognition, problem decomposition, and debugging)

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* Today is a fun class, albeit a challenging one. In this class, students will complete a series of programming challenges in VBA. As with many classes to come, this one is exercise heavy. Today's class should feel lively as students struggle through challenges and experience many "light bulb" moments. Do your part to facilitate this atmosphere by encouraging continual dialogue within groups.

* Because today's class is heavy on exercises, your time behind the podium should feel minimal. Instead, wander the class continually and bring your "teaching" to their seats. This approach will allow you to tailor your teaching to the needs of specific students.

* As with the previous class, it is important to stress that today's exercises are very much paradigmatic of fundamental programming across languages. At times, you may hear students express frustration at VBA. In these moments, do your part to re-frame their thinking. Inform them that the real challenge isn't from VBA, but rather from the increased complexity that comes when fundamental building blocks are layered atop one another.

* Have your TAs refer to the [Time Tracker](TimeTracker.xlsx) to stay on track.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-02-vba-scripting) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* When the lesson plan calls for files to be sent to students there are a few ways to do so. For the first couple of weeks it may be easiest to use Slack, but as the files and directories get more complex you may look to try alternate methods such as pushing and pulling from GitHub/GitLab and sending out the link, using a file storage like google drive, or zipping up files and continuing to Slack out. Please use whatever method you find most comfortable for sending files out to students.

* Lastly, as a reminder these slideshows are for instructor use only - when distributing slides to students, please first export the slides to a PDF file. You may then distribute send out the PDF file.

</details>

<details>
  <summary><strong>Sample Class Video</strong></summary>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=c61448c1-d0f1-4033-911a-2578c22a2b8b)

</details>

- - -

# Class Activities

## 1. Welcome & Budget Checker

| Activity Time:       0:30 |  Elapsed Time:      0:30  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Welcome Students (0:05)</strong></summary>

* Spend a few moments to welcome students. Inform them that in today's class, we'll be “ripping off the band-aid.” They'll be spending the majority of class focused on exercises that will build their programming skills.

* If you'd like, feel free to use the [slideshow](https://drive.google.com/open?id=1L-_yIwbWQTkFix_af4cWoKM6fV3-BkStu-GyVqON138) included in the lesson plan to tee off class with some warm-ups.

</details>

<details>
  <summary><strong>👥 1.2 Partners Do: Warm-up Activity (Budget Checker) (0:15)</strong></summary>

* After your welcome, direct students to the Warm-Up Activity. This activity involves them creating a script to calculate and correct a price inclusive of fees.

![Images/01-Stu_Warmup_1.png](Images/01-Stu_Warmup_1.png)

* Show students how the solved code should work, then have your TAs send out the instructions and unsolved file:

  * **Files:**

    * [budget_checker_unsolved](Activities/01-Stu_Warmup/Unsolved/budget_checker_unsolved.xlsm)
    * [README](Activities/01-Stu_Warmup/README.md)

  * **Instructions:**

    * Create a VBA Script to complete the budget checker.

    * There are three parts to this problem.

      * Part 1: Calculate the total after fees and enter the value in the "Total" cell.

      * Part II: Create a Message Box to alert the user as to whether the amount including fees is within or over budget.

      * Part III (Challenge): If the total is over budget, correct the price so that it fits within the max of the user's budget. Be sure to round down! (Example: If the user's budget is 100 and the fees are 15%, the max price should 86)

  * **Hints:**

    * Break up the problem into smaller steps.

    * Look at old code!

    * You got this!

</details>

<details>
  <summary><strong>⭐ 1.3 Review: Warm-up (Budget Checker) (0:10)</strong></summary>

* **File:** [Activities/01-Stu_Warmup/Solved/budget_checker_solved.vbs](Activities/01-Stu_Warmup/Solved/budget_checker_solved.vbs)

* Once time is complete, review the solution of the previous exercise. As you are doing so, encourage students to explain what is happening in the code for you.

* In your discussion of Part I, be sure to point out the following:

  * First, we created a variable called `total` (as a double) to hold our full cost.

  * Next, we combined the price and (1 + tax) to calculate the full cost.

  * Finally, we entered the final cost into the total cell.

```vb
  ' Part I
  ' ----------------------------------------------------

  ' 1. Retrieve the Price and Fees from the cells
  Dim total As Double

  ' 2. Use these values to calculate the total
  total = Range("F3").Value * (1 + Range("H3").Value)
  ' MsgBox(total)

  ' 3. Enter the total into the appropriate cell
  Range("L3").Value = total
```

* In your discussion of Part II, be sure to point out the following:

  * First, we created a variable called `budget` to hold our budget amount.

  * We then compared the value of our budget against the total.

  * If the budget was greater than the total, we displayed a message that we were under budget. If greater, the message stated that we were over budget.

```vb
  ' Part II
  ' ----------------------------------------------------
  ' 4. Create a variable to store budget
  Dim budget As Double
  budget = Range("B3").Value
  ' msgbox(budget)

  ' 5. Compare using conditionals whether total is greater than or less than the budget
  If budget > total Then

      MsgBox ("Under budget")

  Else

      MsgBox ("Over budget")
  End If
```

* In your discussion of Part III, be sure to point out the following:

  * First we needed to do some basic algebra to determine our formula for the new price. In this case new price was equal to the budget divided by (1 + tax).

  * We then stored the new price into a variable and used it with the tax to calculate the new total.

  * We rounded the new price down to the nearest whole dollar using a `WorksheetFunction`. This method allows users to access many of the functions available in Excel. `RoundDown(newPrice, 0)` stipulates that we're rounding down the `newPrice` variable and that we're not including any digits past the decimal.

  ```vb
  'Use a worksheet function to round the new price down to the nearest whole dollar
  newPrice = Application.WorksheetFunction.RoundDown(newPrice, 0)
  ```

  * Finally, we changed the price and the total in the appropriate cells.

```vb
  ' Part III
  ' ----------------------------------------------------
  Dim newPrice As Double
  newPrice = budget / (1 + Range("H3").Value)

  ' Change the price
  Range("F3").Value = newPrice

  ' Change the new total
  Range("L3").Value = newPrice * (1 + Range("H3").Value)
```

* Ask if there are any questions before providing students with the solution and proceeding to the next section.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2V9kkll)</sub>

- - -

## 2. Chicken Nugget Loop

| Activity Time:       0:25 |  Elapsed Time:      0:55  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: For Loop   (0:10)</strong></summary>

* **File**:

  * [Activities/02-Ins_ForLoops/Solved/basic_for_loop_solved.vbs](Activities/02-Ins_ForLoops/Solved/basic_for_loop_solved.vbs)

  * [Activities/02-Ins_ForLoops/Solved/basic_for_loop_solved.xlsm](Activities/02-Ins_ForLoops/Solved/basic_for_loop_solved.xlsm)

* Next, you'll be introducing for-loops. Walk students through the code and run the VBA script. This code, quite simply inserts a series of numbers across rows and columns.

* In explaining the code be sure to note the parts of a VBA for loop:

  * `For i = 1 to 20` specifies the range to loop through.

  * Subsequent uses of `i` change with the loop

  * `Next i` iterates to the next value of `i`.

  * **Note**: While semantic variable declaration is more prevelant, `i` is deliberately chosen here because it has been commonly used in programming for decades; it is also the default mathematical notation. Iterators such as `i` and `j` are expected to be encountered both later in the course and in the field.

* Spend a few extra moments in your discussion to have students guess how the spreadsheet will look before running the code. In particular, challenge them to understand why `Cells(i, 1)` creates entries across rows and `Cells(1, i)` create entries across columns.

![Images/02-Ins_ForLoops-1.png](Images/02-Ins_ForLoops-1.png)

* Once you feel confident in their understanding, provide them with your code.

</details>

<details>
  <summary><strong>✏️ 2.2 Students Do: Chicken Nugget Loop  (0:10)</strong></summary>

* **Files:**

  * [Activities/03-Stu_ChickenNuggets-ForLoop/README.md](Activities/03-Stu_ChickenNuggets-ForLoop/README.md)

* Proceed with the next student exercise. In this example, students create a basic VBA script that prints "I will eat `i` Chicken Nuggets," where the value of `i` changes within the for loop.

* Show students what happens after the code runs, before sending them the instructions.

* **Instructions:**

  * Create a `For` loop that will produce the following example. (Note: The lines signify new cells.)

    | A1         | B1 | C1              |
    |----------|:-------------:|------:|
    | I will eat | 11 | Chicken Nuggets |
    | I will eat | 12 | Chicken Nuggets |
    | I will eat | 13 | Chicken Nuggets |
    | I will eat | 14 | Chicken Nuggets |
    | I will eat | 15 | Chicken Nuggets |
    | I will eat | 16 | Chicken Nuggets |
    | I will eat | 17 | Chicken Nuggets |
    | I will eat | 18 | Chicken Nuggets |
    | I will eat | 19 | Chicken Nuggets |
    | I will eat | 20 | Chicken Nuggets |

  * **Bonus**

    * If you finish early, talk to your neighbor about why you may want to use a For loop over the "range" function.

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Chicken Nuggets Loop (0:05)</strong></summary>

* **Files**:

  * [chicken_nuggets_solved.vbs](Activities/03-Stu_ChickenNuggets-ForLoop/Solved/chicken_nuggets_solved.vbs)

  * [chicken_nuggets_solved.xlsm](Activities/03-Stu_ChickenNuggets-ForLoop/Solved/chicken_nuggets_solved.xlsm)

* Once the timer is done, review the exercise with students.

* As you are doing so, be sure to point out the following:

  * We created a for loop that iterates from 1 through 10.

  * We set the value of `(i, 1)` and `(i, 3)` to be fixed value of "I will eat " and "Chicken Nuggets"

  * We set the value of `(i, 2)` to be `i +10`. This forces the loop to print 11 through 20.

  * Lastly, we use `Next i` to signal we are done with the loop and onto the next one.

  ![Images/03-Stu_ChickenNuggets-1.png](Images/03-Stu_ChickenNuggets-1.png)

* Ask if there are any questions before proceeding to the next example.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/345YTWn)</sub>

- - -

## 3. Fizz Buzz

| Activity Time:       0:40 |  Elapsed Time:      1:35  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: Loop Conditionals  (0:10)</strong></summary>

* **Files**:

  * [Activities/04-Ins_LoopConditionals/Solved/conditional_loops_solved.vbs](Activities/04-Ins_LoopConditionals/Solved/conditional_loops_solved.vbs)
  * [Activities/04-Ins_LoopConditionals/Solved/conditional_loops_solved.xlsm](Activities/04-Ins_LoopConditionals/Solved/conditional_loops_solved.xlsm)
  * [Activities/04-Ins_LoopConditionals/Solved/modulus_solved.vbs)](Activities/04-Ins_LoopConditionals/Solved/modulus_solved.vbs)
  * [Activities/04-Ins_LoopConditionals/Solved/modulus_solved.xlsm](Activities/04-Ins_LoopConditionals/Solved/modulus_solved.xlsm)

* Next, introduce one of the most important concepts of this week: Looped Conditionals. As a proficient developer, this will be a simple concept to you, but do not underestimate how critical it is for students to grasp.

* Open [Activities/04-Ins_LoopConditionals/Solved/modulus_solved.vbs](Activities/04-Ins_LoopConditionals/Solved/modulus_solved.vbs) and explain the modulus essentially performs long division on a number and returns the remainder (Note that in VBA modulus is denoted by `Mod`). Run the code in [Activities/04-Ins_LoopConditionals/Solved/modulus_solved.xlsm](Activities/04-Ins_LoopConditionals/Solved/modulus_solved.xlsm).

* Then open [Activities/04-Ins_LoopConditionals/Solved/conditional_loops_solved.vbs](Activities/04-Ins_LoopConditionals/Solved/conditional_loops_solved.vbs) and walk students through the code. Have them guess what it will do, before running the code.

* Then explain it line by line.

  * Start by pointing out the basic for loop structure.

  * Then introduce the concept of the modulus to determine remainder.

  * Point out that we are using if-else statements to route the flow of logic depending on whether `i` is even or odd.

  * Point out that we need to include the `End If` and also the `Next i` to close each respective block.

![Images/04-Ins_LoopConditionals-1.png](Images/04-Ins_LoopConditionals-1.png)

* Check if there are any questions before sending out the solution.

</details>

<details>
  <summary><strong>✏️ 3.2 Students Do: Fizz Buzz  (0:20)</strong></summary>

* **Files**:

  * [Activities/05-Stu_FizzBuzz/README.md](Activities/05-Stu_FizzBuzz/README.md)
  * [fizzbuzz_unsolved.xlsm](Activities/05-Stu_FizzBuzz/Unsolved/fizzbuzz_unsolved.xlsm)

* Fizzbuzz is a very popular logic problem in coding. Inform students that this next exercise is a classic problem in technical interviews -- across all programming languages. Run the code once for them so they can see how it works.

![Images/05-Stu_FizzBuzz-1.png](Images/05-Stu_FizzBuzz-1.png)

* Explain at a high-level, the rules of the exercise:

  * If a number is divisible by just 3, then the code should print Fizz.

  * If a number is divisible by just 5, then the code should print Buzz.

  * If a number is divisible by both 3 and 5, then the code should print FizzBuzz.

* Then send students the instructions to the exercise:

* **Instructions:**

  * Create a VBA Script that populates the second column with the word "Fizz", "Buzz", or "Fizzbuzz" based on the value in the first column.

  * If the value in column 1 is a multiple of both 3 and 5, print "Fizzbuzz" in column 2.

  * If the value in column 1 is a multiple of just 3, print "Fizz" in column 2.

  * If the value in column 1 is a multiple of just 5, print "Buzz" in column 2.

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Fizz Buzz (0:10)</strong></summary>

* **Files:**

  * [fizzbuzz_solved.vbs](Activities/05-Stu_FizzBuzz/Solved/FizzBuzz_solved.vbs)

  * [fizzbuzz_solved.xlsm](Activities/05-Stu_FizzBuzz/Solved/fizzbuzz_solved.xlsm)

* Then walk students through the solution. As you do so, be sure to explain:

  * That we started the exercise by creating a basic for loop.

  * We then created a variable to track the value of the number in column 1.

  * We then created a series of if-then statements. We started these by checking for numbers that are both divisible by 3 and 5. It is important to start here, because if-then statements move from least specific to most specific. (i.e. If a number is divisible by 3 and 5, it is also divisible by 3. We have to make sure our code handles the more specific scenario first). Let them know that this isn't an obvious solution, but rather something that emerges as you approach your code.

  * Each of our if-then statements triggers a change to `Cells(i, 2)` (column 2).

```vb
  ' Loop through the values in Column 1
  For i = 2 To 100

      'Set cell value to variable
      num = Cells(i, 1).Value


      ' Check if the number is divisible by 3 and 5....
      If (num Mod 3 = 0 And num Mod 5 = 0) Then

          ' If so, print Fizzbuzz
          Cells(i, 2).Value = "Fizzbuzz"

      ' Check if the number is divisible by just 3...
      ElseIf (num Mod 3 = 0) Then

          ' If so, print "Fizz"
          Cells(i, 2).Value = "Fizz"

      ' Check if the number is divisible by just 5...
      ElseIf (num Mod 5 = 0) Then

          ' If so, print "Buzz"
          Cells(i, 2).Value = "Buzz"

      End If

  Next i
```

* See if there are any questions before proceeding to break.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2xDKN29)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:50  |
|---------------------------|---------------------------|

- - -

## 4. Lotto Search

| Activity Time:       0:25 |  Elapsed Time:      2:15  |
|---------------------------|---------------------------|

<details>
  <summary><strong>👥 4.1 Partners Do: Lotto Search (0:20)</strong></summary>

* **Files**:

  * [Activities/06-Stu_Lotto-AdvancedForLoops/README.md](Activities/06-Stu_Lotto-AdvancedForLoops/README.md)
  * [lotto_numbers_unsolved.xlsm](Activities/06-Stu_Lotto-AdvancedForLoops/Unsolved/lotto_numbers_unsolved.xlsm)

* As students return, introduce the next exercise. Warn them that it's a challenging one, but they will likely have fun with it. In this exercise, students are given a series of lotto tickets. Their task is to create a VBA script that finds these lotto winners in the list of all ticket purchases. For the bonus, they must additionally find the first instance in which any runner up appears in the list.

* Show them what the code does by running it in VBA. Point out that the winners in the Winner Table matches what you'd find if you did a `Ctrl+F` to search for the same numbers.

![Images/06-Stu_Lotto-1.png](Images/06-Stu_Lotto-1.png)

* Then deliver the instructions:

  * **Instructions:**

    * You are in charge of finding our winners for a local lotto drawing.

    * The results are, in order:

      * First: 3957481
      * Second: 5865187
      * Third: 2817729

    * Create a script that will return those lucky winners and print them on the sheet.

      * For each winner include the following pieces of information:

        * First name
        * Last name
        * The winning number

      * They should be placed in winning order of First, Second, Third.

      * There should also be a message box that congratulates the first place winner.

  * **Bonus:**

    * There may just be one other winner! The below numbers are Wild Lotto Balls. Whichever comes up first in the list will be the fourth place (runner-up) winner. (Note: You must find the _first_ runner up to appear in the list.)

      * 2275339
      * 5868182
      * 1841402

  **Hints:**

  * Remember to utilize variables to keep your code clean.

  * For the bonus, you may need to use `Exit For`

</details>

<details>
  <summary><strong>⭐ 4.2 Review: Lotto Search (0:05)</strong></summary>

* **Files**:

  * [lotto_numbers_solved.xlsm](Activities/06-Stu_Lotto-AdvancedForLoops/Solved/lotto_numbers_solved.xlsm)
  * [lotto_numbers_solved.vbs](Activities/06-Stu_Lotto-AdvancedForLoops/Solved/lotto_numbers_solved.vbs)

* Once the time is complete, walk students through the solution:

  * We began by creating a series of variables to hold our ticket numbers and winner information. (Note: Because the length of the tickets is so long, we needed to use `double` or `long`. Explain to students that these are alternative formats that allow for longer numbers. These different variable types emerge for space saving considerations).

![Images/06-Stu_Lotto-2.png](Images/06-Stu_Lotto-2.png)

* Proceed to point out that we then created a for loop to scan through each of the rows. All the while, our code is searching for instances when the value in Column 3 (`Cells(i, 3)`) matches the value of our first, second, or third place winners. If there is a match we copy the winner's first name, last name, and ticket information and place them into the winners table (`Cells(2,6)` - `Cells(4,8)`).

![Images/06-Stu_Lotto-3.png](Images/06-Stu_Lotto-3.png)

* Lastly, regarding the bonus, we needed to create a second _separate_ for loop. This was necessary, because our current for loop will replace our Runner Up winner with the last instance and not the first. To avoid this, we needed to create a for-loop with an `Exit for`. This code would exit the loop the moment the first runner up is found, allowing us to avoid replacing our runner-up.

![Images/06-Stu_Lotto-4.png](Images/06-Stu_Lotto-4.png)

* Send students the final version of the code. Stress that this exercise introduced some tricky concepts, but encourage them to repeat this exercise at home.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2QZNKRx)</sub>

- - -

## 5. Hornet's Nest

| Activity Time:       0:45 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 5.1 Instructor Do: Nested For Loops (0:10)</strong></summary>

* **Files**:

  * [Activities/07-Ins_NestedForLoops/Solved/nested_for_loop_solved.vbs](Activities/07-Ins_NestedForLoops/Solved/nested_for_loop_solved.vbs)

  * [Activities/07-Ins_NestedForLoops/Solved/nested_for_loop_solved.xlsm](Activities/07-Ins_NestedForLoops/Solved/nested_for_loop_solved.xlsm)

* Proceed now to the final instructor demo: Nested for-loops. Like looped conditionals, this is an extremely important concept and one that leaves students easily confused. Encourage them to focus on this section.

* Walk students through the spreadsheet and code. Point out that in this example, we are looking to loop through both the rows and columns. Try to highlight cells as you try to simulate the actions of each loop. Begin at the top left, move across the columns, before proceeding to the next row.

* Encourage students to re-do this process themselves to one another before moving on to the next exercise.

* ![Images/07-Ins_NestedForLoops-1.png](Images/07-Ins_NestedForLoops-1.png)

</details>

<details>
  <summary><strong>✏️ 5.2 Students Do: Hornets Nest (0:25)</strong></summary>

* **Files**:

  * [Activities/08-Stu_HornetsNest-NestedForLoops/README.md](Activities/08-Stu_HornetsNest-NestedForLoops/README.md)
  * [hornets_nest_unsolved.xlsm](Activities/08-Stu_HornetsNest-NestedForLoops/Unsolved/hornets_nest_unsolved.xlsm)

* Finally, introduce the last exercise of the day: Hornets Nest. This is a fun exercise, but another challenging one. In essence the problem of this exercise is as follows:

  * You have been given a spreadsheet that's been infested by Hornets.

  * In Part I, you are responsible for counting the number of Hornets in the spreadsheet.

  * In Part II, you are responsible for replacing all instances of the word "Hornets" with the word "Bugs".

  * In Part III, you are given a set number of "Bugs" and "Bees". Each time you replace a Hornet with a Bug or Bee, you are deducting from your supply. You must replace as many hornets as you can and indicate whether all the Hornets have been replaced.

* Run the code [hornets_nest_solved.xlsm](Activities/08-Stu_HornetsNest-NestedForLoops/Solved/hornets_nest_solved.xlsm) to show students what the code does. (Note: Do not save over your file as the macro will overwrite the contents.)

![Images/08-Stu_HornetsNest-1.png](Images/08-Stu_HornetsNest-1.png)

* Then send the instructions and initial file:

  * **Instructions:**

    * Create a VBA script to handle the growing Hornet infestation in your spreadsheet.

    * There are three parts to this problem:

      * Part I: Count the number of Hornets found and display the number to your user in the form of a message box.

      * Part II: Modify the script such that it changes the word Hornets to "Bugs".

      * Part III: Modify the script a third time, this time keeping in mind that you have a limited number of Bugs and Bees. Use the full set of Bugs and Bees you have available to replace the Hornets with all available Bugs first then Bees. If you run out of Bugs or Bees provide the user with the message: "Oh no! We still have hornets..."

  * **Hints**

    * You may want to create a backup of your spreadsheet as your macro will write over the contents.

</details>

<details>
  <summary><strong>⭐ 5.3 Review: Hornets Nest (0:10)</strong></summary>

* **Files**:

  * [hornets_nest_solved.xlsm](Activities/08-Stu_HornetsNest-NestedForLoops/Solved/hornets_nest_solved.xlsm)
  * [hornets_pt_i_solved.vbs](Activities/08-Stu_HornetsNest-NestedForLoops/Solved/hornets_pt_i_solved.vbs)
  * [hornets_pt_ii_solved.vbs](Activities/08-Stu_HornetsNest-NestedForLoops/Solved/hornets_pt_ii_solved.vbs)
  * [hornets_pt_iii_solved.vbs](Activities/08-Stu_HornetsNest-NestedForLoops/Solved/hornets_pt_iii_solved.vbs)

* Once the timer completes, review the solution with the group.

* In discussing Part 1, point out that we utilized a simple nested for loop to search for the term "Hornets" in each of the cells. In Part 2, we subsequently change the value of these cells to be "Bugs".
  ![Images/08-Stu_HornetsNest-2.png](Images/08-Stu_HornetsNest-2.png)

* In Part 3, we had the added challenge of continually tracking our Bug and Bee count. The easiest way to approach this problem was to draw from our Bug stash first and then once depleted to draw from our Bee stash. In essence, this code works by storing our initial bug and bee count, then continually subtracting one from these variables each time we utilized either. Once the Bug or Bee count is equal to 0, we can no longer draw from that stash.
  ![Images/08-Stu_HornetsNest-3.png](Images/08-Stu_HornetsNest-3.png)

* For the last requirement of Part 3, we deftly avoided the for loop completely. Instead, we concluded if hornets were unaccounted for by comparing the sum of bugs and bees to the initial number of hornets. If there were more hornets than bugs and bees to start, then we know there are still hornets after our replacement efforts. Take a moment to explain to students that creative thinking like this is often the real skill in programming.
  ![Images/08-Stu_HornetsNest-4.png](Images/08-Stu_HornetsNest-4.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/39xCIJv)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
