# 23.2 Final Projects

## Overview

In this class, students will lean how to use pre-trained convolutional neural networks (CNNs) for image classification. The remaining class will be used for project work.

## Instructor Prep

<details>
  <summary><strong>Instructor Priorities</strong></summary>

* Students should have time to work on their projects.

* Make sure your students make measurable progress with their project work.

</details>

<details>
  <summary><strong>Instructor Notes</strong></summary>

* While today's class covers a very advanced topic, the material is a lot of fun. Students will learn how to use pre-trained CNNs to classify images.

* Despite the advanced topic, students are only using pre-trained models. Students that are interested in more theory with CNNs can reference the excellent Stanford course: [Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu/).

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

</details>

<details>
  <summary><strong>Sample Class Video</strong></summary>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=1777447c-e505-4e48-86dd-a89b01834a52)

</details>

- - -

## Class Objectives

* Students will be able to import a pre-trained CNN model.

* Students will be able to load an image from file into a data array.

* Students will be able to apply preprocessing to the input data.

* Students will be able to use the pre-trained model to make a prediction.

- - -

# Class Activities

## 1. Explore CNN

| Activity Time:       0:45 |  Elapsed Time:      0:45  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 👥 1.1 Partners Do: Explore CNN (0:15)</strong></summary>

* For the remainder of class students will use pre-trained CNN models.  The goal of this activity is to gain a high level understanding of CNN and their application.

* **Instructions:** [README.md](Activities/01-Par_Explore_CNNs/README.md)

  * Work with a partner to answer the following questions:

    1. What is a Convolutional Neural Network (CNN)?

    2. What is a CNN typically used for?

    3. What is the difference between a CNN and Deep Neural Network?

</details>

<details>
  <summary><strong> 📣 1.2 Instructor Do: Review Explore CNN (0:15)</strong></summary>

* The discussion here depends largely on your familiarity with CNN.  Feel free expose students to a more in-depth discussion if you are comfortable.

* Ask for student volunteers for answers to the CNN questions.

  1. What is a Convolutional Neural Network (CNN)?

  2. What is a CNN typically used for?

  3. What is the difference between a CNN and Deep Neural Network?

* This blog post has a nice high-level explanation of CNN: [The Data Science Blog - An Intuitive Explanation of Convolutional Neural Networks](https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/)

</details>

<details>
  <summary><strong> 📣 1.3 Instructor Do: Pre-trained Models (0:15)</strong></summary>

**File**: [PreTrained_Model.ipynb](Activities/02-Ins_PreTrained_Models/Solved/PreTrained_Model.ipynb)

* Walk through the Jupyter Notebook and highlight the following:

  * Explain that training CNN is often a complex and long process. However, once a model has been trained and evaluated, it can be shared and reused.

  * Explain that Keras provides several pre-trained models that are available for use right out of the box. These models are all trained using the ImageNet dataset. Send out the link to the ImageNet [website](http://www.image-net.org/) as a reference.

  * Explain that there are several models available to choose from, but this example uses the `VGG19` model.

  * Show that Keras provides utility functions to assist with image loading and data pre-processing. In fact, each model provides it's own pre-processing function to resize, scale, and pre-process an input image into the same format that the model was originally trained on. Without this pre-processing function, users would have to do all of that work themselves before using the model.

  * Explain that the image size can be found directly from the [Keras documentation for the model](https://keras.io/api/applications/vgg/#vgg19-function).

  ![vgg_16_docs.png](Images/vgg_16_docs.png)

  * Load the image and utilize the preprocessing function to scale and normalize the data.

  ![vgg-19.png](Images/vgg-19.png)

  * Use the loaded model to make predictions.  The `decode_predictions` function is used to find the original image labels for the predicted output label.

  ![vgg-19-predictions.png](Images/vgg-19-predictions.png)

  * Combine the pre-processing and prediction steps into a reusable function.

  * Use the function to make a prediction.

  ![vgg-predict-function.png](Images/vgg-predict-function.png)

  </details>

  <sub>[Having issues with this activity? Report a bug!](https://bit.ly/3c1ha9P)</sub>

## 2. Xception

  | Activity Time:       0:30 |  Elapsed Time:      1:15  |
  |---------------------------|---------------------------|

  <details>
    <summary><strong> ✏️ 2.1 Students Do: Xception (0:20)</strong></summary>

In this activity, students use the pre-trained `Xception` CNN model to predict image labels.

* **File**: [Xception.ipynb](Activities/03-Stu_Xception/Unsolved/Xception.ipynb)

* **Instructions:** [README.md](Activities/03-Stu_Xception/README.md)

  * Visit the [Xception](https://keras.io/api/applications/xception) documentation to determine the image_size and other parameters needed to load and use the model.

  * Pre-process the test image using the model's `preprocess_input` function.

  * Use the trained model to predict the output label for the puppy image.

* **Bonus:**

  * Refactor the above steps into a reusable function that accepts an input image and returns a pre-processed image.

  * Test the code by preprocessing the image of a kitten and printing the predicted labels.

  </details>

<details>
  <summary><strong> ⭐ 2.2 Review: Xception (0:10)</strong></summary>

* Open [03-Stu_Xception/Xception.ipynb](Activities/03-Stu_Xception/Solved/Xception.ipynb).

* Explain that in this activity, the `Xception` pre-trained model from Keras is used.

* Show the [documentation for the model](https://keras.io/applications/#xception) and explain that this model uses an image size of 299x299 pixels.

* Show that the code for using this model is very similar to the previous example. The Keras pre-processing utilities for the Xception model are used without having to significantly change the code.

  ![06-Xception](Images/06-Xception_puppy.png)

* For the bonus, the above steps are organized in a function and the function is called to predict labels for the image of the kitten.

  ![06-Xception](Images/06-Xception_kitten.png)

* Ask for any additional questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2xW0W38)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:30  |
|---------------------------|---------------------------|

- - -

## 3. Project Work

| Activity Time:       1:30 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong> ✏️ 3.1 Students Do: Project Work (1:30)</strong></summary>

* **Important:** warn students that if they choose to use any AWS resources to closely monitor what they use. Remind them to clean up and stop or shutdown any resources they may choose to use as to not accrue any additional costs.

* Send out the [AWS Billing Check](AWS_check_billing.pdf) that instructs students how to double their billing costs.

* Students will spend the rest of the class working on their projects.

</details>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
