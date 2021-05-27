# 11.2 Introduction to GitHub Pages and CSS

## Overview

Today's class will focus on introducing students to styling HTML pages using basic CSS while also teaching them how to deploy the websites they create to GitHub Pages.

## Class Objectives

* Students should have a firm understanding of how to deploy HTML webpages to the internet using GitHub Pages.

* Students will understand the basics of CSS styling.

* Students will have a basic grasp on how to position HTML elements on a webpage using CSS.

## Instructor Prep

<details>
    <summary><strong>Instructor Priorities</strong></summary>

* Since we are going to start off this class by creating a personal/organization site using GitHub Pages, it would be a good idea to create an account specifically for your class that you can work with. Do this before today's class if you can.

* Students should fully understand how to deploy simple HTML/CSS webpages to GitHub Pages

* Students should have a basic understanding on how to use CSS to style and design basic HTML webpages

</details>

<details>
    <summary><strong>Instructor Notes</strong></summary>

* The main priority of this class is to get students comfortable using CSS. While it is important for your students to understand how to deploy to GitHub Pages as well, students will need a solid foundation of CSS in order to understand the topics covered in the next class.

* This class is also a critical step towards the next Career Services Milestone. Students will need an employer competitive portfolio to showcase their work. The material covered today will enable students to complete this next milestone. Look for talking points about this at the end of today's lesson.

* We are going to be covering a lot of material in very little time today and, as such, there may be times when your students are confused as to why something works the way it does. This will especially be the case when you get to the sections on floats and positioning. If/When this happens, make sure to assist your students as best you can and let them know just how many external resources there are which could help them better understand some of the complexities of CSS styling.

* Remember, we are simply trying to instill our students with a solid grasp of the fundamentals. Try not to go too far off-topic answering questions regarding complicated styling. Much of what we teach today is going to be supplemented and made easier next class through Bootstrap. Watch out for positioning especially as that topic can be a major time sink.

* Lastly, as a reminder these slideshows are for instructor use only - when distributing slides to students, please first export the slides to a PDF file. You may then send out the PDF file.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-11-web) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

</details>

<details>
    <summary><strong>Sample Class Video</strong></summary>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=df02fb76-0f16-4de5-bf4b-05096f00723b)

</details>

<details>
    <summary><strong>Troubleshooting Guide</strong></summary>

* Below is a list of the most common issues that students present when trying to do Github Pages deployments.

* **Forgetting to "git add", "git commit -m":** Often students will completely skip the step where they save and commit their changes prior to pushing to GitHub. This will mean their web page is essentially blank. As a starting point, ensure their code is present in GitHub.

* **Didn't name the repo correctly:** Students will likely not name the repository for their custom site correctly - ensure it follows the pattern `_username_.github.io`

* **Images and/or CSS not appearing:** All filenames and paths are case sensitive. Ensure that all links in HTML are using case-sensitive paths that match the folder directories casing.

* **Not using relative paths:** Many students are still using absolute paths to reference their CSS or image files. Help them to convert these to relative paths.

* **Not knowing where their site deployed:** Show students that they need to login to the site and they will see the new app deployed on their menu. Give them guidance as to what the URL for their repo will be.

* Beyond that... Good luck!

</details>

- - -

# Class Activities

## 1. Welcome & HTML Warm-up

| Activity Time:       0:20 |  Elapsed Time:      0:20  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 1.1 Instructor Do: Welcome the Class (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 1 and 2 to welcome the students.

* Take a few moments to welcome the class and remind them of this week's topic: basic web development.

* Let them know that today's class will be focusing on deploying simple webpages to the internet and styling them using CSS

* Before diving into new content, however, slack out the following activity to refresh students on the basics of HTML

</details>

<details>
    <summary><strong>✏️ 1.2 Students Do: HTML Warm-Up (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 3 and 4 to present this activity to the class.

* For this activity, students will create an HTML page to serve as a personal bio.

* **Instructions:** [README](Activities/01-Stu_HTMLBio/README.md)

</details>

<details>
    <summary><strong>⭐ 1.3 Review: HTML Warm-Up (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slide 5 to review this activity.

* Invite some students from the class to share their code on Slack so that they can show off their work.

  * Do a walk through of the code with your class, calling upon students to explain the HTML to their peers.

* If no one was able to find a solution to the bonus, take a few moments to explain how you can use links to move between pages contained within the same folder system.

  * The address for the link is the path to the file within your folder system. So if the HTML files were stored in the same folder, the link would be `<a href="filename.html">Link to File</a>`

  * Make certain to point out to the class that it is far wiser to use relative paths and not absolute paths when linking between files within the folder system. This ensures that, when the files are eventually deployed, the path linking between the pages changes to fit the new folder system.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2UV4ydw)</sub>

- - -

## 2. Deploying Personal Bios to Github Pages

| Activity Time:       0:20 |  Elapsed Time:      0:40  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 2.1 Instructor Do: Deploying to GitHub Pages - Personal (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 6 - 8 to over this lesson.

* Now that our class has created a few basic webpages locally, it's about time we started putting these pages online for the world to see. In order to do this, we are going to be hosting our websites on GitHub Pages.

* Explain to the class what the concept of a "host" is.

  * A web host is the activity or business of providing storage space and access for websites. You cannot put a website online without it being hosted on a server somewhere.

* Open up the [GitHub Pages website](https://pages.github.com/) and explain how it essentially allows us to turn GitHub repositories into live webpages without having to worry about pushing our code to another web host provider.

  * GitHub Pages even boasts about how it can turn simple text documents into live websites using a built-in system called "Jekyll"... We will not be using this at the moment but it is very cool. Your students may want to look into it at some point in the future.

  * GitHub Pages also allows you to create personal/organization sites for your account OR sites that are specific to a project! We will be going over both methods.

* Walk through the steps of creating a personal website using GitHub Pages...

  1. Create a new repository on GitHub called "_username_.github.io" where _username_ is your account name on GitHub.
  2. Next, open up Git Bash or Terminal on your computer. Navigate into the folder that you would like to store your project in and then clone the repository you just created.
  3. Within this new folder, add an HTML file called "index.html" which contains the code for the website you would like to publish.
  4. Add, commit, and push your changes to the repository and... That's it! Whenever anyone navigates to "_username_.github.io" they will now land on your webpage!
  5. Navigate to the website on your browser to show your class that the webpage is now fully online.

* Recap the steps for deploying to GitHub Pages one more time before continuing onto the next activity.

  1. New repo that is labeled "_username_.github.io".

     ![new repo](Images/create_repo.png)

  2. Navigate into a folder and clone the repo into it

  3. Add an HTML file named "index.html" and code out your webpage

     ![add_index](Images/add_index.png)

  4. Add, commit, and push your changes into the repository

  5. Go to the settings tab in the repo and scroll down to GitHub pages to confirm the page was published.

     ![settings](Images/settings_page.png)

  6. Finally click the link or navigate to `https://_username_.github.io` to visit the webpage.

</details>

<details>
    <summary><strong>✏️ 2.2 Students Do: Deploying Personal Bios to GitHub Pages (0:10)</strong></summary>

* For this activity, students will be deploying the bio pages they made in the last activity to Github Pages.

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 9 and 10 to to present this activity to the class.

* **Instructions:** [README](Activities/02-Stu_GithubPagesPersonal/README.md)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3dRl46R)</sub>

- - -

## 3. Creating a Project Site

| Activity Time:       0:20 |  Elapsed Time:      1:00  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 3.1 Instructor Do: Deploying to GitHub Pages - Projects (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 11 - 14 to go over this lesson.

* Not every website can be a personal website, however, as there are many times in which we will want to create websites that are customized for specific projects. Luckily for us, GitHub Pages includes a VERY simple way to deploy webpages for individual projects as well!

* Walk through the steps required to create a website for a specific repository...

  1. Create a new repository on your GitHub account. You can name this repository whatever you would like.
  2. Once inside of the repository, create a new file and name it "index.html"
  3. Add some very basic HTML into this file, save it, and then navigate into your repository's Settings tab.
  4. Scroll down to the GitHub Pages section and then, in the section labeled "Source", select that you would like to use the main branch as your source.
  5. Navigate to "_username_.github.io/_repositoryname_" and you will find that your new web page has gone live!

* It is very likely that your students will be wondering how to get a custom domain for their projects as opposed to a site that is clearly linked to their GitHub account...

  * Mention that custom domains are more heavily coveted since they are more easily searchable online. This means that custom domains have to be purchased from companies known as "DNS Providers". These companies allow users to buy and register unique domain names and connect that name to an IP address. **GitHub Pages does not sell domain names.**

  * Tell your students not to worry about custom domains at this time since it is not necessary for the web work that we will be doing. If they really wish to link a webpage of theirs to a custom domain, however, GitHub Pages has great documentation on how to go about doing this.

</details>

<details>
    <summary><strong>✏️ 3.2 Students Do: Creating a Project Site (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 15 - 17 to present this activity to the class.

* For this activity students will be creating a web page to display and explain a data science project they've already completed. Students will deploy the HTML to a github pages project page.

* **Instructions:** [README](Activities/03-Stu_GithubPagesProject/README.md)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2w83Dho)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:15  |
|---------------------------|---------------------------|

- - -

## 4. Intro to CSS & Dull Corp

| Activity Time:       0:30 |  Elapsed Time:      1:45  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 4.1 Instructor Do: Introduction to Basic CSS Styling (Slides + Demo) (0:05)</strong></summary>

* Congratulations! We now know how to make our web pages live for the entire world to see! That's pretty awesome! Well... Maybe minus the "pretty" part, at least. Our sites are still very basic looking. So how do we go about making our webpages look better?

* Luckily for us, another web development language was developed to work alongside HTML for exactly this purpose: CSS.

* CSS stands for "**C**ascading **S**tyle **S**heets" and it is a computer language which is used to "format" HTML. In simpler terms, CSS is a presentation language which tells web browsers how the content of a particular page should look.

* While HTML was developed to describe the content of a webpage, CSS was developed to present what that content should look like.

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 19 - 22 to present this lesson to the class.

</details>

<details>
    <summary><strong>📣 4.2 Instructor Do: Live Code Basic CSS (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and leave slide 23 while you live code.

* When prompted by the slide deck, create a new HTML file and show the class some examples of how CSS can be used to change a page's styling.

  * **Stick with very simple styling for now!** Show your class how to change coloring, size, font boldness/italics, and alignment. We will delve into more complex CSS styling soon enough.

  * An example of an HTML page with some CSS styling has been provided within [04-BasicCSS](./Activities/04-Ins_BasicCSS/Solved/quick-example-internal-css.html) for you to use, but it is recommended that you live code all of the CSS so that your students get a good example of its usage.

    * The same file minus the CSS styling can be found in [04-BasicCSS](Activities/04-Ins_BasicCSS/Unsolved/quick-example-no-CSS.html) as well.

* To start, alter the style of the page within a pair of `<style>` tags that are contained within the HTML file.

  * Show them how you can create a "stylesheet" which contains CSS rules that can then be applied to multiple tags/elements.

  * Make certain to point out the syntax of CSS once more
    ![CSS Syntax](./Images/CSS-Syntax.gif)
    * Selector points to the HTML element you would like to style
    * Declaration blocks are bounded by curly-brackets
    * Each declaration block is separated by semicolons
    * Each declaration includes a CSS property and a value that is separated by a colon

* Explain and show your students how they can also change the style of specific elements within the HTML tags themselves using "inline styling".

  * Point out that this is more tedious than just having a separate stylesheet, as inline styling applies only to the individual tags the `style=""` attribute is placed inside. It also takes away the benefits you get from having your content and presentation separate from one another, making the code that much harder to maintain.

* Once you have described the syntax of CSS and shown off how CSS stylesheets work, open up a new file, save it as `stylesheet.CSS`, place all of the CSS you have written into this file, and then explain how you can reference external stylesheets in HTML using a `<link>` tag.

  * Ask the class why it might be better to have an external stylesheet as opposed to having all of your CSS styling contained within the HTML file.

  * External stylesheets can be changed out more easily than having to rewrite every CSS rule

</details>

<details>
    <summary><strong>✏️ 4.3 Students Do: Dull Corp CSS Styling (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 24 and 25 to present this activity to the class.

* For this activity, students will be updating the _DULL Corporation's_ website so that it is not nearly so... Dull. To do so, they will be creating an external stylesheet and linking it to pre-made HTML.

* **Instructions:** [README](Activities/05-Stu_DullCorpCSS/README.md)

</details>

<details>
    <summary><strong>⭐ 4.4 Review: Dull Corp Activity (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slide 26 to review this activity.

* Open up the [solution file](Activities/05-Stu_DullCorpCSS/Solved) and go over the code contained within with your class.

* Answer whatever questions your students may have before moving onto the next activity

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/34cyNRl)</sub>

- - -

## 5. Targeted CSS

| Activity Time:       0:20 |  Elapsed Time:      2:05  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 5.1 Instructor Do: Classes, IDs, and Divs (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 27 - 29 to present this activity to the class.

* Before going back into the slides, explain to the class why changing entire HTML elements may not exactly be the best practice.

  * If we were to have a CSS rule that applies to all paragraph tags, then all of our paragraphs would look the same. What if we wanted one to look differently from another?

  * Luckily there are HTML classes and ids which allow us to pick and choose which HTML elements we want to style in particular ways.

* To create an HTML class, place a `class="((className))"` attribute within an HTML element. To reference that class within the CSS, simply put a period in front of _className_ in your stylesheet.

  * Show this to your students by live-coding the following HTML/CSS
    ![Classes Example](./Images/classesExample.png)

* To create an HTML id, place a `id="((idName))"` attribute within an HTML element. To reference that id within the CSS, simply put a hashtag in front of _idName_ in your stylesheet.

  * Show this to your students by live-coding the following HTML/CSS
    ![ID Example](./Images/idExample.png)

* As a callback to the previous class, ask your students what the differences between a `div` element and a `section` element are.

  * Explain that `div` elements are used to group elements into visually related segments while `section` elements define a specific part of a page and thus should be used as a container element regardless of styling.

  * Container elements like `div` and `section`, combined with classes and ids, allow users to group and style HTML elements in chunks. This is especially useful in positioning.

</details>

<details>
    <summary><strong>✏️ 5.2 Students Do: Targeted CSS (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 30 - 31 to present this activity to the class.

* In this activity, students will be given a very basic HTML file and will have to create an external CSS stylesheet which changes the page's styling.

* **Instructions:** [README](Activities/06-Stu_TargetedCSS/README.md)

</details>

<details>
    <summary><strong>⭐ 5.3 Review: Targeted CSS (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slide 32 to review this activity.

* Open up the [solved version](Activities/06-Stu_TargetedCSS/Solved) of the previous activity and go through the code with your class, answering whatever questions they may have.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2UCHu4m)</sub>

- - -

## 6. Aimed Positioning

| Activity Time:       0:30 |  Elapsed Time:      2:35  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 6.1 Instructor Do: Box Model and CSS Positioning (Slides) (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slide 34 to explain box models and slides 35 - 40 on using CSS to position elements, answering whatever questions the class may have.

  * After you have gotten through the slide on the box model, open up Google Chrome and show off the HTML/CSS inspector in its developer's tools.

  * For the time being, specifically focus upon the box-model visualizer.

  * Once you have covered the inspector, provide your students with some time in which to visit their favorite website and play around with the inspector on that page.

  * After a small amount of time has passed, continue through the slides once more.

* We are going to want to move through these slides on CSS Positioning rather quickly so that we can get into the [live-coding examples](Activities/07-Ins_CSSPositionedLayout).

  * If you are running low on time, it is more important to go over the positioning examples than it is to go through the slides themselves.

  * When going through the examples one-by-one, make sure to have the inspector open in Google Chrome so that we can show the class the differences between one form of CSS positioning and another both on the page and in the code.

  * If you have time, this would be a good opportunity to ask your students what they feel are the advantages and disadvantages of each form of positioning.

* Once you have completed the live-coding examples for CSS positioning, open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 41 - 49 and 10 to move into floats and then dive into the next activity.

</details>

<details>
    <summary><strong>✏️ 6.2 Students Do: Aimed Positioning (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 50 and 51 to present this activity to the class.

* For this activity, students will be given an HTML file they will style using CSS. In particular, they will be positioning certain elements as described in the instructions.

* **Instructions:** [README](Activities/08-Stu_AimedPositioning/README.md)

</details>

<details>
    <summary><strong>⭐ 6.3 Review: Aimed Positioning (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slide 52 to review this activity.

* Bring the class altogether and then go over the activity once more as a class

* Ask the class which method was the easiest and which was the hardest

* Ask them if they can see any relative advantages and/or disadvantages to each individual method

  * Positioning can be used to better place elements without having to move them around in the HTML. They can also be placed on the same line far more easily and, if you use percentages, are more reactive to the viewport's size.

  * Using the box model alone makes the exact placement of separate elements quite difficult since they cannot easily be placed on the same line.

  * Using the box model alone to position elements is also heavily frowned upon and should be avoided when possible.

  * Floats and clears are useful but can be quite difficult to pick up initially. They are more situationally useful than positioning in cases where you would like text to wrap around an element.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2wQNCgs)</sub>

- - -

## 7. Reworking the Bio Page

| Activity Time:       0:25 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
    <summary><strong>✏️ 7.1 Students Do: Reworking the Bio Page (0:20)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slides 53 - 57 to present this activity to the class.

* For this activity, students will be given a Bio Page HTML skeleton and will style it with CSS so the HTML resembles the image provided in the unsolved folder.

* **Instructions:** [README](Activities/09-Stu_StudentBio/README.md)

</details>

<details>
    <summary><strong>⭐ 7.2 Review: Bio Page (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1GfR6zMkrNdpm9Dwe0hQgDtB82i8Ab82Sc469XzSw8c8/edit?usp=sharing) and use slide 58 to review this activity.

* Invite some students from the class to share their webpages/code on Slack so that they can show off their work.

  * Do a walk-through of the code with your class, calling upon students to explain the HTML and CSS to their peers.

* If there are any areas where your students are struggling, be sure to recap that area for them briefly so that they can catch up.

* Emphasize the following points about the importance of today's material:

  * Students will be able to build upon the bio and project pages they made today to create an effective portfolio to share with employers.

  * Students should spend time adapting and customizing these pages to showcase their personal brand and skills throughout the remainder of the program so that they can be employer ready at graduation. Employer ready would be a completed resume and portfolio to send to job opportunities.

  * In an upcoming Milestone with Career Services, students will be asked to submit their portfolio for review and feedback. At that time Career Services will continue to help develop an employer ready portfolio to showcase skills and abilities. Remember that this is needed to successfully apply to jobs.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/39DsR5a)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
