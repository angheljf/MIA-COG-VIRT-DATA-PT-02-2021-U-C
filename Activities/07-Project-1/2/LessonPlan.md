# 7.2 Pulling and Merging with Git

## Overview

Today, students will study **pulling from GitHub**, **merging branches with Git**, and **distributed PR workflows**.

## Class Objectives

* Students will be able to **pull a branch from GitHub**.

* Students will be able to **merge branches with Git**.

* Students will be able to **open, review, and merge PRs with GitHub**.

## Instructor Prep

<details>
    <summary><strong>Instructor Priorities</strong></summary>

* Install the appropriate text editor plugin to help visualize Git histories: [Git History](https://github.com/DonJayamanne/gitHistoryVSCode) in VS Code, [Git Time Machine](https://github.com/pidu/git-timemachine) for Sublime Text, and [git-time-machine](https://atom.io/packages/git-time-machine) for Atom.

</details>

<details>
    <summary><strong>Instructor Notes</strong></summary>

* Students should have most of today to work on projects, and the Git activities require group work.

  * To that end, you will send out today's activities for groups to work through on their own time, for at most the first half of class.

  * You should, however, reserve some time at the beginning of class to both **demonstrate pull.sh** from [01-Ins_Pull/pull.sh](Activities/01-Ins_Pull/Solved/pull.sh); and **how to merge branches with Git**.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-07-project-1) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Have your TAs refer to the [TimeTracker](TimeTracker.xlsx) to stay on track.

</details>

<details>
    <summary><strong>Sample Class Video</strong></summary>

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e5096f79-710a-427b-accd-a8630029451d)

</details>

- - -

# Class Activities

## Git and GitHub

| Activity Time:       1:20 |  Elapsed Time:      1:20  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 1.1 Everyone Do: Merging on Git and GitHub (01:20)</strong></summary>

* **Files**

  * [README.md](Activities/02-Stu_Pull/README.md)—`pull` activity

  * [README.md](Activities/03-Evr_Merge/README.md)—`merge` activity

  * [README.md](Activities/04-Evr_Pull_Requests/README.md)—PR Workflow activity

#### Instructions

* Open the [slideshow](https://docs.google.com/presentation/d/1E1BLzBzc56YO6N2PnRvsJLYuFPpMVvySufm-R9FiFXM) and use slides 1-13 to accompany this next activity.

* Welcome the class, and let remind them that today will mostly be dedicated to projects.

* However, explain that:

  * You'll take a few minutes from the beginning of class to review Git concepts from the previous class as well as  **demonstrate some new (and crucial!) Git commands**

  * Groups will have a series of collaborative Git assignments to work on through the first half of class.

  * Explain that groups should work on the activities until lunch _at latest_, and spend the rest of class working on projects.

* Get started by asking a student to explain what a **branch** is.

* Explain that a **branch** is a timeline: It's its own independent history of changes.

  * In the most basic case, we would create a new branch from the main branch to create and track new changes.

* Point out that there are a number of benefits to making changes and "developing" on a separate branch:

  * It allows collaborators to edit and review changes before they are implemented on the shared `main` branch.

  * We can easily checkout commits unique to our changes without modifying other files.

* Ask a student to define what is **merging**.

* Explain that merging combines two branches together - the files, the commits and all other differences between the two branches are folded together and saved into a single branch.

  * Explain that the most common form of merging compares every pair of file's timelines between the two branches, and keep the one with the most recent updates.

  * When programming we will typically work on new features, bug fixes and other improvements on separate branches from the `main` branch. Once we finish developing and testing, we will merge the feature branches back to the `main` branch.

  * The end result is a _single branch_ with _every change_ made to either `other_branch` or `main`.

* Point out that we can merge branches using a local repository _or_ merge branches from a remote repository.

* Take a moment to demonstrate merging via local repository:

  * Create a new Git repo, and add a simple text file on `main`. Make a series of changes and commits.

  * Checkout a new branch, and change the text file on that branch. Make a different series of changes and commits.

  * Switch back to `main`, and use `git log` to demonstrate the commit history.

  * Then, switch to your development branch, and use `git log` to demonstrate the commit history.

  * Use the appropriate text editor plugin to visualize the differences between the branches: [Git History](https://github.com/DonJayamanne/gitHistoryVSCode) in VS Code, [Git Time Machine](https://github.com/pidu/git-timemachine) for Sublime Text, and [git-time-machine](https://atom.io/packages/git-time-machine) for Atom.

  * Point out that, along the way, we need to be aware if and when multiple branches are tracking changes for the same file.

  * Explain that when a file is modified simultaneously across multiple branches, Git will ask which version "wins" when we merge — this is called a **conflict**.

    * We will practice resolving conflicts later in the course.

* Take another moment to demonstrate merging via remote repository:

  * Navigate to the cloned github repository that we created in last class.

  * Checkout a new branch, and create a simple text file on that branch. Make a different series of changes and commits.

  * Push up your branch to the GitHub remote repository using the `git push origin <branch name>`

  * Demonstrate how to create a PR and merge using the Github interface. Be sure to merge your edited branch to main.

* Remind students that before we merge our branches locally it is important that we ensure that our local branch is up-to-date with the remote repository.

* We can ensure our local branch is up-to-date by performing a `git pull origin <branch name>` before performing the `git merge`.

  * You do not need to wait to use `git pull` when there are new changes, improvements or bug fixes on the remote branch. Pulling down changes to a branch while it is being actively developed is called **fast-forwarding** and is very common in software development.

* Open up [pull.sh](Activities/01-Ins_Pull/Solved/pull.sh), and talk through the `Git` commands it contains.

  * Explain that, to pull from GitHub to a branch that we're on, we checkout the branch and write: `git pull origin <branch name>`.

  * Explain that if you run: `git pull origin main` _while on_ `other_branch`, you will **merge the most recent version of** `main` **on GitHub into** `other_branch`.

* Send out the instructions for each of the activities.

* Send out the [Pull Workflow](Supplemental/PullWorkflow.md) and [Pull Request Workflow](Supplemental/PullRequestWorkflow.md) documents.

* Dismiss class to work on the GitHub activities.

  * Be sure to check-in with each group throughout the activity period to trouble shoot and/or offer conceptual input.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2R9Iqef)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:35  |
|---------------------------|---------------------------|

- - -

## Continue Project Work

| Activity Time:       1:25 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
    <summary><strong>🎉 2.1 Everyone Do: Continue Project Work (01:25)</strong></summary>

* Groups should work on projects for the remainder of class.

</details>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
