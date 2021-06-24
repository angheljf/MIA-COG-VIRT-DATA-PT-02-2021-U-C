# 21.2 Classification

## Overview

Today's lesson plan introduces students to classification algorithms in Scikit-learn.

## Class Objectives

* Students will understand how to calculate and apply the fundamental classification algorithms: logistic regression, SVM, KNN, decision trees, and random forests.

* Students will understand how to quantify and validate classification models including calculating a classification report.

* Students will understand how to apply `GridSearchCV` to hyper tune model parameters.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</summary></strong>

* Today's class introduces students to a variety of classification and clustering algorithms within the Sklearn ecosystem.

* Today's material should be exciting. Several algorithms are covered conceptually and then applied to a real dataset. The variety of algorithms should keep students engaged while the common dataset provides a thread that ties everything together.

* Today's class transitions from regression analysis to classification and clustering. Students will learn several algorithms conceptually and then apply those algorithms to a common dataset. This allows students to focus on the algorithms and the subtle performance differences rather than with data preprocessing. Students will learn how to generate classification reports to compare model performance and how to tune hyper parameters to optimize their models.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-21-machine-learning) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Have your TAs refer to the [Time Tracker](TimeTracker.xlsx) to stay on track.

* Lastly, as a reminder these slideshows are for instructor use only - when distributing slides to students, please first export the slides to a PDF file. You may then send out the PDF file.

</details>

<details>
  <summary><strong>Sample Class Video</summary></strong>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a7866f95-550e-47da-a107-a89401847672)

</details>

- - -
# Class Activities

## 1. Welcome & Logistic Regression

| Activity Time:       0:45 |  Elapsed Time:       0:45 |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 1.1 Welcome Class (0:05)</summary></strong>

* Explain that today's class will focus on classification.

* Remind students that classification is the prediction of discrete outputs or labels.

</details>

<details>
  <summary><strong> 📣 1.2 Instructor Do: Logistic Regression (0:10)</summary></strong>

* **File**: [Ins_Logistic_Regression.ipynb](Activities/01-Ins_Logistic_Regression/Solved/Ins_Logistic_Regression.ipynb)

* Walk through the [slideshow](https://docs.google.com/presentation/d/1_qXHdIKKDbeofL07xuS2QlfVtgpPfokI7HqX6GNaUlI/edit?usp=sharing) and highlight the following points:

  * Logistic Regression is a statistical method for predicting binary outcomes from data. With linear regression, our linear model may provide a numerical output such as job qualification. With logistic regression, the numerical value for job qualification could be translated to a probability between 0 and 1. This discrete output could then be labeled as "qualified" vs "unqualified".

    ![logistic-regression.png](Images/logistic-regression.png)

  * Logistic regression is calculated by applying an activation function as the final step to our linear model. This transforms a numerical range to a bounded probability between 0 and 1.

  * We can use logistic regression to predict which category or class a new data point should have.

    ![logistic_1.png](Images/logistic_1.png)
    ![logistic_2.png](Images/logistic_2.png)
    ![logistic_3.png](Images/logistic_3.png)

* After presenting the slideshow, open the Jupyter notebook and walk through the Scikit-Learn implementation for logistic regression.

  * Explain that we can use the `make_blobs` function to generate two different groups (classes) of data. We can then apply logistic regression to determine if new data points belong to the purple group or the yellow group.

    ![make-blobs.png](Images/make-blobs.png)

  * We create our model using the `LogisticRegression` class from Sklearn.

    ![logistic-regression-model.png](Images/logistic-regression-model.png)

  * Then we fit (train) the model using our training data.

    ![train-logistic-model.png](Images/train-logistic-model.png)

  * And validate it using the test data.

    ![test-logistic-model.png](Images/test-logistic-model.png)

  * And finally, we can make predictions.

    ![new-data.png](Images/new-data.png)

    ![predicted-class.png](Images/predicted-class.png)

</details>

<details>
  <summary><strong> ✏️ 1.3 Students Do: Gender Voice Recognition (0:20)</strong></summary>

* **File**: [Stu_Voice_Recognition.ipynb](Activities/02-Stu_Voice_Recognition/Unsolved/Stu_Voice_Recognition.ipynb)

</details>

<details>
  <summary><strong> ⭐ 1.4 Review Activity (0:10)</strong></summary>

* Walk through the [solution](Activities/02-Stu_Voice_Recognition/Solved/Stu_Voice_Recognition.ipynb) and highlight the following:

  * Remind students that logistic regression is used to predict categories or labels.

  * Explain that we will perform logistic regression to our dataset in order to predict the label `male` or `female`.

  * Show the prediction results for at least 10 of the test data samples. The output labels will be `male` or `female`.

    ![gender-predictions.png](Images/gender-predictions.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2VfFqy7)</sub>

## 2. Decision Trees & Random Forests

| Activity Time:       0:30 |  Elapsed Time:       1:15 |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 2.1 Instructor Do: Decision Trees & Random Forests (0:10)</summary></strong>

* **File**: [Ins_Trees.ipynb](Activities/03-Ins_Trees/Solved/Ins_Decision_Trees.ipynb)

* Walk through the [slideshow](https://docs.google.com/presentation/d/1_qXHdIKKDbeofL07xuS2QlfVtgpPfokI7HqX6GNaUlI/edit?usp=sharing) (Slides 1-5) and highlight the following points about Decision Trees:

  * Decision Trees encode a series of True/False questions that can be interpreted as if-else statements

    ![decision-tree.png](Images/decision-tree.png)

    ![dtree-ifelse.png](Images/dtree-ifelse.png)

  * Decision trees have a depth: the number of `if-else` statements encountered before making a decision.

  * Decision trees can become very complex and very deep, depending on how many questions have to be answered. Deep and complex trees tend to overfit to the data and do not generalize well.

    ![tree.png](Images/tree.png)

* Next, cover the slide (Slide 6) on Random Forests and highlight the following points:

  * Instead of one large, complex tree, you use many small and simple decision trees and average their outputs.

  * These simple trees are created by randomly sampling the data and creating a decision tree for only that small portion of data. This is known as a **weak classifier** because it is only trained on a small piece of the original data and by itself is only slightly better than a random guess. However, many "slightly better than average" small decision trees can be combined to create a **strong classifier**, which has much better decision making power.

  * Another benefit to this algorithm is that it is robust against overfitting. This is because all of those weak classifiers are trained on different pieces of the data.

    ![random-forest.png](Images/random-forest.png)

* After presenting the slideshow, open the Jupyter notebook and walk through the Scikit-Learn implementation for a decision tree.

* If you are able to successfully install `graphviz` and `pydotplus` open the Decision Tree Jupyter notebook [here](Extra_Content/Ins_Decision_Trees_Graphviz.ipynb) from the `Extra_Content` folder.

* If you are not able to successfully install `graphviz` and `pydotplus` open the `iris.png` image below.

* Whether using the Jupyter notbook or the PNG file, show how each node in the tree attempts to split the data based on some criteria of the input data. The top of the tree will be the decision point that makes the biggest split. Each sub-node makes a finer and finer grain decision as the depth increases.

  ![iris.png](Images/iris.png)

* Point out that the training phase of the decision tree algorithm learns which features best split the data.

* Explain a byproduct of the Random Forest algorithm is a ranking of feature importance (i.e. which features have the most impact on the decision).

* Show that Scikit-Learn provides an attribute called `feature_importances_`, where you can see which features were the most significant.

  ```python
  sorted(zip(rf.feature_importances_, iris.feature_names), reverse=True)
  ```

</details>

<details>
  <summary><strong> ✏️ 2.2 Students Do: Trees (0:15)</strong></summary>

* **File**: [Stu_Trees.ipynb](Activities/04-Stu_Trees/Unsolved/Stu_Trees.ipynb)

</details>

<details>
  <summary><strong> ⭐ 2.3 Review Activity (0:05)</strong></summary>

* Walk students through the [solution](Activities/04-Stu_Trees/Solved/Stu_Trees.ipynb) and highlight the following:

  * In this activity, the model accuracy is low and the complexity is high. Show the diagram of the decision tree and explain that this tree may be too complex to generalize to other diabetes datasets.

    ![tree.png](Images/tree.png)

  * The accuracy improves slightly when using a random forest classifier. Change the number of estimators in the random forest model and re-compute the score to show how it changes.

    ![nestimators.png](Images/nestimators.png)

</details>

<sub>[Having issues with this activity? Report a bug!](hhttps://bit.ly/39Tfn5l)</sub>

## 3. KNN

| Activity Time:       0:30 |  Elapsed Time:      1:45  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 3.1 Instructor Do: KNN (0:10)</strong></summary>

* **File**: [Ins_K_Nearest_Neighbors.ipynb](Activities/05-Ins_KNN/Solved/Ins_K_Nearest_Neighbors.ipynb)

* Walk through the [slideshow](https://docs.google.com/presentation/d/1_qXHdIKKDbeofL07xuS2QlfVtgpPfokI7HqX6GNaUlI/edit?usp=sharing) and highlight the following points:

  * The KNN algorithm is a simple, yet robust machine learning algorithm. It can be used for both regression and classification. However, it is typically used for classification.

  * Walk through the examples provided and show how K changes the classification. Be sure to point out that we use odd numbers for k so that there isn't a tie between neighboring points.

    ![k1.png](Images/k1.png)

    ![k3.png](Images/k3.png)

    ![k5.png](Images/k5.png)

    ![k7.png](Images/k7.png)

  * Finally, explain that the `k` for KNN is often calculated computationally with a loop.

* After presenting the slideshow, open the Jupyter notebook and walk through the Scikit-Learn implementation for K Nearest Neighbor algorithm. This code should look familiar by now since it uses the standard model-fit-predict pattern.

  * Point out that the best `k` value for this dataset is where the score is both accurate and has started to stabilize.

  ![knn-scores.png](Images/knn-scores.png)

  ![knn-plot.png](Images/knn-plot.png)

</details>

<details>
  <summary><strong> ✏️ 3.2 Students Do: KNN (0:15)</summary></strong>

* **File**: [Stu_Brains.ipynb](Activities/06-Stu_KNN/Unsolved/Stu_KNN.ipynb)

</details>

<details>
  <summary><strong> ⭐ Review Activity (0:05)</strong></summary>

* Walk students through the notebook and highlight the following:

  * For this activity, `K=13` seems to be the best combination of both the train and test scores.

    ![knn-train-test.png](Images/knn-train-test.png)

* Ask students for any additional questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2wlJJzA)</sub>

- - -

## BREAK

| Activity Time:       0:15 |  Elapsed Time:      2:00  |
|---------------------------|---------------------------|

- - -

## 4. SVM

| Activity Time:       0:30 |  Elapsed Time:      2:30  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 4.1 Instructor Do: SVM (0:10)</strong></summary>

* **File**: [Ins_Support_Vector_Machine.ipynb](Activities/07-Ins_SVM/Solved/Ins_Support_Vector_Machine.ipynb)

* Walk through the SVM [slideshow](https://docs.google.com/presentation/d/1_qXHdIKKDbeofL07xuS2QlfVtgpPfokI7HqX6GNaUlI/edit?usp=sharing) and highlight the following points:

  * The goal of a linear classifier is to find a line that separates two groups of classes. However, there may be many options for choosing this line and each boundary could result in misclassification of new data.

    ![linear-discriminative-classifiers.png](Images/linear-discriminative-classifiers.png)

    ![classifier-boundaries.png](Images/classifier-boundaries.png)

  * SVM try to find a hyperplane that maximizes the boundaries between groups. This is like building a virtual wall between groups where you want the wall to be as thick as possible.

    ![svm-hyperplane.png](Images/svm-hyperplane.png)

* After presenting the slideshow, open the Jupyter notebook and walk through the Scikit-Learn implementation for the support vector machine classifier algorithm.

  * Point out that there are different kernels available for the SVM model in SciKit-Learn, but we are going to use the linear model in this example.

    ![svm-linear.png](Images/svm-linear.png)

  * Show how to plot the decision boundaries for the trained model. It isn't important for students to fully understand the plotting code, but conceptually, they should be able to see how the algorithm maximized the boundaries between the two groups.

    ![svm-boundary-plot.png](Images/svm-boundary-plot.png)

  * Next, show an example of "real" data where the boundaries are overlapping. In this case, the svm algorithm will "soften" the margins and allow some of the data points to cross over the margin boundaries in order to obtain a fit.

    ![svm-soften.png](Images/svm-soften.png)

  * Finally, show how to generate a classification report to quantify and validate the model performance.

    ![svm-report.png](Images/svm-report.png)

  * Optionally, use the supplemental [slideshow](https://docs.google.com/presentation/d/1_qXHdIKKDbeofL07xuS2QlfVtgpPfokI7HqX6GNaUlI/edit?usp=sharing) on precision and recall to deep dive into the meaning behind each score.

</details>

<details>
  <summary><strong> ✏️ 4.2 Students Do: SVM (0:15)</strong></summary>

* **File**: [Stu_SVM.ipynb](Activities/08-Stu_SVM/Unsolved/Stu_SVM.ipynb)

</details>

<details>
  <summary><strong> ⭐ 4.3 Review Activity (0:05)</strong></summary>

* Walk students through the [solution](Activities/08-Stu_SVM/Solved/Stu_SVM.ipynb) notebook and highlight the following:

  * The F1 scores indicate that this model is slightly more accurate at predicting negative cases of diabetes than positive cases.

  ![svm-f1.png](Images/svm-f1.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2XrmkYy)</sub>

## 5. Grid Search

| Activity Time:       0:30 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 5.1 Instructor Do: GridSearch (0:10)</strong></summary>

* **File**: [Ins_GridSearch.ipynb](Activities/09-Ins_GridSearch/Solved/Ins_GridSearch.ipynb)

* Open the Jupyter notebook and walk through the code for hyperparameter tuning with `GridSearchCV`.

  * Show the output of the SVM model to highlight the different features available for the model. Each of these features can be adjusted and tweaked to improve model performance.

    ![svm-model.png](Images/svm-model.png)

  * Explain that in machine learning, there are few if any general rules on how to adjust these parameters. Instead, machine learning practitioners often use a brute force approach where they try different combinations of values to see which has the best performance. This is known as `hyperparameter tuning`.

  * To simplify the hyperparameter tuning process, SciKit-Learn provides a tool called `GridSearchCV`. This class is known as a `meta-estimator`. That is, it takes a model and a dictionary of parameter settings and tests all combinations of parameter settings to see which settings have the best performance.

    ![grid-model.png](Images/grid-model.png)

    ![grid-fit.png](Images/grid-fit.png)

  * Once the model has been trained, the best parameters can be accessed through the `best_params_` attribute.

    ![grid-best-params.png](Images/grid-best-params.png)

  * The test score can be accessed through `grid.score(X_test,y_test)`.

  * The grid meta-estimator basically wraps the original model, so you can access the model functions like `predict`.

    ![grid-predict.png](Images/grid-predict.png)

</details>

<details>
  <summary><strong> ✏️ 5.2 Students Do: Grid Search (0:15)</strong></summary>

* **File**: [Stu_GridSearch.ipynb](Activities/10-Stu_GridSearch/Unsolved/Stu_GridSearch.ipynb)

</details>

<details>
  <summary><strong> ⭐ 5.3 Review Activity (0:05)</strong></summary>

* Walk students through the [solution](Activities/10-Stu_GridSearch/Solved/Stu_GridSearch.ipynb) notebook and highlight the following:

  * Explain that Grid Search tested our model with 27 different combinations of parameters and data. Applying GridSearch saves us considerable time vs manually changing these values ourselves.

  * Explain that knowing which parameters to tune and which values to use comes from both experience and Sklearn's documentation for their algorithms.

  * Remind students that even though our model test score remained the same, there are multiple ways to accomplish similar tasks. We want to show them different ways of being able to approach problems they may see in their jobs.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2xbWywM)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
