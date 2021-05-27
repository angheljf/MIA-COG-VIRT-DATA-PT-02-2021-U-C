# 11.3 Bootstrap

## Overview

In today's class, we introduce students to the Bootstrap CSS framework.

## Class Objectives

* Students will be able to discuss media queries, the technology that is used to create the responsive Bootstrap grid.

* Students will cover the Bootstrap Grid, and discover how to utilize it to position the elements on the page.

* Students will discover how to quickly and easily build web pages using pre-built Bootstrap components.

## Instructor Prep

<details>
  <summary><strong>Instructor Priorities</strong></summary>

* Students should become familiar with different Bootstrap components and understand the Bootstrap grid.

* Students should have a high-level understanding of media queries.

* Students should have an understanding of how to use different column sizes to make websites responsive for smaller screens and mobile devices.

</details>

<details>
  <summary><strong>Instructor Notes</strong></summary>

* You may find that this lesson falls on a weekday due to a holiday shifting the course schedule. In this case, we have provided notes within the LP that will allow you to **easily adjust the length of the lesson to fit into a weekday class**.

  * Be on the lookout for a ⏰**3-Hour Adjustment** note at the top of activities in this Lesson Plan. If this class is being taught on a weekday, please utilize the directions found in the note. Keep in mind that breaks will be reduced from 40 minutes to the typical 15 minutes for a weekday class as well.

  * Shortening these activities could potentially limit the students' ability to finish them, so please remind them to utilize office hours to clear up any questions they may have.

* Today's class serves to provide an introduction to Bootstrap CSS. By the end of class, students should be able to build responsive websites using Bootstrap.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-11-web) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

</details>

<details>
  <summary><strong>Sample Class Video</strong></summary>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=99e109b3-b9ce-42a5-aa0b-aa790183e206)

</details>

- - -

# Class Activities

## 1. Welcome & Styling Classes and IDs

| Activity Time:       0:35 |  Elapsed Time:      0:35  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Welcome Class</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slides 1 and 2 to welcome the class, congratulate them on making it to day 3. Inform students today we'll focus on making our web pages responsive on any size device, as well as how to create websites quickly and easily by using prebuilt Bootstrap components.

</details>

<details>
  <summary><strong>✏️ 1.2 Students Do: Styling Classes and IDs (0:20)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slides 3 and 4 to introduce this activity to the class.

* Explain to students that we're going to start off with a quick review of some of the material covered in the previous class.

* For this activity they'll try their best to create a CSS layout from this image already supplied in the [01-Stu_ReviewActivity](Activities/01-Stu_ReviewActivity/Unsolved) unsolved folder.

![CSS Review](Images/01-CSS-Review.png)

* **Instructions:** [README](Activities/01-Stu_ReviewActivity/README.md)

</details>

<details>
  <summary><strong>⭐ 1.3 Review: Styling Classes and IDs (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slide 5 to review this activity.

* Open the [01-Stu_Review_Activity_Solved](Activities/01-Stu_ReviewActivity/Solved) folder and walk the class through each piece of the code in styles.css

* Navigate to the CSS, the HTML, and the rendered document in your web browser as you're explaining this.

* Point out how since we included a `reset.css file`, we need to specify what sizes our `h1` tags should be. Otherwise, they'll all be the same size.

* Point out how we target the `li` inside of the navbar, and we give our header a fixed height, some padding, and a background color.

* Be sure to point out how we target the h1 tag inside of the header here.

* Finally, show students how we can give each post some margin to create separation between posts. In this case, we could have used padding as well and gotten **seemingly** the same result, although margin and padding are different.

* Test your student's understanding by asking the following:

  * "Say I'm sitting in a car. I want the car to be an analogy for the box model. Say I'm the content - what would be the equivalent of the padding?"

    * The car interior is the padding. It's the space around me, but still inside the car.

  * "Using the same analogy, where my car is an HTML element, I am the content, and my car's interior is the padding, what's the border?

    * The border is the outer surface of the car.

  * "Using the same analogy, where my car is an HTML element, I am the content, my car's interior is the padding, and the surface of my car is the border, what is the margin?

    * The margin is the space put between the surface of the car and all the things around it.

* Take a moment to answer any additional questions. Let students know that it's okay if they took a different approach to solving this problem. As in most things when it comes to programming, there are multiple ways to achieve the same result.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/39HT4PM)</sub>

- - -

## 2. Chrome Devtools

| Activity Time:       0:25 |  Elapsed Time:      1:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Chrome Dev Tools (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slides 6 and 7 to introduce Chrome DevTools to the class.

* Inform students that because HTML and CSS won't throw errors when we do something wrong, they can be tricky to debug. One of the tools we use to accomplish this is Chrome Devtools.

  * Students should have been given a brief introduction to Chrome Devtools earlier in the week, but remind them that it's a set of web authoring and debugging tools built into Google Chrome.

  * We can open Chrome Devtools with `Cmd + Option + I` on  a Mac and `Ctrl + Shift + I` on a PC. Alternatively, we can right click anywhere on a web page and click the `inspect` option to bring up Chrome Devtools.

  ![Devtools](Images/06-Devtools.png)

* Devtools gives us a few different options, including the ability to see incoming and outgoing network requests, debug JavaScript, manage client-side storage (cookies, local storage, sessions).

* For now the only feature we're concerned with is the ability to inspect our HTML elements and CSS.

* Demonstrate this with a website of your choice for students. Show students how when we navigate to the `Elements` tab, we can see all of the rendered HTML, as well as any CSS applied to each element in the right sidebar.

* Show students how we can change the text inside of the HTML here by changing the values inside the element inspector inside Chrome Dev Tools. Also, modify some of the CSS values in the right sidebar of the element inspector.

  * Once you've made a few changes, refresh the page and show students how those changes have cleared.

  * Inform students that these changes were client side only. In other words, we only affected how the website looked on our computers.

* Inform students that we can make changes locally to our HTML and CSS files using Chrome Devtools, and then copy/paste those changes into our actual HTML and CSS files when we're satisfied. We can test changes quickly without having to refresh our browser or edit our actual document right away if we're unsure about making a change.

  * This is great for debugging CSS styles, as we can see if the styles we're trying to apply are being overridden by another style. We can also see the default styles applied to a web page by the web browser.

* We can use the element inspector to learn how to implement something we see on another website into our own. For example, if we visited a web page and liked its style of buttons, we could inspect those buttons and see the exact CSS being applied to make it look that way.

* Answer any questions before the next exercise.

</details>

<details>
  <summary><strong>✏️ 2.2 Students Do: Chrome Devtools (0:10)</strong></summary>

* ⏰**3-Hour Adjustment**: Skip this **Students Do** activity and continue on to the review activity.

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slides 8 and 9 to instruct students for this activity.

* For this activity, students will be modifying a website of their choice using Chrome Devtools. Each student should take a screenshot of the website they modified and post it in the class's slack channel.

  * **Instructions:** [README](Activities/02-Stu_ChromeDevtools/README.md)

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Chrome Devtools (0:05)</strong></summary>

* ⏰**3-Hour Adjustment**: This review activity is now an **Everyone Do**.

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slide 10 to review this activity.

  * Spend only 10 minutes on this activity.

  * Use the review section as guidance for talking points as you live-code along with the students.

  * Be sure to take your time and answer all student questions along the way.

* As a class, go over the last activity.

* Review a few of the submitted screenshots from the last exercise in the class slack channel.

* Have students discuss the changes they were able to make.

* Have students to explain to you how they were able to to make those changes.

* Inform students that we'll be using Chrome Devtools more frequently, so there's no need to worry if they aren't comfortable with it yet.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3bS8EtV)</sub>

- - -

## 3. Media Queries

| Activity Time:       0:35 |  Elapsed Time:      1:35  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: Introduce Media Queries (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slides 11 - 15 to present this lesson.

* Explain to students that so far we haven't been too concerned about whether or not out websites looked good on different size screens.

  * This is important to think about since there is now more web traffic from mobile devices than there is from desktop and laptop computers.

* Show students how we can get an idea of how our web pages would look on smaller sized devices by dragging the browser window to shrink the page's width.

* You'll notice that once we reach a certain point, our navbar doesn't look right and the padding we used to have on the sides of each article makes it harder to read.

* Thankfully we can use media queries to fix this. Explain to students that there isn't much to them - they essentially tell the browser browser to apply additional styles if a given condition is met. To that end, we can use them to alternate and override existing styles conditionally.

* To help illustrate this, open [03-Ins_MediaQueries](Activities/03-Ins_MediaQueries/Solved/index.html). Show students each colored div in your browser, and then bring them to the styles.css file.

* Point out how we define our styles to our elements as usual, but down at the bottom we have some new syntax:

![03-Media-Queries](Images/03-Media-Queries.png)

* Inform students that @media is a keyword in CSS that means we're about to define some styles that are only going to be applied when our device is a specified size or type. In this case, only when the viewport (device screen) is under 480px. We can also declare whether we want this to happen on just screens or only when printing as well. We can add as many media queries as we want and at any screen size.

  * Assure students they don't need to memorize or be frightened by the new syntax. Examples are **very** easy to find with a quick web search of "CSS media queries."

* Ask students what they expect to happen when you uncomment the .box-1 media style.

  * After hearing their answers, uncomment this and reopen the HTML in your browser. Slowly drag the edge of your browser window until the box-1 div turns purple.

  * Repeat this process with a few of the other styles inside the media query.

* Ask students what they think you should do if you wanted to make it so that the CSS inside the media query was only applied when our screen was **larger** than 480px?

  * We'd just change max-width to say min-width. i.e. The screen needs to be **at least** this width for these styles to take effect.

* Make sure that everyone understands that this works because we're defining our media queries after our base styles. These new media query styles override the old styles because they come after them inside our CSS document.

* Let students know that they can define media queries at any size. Sometimes it takes a little bit of playing around to find the right breakpoints to add media queries.

  * An easy way to tell at what size we need to add a media query is to resize our Chrome window with inspector open.

    ![02-Inspector-Resize](Images/02-Inspector-Resize.png)

  * The browser window dimensions will be displayed at the top right corner.

* While we have inspector open, show students how we can see the styles being to elements applied by the media query. A good way to do this would be to select an element affected by the media query inside the element inspector, point out the CSS rules on the right side of the inspector, and watch as the media styles appear as you shrink the window.

  ![Media Inspect Before](Images/07-Media-Inspect-Before.png)

  ![Media Inspect After](Images/08-Media-Inspect-After.png)

</details>

<details>
  <summary><strong>✏️ 3.2 Students: Media Queries (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slides 16 and 17 to instruct students to this activity.

* For this activity, students will be modifying the solution to the last CSS review activity to be more mobile responsive using media queries.

* **Instructions:** [README](Activities/04-Stu_MediaQueries/README.md)

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Media Queries (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slide 18 to review this activity.

* Go over [04-Stu_Media_Queries_Solved](Activities/04-Stu_MediaQueries/Solved) with the class. Show them how we can target the `li`'s inside the `navbar` and reduce its padding inside the media query. Show them how we decrease the padding on either side of the `article` as well.

* Uncomment the code inside the media query here for the bonus solution. Show students how we can show and hide elements using the visibility property. Explain that `visibility: hidden` hides an element, and `visibility: visible`shows it. They've probably seen on plenty of websites how the `navbar` menu seems to collapse into a drop-down on mobile devices. Now they know how they can implement this functionality themselves!

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/39DtzPS)</sub>

- - -

## 4. Bootstrap & Lorem Grid

| Activity Time:       0:50 |  Elapsed Time:      2:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: Introduce Bootstrap (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slides 19 and 20 to introduce Bootstrap to the class.

* Explain to students that it's important to understand how media queries work, at least on a high level, but they probably won't have to use them too frequently because of CSS frameworks.

* Inform students that we're now going to get started with Bootstrap.

  * Bootstrap helps us write front end HTML and CSS much more quickly because it provides us with a few features such as:

    * A responsive 12 column grid.

      * Rather than specify exact pixel locations we want specific elements to appear, we can instead define where we want to add our element inside of the grid. Because the Bootstrap grid is responsive out of the box, we'll automatically have decent looking web pages on mobile without any extra work (although we'll want to tweak a few things here and there depending on how we want our content to be displayed)

    * Bootstrap offers us dozens of pre-built components we can use right away such as navbars, buttons, thumbnails, tables, and more. We have these components available to us at [Bootstrap's Website](http://getbootstrap.com/components/) to copy and paste into our apps.

    * We no longer need to worry about including a reset.css file, since Bootstrap normalizes CSS across various browsers, giving us a consistent looking web page on every device.

    * Bootstrap also includes various JavaScript components we can take advantage of such as sleek looking drop-down boxes and modals.

* Explain to students that while Bootstrap does give us a lot, we want to further customize the provided components by adding additional CSS to our stylesheets. If no one did this, every website using Bootstrap ([at least 11,987,613 currently](https://trends.builtwith.com/docinfo/Twitter-Bootstrap) would look the same. The main benefit here is that we no longer need to reinvent the wheel every time we create a web page.

* Send out the link to the [Bootstrap Expo](http://expo.getbootstrap.com/) and allow students to spend a few minutes browsing a few of the featured websites built with Bootstrap.

</details>

<details>
  <summary><strong>📣 4.2 Instructor Do: The Bootstrap Grid (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slides 21 - 23 to present Bootstrap Grid to the class.

* To demonstrate how we include Bootstrap into a project, navigate to the [Bootstrap Getting Started Page](https://getbootstrap.com/docs/4.3/getting-started/introduction/) and show the class from where they can copy the Bootstrap CSS CDN.

  * Inform students that they will only need the CSS CDN for now, we won't be using JavaScript until next week.

  * Explain to students that CDN stands for **C**ontent **D**elivery **N**etwork. Essentially a CDN is a network of distributed servers designed to handle large amounts of traffic and deliver content to users based on their geographic location. A CDN link will typically provide fast download speeds. Additionally, this allows us to include Bootstrap without having to manually download the entire framework to our computers every time we wanted to use it.

* Now open the [Bootstrap Demo](Activities/05-Ins_BootstrapDemo/Solved/index.html)

* Inform students that while Bootstrap offers us a ton of functionality, the most important thing they need to understand today is the grid system. Everything else we'll talk about today can just be copied/pasted from Bootstrap's website. The grid, however, is going to require a little more understanding.

* Walk students through the code in the [Bootstrap Demo Example](Activities/05-Ins_BootstrapDemo/Solved/index.html). For now, we're going to focus on medium sized columns. If nothing else, make sure students understand the following:

  * Columns go inside rows. Rows sit inside containers.

  * A row is comprised of up to 12 columns.

  * Don't alter the Bootstrap grid. i.e. don't add new CSS rules directly to `container`, `row`, or `col-*` (column) classes.

* Answer any questions before slacking out the next activity.

</details>

<details>
  <summary><strong>✏️ 4.3 Students Do: Lorem Grid (0:20)</strong></summary>

* ⏰**3-Hour Adjustment**: Skip this **Students Do** activity and continue on to the review activity.

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slides 24 and 25 to instruct students to this activity.

* For this activity, students will be given an image of a simple web page layout created using the Bootstrap grid. They will attempt to recreate this layout from scratch.

* **Instructions:** [README](Activities/06-Stu_LoremGrid/README.md)

</details>

<details>
  <summary><strong>⭐ 4.4 Review: Lorem Grid (0:10)</strong></summary>

* ⏰**3-Hour Adjustment**: This review activity is now an **Everyone Do**.

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slide 26 to review this activity.

  * Spend only 20 minutes on this activity.

  * Use the review section as guidance for talking points as you live-code along with the students.

  * Be sure to take your time and answer all student questions along the way.

* Using [06-Stu_Lorem_Grid_Solved](Activities/06-Stu_LoremGrid/Solved/index.html), walk students through the solution to the previous activity.

  * Note the different size columns we use depending on the portion of the screen we want our content to take up.

  * Open inspector and resize your browser window. Ask students why the layout changes when your screen shrinks past a certain size.

    * Since we used medium sized columns, they each resize into full sized small columns when displayed on a screen smaller than 768px.

  * Ask students what technology Bootstrap must be using under the hood to make this work the way it does.

    * Media Queries, 768px is the breakpoint Bootstrap set for this size column. On any screen size lower than this, all medium columns go full-wide by default.

  * Ask students what we would do if we wanted the columns to go half-wide when the screen was at a "small" screen size.

    * We'd add on additional Bootstrap classes for small columns, e.g. `<div class="col-sm-6 col-md-3">...`

* We'll have a demonstration of different column sizes a little later today, but make sure students otherwise have a basic understanding the Bootstrap grid and answer any further questions before going on break.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2UDNsSA)</sub>

- - -

## Break

| Activity Time:       0:40 |  Elapsed Time:      3:05  |
|---------------------------|---------------------------|

⏰ **3-Hour Adjustment**: Break will be 15 minutes.

- - -

## 5. Bootstrap Components

| Activity Time:       0:20 |  Elapsed Time:      3:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong>👥 5.1 Partners Do: Bootstrap Components (0:10)</strong></summary>

* ⏰**3-Hour Adjustment**: Reduce activity time to 5 minutes.

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slides 28 and 29 to instruct this activity.

* For this activity, students will create a basic web page using Bootstrap components.

* **Instructions:** [README](Activities/07-Stu_BootstrapComponents/README.md)

</details>

<details>
  <summary><strong>🎉 5.2 Everyone Do: Discuss Bootstrap Components (0:10)</strong></summary>

* ⏰**3-Hour Adjustment**: Reduce activity time to 5 minutes.

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and leave slide 30 while discuss this topic.

* Call on a few groups and have them tell you some of the different Bootstrap components they discovered.

* Open the [Bootstrap Components Docs](http://getbootstrap.com/components/) and scroll down to a few of them as they're called out.

* Inform students that Bootstrap's documentation encourages copying and pasting. Assure them that there's nothing wrong with this. There isn't much benefit in memorizing a Bootstrap component when we can easily copy/paste the code from their website.

* Explain that components need to be placed inside a column in order to span the whole page.

* Explain to the class that at times we will need to modify the snippets we copy from Bootstrap's website. The Bootstrap navbar for example. With these, we'll remove any links or drop-down we aren't going to be using before we fill the remaining ones in with our information.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3dMu1yx)</sub>

- - -

## 6. Clone a Website

| Activity Time:       0:35 |  Elapsed Time:      4:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 6.1 Instructor Do: Different Column Types (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slides 31 and 32 to present this lesson.

* Inform students that so far we've just used the medium sized Bootstrap columns. These are designed primarily for medium-sized screens such as a laptop or large tablet screens. These are what we'll use most often, but we can also take advantage of large, small, and extra small columns.

* Open your browser to the [Bootstrap Grid Docs](https://getbootstrap.com/docs/4.3/layout/overview/) and resize your browser window to show students how the medium sized columns fill up the entire width of the container as the screen shrinks.

* Also point out how extra small columns don't change at all when the screen shrinks.

* Explain to students that we can combine different types of columns to have our layout behave the way we want on different screen sizes.

* Open [Responsive Cols](Activities/08-Ins_ResponsiveCols/Solved/index.html) and demo this to the class.

    ![05-Responsive-Cols](Images/05-Responsive-Cols.png)

* Resize your browser window to demonstrate to students how the columns resize according to to the device width.

* Once more, ask students how it's possible for these columns to resize themselves on different screen sizes.

  * Media queries! Bootstrap uses media queries at various breakpoints to determine how large each column should be at each screen size.

</details>

<details>
  <summary><strong>✏️ 6.2 Students Do: Clone a Website (0:25)</strong></summary>

* ⏰**3-Hour Adjustment**: Reduce activity time to 12 minutes. Note: in case of a 3-hour class, students may require more than the allotted time. If students are unable to complete the activity in time, encourage them to finish it on their own, and remind them that learning Bootstrap initially requires some trial and error.

* Open the [slideshow](https://docs.google.com/presentation/d/1p_l-eCkT-Z1RCQeUyIjmSCbJbAhr4cbgmvA94HiCNqE/edit?usp=sharing) and use slides 33 and 34 to instruct the class to this activity.

* For this activity, students will attempt to recreate an existing website using the Bootstrap grid and Bootstrap components.

  * **Instructions:** [README](Activities/09-Stu_CloneAWebsite/README.md)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/39FDUL5)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
