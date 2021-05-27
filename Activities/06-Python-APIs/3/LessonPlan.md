# 6.3 APIs and Geospatial Data Visualization

## Overview

In this class, students will be introduced to the Google Maps and Places API as well as Jupyter gmaps. Using these new tools, along with data from the US Census, students will be tasked with creating visualizations to capture the socioeconomic trend of [banking deserts](http://www.theatlantic.com/business/archive/2016/03/banking-desert-ny-fed/473436/).

### Class Objectives

* Students will be able to successfully use the Google Maps and Places API to obtain information about geographic areas.
* Students will understand how to use the Census API wrapper.
* Students will understand the concept of rate limits and the importance of creating "test cases" prior to running large scripts.
* Students will have a firmer understanding of how to dissect new API documentation.
* Students will be able to visually represent data on a map with Jupyter Gmaps.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* You may find that this lesson falls on a weekday due to a holiday shifting the course schedule. In this case, we have provided notes within the LP that will allow you to **easily adjust the length of the lesson to fit into a weekday class**.

  * Be on the lookout for a **3-Hour Adjustment** note at the top of activities in this Lesson Plan. If this class is being taught on a weekday, please utilize the directions found in the note. Keep in mind that breaks will be reduced from 40 minutes to the typical 15 minutes for a weekday class as well.

  * Shortening these activities could potentially limit the students' ability to finish them, so please remind them to utilize office hours to clear up any questions they may have.

* Today's class is a fun one! In this class, students take on the role of social scientists and are tasked with using their newfound programming skills and API insights to visualize a real-world phenomenon: banking deserts.

* What _is_ a banking desert? In predominantly lower-income or elderly neighborhoods, there is often a dearth of banks. In their place is an abundance of high-interest "check-cashing" and "money transfer" providers. These shifty providers benefit from the fact that banks avoid such neighborhoods, leaving residents with few safe options to obtain cash, loans, or withdrawal services. To showcase this trend, students will use a dataset obtained from the US census that lists the socioeconomic factors (population, median age, household income, poverty rate, etc.) of each zip code in the country. They will then need to create code that randomly selects 700 zip codes and uses Google Places to identify the number of banks present within a 5 mile radius of that zip code. Finally, they will plot the relationship between "bank count" and  socioeconomic factors.

* Leading up to this exercise, you as Instructors and TAs will be responsible for teaching students how to correctly use the Google Geocoding and Places APIs — along with how to use them in combination. Today's class is also important, because these APIs will be useful tools in students' upcoming projects.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-06-python-APIs) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Have your TAs reference the [6.3-TimeTracker](TimeTracker.xlsx) to help keep track of time during class.

* **Note**:  The API keys used throughout this lesson have been disabled and will have to be replaced with active keys.

</details>

<details>
  <summary><strong>Sample Class Video</strong></summary>

* To view an example class lecture visit (Note video may not reflect latest lesson plan):

[Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=0fd1cd27-0c6b-4525-b1a7-aa1200e303b0)

</details>

- - -

# Class Activities

## 1. Google Maps and Places

| Activity Time:       0:45 |  Elapsed Time:      0:45  |
|---------------------------|---------------------------|

<details>
  <summary><strong>🎉 1.1 Everyone Do: Demonstrate Google Maps / Places (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1TSi886_pX1_naQAB89-vIr_fDIaNpJQN_2HFMNeJxic) and use slides 1–2 to cover today's class objectives.

* Use slides 2-6 to accompany the beginning of this demonstration.

* Explain to students that, for the remainder of class, they will be working with the Google Maps and Places API. Let them know that this section is critical and may confuse them if they lose focus.

* Begin your discussion by opening the URL for the [Google Maps API](https://developers.google.com/maps/) and [Google Places API](https://developers.google.com/places/).

  * Google has made available some of the vast set of tools that power Google Maps, such that any developer can utilize the same technologies and datasets in their own applications.

  * At a basic level, these APIs allow developers to quickly convert locations into latitudinal and longitudinal coordinates, identify nearest restaurants to a given location, determine the distance between two points, and much more!

  * For the purposes of today's class, students will ultimately be using the data from Google Maps and Places to determine the number of banks in a given zip code and then compare those counts to socioeconomic factors associated with zip code.

* Once students have the picture in mind, show them how they can go about obtaining their own API key.

  * Start off by clicking the `Get Started` button on the [Google Maps Platform](https://cloud.google.com/maps-platform/) webpage.

  * Select the boxes for the `Maps` and `Places` products.

  * At this point, click Create a New Project and give the project a name. Once that has been done, click Create Billing Account. Explain that while Google now charges for services, a $200 credit is provided for these API services.

  * Warn students that any API usage beyond the $200 credit will be charged to their personal accounts. Send out a link to Google's billing page as a reference, and explain that API usage limits and billing alerts can be setup so that the free credit is not exceeded.

    * Navigate through the Acceptances to try the cloud platform, then complete the next form to establish a Google Cloud Platform account.

    * The following windows will automatically enable the Google Maps Platform. Once complete, a window containing a unique API key will appear. Copy this key for use in Python.

  * Send out the [Capping Queries](Activities/Resources/Capping_Queries.md) document to set query limits for API usage.

    * You can begin following the document from step 3 if you have not navigated away from your list of active APIs.

    ![API List](Images/API_List.png)

</details>

<details>
  <summary><strong>📣 1.2 Instructor Do: Google Geocode (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1TSi886_pX1_naQAB89-vIr_fDIaNpJQN_2HFMNeJxic) and use slides 7–10 to accompany the beginning of this demonstration.

  * Now that everyone has an API Key (Congratulations!), it is time to start using it!

* To begin, show students how to utilize the Google Maps Geocoding API to turn addresses into latitudinal and longitudinal coordinates.

  * This process of converting an address to coordinates is called **geocoding**.

  * Since many APIs only understand locations formatted in terms of latitude/longitude, geocoding will be very valuable in translating addresses into data that APIs - like the Google Places API - can understand.

* At this point, either open [Google_Geocode.ipynb](Activities/01-Ins_Google_Geocode/Solved/Google_Geocode.ipynb) in Jupyter Notebook explaining the code in sequence, or live-code the script.

  * Utilize the API key from  `config.py`.

    * Google's API is not free and if credit card information is provided, they charge past a certain usage point. Here is a good time to again stress to students that they avoid pushing their API key to github by using adding the `config.py` to their `.gitignore` file or using environment variables.

  * Build the endpoint URL.

    * Remind students that printing the url will also expose their key. While it is useful for demonstration purposes here, it should be avoided in projects and homework.

  * Run a Python request on the URL.

  * Explore the resulting JSON in a pretty printed format.

  * Extract the components of the JSON we desire.

  * Format the results for printing.

    * This may be the first time students have seen string formatting using %s. Explain to them that `%s` can be used to substitute a string variable. After closing the quotations, the expression must be followed by `%` and then a tuple of string variables to be substituted respectively into each occurrence of `%s`.

    ![Images/03-Geocoding.png](Images/03-Geocoding.png)

* Once complete, take a moment to visit the [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/start) documentation page and show students that the code created is effectively the same as what's expressed in the documentation.

  * Let them know that it's easy to be intimidated by code documentation but with a little practice it becomes simple to comprehend.

</details>

<details>
  <summary><strong>📣 1.3 Instructor Do: Google Places (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1TSi886_pX1_naQAB89-vIr_fDIaNpJQN_2HFMNeJxic) and use slides 11–13 to accompany the beginning of this demonstration.

* Feel free to open up the [Google Places API](https://developers.google.com/maps/documentation/javascript/places#place_searches) and walk students through the documentation for a few minutes.

  * The points to emphasize are: [Nearby Search](https://developers.google.com/places/web-service/search#PlaceSearchRequests), [Text Search](https://developers.google.com/places/web-service/search#TextSearchRequests), and [Place Search](https://developers.google.com/places/web-service/search#RadarSearchRequests).

  * When using each of the different types of searches, there are expected inputs such as Latitude, Longitude or Radius. Additionally there are various optional parameters including: keyword, minPrice, maxPrice, type, etc.

  * It may also be beneficial to point out the various [types](https://developers.google.com/places/supported_types) Google categorizes by default. Students will be using the "bank" type later in the day when they start creating visualizations for Banking Deserts.

* Once students have a decent enough understanding of the API, open up [Google_Places.ipynb](Activities/02-Ins_Google_Places/Solved/Google_Places.ipynb) in Jupyter Notebook and explain the code.

  * For the most part, the code is similar to the earlier example. The base URL, however, has changed since the class is now using the Google Place Search API.

  * In this example, we are using a feature of the [requests library](http://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls) in order to easily construct our url by passing in a dictionary of parameters.

  * During the discussion of this example, point out the various URL parameters like `keyword`, `location`, and `types`. Also point out the different JSON structure that is provided back to the user.

    ![Images/04-Places.png](Images/04-Places.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/39CIN7x)</sub>

- - -

## 2. Google Drills

| Activity Time:       0:20 |  Elapsed Time:      1:05  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 2.1 Students Do: Google Drills (0:15)</strong></summary>

* ⏰ **3-Hour Adjustment**: Skip this **Students Do** activity and continue on to the review activity.

* The class will now create some code that makes calls to both the Google Places and Google Geocoding APIs.

* **File:** [Google_That.ipynb](Activities/03-Stu_Google_Drills/Unsolved/Google_That.ipynb)

* **Instructions:** [README.md](Activities/03-Stu_Google_Drills/README.md)

* The class will now create some code that makes calls to both the Google Places and Google Geocoding APIs.

* Send out the starter file for [Google_That.ipynb](Activities/03-Stu_Google_Drills/Unsolved/Google_That.ipynb) and open in Jupyter Notebook in order to explain the instructions to students.

* Open the [slideshow](https://docs.google.com/presentation/d/1TSi886_pX1_naQAB89-vIr_fDIaNpJQN_2HFMNeJxic) and use slides 14–16 to display the activity's instructions.

</details>

<details>
  <summary><strong>⭐ 2.2 Review: Google Drills (5 mins)</strong></summary>

* ⏰ **3-Hour Adjustment**: This review activity is now an **Everyone Do**.

  * Spend only 10 minutes on this activity.

  * Use the review section as guidance for talking points as you live-code along with the students.

  * Be sure to take your time and answer all student questions along the way.

* Open up [Google_That.ipynb](Activities/03-Stu_Google_Drills/Solved/Google_That.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, making certain to hit upon the following points.

  * For the most part, the solution to these drills are self-explanatory. The only notable differences are that, in the last two drills, students would need to use a "Keyword Search" and a "Text Search". Both of these search types are articulated in the Google Places documentation.

  * Keyword Search

    ![Images/05-GoogleThat.png](Images/05-GoogleThat.png)

  * Text Search

    ![Images/05-GoogleThat2.png](Images/05-GoogleThat2.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/39CIQ3d)</sub>

- - -

## 3. Google Complex (Airport)

| Activity Time:       0:30 |  Elapsed Time:      1:35  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: Nearest Restaurants (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1TSi886_pX1_naQAB89-vIr_fDIaNpJQN_2HFMNeJxic) and use slides 17–19 to accompany the beginning of this demonstration.

* Remind students that last class we learned how to make multiple queries and handle missing data using try/except and list comprehension.

  * Another way to build out an API dataset is to use pandas.

* Explain that we can use Pandas's `iterrows()` and `.loc` methods to find the closest restaurant of each type and store them in a data frame.

* Point out that just was we did last class, we will need to encapsulate our parsing logic using try/except blocks to allow for the API queries to continue when there are missing values.

* Open [NearestRestr.ipynb](Activities/04-Ins_NearestRestr/Solved/NearestRestr.ipynb) and explain the code to students while highlighting the following:

  * Set up empty columns to for values retrieved from API.

    ![00-NearestRestr1.png](Images/00-NearestRestr1.png)

  * `iterrows()` iterates through each row of the dataframe returning an index number and the contents of each row. Those row values can then be individually accessed using the column label like so `row['column label']`.

  ```python
  # use iterrows to iterate through pandas dataframe
  for index, row in types_df.iterrows():
  ```

  * In each iteration, the `keyword` value is overwritten to be the new target.

  ```python
  # get restaurant type from df
  restr_type = row['ethnicity']

  # add keyword to params dict
  params['keyword'] = restr_type
  ```

  * To retrieve `results` if it exists, we use `requests.get`. This works by sending a get request to the API by passing in the `base_url` and an optional parameter: `params`. This `params` parameter will then take the dictionary and send it to the query string for the request. The result of the request is then converted to a JSON.

  ```python
  # assemble url and make API request
  print(f"Retrieving Results for Index {index}: {restr_type}.")
  response = requests.get(base_url, params=params).json()

  # extract results
  results = response['results']
  ```

  * We use try/except block to attempt to retrieve the `name`, `vicinity`, `price_level` and `rating` from the request results. If the results don't contain any of these values a KeyError or IndexError will occur and trigger the except clause to run, but allow the code to keep running.

  * If no error occurs, then `.loc` is used to update the cells with the desired information from the results.

  ```python
  try:
      print(f"Closest {restr_type} restaurant is {results[0]['name']}.")

      types_df.loc[index, 'name'] = results[0]['name']
      types_df.loc[index, 'address'] = results[0]['vicinity']
      types_df.loc[index, 'price_level'] = results[0]['price_level']
      types_df.loc[index, 'rating'] = results[0]['rating']

  except (KeyError, IndexError):
      print("Missing field/result... skipping.")

  print("------------")
  ```

</details>

<details>
  <summary><strong>👥 3.2 Partners Do: Google Complex (Airport) (20 mins)</strong></summary>

* ⏰ **3-Hour Adjustment**: Skip this **Partners Do** activity and continue on to the review activity.

* **Files:**

  * [Airport_Ratings.ipynb](Activities/05-Stu_Google_Complex/Unsolved/Airport_Ratings.ipynb)

  * [Cities.csv](Activities/05-Stu_Google_Complex/Resources/Cities.csv)

* **Instructions:** [README.md](Activities/05-Stu_Google_Complex/README.md)

* In this activity, they will be tasked with obtaining the rating of every airport in the top 100 metropolitan areas according to Google Users. They will be given a list of airports and cities, and will need to use the Google Geocoding API and Google Places API to obtain the rating information.

* Next, open up the solved version [05-Stu_Google_Complex/Airport_Ratings.ipynb](Activities/05-Stu_Google_Complex/Solved/Airport_Ratings.ipynb) and show students the ending Data Frame.

  ![Airport - Output](Images/06-Airport_Output.png)

* Open the [slideshow](https://docs.google.com/presentation/d/1TSi886_pX1_naQAB89-vIr_fDIaNpJQN_2HFMNeJxic) and use slides 20-22 to display the activity's instructions.

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Google Complex (Airport) (0:05)</strong></summary>

* ⏰**3-Hour Adjustment**: This review activity is now an **Everyone Do**.

  * Spend only 10 minutes on this activity.

  * Use the review section as guidance for talking points as you live-code along with the students.

  * Be sure to take your time and answer all student questions along the way.

* Open up [Airport_Ratings.ipynb](Activities/05-Stu_Google_Complex/Solved/Airport_Ratings.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, making certain to hit upon the following points.

  * `iterrows()` is used to loop through each city in the DataFrame to obtain the geo-coordinates for each airport.

  * `.loc` sets the value of lat/lng columns to match the retrieved coordinates that Google Geocoder API provides.

    ![Images/06-Airport.png](Images/06-Airport.png)

    ![Images/06-Airport2.png](Images/06-Airport2.png)

  * The iteration is repeated a second time utilizing the newfound lat/lng to obtain the airport information according to Google Places.

  * Also, point out that the application uses a try-except block to avoid situations where Google Places is missing review information.

    ![Images/06-Airport3.png](Images/06-Airport3.png)

    ![Images/06-Airport4.png](Images/06-Airport4.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2UF7Y5o)</sub>

- - -

## Break

| Activity Time:       0:40 |  Elapsed Time:      2:15  |
|---------------------------|---------------------------|

⏰ **3-Hour Adjustment**: Reduce break time to 15 minutes.

- - -

## 4. Hot Airports

| Activity Time:       0:40 |  Elapsed Time:      2:55  |
|---------------------------|---------------------------|

<details>
  <summary><strong>🎉 4.1 Everyone Do: Jupyter gmaps (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1TSi886_pX1_naQAB89-vIr_fDIaNpJQN_2HFMNeJxic) and use slides 24–28 to accompany the beginning of this demonstration.

* **Note:** if you having trouble displaying the maps try running `jupyter nbextension enable --py gmaps` in your environment and retry.

* Upon returning to class, explain the use-case for [Jupyter gmaps](http://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html). While discussing Jupyter gmaps, be sure to explain:

  * _gmaps_ is a plugin for Jupyter, allowing users to embed Google maps directly into their notebooks.

  * This grants the ability to visualize multiple layers of data as well as customize the appearance of the map.

* Before beginning the installation:

  * First revisit the steps to enable a google API.

  * Direct the students to return to the [Google API Console](https://console.developers.google.com/) and ensure the project created earlier is selected.

    ![Images/02-GoogleKey.png](Images/02-GoogleKey.png)

  * Click the library on the side panel and search for _Maps JavaScript API_.

  * Direct the students to enable the API.

* After the API is enabled, run these commands either in a jupyter notebook or terminal/git-bash.

* **Note:** The jupyter notebook server may need restarted for the changes to take place.

```
# enable jupyter extensions
jupyter nbextension enable --py --sys-prefix widgetsnbextension

# install gmaps
conda install -c conda-forge gmaps

# enable gmaps
jupyter nbextension enable --py --sys-prefix gmaps
```

* Before moving on to the demonstration, address questions and troubleshoot any installation issues.

* Explain to the students the following steps to create a Gmap:

  * First, configure gmaps by passing in the unique API key.

  * Building a base map is the first building block when creating visualizations with gmaps.

    * **Note**: some students may encounter an error with Jupyter Widgets when displaying the first figure. Reference the [Jupyter Widget documentation](http://ipywidgets.readthedocs.io/en/latest/user_install.html) for additional instructions.

  * In order to add layers to the map, a `marker_layer` is used by creating a list of tuples in the kernel. Each tuple is a coordinate for a US city.

  * Maps can be further  customized  by adding width and height attributes. Margin and padding can also be specified.

* Discuss that gmaps accepts coordinates from several different forms: the list of tuples as demonstrated, a dictionary of lists, and from a dataframe containing a column each for latitude and longitude.

* Once all students have their API keys and tools installed, send out the notebook file [gmap.ipynb](Activities/06-Evr_Jupyter_Gmaps/Unsolved/gmaps.ipynb). Live code and explain along the way:

  * Configuring gmaps by passing in their unique API key.

  * Building a base map. Explain to the students that this is the first building block when creating visualizations with gmaps.

  ```python
  import gmaps
  from config import gkey

  gmaps.configure(api_key=gkey)

  fig = gmaps.figure()
  ```

  ![Base Map](Images/07-Base_Map.png)

  * **Note**: some students may encounter an error with Jupyter Widgets when displaying the first figure. Reference the [Jupyter Widget documentation](http://ipywidgets.readthedocs.io/en/latest/user_install.html) for additional instructions.

  * Adding layers to the map. Demonstrate a `marker_layer` by creating a list of tuples in the kernel. Each tuple is a coordinate for a US city.

  ```python
  coordinates = [
      (40.71, -74.00),
      (30.26, -97.74),
      (46.87, -96.78),
      (47.60, -122.33),
      (32.71, -117.16)
  ]

  fig = gmaps.figure()
  markers = gmaps.marker_layer(marker_locations)
  fig.add_layer(markers)
  fig
  ```

  * Adjusting the viewport. Note how the map automatically adjusts the view as data is added. The zoom and map center and be manually adjusted within `gmaps.figure()`, though both parameters must be met to apply the adjustment.

  * Explain that the figure can also be centered within the user's output cell by setting the left and right margins to auto:

  ```python
  figure_layout = {'width': '400px', 'margin': '0 auto 0 auto'}

  gmaps.figure(layout=figure_layout)
  ```

  * Next, demonstrate map customization by adding width and height attributes. Margin and padding can also be specified.

  ```python
  import gmaps
  gmaps.configure(api_key="your_key")

  figure_layout = {
    'width': '400px',
    'width': '300px',
    'border': '1px solid black',
    'padding': '1px'
  }

  fig = gmaps.figure(layout=figure_layout)
  fig
  ```

  ![Customized Map](Images/07-Customized_Map.png)

* Finally, demonstrate exporting the completed figure as a .png file via the download button.

  ![Download Button](Images/07-Download.png)

* Discuss that gmaps accepts coordinates from several different forms: the list of tuples as demonstrated, a dictionary of lists, and from a dataframe containing a column each for latitude and longitude.

</details>

<details>
  <summary><strong>✏️ 4.2 Student Do: Hot Airports (15 mins)</strong></summary>

* ⏰ **3-Hour Adjustment**: Reduce activity time to 10 minutes.

* **Files:**

* [Airport_Output.csv](Activities/07-Stu_Airport_Map/Resources/Airport_Output.csv)

* [airport_heatmap.ipynb](Activities/07-Stu_Airport_Map/Unsolved/airport_heatmap.ipynb)

* **Instructions:** [README.md](Activities/07-Stu_Airport_Map/README.md)

* In this activity students will create a heat map based on airport ratings.

* Open the [slideshow](https://docs.google.com/presentation/d/1TSi886_pX1_naQAB89-vIr_fDIaNpJQN_2HFMNeJxic) and use slides 29–32 to display the activity's instructions and sample output.

</details>

<details>
  <summary><strong>⭐ 4.3 Review: Hot Airports (10 mins)</strong></summary>

* Open [airport_heatmap.ipynb](Activities/07-Stu_Airport_Map/Solved/airport_heatmap.ipynb) in jupyter notebook, explaining as you progress through the code.

  * Start by configuring gmaps by loading in an API key, then reading in the csv and storing it as a dataframe.

  * The Airport Rating column contains `NaN` values and strings. Using pandas methods `fillna` and `astype`, the column will be cleaned and usable.

    ![airport layer](Images/airport_layer.png)

  * At minimum, two things are needed for a heatmap: locations and a weight. The `"Lat"` and `"Lng"` columns are pulled out for locations and the `"Airport Rating"` for the weight.

  * For the bonus, the arguments `dissipating=False`, `max_intensity=10`, and `point_radius=1` allow the map to handle being zoomed.

  * Finally, a Gmap figure is created. Create the `heat_layer` by passing in locations and ratings, then the layer is added and the figure is displayed.

  * For the bonus, `map_type` can be changed by being passed in as a argument to `gmaps.figure()`

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3dJyfHb)</sub>

- - -

## 5. Census Activity

| Activity Time:       0:35 |  Elapsed Time:      3:30  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 5.1 Instructor Do: Census Demo (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1TSi886_pX1_naQAB89-vIr_fDIaNpJQN_2HFMNeJxic) and use slides 33-36 to accompany the beginning of this demonstration.

* **Note:** These census examples are definitely stretch targets. If you cannot get to it, don't sweat it!)

* As you transition to the next activity, explain to students that in the previous example all of the census data was provided to them. However, obtaining similar or other census data is fairly straightforward using the Python library census-wrapper.

* Have students visit the page [census-wrapper](https://github.com/datamade/census). Have them run `pip install census` and obtain a [Census API key](https://api.census.gov/data/key_signup.html) from the US Census Bureau. **Note:** It will take 2-3 minutes after you enter your information into the form to get your Census API key. To save time, you can simply provide students with your own key if there are issues with students getting a key.

* Once students are set up, walk students through the general documentation of the census-wrapper API.

  * In essence, the wrapper provides a fairly easy method of retrieving data from the 2013 census based on zip code, state, district, or county.

  * Each census field (e.g. Poverty Count, Unemployment Count, Number of Asians, etc.) is denoted with a label like B201534_10E. In using the API, developers list out each of the desired fields based on their labels.

  * The results are then returned as a list of dictionaries, which can be immediately converted into a DataFrame.

  * While discussing the API, it's fair to point out to students that the US Census API isn't the best documented API out there.

* Now open the file [Census_Demo.ipynb](Activities/08-Ins_Census/Solved/Census_Demo.ipynb) using Jupyter. Explain to students that this is the code used to create the csv in the banking deserts example. In particular, point out how:

  * We used the `c.acs5.get` method to grab data on each of the fields we needed. (Note: For ease of use a gist has been provided that explains what field each label in the US Census correlates with. We know. Your welcome.)

  * We divided the Poverty Count by Total Population to evaluate Poverty Rate. This is because the US census doesn't calculate Poverty Rate explicitly.

      ![Images/09-Census.png](Images/09-Census.png)

  * Ask if there are any questions before slacking out the code and proceeding with the activity.

</details>

<details>
  <summary><strong>✏️ 5.2 Students Do: Census Activity (20 mins)</strong></summary>

* ⏰ **3-Hour Adjustment**: Reduce activity time to 15 minutes.

* **Files:** [09-Stu_Census_API_Gmap/Census_States.ipynb](Activities/09-Stu_Census_API_Gmap/Unsolved/Census_States.ipynb)

* **Instructions:** [README.md](Activities/09-Stu_Census_API_Gmap/README.md)

* In this activity students will utilize the Census API to obtain census data at a state level and visualize it with gmaps.

* Open the [slideshow](https://docs.google.com/presentation/d/1TSi886_pX1_naQAB89-vIr_fDIaNpJQN_2HFMNeJxic) and use slides 37-39 to display the activity's instructions.

</details>

<details>
  <summary><strong>⭐ 5.3 Review: Census Activity (5 mins)</strong></summary>

* Review the solution in [Census_States.ipynb](Activities/09-Stu_Census_API_Gmap/Solved/Census_States.ipynb) explaining the code as you go along:

  * Using the census API to add the code `B23025_005E` and `{for': 'state:*'}` to retrieve data at the state level and adding this to the columns dictionary. This allows for a deeper look at the data.

  * Calculating the unemployment rate by dividing unemployment count by state population.

  ![Images/09-StateCensus.png](Images/09-StateCensus.png)

  * Reading in the csv file containing state centroid coordinates and appending them to the dataframe enables plotting on the map; this is because gmaps requires a set of coordinates to map the data.

  * Converting the 'Poverty Rate' column to a list then looping through it allows gmaps to assign the poverty rate for each state to its corresponding marker.

  ![10-State_Markers.png](Images/10-State_Markers.png)

* Check if there are any questions before proceeding to send out the solution.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2Va47ML)</sub>

- - -

## 6. Banking Deserts Heatmap

| Activity Time:       0:30 |  Elapsed Time:      4:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 6.1 Students Do: Banking Deserts Heatmap (15 mins)</strong></summary>

* **Files:**

* [zip_bank_data.csv](Activities/10-Stu_BankDeserts_Heatmap/Resources/zip_bank_data.csv)

* [Unsolved/Banking_Deserts_HeatMap.ipynb](Activities/10-Stu_BankDeserts_Heatmap/Unsolved/Banking_Deserts_HeatMap.ipynb)

* **Instructions** [README.md](Activities/10-Stu_BankDeserts_Heatmap/README.md)

* Explain to students that they'll be creating a data visualization to understand how prominent the "banking desert" phenomenon truly is. In order to accomplish this, they will be utilizing the US Census and their newfound skills with the Google Geocoder API and Jupyter gmaps.

* Send out the article on [banking deserts](https://www.theatlantic.com/business/archive/2016/03/banking-desert-ny-fed/473436/) from the Atlantic. Explain to students that "banking deserts" are a socioeconomic phenomenon in which many low-income and elderly areas tend to have no or few banking services available. The end-result is that these communities are often preyed upon by high-interest "check cashing" and "fast cash now" providers.

* Open the [slideshow](https://docs.google.com/presentation/d/1TSi886_pX1_naQAB89-vIr_fDIaNpJQN_2HFMNeJxic) and use slides 40-42 to display the activity's instructions.

</details>

<details>
  <summary><strong>⭐ 6.2 Review: Banking Deserts Heatmap (10 mins)</strong></summary>

* Open [Banking_Desert_HeatMap.ipynb](Activities/10-Stu_BankDeserts_Heatmap/Solved/Banking_Desert_HeatMap.ipynb) in jupyter notebook and go through the code. Along the way be sure to explain:

  * Find the poverty rate by dividing the `Poverty Count` by `Population`. Be sure to that each column is converted to an integer.

  * Create a new census dataframe  by selecting  "Zipcode", "Population", and "Poverty Rate".

  * Combine the data by loading "zip_bank_data.csv" into a dataframe and merge on  **Zipcode** with the census dataframe that was just created.

    ![merge data](Images/merge_data.png)

  * Configure `gmaps` by adding in an API key.

  * Grab the "Lat" and "Lng" to be stored as the locations that will be used in the heatmap. "Poverty Rate" will be used as the weight on the heatmap. Both these values will need to convert into floats.

  * A `heatmap_layer` is then created, added to the figure and displayed. Be sure to pass the arguments that handle the map dissipating when zoomed.

    ![heatmap](Images/heatmap.png)

  * "Bank Rate" is converted to a list in order to be passed in as `info_box_content` to the `symbol_layer`.

  * A symbol layer is created by passing in locations and "Bank Rate". The additional arguments are stylistic and can adjusted to help clear up how the map will look. The list comprehension `f"Bank amount: {bank}" for bank in bank_rate` will allow the bank data to be customized and added to the map. Finally the `symbol_layer` is added to the figure and displayed.

    ![bank map](Images/bank_map.png)

  * For the last steps, a new map is created by adding both the `heatmap_layer` and the `symbol_layer` before displaying the figure.

    ![final map](Images/final_map.png)

* Answer any questions on the maps before moving on to the statistics portion of the assignment. Go through the rest of the code and explain:

* The summary statistics can be found by using `mean()`, `median()`, and `mode()`.

```python
# Mean, median, mode for Poverty Rate
poverty_mean = round(census_data_complete['Poverty Rate'].astype('float').mean(), 2)
poverty_median = round(census_data_complete['Poverty Rate'].astype('float').median(), 2)
poverty_mode = round(census_data_complete['Poverty Rate'].astype('float').mode(), 2)

print(f"Poverty Rate Mean: {poverty_mean}")
print(f"Poverty Rate Median {poverty_median}")
print(f"Poverty Rate mode {poverty_mode}")
```

* For linear regression and scatter plot, we need to declare the independent (x) and dependent (y) values. `Poverty Rate` and `Bank Count` are stored as the independent and dependent values, respectively.

  * A linear regression model is generated for these variables.

  ```python
  # Run linear regression
  (slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
  regress_values = x_values * slope + intercept
  line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
  ```

  * A scatter plot is created with a superimposed regression line.

  * The R squared value is printed and the chart displayed.

* Explain there is a very weak correlation between poverty rates and bank counts.

  * Keep in mind that linear regression will not consider other factors such as population or size of the city.

</details>

<details>
  <summary><strong>📣 6.3 Instructor Do: Video Guide and Close Class (5 mins)</strong></summary>

* Before finishing up for the night, send out the [Video Guide](../VideoGuide.md) containing walkthroughs of this week's key activities. Encourage students to review them later and utilize office hours if they have further questions.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2JAUjG8)</sub>

- - -

## References

Google Maps Platform. (2020). Place Types. Places API. [https://developers.google.com/places/supported_types](https://developers.google.com/places/supported_types)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
