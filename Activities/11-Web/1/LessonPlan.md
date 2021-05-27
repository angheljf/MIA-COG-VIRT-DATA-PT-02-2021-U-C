# 11.1 Introduction To HTML

## Overview

In today's class students will be introduced to front-end web technologies and learn enough HTML to be able to build simple web pages.

## Class Objectives

* Students will gain a high-level understanding of HTML, CSS, and JavaScript and what their roles are when creating websites.

* Students will understand the basic parts of an HTML web page and how to create one from scratch.

* Students will learn to cover and utilize some of the most common HTML tags and selectors.

## Instructor Prep

<details>
  <summary><strong>Instructor Priorities</strong></summary>

* Students should understand the overall structure of a web page.

* Students should have a very high-level understanding of HTML, CSS, and JavaScript and what their roles are in creating a website.

* Students should become familiar with the most commonly used HTML tags and attributes.

* Students should be able to build basic websites using HTML.

</details>

<details>
  <summary><strong>Instructor Notes</strong></summary>

* Today's class will serve to provide an introduction to HTML. By the end of today's class, students should have a basic grasp of the structure of an HTML document, as well as some commonly used tags and attributes.

* We have a lot of ground to cover this week and want to make sure students are comfortable with the material needed to complete this week's homework assignment. That being said, don't feel as though you need to cover **all** of HTML and CSS this week. A solid grasp of the fundamentals with the knowledge of how to find answers to their questions would be ideal.

* Lastly, as a reminder these slideshows are for instructor use only - when distributing slides to students, please first export the slides to a PDF file. You may then send out the PDF file.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-11-web) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

</details>

<details>
  <summary><strong>Sample Class Video</strong></summary>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=8c02274b-345b-4128-92de-a85f00085623)

</details>

- - -

# Class Activities

## 1. Instructor Presentation

| Activity Time:       0:15 |  Elapsed Time:      0:15  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Welcome Class (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slides 1 - 4 to welcome students to the class.

* Take a minute to welcome students and introduce them to this week's topic: The Web.

* Inform students that this week they will be creating, styling, and deploying their own web pages.

* Over the next few weeks, students will also learn CSS, JavaScript, and a few JavaScript libraries.

* Using their new skills, students will be able to create impressive interactive visualizations to help represent their data. We'll have a brief demonstration of this at the end of the slides in the next activity.

</details>

<details>
  <summary><strong>📣 1.2 Instructor Do: The Web (0:10)</strong></summary>

* Explain to students that the topics we will cover over the next few weeks will be composed of what is considered front-end web development.

* Assure students they don't need to fully understand any of the code snippets in the slides right away. The main thing we want them to understand is that these three languages exist, what they're for, and why we need to know them to build web applications.

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slides 5 - 8 to quickly explain the core Front-End technologies; HTML, CSS, and JavaScript.

* Encourage questions here, but avoid getting too off track.

* Take a minute at the end to show them a few of the D3 visualizations using the link at the bottom of the last slide. This will help provide some context for why we're learning these technologies now.

</details>

## 2. Hello, HTML

| Activity Time:       0:20 |  Elapsed Time:      0:35  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Hello, HTML (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slides 9 - 16 to introduce students to HTML.

* For this activity, **don't just display this file or copy and paste the code onto your screen.** Type it out from scratch, and let your students follow along.

* Create a new HTML file in your editor. Allow students to code along if they can, but tell them not to worry if they are having trouble keeping up. They will have a chance to work on an example of their own in a couple of minutes.

* Use the code in [`my-first.html`](Activities/04-Stu_MyFirst_HTML/Solved/my-first.html) as a guide.
  ![02-Example](Images/01-Example-HTML.png)

* As you code, make sure to stress which elements are **required** for a valid HTML page, which they'll have to type out each and every time.

  * Required elements include:

    * `<!DOCTYPE html>` - **required** - informs the browser which version of HTML (or XML) you used to write the document. Doctype is a declaration, not a tag; you can also refer to it as "document type declaration", or "DTD" for short.

    * `<html>` - **required** - represents the root (top-level element) of an HTML document, so it is also referred to as the root element. All other elements must be descendants of this element.

    * `<head>` - **required** - not to be confused with [header](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header), the head provides general information about the document, including its title and links to its scripts and stylesheets. None of the content inside the head should be content that needs to be visible on the rendered page.

    * `<meta charset-"utf-8">` - **required** - the meta element is used for representing any metadata information that can't be represented by another HTML meta-related element (`<title>`, `<style>`, `<script>`, etc.). In this case, we're specifying that we want to specify the character encoding of a web page. Essentially this helps tell the browser which language, writing system, and characters are being used in a web page. utf-8 is one of the most comprehensive and widely used and recommended. Students may occasionally see this not used, since most of the time this will be correctly inferred by the browser, or sent back from the server; it's still a good idea to include it to make sure that characters in our content are correctly interpreted, according to [The World Wide Web Consortium](https://www.w3.org/International/questions/qa-html-encoding-declarations.en)

    * `<title>` - **required** - defines the title of the document as shown in the browser's title bar or on the page tab. It can only contain text, any contained tabs are ignored.

    * `<body>` - **required** - represents the content of an HTML document. All content that needs to be rendered to the page should be placed inside the body.

* Make sure you're going from your editor to the rendered HTML in your browser in order to better show students the progress we're making as we're coding and to compare the written HTML code to the rendered page.

* As you type  `<img src="https://...">` (and other tags with attributes), explain briefly HTML attributes, and how they affect the HTML element: attributes on HTML elements are additional values that configure the elements or adjust their behavior. The `src` attribute here, for example, is a mandatory attribute for `img` that defines the URL of the image to be displayed. In anchor tag,  `<a href="https://...", the`href\` attribute describes the URL we should be taken to when a user clicks on a hyperlink created by the anchor tag.

* Be sure to point out any tags that are self-closing, such as the image tag. Explain that while **most** HTML elements are paired with a closing tag, some are self-closing. Elements without a closing tag are known as **void elements**. A closing slash is optional with these, e.g. `<img src="https://www.placehold.it/350x150"/>` vs `<img src="https://www.placehold.it/350x150">`. Whether you decide to use the closing forward slash or not, it's a good idea to be consistent in your usage.

* Once we have a few elements on the page, take this a step further and open Chrome Devtools. Devtools can be opened by any of the following:

  * Right clicking the rendered HTML document inside of Chrome and clicking the `inspect` option.

  * Pressing `F12` on Windows while in Chrome.

  * Pressing `command + option + i` on a Mac.

  ![Chrome Devtools](Images/02-Chrome-Devtools.png)

* Make sure the `Elements` tab is selected here.

* We don't need to dive too deeply into Devtools today, but it can be a helpful visual aid when showing students how our written HTML matches up to rendered elements on the page. Any element we click on inside the element inspector is highlighted on the rendered page.

  ![02-HTML](Images/03-HTML.png)

* Answer any questions before proceeding to the next exercise.

</details>

<details>
  <summary><strong>👥 2.2 Partners Do: Inspect Hello, HTML (0:05)</strong></summary>

* For this activity, students will spend a few minutes going over the example coded out in the last example and use Chrome Devtools to inspect it.

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slides 17 and 18 to introduce this activity to students.

* Instructions: [Stu_Inspect_Last_Activity](Activities/01-Stu_InspectLastActivity/README.md)

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Inspect Hello, HTML (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slide 17 to review this activity.

* Take a moment to make sure everyone was able to inspect the HTML using Chrome Devtools and answer any immediate questions.

* Point out to students that what we see in the elements inspector is what's known as the DOM, or the **D**ocument **O**bject **M**odel. This is essentially a tree of objects our web browser uses to model our HTML.

  * If we were to make a minor mistake in our HTML code, such as spelling the `head` tag as `hea`, we'd probably notice that this would be corrected inside of the element inspector. While Chrome won't change our actual HTML code for us, it will be smart enough to guess what we were trying to do and make sure that's fixed in the DOM.

    * It's important to note that we shouldn't rely on these corrections. Not all browsers will interpret invalid HTML the same way, so we want to be as accurate as possible to ensure consistent behavior across browsers.

* We'll dive a bit deeper into the DOM and Chrome Devtools in later sections, but this brief introduction is fine for now.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2xOZoYt)</sub>

- - -

## 3. HTML Tags

| Activity Time:       0:20 |  Elapsed Time:      0:55  |
|---------------------------|---------------------------|

<details>
  <summary><strong>👥 3.1 Partners Do: Research HTML Tags (0:10)</strong></summary>

* For this activity, students will create a list of HTML elements and their descriptions. Students should create a valid, informational HTML document in which they use and describe as many of their researched elements as possible.

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slides 20 and 21 to introduce this activity to the students.

* **Instructions:** [Stu_Research_HTML_Tags](Activities/02-Stu_Research_HTML_Tags/README.md)

</details>

<details>
  <summary><strong>🎉 3.2 Everyone Do: Discuss HTML Tags (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slide 22 to present this discussion to the class. Leave slide 23 while discussing this topic with the students.

* As a class, discuss some of the different HTML elements students were able to research in the last activity. Have students describe these.

* Be sure to ask for practical examples for each element, and give a few examples of your own. e.g. "The Google search bar would be an example of an input element", and then maybe go to [google.com](https://www.google.com) and inspect the search bar.

  * Try to stick to simple examples if you use inspector here; more complicated web pages may feel overwhelming at this point.

* Open the [`html-tags.html`](Activities/03-Ins_HTML_Tags/Solved/html-tags.html) in your browser and gloss over any of the HTML tags just discussed, spend a minute discussing any not mentioned.

* Explain to students that there isn't any need to memorize every single HTML tag. As they've probably already discovered by now, these are relatively easy to look up, and they'll mostly use a handful of the same ones over and over again.

  * If students encounter an unfamiliar HTML element, a great resource is [HTML5 Doctor](http://html5doctor.com/), which has an [Element Index](http://html5doctor.com/element-index/) we can look up unfamiliar tags with.

  * It's worth mentioning that students will likely stumble across [W3 Schools](http://www.w3schools.com/) as they're learning HTML, CSS, and JavaScript. Often times this will be the first Google search result. While many times W3 Schools will provide fast, easy to read answers, they aren't a considered a reputable source and have been known to provide inaccurate information at times.

    * The [Mozilla Developer Network](https://developer.mozilla.org/en-US/) is considered a much more authoritative resource for web development technologies. Encourage students to become familiar with finding answers on there before looking elsewhere.

Send out the [`html-tags.html`](Activities/03-Ins_HTML_Tags/Solved/html-tags.html) file.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2V3qof7)</sub>

- - -

## 4. My First HTML

| Activity Time:       0:30 |  Elapsed Time:      1:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 4.1 Students Do: My First HTML (0:15)</strong></summary>

* For this activity, students will create a simple HTML page.

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slides 24 and 25 to present this activity to the students.

* **Instructions:** [Stu_MyFirst_HTML](Activities/04-Stu_MyFirst_HTML/README.md)

</details>

<details>
  <summary><strong>⭐ 4.2 Review: My First HTML (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slide 26 to review this activity.

* When time is up, regroup and open up the solution file [`MyFirst_HTML_Solved`](Activities/04-Stu_MyFirst_HTML/Solved/my-first.html) and walk students through the code. Be sure to point out and quiz them on what each of the different elements does. It's okay if they aren't sure, encourage them to guess!

* In particular, take extra care to make sure they understand why we need the `html`, `title`, and `body` tags. Be sure to mention the `DOCTYPE` and `meta` as well.

  * `doctype` - tells the browser which version of HTML (or XML) we used to create the document. This isn't really a tag like all the others, but a declaration we put at the top of our page above the rest of the code.

  * `html` - represents the root (top-level element) of an HTML document. All other elements go inside the `html` element.

  * `head` - holds elements that provide general information about the HTML document, such as links to external CSS and JavaScript files, the title of the web page, and any other metadata used in the document.

  * `title` -  defines the title of the document as shown in the browser's title bar or on the page tab.

  * `<meta charset-"utf-8">` - the `meta` tag is used for any other metadata that can't be represented by another HTML element inside the head. In this case, we're specifying that we want to use the "utf-8" character set. This has to do with which language, writing system, and characters being used on a web page. This is currently the most widely used and recommended, as well as one of the most comprehensive.

  * `body` - represents the content of an HTML document. Any content that needs to be rendered to the page goes inside the body.

* Once that's been established, move on to the other elements. Go back and forth between VS Code and the rendered HTML page inside Chrome to help explain potentially confusing aspects of the solution.

  * Ask students what they think the alt attribute on the image does. Make sure they understand that while it is **technically** optional, we should always try to include this because:

    * The alt attribute helps users with visual impairments understand what type of content is being displayed on the screen when using a screen reader or braille display.

    * It helps search engines better understand the content of our web pages, helping us with [SEO](https://en.wikipedia.org/wiki/Search_engine_optimization).

    * If there's ever a time where our image can't be loaded properly, the alt attribute text will appear where the image would have.

  * Make sure students understand what `target="_blank"` does. Demonstrate this in the browser.

    * `target="_blank"` opens a link in a new tab.

      * By default, `target="_self"` is the default attribute for anchor tags (even if we don't write it explicitly). A hyperlink's default behavior is to open the web page in its current tab.

        * There are a few other, less frequently used options described in the [Mozilla Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attr-target), although we most likely won't need to use them.

  * If everyone's feeling confident with the solution, move on to the [bonus solution](Activities/04-Stu_MyFirst_HTML/Solved/my-first-bonus.html).

    * Point out how we can create ordered and unordered lists by nesting `li` elements inside either an `ol` (ordered list), or `ul` (unordered list) element.

      * We can nest any kind of content inside of lists, we aren't limited to only using text. When we visit a website with a navigation bar, it's often built with links inside of unordered lists.

    * Lastly, show students how the iframe element works.

      * This isn't just for videos, although that's where most people have seen them before.

      * If we were to change the iframe's `src` attribute to another website e.g. `https://www.wikipedia.org`, and reloaded the page, we'd see a nested window to wikipedia.org.

        * It's important to note that some websites block themselves from being loaded in iframes on external sites or on locally hosted files.

        * Most importantly, make sure students understand that an iframe effectively embeds an entire web page into the current page.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2waRp7M)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:40  |
|---------------------------|---------------------------|

- - -

## 5. Fix the HTML

| Activity Time:       0:15 |  Elapsed Time:      1:55  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 5.1 Students Do: Fix the HTML (0:05)</strong></summary>

* For this activity, students will be tasked with fixing mistakes in an HTML document.

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slides 28 and 29 to introduce this activity to the students.

* **Instructions:** [Stu_FixThe_HTML](Activities/05-Stu_FixThe_HTML/README.md)

</details>

<details>
  <summary><strong>⭐ 5.2 Review: Fix the HTML (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slide 30 to review this activity.

* Go over the [Solved](Activities/05-Stu_FixThe_HTML/Solved) version of the last activity as a class. Each comment in the corrected HTML describes what was changed from the incorrect version.

  ![Fix-HTML.png](Images/04-Solved-Fix-HTML.png)

* Ask students which mistakes they missed if any and answer any questions about the solution.

* Inform students that even though this document was full of issues, it still loaded in the browser, albeit not entirely as intended. This is because as mentioned earlier, web browsers will attempt to fix these issues as they get rendered to the DOM. We don't want to rely on this because it's inconsistent across browsers, or even across versions of the same browser.

* In your web browser, navigate to the [W3 Validator](https://validator.w3.org/#validate_by_input) and show students how we can validate our HTML code by pasting it into this tool.

  ![HTML Validate](Images/05-HTML-Validate.png)

  * The W3 Validator is a free tool offered by the World Wide Web Consortium, an international community that develops web standards.

  * This is a great tool to use to make sure our websites meet web standards. Had we used it for the last activity, we could have confidently worked through all of the errors and been sure nothing was missed.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2UGfI7a)</sub>

- - -

## 6. Working With Tables

| Activity Time:       0:35 |  Elapsed Time:      2:30  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 6.1 Instructor Do: Demonstrate Working With Tables (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slides 31 and 32 while demonstrating this lesson.

* Inform students that they'll often need to display tabular data they pulled from a spreadsheet or database. Lists just aren't going to cut it here.

* To accomplish this, we're going to use tables. We might have mentioned them during the HTML tags activity, but now students will be given a spreadsheet they'll use to create a table with HTML.

* Create a simple HTML table live for students. Make sure this table includes th, tr, and td elements. This doesn't need to be any more than 2 columns and a few rows for them to get the gist. Possible options might include:

  * A table of student names and their row numbers.

  * A table of student names and their favorite animal.

  * Try and have fun here!

  * Example:

  ![Table Example](Images/06-Table-Example.png)

* Make sure you explain the function of each element that goes into making a table. Show students your code, as well as the rendered table in the browser.

  * **table:** Acts as a container for our rows and columns.

  * **tr (Table Row):** These elements serve as rows for our table. They contain a row of table cells.

  * **th (Table Header):** These are table cells that are for containing column titles. These will have bold text by default.

  * **td (Table Data):** These are table cells for holding data. These are not column titles.

  * We also have a few other optional table tags that can be used to give semantic meaning to our table. These include:

    * **thead (Table Head):** Acts as a container for the row(s) holding our table headers.

    * **tbody (Table Body):** Acts as a container for the rows holding our table data that is not part of the table head.

    * **tfoot (Table Footer):** Acts as a container for bottom rows in a table which acts as a summary of the tables content. The `tfoot` element is rendered at the bottom of the table by default, regardless of which row(s) it's holding.

* Answer any questions before they start the next activity.

</details>

<details>
  <summary><strong>✏️ 6.2 Students Do: Working With Tables (0:15)</strong></summary>

* For this activity students will create an HTML5 table modeled from a spreadsheet. They will use the border and colspan properties, as well as make use of the `thead`, `tbody`, and `tfoot` elements.

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slides 33 and 34 to present this activity to the students.

  * **Instructions:** [Stu_Working_With_Tables](Activities/06-Stu_WorkingWithTables/README.md)

</details>

<details>
  <summary><strong>⭐ 6.3 Review: Working With Tables (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slide 35 to review this activity.

* As a class, review the solution file, [Stu_Working_With_Tables_Solved](Activities/06-Stu_WorkingWithTables/Solved/index.html).

* Show students how we can achieve the effect of bold text here by using th elements for our headers. We could technically use strong tags, but since we have elements already made for this specific purpose, it's better to use those instead.

* Show students how we can increase the width of a td or th element by using the colspan property. Some students may have thought to use empty td or th elements to create the empty space, but this wouldn't allow us to actually have content that spans multiple cells.

* Lastly point out the border property. Explain that this gives our table a border we can adjust the thickness of by increasing its value. We'll learn more advanced ways of doing this with CSS, but this is fine for now.

* Lastly point out the use of the thead, tbody, and tfoot elements. Explain that we can make a valid HTML table without these, but we add semantic meaning to the content inside of our table if we do, so we should try to whenever possible.

* Let students know that it would probably take them a long time to insert more than just a few rows from a spreadsheet or database into an HTML document in this way. It's important to become familiar with how different elements work together, but assure students that we're going to learn better, more programmatic methods of rendering HTML populated with external data. More on this next week!

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3dU3mjm)</sub>

- - -

## 7. More With Images and Links

| Activity Time:       0:30 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 7.1 Students Do: More With Images and Links (0:15)</strong></summary>

* For this activity, students will create a webpage using images downloaded from their Jupyter notes from a previous project.

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slides 36 and 37 to present this activity to the class.

  * **Instructions:** [Stu_Image_And_Links](Activities/07-Stu_ImageAndLinks/README.md)

</details>

<details>
  <summary><strong>⭐ 7.2 Review: More With Images and Links (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slide 38 to review this activity.

* Open the [Stu_Image_And_Links_Solved](Activities/07-Stu_ImageAndLinks/Solved/index.html) file in your browser and show students the finished page. Be sure to demonstrate how a new tab is opened in our browser whenever our image is clicked.

* Open the solution in your editor and show students how we can make the images clickable links by wrapping them in anchor tags. Instead of inserting text inside of anchor tags to be displayed as a hyperlink, we used an image instead.

* Point out the `article` and `section` tags. Explain to students that these are relatively new semantic elements we can use to group our content into related sections. These are optional, but it can help to organize our HTML into different parts. Explain that grouping related content makes our code more organized, can make styling specific elements with CSS easier, and can make our web pages more accessible to users with disabilities.

  * With a few different elements which behave the same on the page, it can sometimes be difficult to choose the appropriate semantic tag. HTML5 Doctor has an informative [flowchart](http://html5doctor.com/downloads/h5d-sectioning-flowchart.pdf) for deciding which semantic tag to use.

  * It's worth mentioning that the `div` element can also be used to divide content and behaves the same way the `article` and `section` elements do when rendered to the page. The `div` tag, however, doesn't have any semantic meaning and should be used only when no other semantic element is appropriate.

* Point out that we can make text italicized by using the `<em>` element. In additional to making text italicized, the `<em>` element has a semantic meaning as it marks text which has stress emphasis.

* Point out the use of `figure` and `figcaption` as a more semantic approach for these figures than articles. Mention that:

  * The `figure` element is intended to be used in conjunction with the `figcaption` element to mark up diagrams, illustrations, photos, and code examples (among other things).

* Answer any lingering questions before introducing the homework.

</details>

<details>
  <summary><strong>📣 TAs Do: Introduce the Homework (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1i-QXlNque9qS78xbqd7iMJbKkOlfIfAvsOXaERCsNMk/edit?usp=sharing) and use slide 39 while TAs present the homework to the students.

* Introduce this week's [homework assignment](../../../02-Homework/11-Web/Instructions/README.md).

* Answer any questions about the homework.

* Assure students that while they may not know everything they need to complete the assignment, they do know enough to get started today.

* If there's any time leftover, have students get a head start on this week's homework assignment!

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2JytzpI)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
