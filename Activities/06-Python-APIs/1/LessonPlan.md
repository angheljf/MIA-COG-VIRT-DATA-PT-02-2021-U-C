# 6.1 APIs

## Overview

Today's lesson introduces students to JSON traversal and the fundamentals of making API requests with the [requests library](http://docs.python-requests.org/en/master/), using the [OMDb](https://www.omdbapi.com/) and [New York Times](https://developer.nytimes.com/) APIs.

### Class Objectives

* Students will be able to make GET requests with `requests`.
* Students will be able to convert JSON into a Python dictionary.
* Students will read and apply API documentation.
* Students will sign up for and use an API key.

## Instructor Prep

<details>
  <summary><strong>Instructor Priorities</strong></summary>

* Students will make GET requests with the `requests` Library.

* Students will manipulate JSON response to retrieve necessary values.

* Students will store JSON response in python lists and dictionaries.

* Students will identify and generate the type of request needed to request movies by leveraging the OMDB API documentation.

</details>

<details>
  <summary><strong>Instructor Notes</strong></summary>

* The NYT API imposes rate limits on requests. It shouldn't interfere with instructor demonstrations or student exercises, but be aware of it as a potential source of errors.

* You will need to provide your own unique NYT API key for the instructor demonstration and the student activity.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-06-python-APIs) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

</details>

<details>
  <summary><strong>Sample Class Video</strong></summary>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=91755e9a-1567-422a-b60e-a93b01855609)

</details>

- - -

# Class Activities

## 1. Intro & Requesting SpaceX

| Activity Time:       0:25 |  Elapsed Time:      0:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Intro to APIs (5 mins)</strong></summary>

* Send out the [Student Guide](../StudentGuide.md) for students to use as a reference as they advance through this week's activities.

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o/edit#slide=id.g5bfb14603e_0_0) and use slides 1-6 to cover the first activity. Be sure to cover the following:

* Welcome the class and let them know that the today's lesson will focus on making API calls.

* Explain that a **client** is the application/device that _asks_ for information.

* Explain that a **server** is an application/device that _supplies_ the information to the client.

  * As an analogy, give the example of a doctor asking for a patient's medical records. The doctor _requests_ information, so they are the **client** in this case. The hospital _provides_ the information and thus could be seen as the **server**. The medical records themselves are the _information_ requested.

* Ask the class the following questions:

  * Has anyone heard of the term API before?

  * Can anyone define what an API is?

* Explain that API stands for Application Programming Interface.

  * An API allows for clients and servers to communicate using their own language.

  * In the most simple case, an API allows for a client device to make a request to a server and then decipher the response.

* Show the students the [API call diagram](Images/01-APIIntro_Diagram.png) to provide an illustration of the concept.

  ![API Call Diagram](Images/01-APIIntro_Diagram.png)

* Point out how, in the diagram, the client only _requests_ information, which the server then provides.

* Explain that an API call that focuses on retrieving data is called a **get request**.

  * There are other ways for clients to interact with servers but that these methods are not necessary for today's activities.

  * API get requests are not all that different than simply visiting a website manually. Often times an API will use a URL to communicate, and the client will use a program to collect some data from the page.

* You may either show the students the example JSON in the slide deck, or visit the [JSON Placeholder page](https://jsonplaceholder.typicode.com/posts/) and explain the contents of the webpage to the class.

  ![JSON Example](Images/01-APIIntro_JSON.png)

  * This webpage acts as an example of a JSON file that would be returned by an API call. Tell students not to worry about the formatting or syntax of this object at the moment.

  * The URL is no different from the URLs students are used to using to visit "normal" websites.

  * Explain that the URLs used to communicate with APIs are often called **endpoints**.

  * Explain that the text inside of the web browser is _identical_ to what a client script would receive when making a call to this endpoint.

* Explain that the de facto standard library for making API calls in Python is [requests.py](http://docs.python-requests.org/en/master/)

* Before the next activity, you may want to direct students to a JSON formatter extension offered by the Chrome Web Store: <https://chrome.google.com/webstore/search/json%20formatter>.

</details>

<details>
  <summary><strong>📣 1.2 Instructor Do: Intro to Requests (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o) and use slides 7-9 to accompany the beginning of this demonstration.

* Explain that for this class we will use Python's `requests` library to interact with web servers.

  * The `requests.get()` function is used to interact with a URL-based API query. It navigates to the URL and then attempts to retrieve the response from the webpage.

  * In most cases we can expect the `requests.get()` function to return a `response` object that contains the JSON (or some other highly-parsable text format) response from the API.

  * In order to interpret and analyze the `response` object we will use the `.json()` function to interact with our other Python libraries.

* Open [01-Ins_RequestsIntro/Ins_Requests_Demo.ipynb](Activities/01-Ins_RequestsIntro/Solved/Ins_Requests_Demo.ipynb) in Jupyter Notebook and go through the code with the class.

  * `import requests` to pull the Requests library into Python. This will allow the code to make API calls and collect data from a server.

  * `import json` allows Python to pull in and parse JSON objects.

  * The `url` variable contains the SpaceX URL that the class visited within a string.

  * Explain that `requests.get(url)` sends a GET request to the URL passed as a parameter. Remind students that this means that the program is _requesting_ the information stored at this URL.

    ![Basic Call](Images/01-RequestsIntro_BasicCall.png)

  * Explain that `requests.get(url)` returns a response object containing much information about the server's response, but does not seem to include the JSON requested.

    ![Response Object](Images/01-RequestsIntro_ResponseObject.png)

  * The `.json()` call must be used to convert the response object received into the JSON format seen earlier in the browser.

  * Point out how the JSON response is contained within one massive block of text. This makes it very hard to understand or read through. To counteract this, the `json.dumps()` method can be used to "pretty print" the response.

    ![Pretty Print](Images/01-RequestsIntro_PrettyPrint.png)

</details>

<details>
  <summary><strong>✏️ 1.3 Students Do: Requesting SpaceX (10 mins)</strong></summary>

* **File:** [02-Stu_SpaceX-Request/Stu_SpaceX.ipynb](Activities/02-Stu_SpaceX-Request/Unsolved/Stu_SpaceX.ipynb)

* **Instructions:** [Activities/02-Stu_SpaceX-Request/README.md](Activities/02-Stu_SpaceX-Request/README.md)

* This activity has students dig into a rather simple and well-documented API - The SpaceX API - and asks them to make a couple calls to the API using the Requests library.

* Open up [02-Stu_SpaceX-Request/Stu_SpaceX.ipynb](Activities/02-Stu_SpaceX-Request/Solved/Stu_SpaceX.ipynb) in Jupyter Notebook or show the students the following image to give them an idea of how the output should look.

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o) and use slides 10-13 to display the instructions and examples JSON response.

</details>

<details>
  <summary><strong>⭐ 1.4 Review: Requesting SpaceX (5 mins)</strong></summary>

* Open up [02-Stu_SpaceX-Request/Stu_SpaceX.ipynb](Activities/02-Stu_SpaceX-Request/Solved/Stu_SpaceX.ipynb) in Jupyter Notebook and run through the code with the class line-by-line, making certain to hit upon the following points.

  * While it is not required to "pretty print" the JSON response, it does make it a lot easier to understand. This means using `json.dumps()` and passing the formatting parameters desired.

    ![SpaceX Code1](Images/02-SpaceX_Code1.png)

  * To modify an API call to search for a single ID, use concatenation or string substitution to build the correct URL.  Here,   it is done in the `requests.get()` method.

    ![SpaceX Code2](Images/02-SpaceX_Code2.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2R5kfO1)</sub>

- - -

## 2. Requesting a Galaxy Far Far Away

| Activity Time:       0:25 |  Elapsed Time:      0:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Manipulating Responses (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o) and use slides 14-16 to accompany the beginning of this demonstration.

* Point out that the solution to the previous activity used the API responses immediately by printing the JSON to the screen.

* The JSON response can be saved within a variable, however, allowing the application to refer to the dictionary multiple times and inspect its properties.

  * JSON is structurally similar to Python's dictionaries as both of these data formats use "key" and "value" pairings.

* Open [03-Ins_ManipulatingResponses/Ins_Manipulating_JSON.ipynb](Activities/03-Ins_ManipulatingResponses/Solved/Ins_Manipulating_JSON.ipynb) within an IDE and run through the code with the class.

  * So long as a response has been parsed using `response.json()` it becomes possible to navigate through and collect values like one would a dictionary.

    ![Manipulating JSON - SavingJSON](Images/03_ManipulatingResponses_SavingJSON.png)

  * Point out how the application accesses the value stored within the "cost_per_launch" key using `["cost_per_launch"]`.

    ![Manipulating JSON - CostResponse](Images/03_ManipulatingResponses_CostResponse.png)

  * Both Python dictionaries and JSON objects can contain dictionaries within dictionaries. To access the data stored within these sub-dictionaries, simply pass the parent key within brackets and then follow it up with the child key in a second set of brackets. In this case, since there is an array of sub-dictionaries, you must also use the index of the subdictionary before passing the child key.

    ![Manipulating JSON - PayloadResponse](Images/03_ManipulatingResponses_PayloadResponse.png)

</details>

<details>
  <summary><strong>✏️ 2.2 Students Do: Requesting a Galaxy Far Far Away (15 mins)</strong></summary>

* **File:** [Stu_FarFarAway.ipynb](Activities/04-Stu_FarFarAway-APIData/Unsolved/Stu_FarFarAway.ipynb)

* **Instructions:** [04-Stu_FarFarAway-APIData/README.md](Activities/04-Stu_FarFarAway-APIData/README.md)

* Students will now create an application that accesses data from the Star Wars API and prints out values from within it.

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o) and use slides 17–20 to accompany this activity. Otherwise, show the students what chart they will be attempting to create.

  ![FarFarAway - Output](Images/04-FarFarAway_Output.png)

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Far Far Away API Request (5 mins)</strong></summary>

* Open up [04-Stu_FarFarAway-APIData/Stu_FarFarAway.ipynb](Activities/04-Stu_FarFarAway-APIData/Solved/Stu_FarFarAway.ipynb) in Jupyter Notebook and run through the code with the class line-by-line, making certain to hit upon the following points.

  * Printing out the original JSON is critical to understanding what keys and values an application should collect. It is also a crucial part of what is known as "Test Driven Development" as it allows the programmer to know what their outputs should be.

  ![04-FarFarAway - JSON](Images/05-FarFarAway_JSON.png)

  * To collect the character's name, reference the `["name"]` key and store it within a variable for later.

  * To collect the number of films a character has been in, reference the `["films"]` key and collect the length of the list it returns.

  * To collect the name of the character's first starship, reference the `["starships"]` key and the value at the index of `[0]`. This returns a URL to use in a second API call. The name of the starship will be held within the `["name"]` key of this JSON object.

    ![04-Far Far Away - Code](Images/05-FarFarAway_Code.png)

* Ask the class how they would go about solving the bonus.

  * Loop through the `["films"]` list and run an API call for each value within the list. Then, from the JSON returned, collect the `["title"]` and append them into a list.

  ![04-Far Far Away - CodeBonus](Images/05-FarFarAway_Bonus.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2ytMVtO)</sub>

- - -

## 3. Number Facts

| Activity Time:       0:25 |  Elapsed Time:      1:15  |
|---------------------------|---------------------------|

<details>
  <summary><strong>👥 3.1 Partners Do: Number Facts - API Application (20 mins)</strong></summary>

* **File:** [05-Par_NumberFacts-APIApplication/Par_NumberFacts.ipynb](Activities/05-Par_NumberFacts-APIApplication/Unsolved/Par_NumberFacts.ipynb)

* **Instructions:** [05-Par_NumberFacts-APIApplication/README.md](Activities/05-Par_NumberFacts-APIApplication/README.md)

* Students will now join forces in creating an interactive application that uses the "numbers" API. The application will take in a number and then return a random fact about that number.

* Open up [05-Par_NumberFacts-APIApplication/Par_NumberFacts.ipynb](Activities/05-Par_NumberFacts-APIApplication/Solved/Par_NumberFacts.ipynb) in Jupyter Notebook and run the application, showing students what they will be attempting to create.

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o) and use slides 21–23 to accompany this activity. Otherwise, show the students what chart they will be attempting to create.

  ![Number Facts - Output](Images/06-NumberFacts_Output.png)

</details>

<details>
  <summary><strong>⭐ 3.2 Review: Number Facts (5 mins)</strong></summary>

* Open up [05-Par_NumberFacts-APIApplication/Par_NumberFacts.ipynb](Activities/05-Par_NumberFacts-APIApplication/Solved/Par_NumberFacts.ipynb) in Jupyter Notebook and run through the code with the class line-by-line, making certain to hit upon the following points.

  * The URL format for the Numbers API is `http://numbersapi.com/<Number>/<Type>?json` unless the "Date" type is being used. If the "Date" type is used then the format is `http://numbersapi.com/<Month>/<Day>/<Type>?json`.

  * Since the API call for "Date" is different from the rest, an `if` statement should check what type of data the user would like to search for. This way the API call can be changed based upon their choice.

    ![Number Facts - Code](Images/06-NumberFacts_Code.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2UV7KpF)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:30  |
|---------------------------|---------------------------|

- - -

## 4. OMDb Movie Questions

| Activity Time:       0:40 |  Elapsed Time:      2:10  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: OMDb API (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o) and use slides 25-28 to accompany the beginning of this demonstration. Be sure to cover the following talking points:

  * After having spent some time working with simple JSON objects, students are now ready to tackle handling JSON responses from more complex APIs.

  * The next couple of exercises will make use of the [OMDb API](https://www.omdbapi.com/) and send out the link.

  * One of the biggest differences of the OMDb API from our previous API examples is the format of the URL. In this case we will have to use URL parameters.

  * The two basic parameters used in the OMDb API get request are `?t=` and `api_key`.

  * Explain that the `t` within the URL string stands for "title". This means that the URL `http://www.omdbapi.com/?t=Aliens` is asking the omdb API to return all of the information on movies with the title "Aliens."

  * Explain that the section of the URL following such a question mark is called a **query string**.

  * Query strings are a way of sending information from the client to the server, which the server can then interpret to return more specific data.

    ![OMDB Query String](Images/07-OmdbIntro_Query.png)

  * The query string also includes something known as an "API Key" at the end. API keys are used by developers to collect data from APIs with some layers of protection on them. Without a valid API key for the omdb API, for example, no data would be returned.

* Open the [06-Ins_OMDbRequests/Ins_OMDbRequests.ipynb](Activities/06-Ins_OMDbRequests/Solved/Ins_OMDbRequests.ipynb) demo in Jupyter Notebook.

* Point out that this looks nearly identical to the API calls students have been working with. The URL for the API is stored before an API call is made. The response is then stored and converted to JSON. The keys are then printed via dictionary access.

* Point out that, other than the query string, there is nothing new here—students are now capable of interacting with complex real-world APIs!

  ![OMDB Print](Images/07-OmdbIntro_Print.png)

</details>

<details>
  <summary><strong>✏️ 4.2 Students Do: Study the OMDb API (5 mins)</strong></summary>

* **Instructions:** [07-Stu_Explore_OMDb_API/README.md](Activities/07-Stu_Explore_OMDb_API/README.md)

* For this first part of the OMDB activity, students will be spending some time reviewing the documentation for the OMDB API and testing it out.

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o) and use slides 29-30 to display the instructions.

</details>

<details>
  <summary><strong>✏️ 4.3 Students Do: Movie Questions (20 mins)</strong></summary>

* **File:** [08-Stu_MovieQuestions/Stu_MovieQuestions.ipynb](Activities/08-Stu_MovieQuestions/Unsolved/Stu_MovieQuestions.ipynb)

* **Instructions:** [08-Stu_MovieQuestions/README.md](Activities/08-Stu_MovieQuestions/README.md)

* The class will now test their skills with the OMDB API as they attempt to collect some data from the API in order to answer a series of questions.

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o) and use slides 31-33 to display the instructions.

</details>

<details>
  <summary><strong>⭐ 4.4 Review: Movie Questions (5 mins)</strong></summary>

* Open up [08-Stu_MovieQuestions/Stu_MovieQuestions.ipynb](Activities/08-Stu_MovieQuestions/Solved/Stu_MovieQuestions.ipynb) in Jupyter Notebook and run through the code with the class line-by-line, making certain to hit upon the following points.

  * Point out that this activity did _not_ require the use of query string parameters other than `t`.

  * Point out that each response contains a full swath of information for each movie by default. This activity could be solved by simply dumping the JSON and identifying the right key to retrieve.

    ![Movie Questions - Code](Images/08-MovieQuestions_Code.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2UD0AY4)</sub>

- - -

## 5. Iterative Requests

| Activity Time:       0:20 |  Elapsed Time:      2:30  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 5.1 Instructor Do: Iterative Requests (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o) and use slides 34-37 to accompany the beginning of this demonstration.

* Point out that the APIs the class has worked with so far have provided all the information needed from single requests.

* Explain that, sometimes, APIs will only respond with _some_ of the information needed on each request made.

  * It's common, for instance, for APIs to send a limited amount of data in response to each call.

  * The New York Times API for retrieving articles, for instance, only returns 10 at a time. In this case, if a programmer wanted to retrieve 30 articles, they would have to make 3 API calls.

* Explain that API calls can be made _iteratively_ by sending GET requests out from within a loop.

* Point out that an application may want to retrieve a small subset of articles with non-sequential IDs. For example, a user might want to see the posts whose IDs are 3; 89; and 74.

  * It would be wasteful to retrieve all 100 records, take the three that are desired, and throw away the rest. Rather, the application should request _only the articles needed_ and nothing more.

  * Explain that this can be done by storing the IDs desired within a list and then making an API call inside a loop for each ID inside of the list.

* Open [09-Ins_IterativeRequests/Ins_IterativeRequests.ipynb](Activities/09-Ins_IterativeRequests/Solved/Ins_IterativeRequests.ipynb).

  * Explain that the line containing `random.sample` simply generates a list of random IDs between 1 and 100 to request from the API.

  * Reassure students that they don't need to focus on this line just yet. This code is for generating data but is not related to iterative API requests per se.

  * Explain that the for loop makes a request to the API for each ID in the list and stores the response in `response_json`.

    ![Iterative Requests - Code](Images/09-IterativeRequests_Code.png)

* Run the sample code a couple of times and draw attention to the command-line output. Point out that the IDs are indeed random on each execution of the script.

</details>

<details>
  <summary><strong>✏️ 5.2 Students Do: Iterative Requests (10 mins)</strong></summary>

* **File:** [10-Stu_MovieLoop/Stu_MovieLoop.ipynb](Activities/10-Stu_MovieLoop/Unsolved/Stu_MovieLoop.ipynb)

* **Instructions:** [10-Stu_MovieLoop/README.md](Activities/10-Stu_MovieLoop/README.md)

* The class will now test their knowledge of iterative requests by looping through a list of movies and collecting data from the OMDB API on each movie.

* Explain to students that the next activity requires them to loop through a given list and return information about that list. You may also want to show them the image below to help them visualize the expected output.

  ![Movie Loop - Output](Images/10-MovieLoop_Output.png)

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o) and use slides 38-41 to display the instructions and sample output.

</details>

<details>
  <summary><strong>⭐ 5.3 Review: Activity (5 mins)</strong></summary>

* Open up [10-Stu_MovieLoop/Stu_MovieLoop.ipynb](Activities/10-Stu_MovieLoop/Solved/Stu_MovieLoop.ipynb) in Jupyter Notebook and run each cell after having students explain the code.

  ![Movie Loop - Code](Images/10-MovieLoop_Code.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3bRoCEF)</sub>

- - -

## 6. Retrieving Articles

| Activity Time:       0:30 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 6.1 Instructor Do: NYT API (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o) and use slides 42- to accompany the beginning of this demonstration.

* Explain that the final activity for the day will be an exercise in exploring yet another, fully-featured, "real-world" API; the New York Times article API.

* Explain that up until this point in time we have been using APIs that do not require an API key. However the NYT article API does requires its user to register for an API key.

  * Walk through the process of acquiring an API key with the class.

  * First create an account with NYT by filling out this [form](https://developer.nytimes.com/accounts/create).

  ![NYT Create Account](Images/11-NYT_account.png)

  * Navigate to the index of the email used to sign-up and activate the account.

  * **Note:** Make sure to have students check their spam folder for the email from New York Times article API.

  * Navigate back the [sign in page](https://developer.nytimes.com/accounts/login) and login with the newly created account.

* Once students have successfully made a NYT account and logged in, it's time to create an app and obtain an API KEY.

  * From the drop down on the top right next to their email, click on apps.

  ![select apps](Images/11-select_apps.png)

  * Click on **+NEW APP**.

  * This will bring you to app creation page. Give the app any name.

  ![Name app](Images/11-NYT_name_app.png)

  * Scroll down to the **Article Search API** and select it.

  ![Article API](Images/11-article_api.png)

  * Scroll back up to the top and click **CREATE**.

* After the app is created, you will be re-directed to the app page, which contains the API key. Explain to students that they will use this key to interact with the NYT API.

  ![NYT API Key](Images/11-NYT_api_key.png)

* Send out the [documentation](https://developer.nytimes.com/docs/articlesearch-product/1/overview) for the NYT API and give a brief overview of some of its features.

    ![NYT Docs](Images/11-NYTApi_Docs.png)

  * Try not to delve too deeply into the documentation, however, as part of the next activity should have students reading through it in order to uncover the query strings they need to create.

* Explain that it is always a better idea to save your API keys in a separate config file from the scripts that use them.

  * This adds security to your scripting/ programming by dissociating your personal information from your analysis

  * As an added bonus you can add all of your API keys from different sites into a single config file that your different API query scripts point to

* Point out that it is critical to never publish your config files/ API keys on Github.

  * Many sites have a bandwidth limit that can be easily exceeded if more than one user uses a single API key. Additionally, some sites charge the user for each query.

* Open the [11-Ins_NYTAPI/Ins_NYT_API.ipynb](Activities/11-Ins_NYTAPI/Solved/Ins_NYT_API.ipynb) demo within an IDE and then run the application while explaining each part of the code.

  * Highlight the use of the `config.py` file to store the `api_key`, and discuss that it is good practice to not upload API keys to GitHub.  While this API key is free, some services charge past a certain usage point.  Therefore, students should protect them from public view.  Discuss with students that they should add `config.py` to their `.gitignore` file or create environment variables for all homework and projects they will be saving to a repo.

  ![NYT API Code](Images/11-NYTApi_Code.png)

</details>

<details>
  <summary><strong>✏️ 6.2 Students Do: Retrieving Articles (20 mins)</strong></summary>

* **File:** [12-Stu_RetrieveArticles/Stu_Retrieve_Articles.ipynb](Activities/12-Stu_RetrieveArticles/Unsolved/Stu_Retrieve_Articles.ipynb)

* **Instructions:** [12-Stu_RetrieveArticles/README.md](Activities/12-Stu_RetrieveArticles/README.md)

* Students will now create an application that grabs articles from the NYT API, stores them within a list, and prints snippets of the articles to the screen.

* Open up [12-Stu_RetrieveArticles/Stu_Retrieve_Articles.ipynb](Activities/12-Stu_RetrieveArticles/Solved/Stu_Retrieve_Articles.ipynb) within the console and run the application, showing students what they will be attempting to create.

  ![Retrieve Articles - Output](Images/12-RetrieveArticles_Output.png)

* Open the [slideshow](https://docs.google.com/presentation/d/1k8c_LxO7rKmMOPkAZkmw0BqBk5UHZCPn-Y9qTgGXd0o) and use slides 47-50 to display the instructions and sample output.

</details>

<details>
  <summary><strong>⭐ 6.3 Review: Activity (5 mins)</strong></summary>

* Open up [12-Stu_RetrieveArticles/Stu_Retrieve_Articles.ipynb](Activities/12-Stu_RetrieveArticles/Solved/Stu_Retrieve_Articles.ipynb) in Jupyter Notebook and run through the code with the class line-by-line, making certain to hit upon the following points.

  * Ask different students to explain their solutions for each bullet point of the Instructions.

  * Focus on explaining the various query parameters used to build the query URL. These include:

  * `api-key`, the parameter that allows the code to query the server

  * `q`, for the keyword to **q**uery on

  * `begin_date` and `end_date`, both with format YYYYMMDD

* Point out that the remainder of the activity is similar to activities students completed before — the major difference is that they had to dig through documentation to find the right keys to use for this one.

  ```python
  # Dependencies
  import requests
  import time
  from config import api_key

  url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"

  # Store a search term
  query = "obama"

  # Search for articles published between a begin and end date
  begin_date = "20160101"
  end_date = "20160130"

  query_url = f"{url}api-key={api_key}&q={query}&begin_date={begin_date}&end_date={end_date}"

  # Retrieve articles
  articles = requests.get(query_url).json()
  articles_list = articles["response"]["docs"]

  # Print out retrieved articles
  for article in article_list:
    	print(f'A snippet from the article: {article["snippet"]}')
    	print('---------------------------')
  ```

* Briefly explain the solution to the bonus.

  * Explain that each API call retrieves 10 articles by default. Each group of articles is called a _page_.

  * If we want more articles, we need to tell the API to respond with _different pages_.

  * To do this, we simply append a `page` parameter, which is equal to the number of the page we want to retrieve.

  * Point out that sending requests like this often exceeds the rate limit for free-tier users.

  * Explain that a **rate limit** is a way for an API to throttle the number of requests a given application can make, in order to prevent abuse or server overload.

  * **Note**: Warn students not to print the query URLs with their key included; this would jeopardize their key if pushed to a public repository.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3dQXYNK)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
