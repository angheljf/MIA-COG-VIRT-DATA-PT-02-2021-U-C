# 21.3 Neural Networks and Deep Learning

## Overview

Today's lesson provides students with an introduction to neural nets and deep learning using Keras.

## Class Objectives

* Students will be able to articulate specific problems on which neural networks perform well.

* Students will be able to use Keras to build and train neural networks.

* Students will be able to use Keras to build and a train a deep neural network.

* Students will understand unsupervised learning and how to apply the k-means algorithm.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</summary></strong>

* You may find that this lesson falls on a weekday due to a holiday shifting the course schedule. In this case, we have provided notes within the LP that will allow you to **easily adjust the length of the lesson to fit into a weekday class**.

  * Be on the lookout for a ⏰**3-Hour Adjustment** note at the top of activities in this Lesson Plan. If this class is being taught on a weekday, please utilize the directions found in the note. Keep in mind that breaks will be reduced from 40 minutes to the typical 15 minutes for a weekday class as well.

  * Shortening these activities could potentially limit the students' ability to finish them, so please remind them to utilize office hours to clear up any questions they may have.

* As a reminder these slideshows are for instructor use only - when distributing slides to students, please first export the slides to a PDF file. You may then send out the PDF file.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-21-machine-learning) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

</details>

<details>
  <summary><strong>Sample Class Video</summary></strong>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f41f4277-27b6-4462-a187-aa88002a53f2)

</details>

- - -

# Class Activities

## 1. Welcome Class & Intro to Neural Nets

| Activity Time:       0:35 |  Elapsed Time:      0:35  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 1.1 Welcome Class (0:05)</strong></summary>

* Explain that today's class will first discuss neural networks and deep learning. Then, move onto the k-means unsupervised clustering algorithm.

</details>

<details>
  <summary><strong> 📣 1.2 Instructor Do: Introduction to Neural Nets (0:15)</strong></summary>

* Walk through slides 1-14 (Intro to Neural Networks) of the [slideshow](https://drive.google.com/open?id=14voz4G22b6m-zBVih7Vf1CtbAkweQKyGD-W3yK4ZwdA) and highlight the following:

  * Discuss a few motivating examples of Neural Networks and Deep Learning.

  * Explain that an Artificial Neuron mimics the behavior of a biological neuron in the brain.

  * Explain that an Artificial Neural Network is simply an architecture of interconnected neurons.

  * Explain that a Neural Network processes information in similar ways to the brain. Inputs flow through the network and are trained to detect higher level features as the progress through the network until an output or decision can be made.

  * Show that Neural Networks are just layer of connected Neurons.

  * Point out that unlike other machine learning models, neural network models can be used for two-class classification, multi-class classification, probability, and regression using the same basic structure.

    * Explain that the most common output of a neural network is a two-class classification or probability.

  * Explain that Neural Networks are trained by feeding inputs (i.e. pictures of cats and dogs) through a network, calculating an output, comparing that to a known label, and then using any error to update all of the weights in the network. A Neural Network essentially learns by adjusting it's weights between each node. This controls the activation of neurons.

  * Show an example of using a trained network to predict the label of a cat or a dog in an image.

  * Ask for any additional questions before moving on.

  </details>

<details>
  <summary><strong> 📣 1.3 Instructor Do: Tensor Flow Playground (0:15)</strong></summary>

* Explain that one of the best ways to develop an intuition for how neural nets work is to watch them learn.

* Explain that [Tensor Flow Playground](http://playground.tensorflow.org) is a website where users can configure and train a neural network on different kinds of problems.

* Explain that the objective of this demonstration is to enhance students' intuition for what kinds of problems neural nets perform well on, and how they learn over time.

* Navigate to the [Tensor Flow Playground](http://playground.tensorflow.org/).

  * Send out the link and encourage students to follow along.

  ![tfp_home.png](Images/tfp_home.png)

* Take a moment to explain the layout of the page to the class.

* Note the "play" button in the top left corner of the page. Explain that clicking this starts training the network.

  ![tf_play.png](Images/tf_play.png)

* In the same row as the play button, there are dropdowns for **Learning Rate**; **Activation Function**; **Regularization**; etc.

  * Explain that these options affect how quickly a network learns, and influence the goodness of its predictions.

  * Explain that tuning these parameters is important, but advanced.

  * For now, leave this row as-is.

* Below this row are headings for **Data**; **Features**; **Hidden Layers**; and **Output**.

* Under **Data**, select the data set on which to train the model.

* Instruct students to select the two blobs in the bottom left.

  ![two_blobs.png](Images/two_blobs.png)

* Explain that changing the **Features** allows the user to  specify properties to look for in the input data.

  * Instruct students to select only x<sub>1</sub> and x<sub>2</sub>, which should be the defaults.

  ![x1_x2.png](Images/x1_x2.png)

* **Hidden Layers** identify "higher-order" patterns and correlations amongst input features.

  * Instruct students to remove all but one hidden layer.

  * Instruct students to configure their hidden layer with 6 neurons.

  * Explain that a common rule of thumb for 3-layer networks is to use three times as many nodes in the hidden layer as in the input layer.

  ![tfp_hidden_layer.png](Images/tfp_hidden_layer.png)

* Finally, note the **Output** image, which plots the network's decision boundaries as it learns.

  * Point out that the output image displays the two blobs in the data on the left.

  ![tfp_setup.png](Images/tfp_setup.png)

* Ask a student to explain how a successful classifier would draw a decision boundary for this data.

  * A good classifier would draw a line between the blobs.

* Emphasize that this data set is **linearly separable**.

* Start training the network, and call attention to the output image on the right-hand side of the page.

* Begin training the model by clicking the play button in the top left corner.

* Point out that, right after the play button is pressed, the fit _changed_ over time.

* The network draws a linear decision boundary, as expected.

  ![nnet_linear_classification.png](Images/nnet_linear_classification.png)

* Explain that this isn't new: A variety of sklearn classifiers already covered in class can draw this boundary just fine.

* Ask a student to name one sklearn model that could distinguish between these two regions.

  * The prototypical model for classifying two distinct regions is **logistic regression**.

* This example shows that neural networks can easily solve linear problems, but doesn't demonstrate their efficacy at modeling nonlinearities.

* Explain to students that neural nets are particularly powerful at modeling nonlinearities.

  * This implies they should be good at distinguishing linearly separable regions, as well.

* Click the blob-in-circle data set on the left.

  ![blob_in_circle.png](Images/blob_in_circle.png)

* Highlight that these two regions are highly nonlinear.

  * The nonlinearity is due to the fact that the regions are separated by a circle, so there's no single _line_ that can be drawn to distinguish them.

* Now, train the network, and observe how neural nets learn nonlinearities.

  * Click the play button in the top left.

  * Point out that, as before, the decision boundary changes in time.

  * Highlight that it takes much longer for the network to find the circular decision boundary than the linear one.

  * It does, nevertheless, manage to separate the regions.

  * Emphasize that this is a huge win over classical methods!

* Explain that, while this is a complicated function to fit, more complicated nonlinearities are common.

* Instruct students to select the spiral data on the left.

  ![spiral.png](Images/spiral.png)

* Point out that this is much more complicated than a simple circle.

* Click the play button in the top left.

* Point out that, this time, the neural net doesn't do such a good job fitting the curves.

  * Point out that this implies there are problems our neural net can't solve.

  ![nnet_failed_spiral.png](Images/nnet_failed_spiral.png)

* Explain that this is because the data is, in some sense, "too nonlinear" for this network.

* Explain that this is where **hidden layers** come in.

* Remind students that each layer of a network distills information that it receives from a previous layer.

  * Explain that, the more complex the nonlinearities in the data, the more "distillation steps" will be required for the network to "understand" where to draw its decision boundaries.

  * Explain that adding hidden layers increases the "level of nonlinearity" a network can detect and fit.

  * Explain that this is why **deep networks**—i.e., those with more than 3 layers—must be used to solve most interesting real-world problems.

* Explain that this problem is, in fact, rather difficult.

* Explain that it requires the addition of hidden layers; more input features; and configuration of the model's learning rate, activation function, and regularization methods.

* Explain that values like the **learning rate** are constants in the learning equations.

* Explain that such constants influence how quickly and how well the network learns.

* Explain that hyperparameter selection is a major topic in deep learning research.

* Set up TensorFlow Playground with the parameters shown in the image below, and click the play button in the top left.

  ![nnet_spiral_setup.png](Images/nnet_spiral_setup.png)

* Point out that the spiral takes much longer to fit than previous data sets.

  * Point out the number in the top left and immediately to the right of the play button.

    * This counts the number of training cycles, or **epochs**, over which the network has been trained.

  * Point out that it takes more epochs to train a network to fit the spiral than to train a network to fit either the circle or two blobs.

* Point out that the final fit still isn't perfect—but, it's extremely good relative to the complexity of the data set and the performance of alternative models.

  ![nnet_successful_spiral.png](Images/nnet_successful_spiral.png)

* Emphasize that this demonstration has shown us:

  * How neural networks learn over time.

  * What properties of a neural network determine how quickly it learns, as well as the goodness of its fit.

* Allow students a few minutes to experiment with the other datasets, features, and layers.

* Take a moment to address remaining questions before proceeding.

</details>

- - -

## 2. Building Neural Networks & Deep Learning

| Activity Time:       0:50 |  Elapsed Time:      1:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣2.1 Instructor Do: Intro to Keras SlideShow (0:05)</strong></summary>

* Walk through slides 15-21 (Why Keras? Who keras?) of the [slideshow](https://drive.google.com/open?id=14voz4G22b6m-zBVih7Vf1CtbAkweQKyGD-W3yK4ZwdA)  and highlight the following:

  * Explain that we are going to use TensorFlow and Keras to build our Neural Networks. TensorFlow allows us to run our code across multiple platforms in a highly efficient way.

  * Explain that Keras is an abstraction layer on top of TensorFLow that makes it easier to build models. You can relate this to using Plotly.js to build charts instead of using the more verbose D3.js library.

  * Show an example of how Keras provides the standard `model -> fit -> predict` interface that they are used to seeing (with a few additional steps that will be covered later).

  * Finally, ask students to install Keras in their python environment using `conda install tensorflow` and `conda install keras` and then test the install by importing keras in a jupyter notebook using `import tensorflow.keras`.

</details>

<details>
  <summary><strong> 📣 2.2 Instructor Do: One-Hot Encoding (0:10)</strong></summary>

* This activity is an introduction to one-hot encoding; an essential step in building a neural network classifier.

* Launch Jupyter Notebook, and step through the [01-Ins_One_Hot_Encoding/One_Hot_Encoding.ipynb](Activities/01-Ins_One_Hot_Encoding/Solved/One_Hot_Encoding.ipynb) notebook.

* Explain that when data contains strings for labels, they need to be converted to numeric values.

* Show the example of an input that contains the strings `dog` and `cat`.

  ![Ins_One_Hot_Encoding1](Images/Ins_One_Hot_Encoding1.png)

* Explain that these labels can be converted into numeric values in two steps.

  1. First, label encoding converts our classes into a numeric value as show in the iris example.

  ![Ins_One_Hot_Encoding2](Images/Ins_One_Hot_Encoding2.png)
  ![Ins_One_Hot_Encoding3](Images/Ins_One_Hot_Encoding3.png)

  * Loop through the encoded values to show students the results.

    ![One_Hot_Encoding_labels.png](Images/One_Hot_Encoding_labels.png)

  2. One-Hot Encoding converts that numeric value to a one-hot encoded array. One-Hot Encoding avoids biasing the model by applying numeric classes.

  ![Ins_One_Hot_Encoding4.png](Images/Ins_One_Hot_Encoding4.png)

* Explain that this processes will be frequently used when classifying data using neural networks.

* Send out a reference for students that are interested in learning more about [One-Hot Encoding](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/).

* Take a moment to address remaining questions before proceeding.

</details>

<details>
  <summary><strong> 🎉 2.3 Everyone Do: Building Neural Nets with Keras (0:20) </strong></summary>

* ⏰**3-Hour Adjustment**: Reduce activity time to 15 minutes.

* This activity is designed to have students practice creating a simple neural network with Keras by replicating a visual representation.  Students should follow along with the instructor demonstration.

* Open [02-Evr_First_Neural_Network/First_Neural_Network.ipynb](Activities/02-Evr_First_Neural_Network/Solved/First_Neural_Network.ipynb) and send out the unsolved version to students: [02-Evr_First_Neural_Network/First_Neural_Network.ipynb](Activities/02-Evr_First_Neural_Network/Unsolved/First_Neural_Network.ipynb).

  * The goal of this activity is to create a neural network that matches the diagram below to classify data.

    ![nnet.png](Images/nnet.png)

    * First, use sklearn to build a dataset with 100 samples and 3 features.  Then, create our training and testing data.

    ![Evr_First_Neural_Network1.png](Images/Evr_First_Neural_Network1.png)

    ![Evr_First_Neural_Network2.png](Images/Evr_First_Neural_Network2.png)

    * Scale the feature data using the StandardScaler.  Remember to scale both the testing and training data.

      * Scaling is extremely important with neural networks.  Without scaling, it is difficult for the training cycle to converge.

      ![Evr_First_Neural_Network3.png](Images/Evr_First_Neural_Network3.png)

      ![Evr_First_Neural_Network4.png](Images/Evr_First_Neural_Network4.png)

    * Note that for regressions the y-values will also be scaled, but in this case it is not necessary since one-hot-encoding is used for the outputs.

      ![Evr_First_Neural_Network5.png](Images/Evr_First_Neural_Network5.png)

    * Create a sequential model.  This means that the data flows from layer to the next.

      ![Evr_First_Neural_Network6.png](Images/Evr_First_Neural_Network6.png)

    * Next, add a layer to the function using `Dense` (for a densely connected layer).

      * Here, specify the number of of inputs as the `input_dim` parameter which should be equal to the input dimensions (number of features).

      * Additionally, `units` is the number of desired nodes in the layer.

      * Also, specify the type of activation function.  Here, ReLu is used.

      ![Evr_First_Neural_Network7.png](Images/Evr_First_Neural_Network7.png)

    * Add an output layer.

      * Since this is a classification model, the number of nodes in this layer should equal the possible outcomes or classes.  For example, if three outcomes were available, then this layer would have 3 nodes.  This example has two outcomes, therefore two nodes are used.

      * The softmax activation function is used which is typically used in a neural network classifier.

      ![Evr_First_Neural_Network8.png](Images/Evr_First_Neural_Network8.png)

    * `model.summary()` gives us the output shape as expected; 4 nodes in the first layer and 2 in the final layer.

      ![Evr_First_Neural_Network9.png](Images/Evr_First_Neural_Network9.png)

    * Now that the structure of the model has been defined, it is compiled using a loss function and optimizer.

      * Use Categorical Crossentropy for classification models and MSE (Mean Squared Error) for linear regression.

      * Here, an additional training metric, `accuracy`, is also specified.

      ![Evr_First_Neural_Network10.png](Images/Evr_First_Neural_Network10.png)

    * Finally, train (fit) the model!

      * Training consists of using the optimizer and loss function to update weights during each iteration of your training cycle.  This training using 1000 iterations or epochs.

      ![Evr_First_Neural_Network11.png](Images/Evr_First_Neural_Network11.png)

    * Evaluate the model using our testing data.

      ![Evr_First_Neural_Network11.png](Images/Evr_First_Neural_Network12.png)

    * Make predictions with the model.

      ![Evr_First_Neural_Network12.png](Images/Evr_First_Neural_Network13.png)

</details>

<details>
  <summary><strong> 🎉 2.4 Everyone Do: Deep Learning (0:15) </strong></summary>

* ⏰**3-Hour Adjustment**: Reduce activity time to 10 minutes.

* This activity compares a regular neural network to a deep learning network. It is designed to be lived coded along with students.

* Open [03-Evr_Deep_Learning/Deep_Learning.ipynb](Activities/03-Evr_Deep_Learning/Solved/Deep_Learning.ipynb) as a resource and send out the unsolved version to students: [03-Evr_Deep_Learning/Deep_Learning.ipynb](Activities/03-Evr_Deep_Learning/Unsolved/Deep_Learning.ipynb)

  * First, show that the output for this dataset is a set of concentric circles where the inner circle is one class and the outer circle is another class.

  ![Evr_Deep_Learning1](Images/Evr_Deep_Learning1.png)

  * This is a classification problem.  Many classification models are designed to simply draw a line between two **linearly separable** regions of a space. However, this dataset is **non-linear** and no such line can be used to designate between the two classes.

  * Reiterate that neural networks are great at classifying non-linear data.

  * First, scale and pre-process the data. This is always the first step before using a neural network.

  ![Evr_Deep_Learning2](Images/Evr_Deep_Learning2.png)

  * This example compares two models.  The first is a regular neural network of 2 inputs, 6 hidden nodes, and 2 output nodes.  The second is a a deep neural network possessing a second hidden layer with 6 hidden nodes. These extra nodes help the network adapt to the non-linear data.

    * First, build the neural network with one hidden layer.

    * Note that the rule-of-thumb for a neural network is to have triple the amount of nodes in the hidden layer as the number of inputs. (This is not true of deep learning.)

    ![Evr_Deep_Learning3](Images/Evr_Deep_Learning3.png)

    * Then, build a deep learning neural network with a second layer of 6 nodes.

    ![Evr_Deep_Learning4](Images/Evr_Deep_Learning4.png)

  * Finally, show that the deep learning neural network has an accuracy score of .92 while the regular neural network has an accuracy score of .68.

    * Remember to use the test set to validate the model.

    ![Evr_Deep_Learning5](Images/Evr_Deep_Learning5.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2Rnp8Cf)</sub>

- - -

## 3. Moons - Neural Networks

| Activity Time:       0:20 |  Elapsed Time:      1:45  |
|---------------------------|---------------------------|

<details>
  <summary><strong> ✏️ 3.1 Students Do: Moons - Neural Networks (0:15) </strong></summary>

* ⏰**3-Hour Adjustment**: Reduce activity time to 10 minutes.

* In this activity, students will create a regular Neural Network and a Deep Neural Network. Then, compare the accuracy of each.

* **Files**

  * [04-Stu_Moons/Moons.ipynb](Activities/04-Stu_Moons_Neural_Networks/Unsolved/Moons.ipynb)

* **Instructions:** [04-Stu_Moons/README.md](Activities/04-Stu_Moons_Neural_Networks/README.md)

  * Create a Neural Network and Deep Neural Network Classifier that correctly classifies both moons from the dataset.

  * Train both models using 100 training epochs.

  * Compare the accuracy of both models.

* **Bonus:**

  * Try to find the minimal architecture (number of nodes) and minimum training iterations required to achieve a score of at least .90.

</details>

<details>
  <summary><strong> ⭐ 3.2 Review: Moons (0:05)</strong></summary>

* Open [04-Stu_Moons/Moons.ipynb](Activities/04-Stu_Moons_Neural_Networks/Solved/Moons.ipynb) and walk through the solution.

  * First, show that the output for this dataset is a set of interweaving half circles (moons).

  ![Stu_Moons1](Images/Stu_Moons1.png)

  * Explain that this is another example of a classification problem where a neural network can excel by adapting to the non-linearity of the dataset.

  * Quickly show that the steps for pre-processing, building, compiling, and training the model are all the same as before.

  * Point out that once again, our deep learning model outperforms the standard neural network.

  ![Stu_Moons2](Images/Stu_Moons2.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/39SgBxF)</sub>

- - -

## Break

| Activity Time:       0:40 |  Elapsed Time:      2:25  |
|---------------------------|---------------------------|

⏰**3-Hour Adjustment**: Reduce break time to 15 minutes.

- - -

## 4. Models

| Activity Time:       1:00 |  Elapsed Time:      3:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong> ✏️ 4.1 Students Do: Deep Voice Deep Learning (0:20)</strong></summary>

* ⏰**3-Hour Adjustment**: Skip this **Students Do** activity and continue on to the review activity.

* In this activity, students apply a deep learning neural network to predict the gender of a voice using acoustic properties of the voice and speech.

* Explain that they will be are revisiting the voice gender dataset from the previous class, but this time applying a neural network classifier.

* **Files**

  * [05-Stu_Voice_Recognition.ipynb](Activities/05-Stu_Deep_Voice_Deep_Learning/Unsolved/Voice_Recognition.ipynb)

  * [05-Stu_Deep_Voice/voice.csv](Activities/05-Stu_Deep_Voice_Deep_Learning/Resources/voice.csv)

  * [05-Stu_Deep_Voice/voice.md](Activities/05-Stu_Deep_Voice_Deep_Learning/Resources/voice.md)

* **Instructions:** [05-Stu_Deep_Voice/README.md](Activities/05-Stu_Deep_Voice_Deep_Learning/README.md)

  * Create a deep learning model with 2 hidden layers.  Each layer should have 100 nodes.

  * Compile and fit the model.

  * Quantify (score) the model.

  * Use the first 5 testing data points to make predictions.  Then, compare the predictions to the actual labels.

</details>

<details>
  <summary><strong> ⭐ 4.2 Review: Deep Voice (0:05) </strong></summary>

* **⏰3-Hour Adjustment**: This review activity is now an **Everyone Do**.

  * Spend only 15 minutes on this activity.

  * Use the review section as guidance for talking points as you live-code along with the students.

  * Be sure to take your time and answer all student questions along the way.

* Point out that this dataset requires applying label encoding and one-hot encoding on the y-labels since they are categorical and contain the strings `male` and `female`.

  ![Stu_Deep_Voice1](Images/Stu_Deep_Voice1.png)

* Explain that for this model, a more complex network is designed with 100 nodes in each hidden layer. This larger number of nodes will allow the neural network to adapt to the dataset.

  ![Stu_Deep_Voice2](Images/Stu_Deep_Voice2.png)

* Warn students that neural networks are often prone to over-fitting. Neural Network architectures should always be validated to ensure that they are not over-fitting to the training data and thus performing poorly on new data values.

* Explain that the `predict_classes` method makes a prediction and returns the original categorical encoding. The `inverse_transform` of our label encoder is applied to convert the encoded prediction to the original string value of `male` or `female`.

  ![Stu_Deep_Voice3](Images/Stu_Deep_Voice3.png)

* Ask students if they have any questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3c2U1DW)</sub>

- - -

## 5. Smartphone Accelerometer

| Activity Time:       0:35 |  Elapsed Time:      4:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 5.1 Instructor Do: Saving Models (0:05)</strong></summary>

* Explain that training a Neural Network can be expensive and time consuming. However, Keras provides a mechanism for saving and loading trained models.

* Open [06-Ins_Saving_Models/Saving_Models.ipynb](Activities/06-Ins_Saving_Models/Solved/Saving_Models.ipynb) in jupyter notebook, and demonstrate to students how to save the trained model created in the previous activity.

* Show that `model.save("modelname.h5")` can be called to save a trained model.

  ![Ins_Saving_Models1](Images/Ins_Saving_Models1.png)

* Explain that the `.h5` file extension refers to the [HDF5 binary format](https://support.hdfgroup.org/HDF5/)

* The `load_model` function is used to load a saved model in Keras.

  ![Ins_Saving_Models2](Images/Ins_Saving_Models2.png)

* Explain that saving a loading models is a common way to share and reuse trained models.

  ![Ins_Saving_Models3](Images/Ins_Saving_Models3.png)

</details>

<details>
  <summary><strong> ✏️ 5.2 Students Do: Predicting Human Activity from Smartphone Accelerometer Data (0:20)</strong></summary>

* **⏰3-Hour Adjustment**: Reduce activity time to 15 minutes.

* **Files**

  * [07-Stu_Smartphone_SavingModels/Smartphone_Activity_Detector.ipynb](Activities/07-Stu_Smartphone_SavingModels/Unsolved/Smartphone_Activity_Detector.ipynb)

  * [07-Stu_Smartphone_SavingModels/X_train.txt](Activities/07-Stu_Smartphone_SavingModels/Resources/Train/X_train.txt)

  * [07-Stu_Smartphone_SavingModels/y_train.txt](Activities/07-Stu_Smartphone_SavingModels/Resources/Train/y_train.txt)

  * [07-Stu_Smartphone_SavingModels/X_test.txt](Activities/07-Stu_Smartphone_SavingModels/Resources/Test/X_test.txt)

  * [07-Stu_Smartphone_SavingModels/y_test.txt](Activities/07-Stu_Smartphone_SavingModels/Resources/Test/y_test.txt)

* **Instructions:** [07-Stu_Smartphone_SavingModels/README.txt](Activities/07-Stu_Smartphone_SavingModels/README.md)

* Follow the comments in the provided starter file to:

  * Encode necessary labels.

  * Build and train a deep learning model.

  * Save the model.

  * Load to model.

  * Use the loaded model to predict the activity of a smartphone user based one data point from the test set.

</details>

<details>
  <summary><strong> ⭐ 5.3 Review: Smartphone Activity (0:10)</strong></summary>

* Ask a student to explain what they had to do to complete the activity.

  * Remind the class that the point of the activity is to determine whether someone is standing, sitting, walking, etc., based on accelerometer data collected from their smartphones.

  * Point out that this is a **multi-class classification** problem, and reiterate that neural nets often perform well on such problems.

* Explain that the "shape" of the solution is as follows:

  * Load and preprocess data, including one-hot encoding of categorical data.

  * Create and fit the model.

  * Persist the model for later use.

  * Test the model's accuracy, and test its performance on a validation set.

* Point out that this is essentially the same process used with any machine learning algorithm.

* Launch Jupyter, and open the solved [07-Stu_Smartphone_SavingModels/Smartphone_Activity_Detector.ipynb](Activities/07-Stu_Smartphone_SavingModels/Solved/Smartphone_Activity_Detector.ipynb).

* Point out that the first several cells of the notebook simply use Pandas to load the _X_-training and _X_-testing data.

  ![load_x_data.png](Images/load_x_data.png)

* Point out that _y_ data is loaded differently.

* After loading `y_train_df`, `y_train` is created with [keras.utils.to_categorical](https://keras.io/utils/#to_categorical).

  * Remind students that `to_categorical` converts a row's class label into a one-hot encoded vector, with a `1` in the slot corresponding to the row's original class, and `0` elsewhere.

  * Remind students that this is done because neural networks require  _numerical_ inputs rather than strings. One-hot encoding maps string-based label encodings (e.g., the label `WALKING`) with a purely numerical vector (e.g., `[0, ..., 1, ..., 0]`, where the slot containing `1` corresponds to the label `WALKING`).

  ![one_hot.png](Images/one_hot.png)

* Point out that, after loading and preprocessing the training data, the test data is loaded.

  ![load_test.png)](Images/load_test.png)

* This concludes the preprocessing steps.

* Ask a student to explain how to initialize a Sequential model in Keras.

  * Explain that to initialize a sequential model, one simply calls the `Sequential` constructor.

  ![Smartphone_sequential.png](Images/Smartphone_sequential.png)

* Ask a student to explain the architecture of the network they built.

  * Remind students that this activity required them to build a 3-layer neural network.

* Ask a student to explain how they they added their hidden layers.

  * Explain that to add a layer to a sequential model, one simply calls `add`.

  * Explain that the input layer is a `Dense` layer.

* Ask a student to explain why this layer has `input_dim=X_train.shape[1]`.

  * Because `X_train.shape[1]` contains the number of columns in our data, it is used to set `input_dim`.

    ![Smartphone_hidden_layers.png](Images/Smartphone_hidden_layers.png)

* Ask a student to explain how they added their output layer.

  * Explain that to add the output layer, `add` is called yet again.

* Ask a student to explain why `y_train.shape[1]` is passed to the `Dense` constructor.

  * Remind students that the output layer must have one neuron corresponding to each class label in the training set. Each neuron generates a probability that the input belongs to _its_ corresponding class. These predictions can be aggregated to produce a single most likely class.

  ![Smartphone_output_layer.png](Images/Smartphone_output_layer.png)

* Now, the model is compiled and fit to the training data.

  * Explain that the defaults chosen for the parameters here should be taken as "fixed" for our purposes, but that students can and should experiment with different options later on in their machine learning practice.

  * Remind students that `epochs` refers to the number of iterations of adjusting weights using the optimizer and loss functions.

  ![Smartphone_compile.png](Images/Smartphone_compile.png)

  ![Smartphone_fit.png](Images/Smartphone_fit.png)

* Explain that, after training, the model is saved and loaded the with the `save` and `load_model` methods, respectively.

  ![Smartphone_save.png](Images/Smartphone_save.png)

* Ask a student to explain why saving a model might be important.

  * Remind students that training a network is computationally expensive, so saving the network's trained weights allows training to be bypassed when making predictions later.

* Finally, explain that the model is tested and used to make predictions in essentially the same way other machine learning models have been tested.

  ![Smartphone_final.png](Images/Smartphone_final.png)

* Take a moment to address remaining questions before slacking out the solution and dismissing class.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/3c05c0e)</sub>

## 6. K-means

| Activity Time:       0:35 |  Elapsed Time:      4:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 6.1 Instructor Do: k-means and Clustering Lecture (0:15)</strong></summary>

* Walk through slides 22-32 (k-means) of the [slideshow](https://drive.google.com/open?id=14voz4G22b6m-zBVih7Vf1CtbAkweQKyGD-W3yK4ZwdA) and highlight the following points:

  * Unsupervised machine learning algorithms draw inferences directly from the data without any previously labeled outputs (i.e. no `y` labels).

  * One common type of unsupervised learning is cluster analysis. That is, the algorithms attempt to group data into clusters based on relationships and features in the data.

    ![clustering.jpg](Images/clustering.jpg)

  * While clustering may be intuitive to humans, clustering algorithms have to decide which data points belong together.

    ![clustered.png](Images/clustered.png)

  * k-means clustering will group the data into `k` groups.

  * The cluster center is the mean of all the points belonging to that cluster. Therefore each point is closer to it’s own cluster’s center than it is to other cluster centers.

    ![cluster-centers.png](Images/cluster-centers.png)

  * A small k will create larger clusters.

    ![k2.png](Images/k2.png)

  * A large k will create smaller clusters.

    ![k6.png](Images/k6.png)

    * Point out that even though we consider identifying clusters to be intuitive, k-means clustering considers more complex relationships which can result in clusters that may defy expectations.

  * Explain that predicting new values with a trained k-means model means that you are looking at the cluster centers to see which cluster is closest to the new data.

    ![kmeans-predict.png](Images/kmeans-predict.png)

  * A centroid in geometry is the center of a geometric object, here it refers to the center of a cluster.

* Open [08-Ins_Kmeans/Kmeans.ipynb](Activities/08-Ins_Kmeans/Solved/Kmeans.ipynb) and walk through the code for k-means and highlight the following:

  * This example creates random data with four data clusters. This can be visualized through the scatter plot.

    ![four-clusters.png](Images/four-clusters.png)

  * Explain that since four clusters can be seen in the data, `k=4` is used when creating our k-means model.

    ![k4-model.png](Images/k4-model.png)

  * The model is fit to the data and the clusters are predicted.

    ![kmeans-fit-predict.png](Images/kmeans-fit-predict.png)

  * The cluster predictions can then be plotted to visually see if the model correctly clustered the data.

    ![kmeans-clustered.png](Images/kmeans-clustered.png)

</details>

<details>
  <summary><strong> ✏️ 6.2 Students Do: K-means (0:15)</strong></summary>

* **⏰3-Hour Adjustment**: Skip this **Students Do** activity and continue on to the review activity.

* **File**: [09-Stu_Kmeans/Kmeans.ipynb](Activities/09-Stu_Kmeans/Unsolved/Kmeans.ipynb)

* **Instructions:** [09-Stu_Kmeans/README.md](Activities/09-Stu_Kmeans/README.md)

  * Use the starter code to fit a Kmeans model to a dataset.

  * Visualize the results by creating a plot that looks like the following.

    ![Stu_Kmeans_plot](Images/Stu_Kmeans_plot.png)

* **Bonus:**

  * Look up how to get the centers of the k-means clusters and plot them!

</details>

<details>
  <summary><strong>⭐ 6.3 Review: K-means (0:05)</strong></summary>

* **⏰3-Hour Adjustment**: This review activity is now an **Everyone Do**.

  * Spend only 15 minutes on this activity.

  * Use the review section as guidance for talking points as you live-code along with the students.

  * Be sure to take your time and answer all student questions along the way.

* Open up the solution, [09-Stu_Kmeans/Kmeans.ipynb](Activities/09-Stu_Kmeans/Solved/Kmeans.ipynb) and walk through the code. Be sure to explain the following:

  * The data for this activity was generated with 6 clusters.

    ![six-clusters.png](Images/six-clusters.png)

  * However, 12 clusters was required for this assignment.

  * Normally, when clustering is used, the user has a general idea about how many clusters are appropriate.  Sometimes, it does not correlate with the number of clusters that are expected after a visual inspection.

    * Contextualize this for students by giving the following example: Imagine looking at a plot of employee skills.  One of the clusters represents programmers, but within that group there exists python programmers and javascript programmers as sub-groups.

    ![k12-model.png](Images/k12-model.png)

  * Use the predicted clusters to show how the algorithm decided to split the data into 12 unique clusters.

    ![clusters-predicted.png](Images/clusters-predicted.png)

  * Show that the `cluster_centers_` attribute from the trained model is used to plot the cluster centers. The `labels_` attribute is used to plot the color of each cluster.

    ![cluster-centers-attributes.png](Images/cluster-centers-attributes.png)

    ![scatter-with-cluster-centers.png](Images/scatter-with-cluster-centers.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2USSIlr)</sub>

- - -

## References

Becker, Kory. (2016). "Identifying the Gender of a Voice using Machine Learning." Accompanying Dataset. [http://www.primaryobjects.com/2016/06/22/identifying-the-gender-of-a-voice-using-machine-learning/](http://www.primaryobjects.com/2016/06/22/identifying-the-gender-of-a-voice-using-machine-learning/)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
