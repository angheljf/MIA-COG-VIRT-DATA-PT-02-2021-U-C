# 20.2 Deeper Into Tableau

## Overview

Today's lesson introduces students to the more advanced aspects of Tableau, including custom calculations, maps, and Level-Of-Detail calculations.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* All the necessary files are in the directories. However, you, as well as your students, may have to connect to the data files, such as Excel and CSV files, from inside Tableau. If an activity does not work, check first to make sure that the data source is connected.
* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-20-tableau) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

### Sample Class Video (Highly Recommended)

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b9df43ce-059c-4c91-aefb-a888018508fb)

</details>

- - -

## Class Objectives

* Students will create groups and sets.

* Students will create maps and use built-in U.S. Census data.

* Students will be able to create custom calculations.

* Students will understand what LOD calculations entail.

- - -

# Class Activities

## 1. Warmup

| Activity Time:       0:20 |  Elapsed Time:      0:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 1.1 Students Do: Warmup (0:15) </strong></summary>


* **Files**: [IPEDS_data.csv](Activities/01-Stu-Warmup/Resources/IPEDS_data.csv)

* In this warm-up activity, students will create visualizations with data on colleges and universities.
  
</details>

<details>
  <summary><strong>⭐ 1.2 Review: Warmup (0:05) </strong></summary>

* **Files**: [Activities/Solved/01-Stu-Warmup](Activities/01-Stu-Warmup/Solved/Higher_Education.twbx)

* Take a few minutes to go over some visualizations possible with the data set. Some of the possible observations might include the following:

  * For example, schools with higher ACT scores appear to award more doctorate degrees.

  ![Images/warmup1.png](Images/warmup1.png)

  * More students in the Southeast and the Southwest regions appear to receive federal grants than other regions. New England students appear to receive the least.

  ![Images/warmup2.png](Images/warmup2.png)

  * Schools that offer only bachelor's degrees appear to graduate a higher percentage of their students within four years than schools that offer advanced degrees.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2xeT6l1)</sub>


## 2. Groups and Sets

| Activity Time:       0:30 |  Elapsed Time:      0:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Groups and Sets (0:10)</strong></summary>

* **Files**: [Activities/02-Ins-Groups_Sets/Solved](Activities/02-Ins-Groups_Sets/Solved/ins_groups_sets.twbx)

* We can group multiple members in a field into a group. For example, if companies A and B have recently merged, we can group them together under a single entity to aggregate their figures. In a dataset showing average salaries by major, we might group English, music, and French majors under Humanities; economics, psychology, and sociology might go under Social Sciences; physics, math, and engineering might go under Sciences.

* In `ins_groups_sets`, go to the `Group` tab. Each state's zip code, as well as the latter's total profits, are shown. In a scenario in which some of the zip codes merge, perhaps through gerrymandering, it would make sense to group them together.

  * Select multiple zip codes, and right click, and choose `Group`

  ![Images/groups1.png](Images/groups1.png)

  * Now they are grouped together, and their profits are also aggregated.

  ![Images/groups2.png](Images/groups2.png)

  * To change the name of the group, right click on it and choose `Edit Alias`.

  ![groups3.png](Images/groups3.png)

* In a similar fashion, members of a field can be grouped into **sets** in Tableau. Sets are more flexible than groups: a set's members can be drawn from multiple dimensions or even conditions.

* We can create a set of members from the same field

  * Go to `Sets0` sheet, click on the subcategory members that involve electronics, right click and select `Create Set...`

  ![Images/sets1.png](Images/sets1.png)

  * Name it `Electronics` or something similar and drag it to the `Rows` shelf

  ![Images/sets2.png](Images/sets2.png)

* As seen here, a set bifurcates a field into two groups:

  * The `In` group's members meet the set's criteria
  * The `Out` group's members do not meet the set's criteria
  * With these, we can perform further operations and visualizations

* We can also create a set to select members that meet a defined criterion. In the following example, we'll create sets to select for product sub-categories that meet two criteria: high sales and low shipping costs

  * Right click on `Sub-Category` and select `Create`, then `Set`

  ![Images/sets3.png](Images/sets3.png)

  * Select `Condition` and define the criteria. In this example, we're filtering for total profits greater than $50,000.

  ![Images/sets4.png](Images/sets4.png)

  * Do the same for low shipping.

  ![Images/sets5.png](Images/sets5.png)

  * Dragging either of these to the `Rows` shelf will display in and out sets.

  ![Images/sets6.png](Images/sets6.png)

* We can combine the criteria created by the two sets by combining them. Right click on either pill of a set. In this case, right click on the `High Profit` set, and select `Create Combined Set`.

  ![Images/sets7.png](Images/sets7.png)

  * Define the two sets, and select inner join.
    ![Images/sets8.png](Images/sets8.png)

  * Dragging the combined sets to the `Rows` shelf now applies both criteria to the sub-category items.

  ![Images/sets9.png](Images/sets9.png)

* As seen in sheet `Sets2`, we can now use the combined sets filter to visually identify product subcategories that meet the criteria:

  ![Images/sets10.png](Images/sets10.png)

* And the sheet `Sets3` visualizes whether products subcategories that have low shipping costs and high profits are more heavily discounted than products that don't meet the criteria:

  ![Images/sets11.png](Images/sets11.png)

</details>

<details>
  <summary><strong>✏️ 2.2 Students Do: Ready, Set, Woof (0:15) </strong></summary>

* **Instructions**: [Activities/03-Stu-Groups_Sets/README.md](Activities/03-Stu-Groups_Sets/README.md)
* **Files**:

  * [Activities/03-Stu-Groups_Sets/Resources/akc_breed_info.csv](Activities/03-Stu-Groups_Sets/Resources/akc_breed_info.csv)
  * [Activities/03-Stu-Groups_Sets/Resources/dog_intelligence.csv](Activities/03-Stu-Groups_Sets/Resources/dog_intelligence.csv)

* In this activity, students will use groups and sets to explore whether the size of a dog has any bearing on its intelligence.

</details>


<details>
  <summary><strong>⭐ 2.3 Review: Ready, Set, Woof (0:05)</strong></summary>

* **Files**: [Activities/03-Stu-Groups_Sets/Solved](Activities/03-Stu-Groups_Sets/Solved/sets_groups.twbx)

* Here's how one might group the dogs:

  ![Images/groups4.png](Images/groups4.png)

  * First, sort the dogs by weight.
  * Hold down the `Shift` key to select multiple members
  * Right click and select `Group`, then name the group

* After grouping medium and large dogs as well, create a bar chart for obedience:

  ![Images/groups5.png](Images/groups5.png)

* Go over creating sets as well.

  * Sets, again, allow flexible grouping. In this case, dogs are categorized into sets by weight.

  * To create a set, one might right-click on the `Breed` pill under the `akc_breed_info.csv` data set:

  ![Images/stu_sets01.png](Images/stu_sets01.png)

  * To specify the criterion for the set, click on the `Condition` tab, then the `By field` radio button. Then specify the weight: in this case, dogs that weight over 60 pounds.

  ![Images/stu_sets02.png](Images/stu_sets02.png)

* Explain that sets can be used to examine large dogs in the aggregate:

  ![Images/stu_sets03.png](Images/stu_sets03.png)

  * Here, the obedience rate of large breeds is examined versus that of other dogs.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3aSog0c)</sub>

  ## 3. Calculations

| Activity Time:       0:25 |  Elapsed Time:      1:15  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: Calculations (0:10)</strong></summary>


* **Files**: [Activities/04-Ins-Calculations/Solved](Activities/04-Ins-Calculations/Solved/ins_calculations.twbx)

* In addition to built-in operations, we can create custom conditional statements and calculations in Tableau.

* Tableau can handle `If` statements. Open the following chart in worksheet `If1`:

  ![Images/calculations1.png](Images/calculations1.png)

  * Highly profitable subcategories are colored in orange; less profitable and unprofitable ones are colored in blue.
  * This was accomplished with an `If` statement.

* To create a custom `If` statement, go to `Analysis` -> `Create Calculated Field`, then enter the desired statement:

  ![Images/calculations2.png](Images/calculations2.png)

* When the newly created pill is dragged to the `Color` mark, the subcategories are automatically colored according to the criteria defined in our if-statement.

* Tableau is also able to deal with unknown quantities. This example is in the `IIF1` sheet. Create a new calculated field, and enter the following:

  ![Images/calculations3.png](Images/calculations3.png)

  * Instead of `IF`, the statement here is `IIF`.
  * This means if the total profit is greater than 50,000, a subcategory is labeled "Profit."
  * Otherwise, it is labeled "Loss."
  * If the quantity cannot be evaluated, however, it is labeled "Unknown."
  * The latter can happen when null values are present, etc.

* Counting the number of items in a column can be valuable, and like Excel, Tableau offers this function. Open up the `Count` worksheet:

  ![Images/calculations4.png](Images/calculations4.png)

  * To re-create this table, drag the `Category` pill to the `Rows` shelf.
  * Then drag `Sales` and `Profit` pills into the table.
    ![Images/calculations5.png](Images/calculations5.png)
  * Then drag the `GlobalSuperstoreOrders2016.xlsx (Count)` pill into either the table, or for the table seen here, into the `Text` box in the `Marks` pane.

* Tableau can also calculate the **distinct** number of dimensions, using the `COUNTD` function, short for "count distinct." Open the `Countd` worksheet. To count the number of orders across categories would be relatively simple. But what if we want to see the number of unique orders in each category?

  ![Images/calculations6.png](Images/calculations6.png)

  * Both count and counted charts here use a custom calculation. `COUNTD`, as seen below, counts the number of unique order ID's.
    ![Images/calculations7.png](Images/calculations7.png)
  * The total number of orders is calculated with `COUNT([Order ID])`.
  * The `Category` dimension pill is dragged to `Columns`, and the `count orders` and `countd orders` are dragged to `Rows`.
  * These charts indicate that there are more duplicate orders in Office Supplies than in any other category. That is, multiple items of office supplies are more likely to be ordered together than the other categories.

* Next, open the `Calc diff` worksheet. This chart shows day-to-day sales in January, 2015.

  ![Images/calculations8.png](Images/calculations8.png)

  * The top chart is a stacked bar chart of daily sales in the three product categories.

  * The bottom chart shows the difference between one day's sales from the previous day's.

  ![Images/calculations9.png](Images/calculations9.png)

  * The chart on the bottom can be created by dragging the `Sales` pill to `Rows`, then clicking on the pill to select `Quick Table Calculation`, then `Difference`.

  * By default, each day's sales is compared against that of the previous day, but can be changed by clicking on the `Sales` pill again, then selecting `Relative to`, then the desired option.

  ![Images/calculations10.png](Images/calculations10.png)

</details>

<details>
  <summary><strong>✏️ 3.2 Students Do: Calculations (0:10)</summary></strong>

* **Instructions**: [Activities/05-Stu-Calculations/README.md](Activities/05-Stu-Calculations/README.md)

* **Files**:

  * [Activities/05-Stu-Calculations/Resources/vehicle_collisions_nyc.csv](Activities/05-Stu-Calculations/Resources/vehicle_collisions_nyc.csv)

* In this activity, students will create visualizations using a data set on motor vehicle accidents in New York City.

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Calculations (0:05)</strong></summary>

* **Files**: [Activities/05-Stu-Calculations/Solved/motor_vehicle_accidents.twbx](Activities/05-Stu-Calculations/Solved/motor_vehicle_accidents.twbx)

* Go over some of the possible solutions. For example, to identify the most dangerous hours for a cyclist, we might consider hours in which the number of cyclists injured **or** killed is above a certain threshold.

  ![Images/calcreview1.png](Images/calcreview1.png)

* If time allows, discuss the validity of these visualizations. For example, the visualizations suggest that 5 pm to 7 pm are the most dangerous hours for a cyclist. What are some possible explanations for this phenomenon? Can we truly conclude that the visualizations are correct?

  * One explanation is that more commuters, including cyclists, are on the road during rush hour. A greater number of cyclists could naturally lead to more accidents, but we cannot necessarily conclude that, relative to other hours, rush hour is more dangerous.

  * In both creating and assessing data visualizations, it is important to consider such confounding factors.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2yL2SMl)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:30  |
|---------------------------|---------------------------|
- - -

## 4. Maps 

| Activity Time:       0:40 |  Elapsed Time:      2:10  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: Maps (0:10)</strong></summary>

* **Files**: [Activities/06-Ins-Maps/Solved/ins_map.twbx](Activities/06-Ins-Maps/Solved/ins_map.twbx)

* Creating a map in Tableau is easy. Open the workbook and display the map of total profits by state:

  ![Images/maps1.png](Images/maps1.png)

  * It is color coded by profit, with profitable states colored in blue, and states that incurred loss colored in orange.

  * Latitude and Longitude of locations in our data, as shown in both the Columns and Rows shelves, and under Measures, are automatically generated by Tableau.

  ![Images/maps2.png](Images/maps2.png)

  * The map gives an immediate bird's-eye view of profitable and unprofitable states.

  * The `Latitude (generated)` pill goes to the `Rows` shelf because latitude lines run horizontally.

  * The `Longitude (generated)` pill goes to the `Columns` shelf because longitude lines run vertically.

* To generate this map, simply drag the `Profit` pill to `Color` in the `Marks` pane:

  ![Images/maps3.png](Images/maps3.png)

  * The colors can be tweaked by clicking on the dropdown menu in the legend and choosing `Edit Colors`:

  ![Images/maps4.png](Images/maps4.png)

* In order to simply categorize profitable states against unprofitable states, we can create a custom logical function (`Analysis` -> `Create Calculated Field`):

  ![Images/maps5.png](Images/maps5.png)

  ![Images/maps6.png](Images/maps6.png)

  * The pill for the custom field is dragged to the `Color` marks to view this map.

* Also show the class that Tableau has built-in layers to add data from the U.S. census!

  * Click on `Map` in the menu, then `Map Layers`.

  ![Images/maps7.png](Images/maps7.png)

  * We are presented with options for borders

  ![Images/maps8.png](Images/maps8.png)

</details>

<details>
  <summary><strong>✏️ 4.2 Students Do: Maps 1 (0:10)</strong></summary>

* **Instructions**: [Activities/07-Stu-Maps1/README.md](Activities/07-Stu-Maps1/README.md)

* **Files**:

  * [Activities/07-Stu-Maps1/Resources/earthquakes_database.csv](Activities/07-Stu-Maps1/Resources/earthquakes_database.csv)

* In this activity, students will chart the intensity of earthquakes over time, as well as create a map comparing the magnitude of earthquakes versus median household income.

</details>

<details>
  <summary><strong>✏️ 4.3 Students Do: Maps 2 (0:10)</strong></summary>

* **Instructions**: [Activities/08-Stu-Maps2/README.md](Activities/08-Stu-Maps2/README.md)

* **Files**:

  * [Activities/08-Stu-Maps2/Resources/employment.csv](Activities/08-Stu-Maps2/Resources/employment.csv)

* In this activity, students will map unemployment in the United States, by county, between 2008 and 2016.

</details>

<details>
  <summary><strong>⭐ 4.4 Review: Maps (0:10)</strong></summary>

* **Files**: [Activities/07-Stu-Maps1/earthquakes.twbx](Activities/07-Stu-Maps1/Solved/earthquakes.twbx)

* **Files**: [Activities/08-Stu-Maps2/Solved/unemployment.twbx](Activities/08-Stu-Maps2/Solved/unemployment.twbx)

* Here are some points to highlight from the previous activities.

* The `Longitude` and `Latitude` pills should be categorized as `Dimension`

  ![Images/maps11.png](Images/maps11.png)

* Global earthquakes can be visualized thus, with more powerful earthquakes being sized larger and colored red.

  ![Images/maps12.png](Images/maps12.png)

* There are several options to color the earthquakes

  ![Images/maps13.png](Images/maps13.png)

  * Colors can be binned into `Steps`
  * `Orange-Blue Diverging` originally had orange to the left and blue to the right, but has been reversed.
  * The upper end of earthquake magnitude is defined as 9.1.
  * The center of the color range is defined as a magnitude of 7.

* Because the Richter scale is logarithmic, it makes sense to use exponential values to size earthquakes on the map.
  ![Images/maps14.png](Images/maps14.png)

  * The CSV file is opened in Excel, and a new column called `Magnitude ^ 10` is created.
  * For example, the formula in cell `J2` is defined as `=I2^10`, and applied to the entire column.
  * This pill is applied to the size mark in Tableau.

* In the instructor solution of a map of earthquakes versus 2017 median household income by county, the earthquakes are filtered for years 2010 through 2016.

  ![Images/maps15.png](Images/maps15.png)

* There does not appear to be a clear trend in the magnitude of earthquakes in the given period. However, sometimes a trend can become clearer by adjusting the range of the axis.

  ![Images/maps16.png](Images/maps16.png)

  * It is possible to adjust the range of the y-axis by right clicking on it, then choosing `Edit Axis...`

* In the unemployment maps, years are used to filter the data, for both 2008-16 and 1990-1998:

  ![Images/maps17.png](Images/maps17.png)
  ![Images/maps18.png](Images/maps18.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2URkRsU)</sub>

## 5. Dashboard

| Activity Time:       0:20 |  Elapsed Time:      2:30  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 5.1 Instructor Do: Dashboard (0:05)</strong></summary>

* **Files**: [Activities/09-Ins-Dashboard/Solved/dashboard.twbx](Activities/09-Ins-Dashboard/Solved/dashboard.twbx)

* Explain that dashboards allow a bird's-eye view of several visualizations. In Tableau, we can also have elements that interact with each other.

* Open up the workbook and show each worksheet, then the worksheet named `Profit Dashboard`

  ![Images/dashboard1.png](Images/dashboard1.png)

  * We can have multiple visualizations in a single page.

* To create a new dashboard, click the `New Dashboard` button at the bottom of the screen.

  ![Images/dashboard2.png](Images/dashboard2.png)

  * Then drag each sheet to be visualized into the parent area, called the `container`.

* To create interactive `actions`, in which an action on one chart can affect the visualization in another, take the following steps:

  * Go to `Dashboard`, then `Actions`

  ![Images/dashboard3.png](Images/dashboard3.png)

  * Click `Add Action`, and in this case, `Filter`

  ![Images/dashboard4.png](Images/dashboard4.png)

  * Click on `Select` under `Run action on:`. Then specify the source and target sheets for the action.

  ![Images/dashboard5.png](Images/dashboard5.png)

* In order to move each chart, click on the dropdown arrow, then `Floating`

  ![Images/dashboard6.png](Images/dashboard6.png)

* And now the charts are interactive. For example, clicking on Texas in the map changes the `Profits by Category` bar chart to reflect only the values for Texas across the years in the three product categories.

  ![Images/dashboard7.png](Images/dashboard7.png)

</details>

<details>
  <summary><strong>✏️ 5.2 Students Do: Dashboard (0:10)</strong></summary>

* **Instructions**: [Activities/10-Stu-Dashboard/README.md](Activities/10-Stu-Dashboard/README.md)

* **Files**:

  * [Activities/10-Stu-Dashboard/Resources/bar_locations.csv](Activities/10-Stu-Dashboard/Resources/bar_locations.csv)
  * [Activities/10-Stu-Dashboard/Resources/party_in_nyc.csv](Activities/10-Stu-Dashboard/Resources/party_in_nyc.csv)

* In this activity, students will identify the most fun neighborhoods in New York City by mapping bars and the number of noise complaints registered against those bars.

</details>

<details>
  <summary><strong>⭐ Review: Dashboard (0:05)</strong></summary>

* **Files**: [Activities/10-Stu-Dashboard/Solved/party_map.twbx](Activities/10-Stu-Dashboard/Solved/party_map.twbx)

* Review the last activity. In the first tab, the number of noise complaint calls made against each bar is plotted, with larger circles indicating more complaints.

  ![Images/dashboard8.png](Images/dashboard8.png)

  * The Census data is also used to color areas by Male/Female ratio.
  * To accomplish this, go to `Map` -> `Map Layers` -> `Data Layer`

* The rest of the visualizations are standard aggregate charts and tables. The most salient ones can be assembled inside a dashboard.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3c3i99D)</sub>

## 6. LOD

| Activity Time:       0:30 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 6.1 Instructor Do: Level of Detail Calculations (0:10)</strong></summary>

* **Files**: [Activities/11-Ins-LOD/Solved/lod.twbx](Activities/11-Ins-LOD/Solved/lod.twbx)

* With Level of Detail calculations, we can retrieve data that is not immediately available in the current level of visualization. This is a confusing statement that requires some explanation.

* Imagine a child wearing a name tag:

  ![Images/LOD1.jpg](Images/LOD1.jpg)

  * This child's name is Annie
  * The name shown (visualized) on the tag is also Annie

* Instead of the child's name, what if we were to display the child's (paternal) grandfather's name instead?

  * The name tag might say, "My grandfather's name is Peter."
  * In this case, the level of visualization (the child) is different from the level of data (the grandfather).

* LOD works similarly in that we can incorporate data that is not immediately available in the current level of visualization.

* In this first worksheet, a map is shown with a state-by-state percentage of contribution toward the total national profit:

  ![Images/LOD2.png](Images/LOD2.png)

  * Here, the level of visualization is by **state**
  * If the level of visualization were national, only a single profit number would be shown in the entirety of the U.S.
  * In addition to the state-level profit, the total **national** profit, which is a figure from a different LOD than the current visualization, is required.
  * The number shown on each state is `state profit/total national profit`

* In order to create this LOD calculation, begin with a basic state-by-state map:

  ![Images/LOD3.png](Images/LOD3.png)

  * Drag `Latitude` and `Longitude` pills to Columns and Rows shelves
  * Then filter by country for only United States.
  * Then drag the `State` pill from Dimensions into the `Marks` pane.

* In the `Marks` pane, select `Map` instead of `Automatic` to get a filled map.

* Next, create a sum of profits at the national level. Once again, because the current level of visualization is at the state level, we use an LOD calculation to **exclude** state from the state summation. In other words, we are not summing the results at the state level, but at a more aggregated level.

* Go to `Analysis` -> `Create Calculated Field...`

  ![LOD5.png](Images/LOD5.png)

  ![Images/LOD6.png](Images/LOD6.png)

  * This calculation is named `National Profit`
  * The calculation is enclosed in `{}`
  * Exclude `[State]` from the level of detail. In other words, the current level of visualization includes states, but leave that out when performing the calculation.
  * If the keyword were `INCLUDE` instead, it would mean add that measure in addition to the current level of detail.
  * Sum the profits at the excluded level.
  * The exclusion criterion and the sum operation are separated by a comma.

* An important concept in using LOD calculations is that of **aggregation versus granulation**.

  * Aggregation means a higher, more abstract level. In this case, national level is more aggregated than the state level.
  * Granulation means a lower, more specific level. In this case, state level is more granular than the national level.
  * At the state-level of visualization, if we exclude the state level from a profit calculation, we are referring to the national level of calculation, which is more aggregated.

* The above creates a calculation of the sum of profits at the national level. Now we need to calculate the contribution of each state to the national profit.

  * Create another calculated field called `Contribution to Nat'l Profit, State`
    ![Images/LOD7.png](Images/LOD7.png)
  * Divide `Sum([Profit])` by the `National Profit`, which was calculated previously, and multiply by 100
  * National Profit is enclosed in `ATTR()`. We will return to what `ATTR` means in a moment.

* To create our final visualization, drag the appropriate pills to the `Marks` pane.

  ![Images/LOD8.png](Images/LOD8.png)

  * Upon dragging `Contribution to Nat'l Profit, State` to the `Color` mark, it automatically is re-labeled as an `AGG`.
  * Upon dragging `National Profit` to the `Tooltip` mark, it is automatically re-labeled as `ATTR`.

* The concept of **attribute** is also important in LOD calculations.

  * ATTR works at the row-level: if all rows have the same value, ATTR returns a value; if all rows do not have the same value, it returns an asterisk.
  * At the state-level, is the **national** profit identical for all states? Yes, and it can be characterized as an attribute.
  * At the state-level, can each state's profit be an attribute? No, because not all rows (states) have the same value.
  * This again brings us to the concept of aggregation versus granulation.

</details>

<details>
  <summary><strong>✏️ 6.2 Students Do: Level of Detail (0:15)</strong></summary>

* **Instructions**: [Activities/12-Stu-LOD/README.md](Activities/12-Stu-LOD/README.md)

* **Files**: [Activities/12-Stu-LOD/Resources/global_superstore.xls](Activities/12-Stu-LOD/Resources/global_superstore.xls)

* In this activity, students will gain practice with creating LOD calculations.

</details>

<details>
  <summary><strong>⭐ 6.3 Review: LOD (0:05)</strong></summary>

* **Files**: [Activities/12-Stu-LOD/lod2.twbx](Activities/12-Stu-LOD/Solved/lod2.twbx)

* Part I requires only a simple calculation to display the contribution of each state toward the national profit:

  ```python
  SUM([Profit]) / ATTR([National Profit]) * 100
  ```

* In Part II, students were required to visualize each city's contribution to the total state profit:

  ![Images/ReviewLOD1.png](Images/ReviewLOD1.png)

* In the `Marks` pane, both `State` and `City` pills are present, but the goal is to keep the visualization at the city level, but bring state-level information into it. So we exclude `City` in our LOD calculation:

  ![Images/ReviewLOD2.png](Images/ReviewLOD2.png)

* In a new calculation, the sum of each city's profit is divided by the total state profit, defined above.

  ![Images/ReviewLOD3.png](Images/ReviewLOD3.png)

  * `[State Profit, LOD Exclude]`, the name of the calculated field, is preceded by `ATTR()` because it is an aggregated figure that is same for all the cities in a given state.

* However, there is a problem that we need to address. Texas has lost money, but cities in Texas that have lost in money are colored as profitable, and vice versa.

  ![Images/ReviewLOD4.png](Images/ReviewLOD4.png)

  ![Images/ReviewLOD5.png](Images/ReviewLOD5.png)

  * Lubbock, TX, a profitable city, is wrongly colored red.

  * This is because a city's profit is divided by the state profit. If the state profit is negative, and the city's profit is negative, the result is mistaken as positive (negative divided by negative is positive).

* To fix this problem, multiply the entire calculation by the sign of the state profit.

  * `[Contribution to State Profit] * SIGN(ATTR([State Profit, LOD Exclude]))`

  * Double click on the pill in the color mark.

  ![Images/ReviewLOD6.png](Images/ReviewLOD6.png)

  * Enter the formula above in place.

  ![Images/ReviewLOD7.png](Images/ReviewLOD7.png)

* Now cities with negative profit are correctly colored.

  ![Images/ReviewLOD8.png](Images/ReviewLOD8.png)

* Finally, in Part III, the chart visualizes the sum of the profits of each state's cities.

  ![Images/ReviewLOD9.png](Images/ReviewLOD9.png)

  * The syntax used here is `INCLUDE` instead of `EXCLUDE`.

  ![Images/ReviewLOD10.png](Images/ReviewLOD10.png)

  * This means that the map is visualized at the state level, but that the data comes from the city-level.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2yKWzbE)</sub>

- - -

## References

The American Kennel Club. (2014). Breeds by Size. Edited and compiled by Len Fishman. [https://data.world/len/dog-canine-breed-size-akc](https://data.world/len/dog-canine-breed-size-akc)

Coren, Stanley (1995). The Intelligence of Dogs: A Guide To The Thoughts, Emotions, And Inner Lives Of Our Canine Companions. New York: Bantam Books. 

Tableau Software, LLC, A Salesforce Company. (2016). The Global Superstore Dataset. [http://www.tableau.com/sites/default/files/training/global_superstore.zip?_ga=2.196289452.1621662692.1614105956-1464408296.1614105934](http://www.tableau.com/sites/default/files/training/global_superstore.zip?_ga=2.196289452.1621662692.1614105956-1464408296.1614105934)

New York City. (2017). Vehicle Collisions in NYC, 2015-2016. Version 2. Compiled from [NYC OpenData Motor Vehicle Collisions - Crashes](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/data) [https://www.kaggle.com/nypd/vehicle-collisions](https://www.kaggle.com/nypd/vehicle-collisions)

U.S. Geological Survey Earthquake Hazards Program. (2017). Significant Earthquakes, 1965-2016. [https://earthquake.usgs.gov/fdsnws/event/1/](https://earthquake.usgs.gov/fdsnws/event/1/)

U.S. Department of Labor. (2016). Minimum Wage by State, 2009-2015. [https://www.dol.gov/agencies/whd/state/minimum-wage/history](https://www.dol.gov/agencies/whd/state/minimum-wage/history)

New York City. (2017). 311 Service Requests 2012-2017. [https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
