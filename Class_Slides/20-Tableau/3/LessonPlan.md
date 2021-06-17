## 20.3 Tableau Mini Projects

## Class Objectives

* Students will perform exploratory data analysis using Tableau.
* Students will clean data prior to creating visualizations.
* Students will will create Tableau dashboards.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</summary></strong>

* You may find that this lesson falls on a weekday due to a holiday shifting the course schedule. In this case, we have provided notes within the LP that will allow you to **easily adjust the length of the lesson to fit into a weekday class**.

  * Be on the lookout for a **3-Hour Adjustment** note at the top of activities in this Lesson Plan. If this class is being taught on a weekday, please utilize the directions found in the note. Keep in mind that breaks will be reduced from 40 minutes to the typical 15 minutes for a weekday class as well.

  * Shortening these activities could potentially limit the students' ability to finish them, so please remind them to utilize office hours to clear up any questions they may have.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-20-tableau) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

</details>

<details>
  <summary><strong>Sample Class Video</summary></strong>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=fcf5ff82-8379-4457-a1b8-a88a00f90fd8)

</details>

# Class Activities

## 1. Psychiatric Health Care

| Activity Time:       0:40 |  Elapsed Time:      0:40  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ Students Do: Psychiatric Health Care (0:30)</strong></summary>

* ⏰**3-Hour Adjustment**: Reduce activity time to 20 minutes.

* **Instructions**: [Activities/01-Stu_Healthcare/README.md](Activities/01-Stu_Healthcare/README.md)

* In this warm-up activity, students will work with 2014 data on in-patient psychiatric patient care in hospitals across the United States.

* The data set contains information on, among other things:

  * The number of patients who were discharged with a continuing care plan
  * The number of patients who were discharged with multiple anti-psychotic medications
  * The use of physical restraint
  * The use of seclusion

* Students will first have to clean the data, at a minimum fixing the column headings. They will use the included **HBIPS_Measure_Sets.pdf** to accomplish this task.

  * For example, `HBIPS3` in the CSV refers to the use of seclusion, in hours.

* Students should first come up with a dashboard summary that resembles the following.

  ![Images/dashboard1.png](Images/dashboard1.png)

* Afterwards, they will create additional visualizations of their choosing. This activity will focus on data exploration, rather than obtaining pre-defined visualizations. Students are encouraged to come up with interesting and creative visualizations, and they are free to bring additional data sources into the workbook.

* Encourage students to slack out screenshots of interesting visualizations.

</details>

<details>
  <summary><strong>⭐ Review: Psychiatric Health Care (0:10)</strong></summary>

* **File**: [Activities/01-Stu_Healthcare/Solved](Activities/01-Stu_Healthcare/Solved)

* If necessary, take a few minutes to review the basics of creating a dashboard and filters. In the current example, dropdown menus are employed.

  * In the dashboard, click on the downward pointing arrow to access the filters submenu, then choose the filter.

  ![Images/filter1.png](Images/filter1.png)

  * Then click on the downward pointing arrow in the _filter_ box to choose a dropdown menu.

  ![filter2.png](Images/filter2.png)

* Also go over the visualizations in the instructor example, as well as visualizations created by students.

  * For example, Texas stands out as a state in which physical restraint is used, or at least reported, more than in other states.

  ![Images/sample1.png](Images/sample1.png)

  * Nebraska, Idaho, and Puerto Rico stand out as places where patients are likelier to be discharged with multiple antipsychotic medications.

  ![Images/sample2.png](Images/sample2.png)

  </details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2xh8a1J)</sub>

## 2. Airline Safety

| Activity Time:       0:20 |  Elapsed Time:      1:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 3.1 Students Do: Airline Safety (0:15) </strong></summary>

* **Instructions**: [Activities/02-Stu_Airline/README.md](Activities/02-Stu_Airline/README.md)

* In this activity, students will explore the safety of the world's airlines. The data set used here is from [fivethirtyeight.com](https://github.com/fivethirtyeight/data/tree/master/airline-safety)

* It will be an open-ended exploration of the data, but some questions to consider might be:

  * What are the safest airlines in the world, and how do we define the idea of safety?
  * Can we group airlines by region to determine whether some regions have better track records than others? What are some possible fallacies of this approach?

</details>

<details>
  <summary><strong>⭐ Review: Airline Safety (0:05)</strong></summary>

* **File**: [Activities/02-Stu_Airline/Solved/airline.twbx](Activities/02-Stu_Airline/Solved/airline.twbx)

* Spend a few minutes reviewing the activity, and having students share their results.

* As noted in the associated [article](https://fivethirtyeight.com/features/should-travelers-avoid-flying-airlines-that-have-had-crashes-in-the-past/), it may be preferable to take incidents into account, rather than fatalities, as fatalities comprise only a quarter of the total incidents.

* In one of the tabs in the instructor solution, airlines from east and southeast Asia were grouped together in a set, and measured against the rest. The Asian airlines show higher fatalities per available seat kilometer, but it is worth noting that the results amount to a difference of about one in ten million, and it is not immediately clear whether they are statistically significant.

* The last visualization plots the number of incidents against available seat kilometer across all airlines in a scatter plot.

  ![Images/airline1.png](Images/airline1.png)

  * It appears, as we might predict, that the number of incidents goes up with more miles flown.
  * To create a regression line, click on the `Analytics` tab next to the `Data` tab, and click on `Trend Line`.

  </details>

  <sub>[Having issues with this activity? Report a bug!](https://bit.ly/3aU6I3X)</sub>

- - -

## Break

| Activity Time:       0:40 |  Elapsed Time:      1:40  |
|---------------------------|---------------------------|

* ⏰**3-Hour Adjustment**: Reduce break time to 15 minutes.

- - -

## 3. Endangered Languages

| Activity Time:       0:30 |  Elapsed Time:      2:10  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 3.1 Student Do: Endangered Languages (0:20)</strong></summary>

* **3-Hour Adjustment**: Skip this **Student Do** activity and continue on to the review activity.

* **Instructions**: [Activities/03-Stu_Languages/readme.md](Activities/03-Stu_Languages/README.md)

* In this activity, students will be required to visualize data on the world's endangered languages. In addition, they will join additional data to their data set to create extra visualizations.

</details>

<details>
  <summary><strong>📣 3.2 Review: Endangered Languages (0:10)</strong></summary>

* **3-Hour Adjustment**: This review activity is now an **Everyone Do**.

  * Spend only 15 minutes on this activity.

  * Use the review section as guidance for talking points as you live-code along with the students.

  * Be sure to take your time and answer all student questions along the way.

* **File**: [Activities/03-Stu_Languages/Solved/languages.twbx](Activities/03-Stu_Languages/Solved/languages.twbx)

* Take a few minutes to review the activity. In the instructor solution, `Countries.csv` is data downloaded from the World Bank. It was joined to the `data.csv` to create the map in the final tab: Wealthier Nations with Endangered Languages.

  ![Images/languages1.png](Images/languages1.png)

  * A custom field was made to divide a country's per capita GDP by its number of endangered languages. This index is meant to highlight the wealthiest countries with the largest number of endangered languages: in other words, countries that have the greatest responsibility to preserve their dying languages, and have the means to do so.

  * A filter has also been applied to select for countries with a minimum per capita GDP of $15,000 USD.

  * The lower the index, the greater the urgency.

  * The per capita GDP must be made into an attribute.

* Solicit students for any interesting visualizations they might have created, and discuss them.
  
</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2Xol1d1)</sub>

## 4. Mini Project

| Activity Time:       1:50 |  Elapsed Time:      4:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 4.1 Students Do: Mini Project (0:55)</strong></summary>

* ⏰**3-Hour Adjustment**: Reduce activity time to 45 minutes.

* In this open-ended activity, students will use their Tableau skills to explore data and create visualizations.

* Students will work in pairs or groups of three.

* They must use at least two data sources.

* They may use their previous group projects for inspiration. However, they should not simply replicate their old projects in Tableau.

* When working with data, they may need to clean it with a tool like Pandas before bringing it into Tableau.

* They will give a brief (3-5 minutes) presentation to the class with a summary of their visualizations and findings.

</details>

<details>
  <summary><strong>✏️ 4.2 Students Do: Presentations (0:55)</strong></summary>

* Groups will deliver a brief presentation of their findings.

</details>

- - -

## References

The World Bank. (2018). World Development Indicators. [https://datacatalog.worldbank.org/dataset/world-development-indicators](https://datacatalog.worldbank.org/dataset/world-development-indicators)

The Guardian Datablog. (2011). Endangered Languages. Compiled from [UNESCO Atlas of Endangered Languages](http://www.unesco.org/languages-atlas/). [https://www.theguardian.com/news/datablog/2011/apr/15/language-extinct-endangered](https://www.theguardian.com/news/datablog/2011/apr/15/language-extinct-endangered)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
