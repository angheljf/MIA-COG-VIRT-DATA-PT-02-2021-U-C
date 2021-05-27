# 8.1 Install PostgreSQL and pgAdmin

## Overview

During this lecture, most of class will center on project work.

## Class Objectives

* Students should have the entirety of class to work on their projects.

* Make sure your students make measurable progress with their project work.

* Asks students to confirm their PostgreSQL and pgAdmin installation with TAs.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

Today's class is primarily a project work day. However, this is a great time to have students verify their PostgreSQL and pgAdmin installation. There are often errors when installing new tools, so checking them early will set up the class for success when they reach the SQL unit.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-07-project-1) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

</details>

- - -

# Class Activities

## 1. Install Postgres

| Activity Time:       0:10 |  Elapsed Time:      0:10  |
|---------------------------|---------------------------|

<details>
  <summary><strong>🎉 1.1 Everyone Do: Install Postgres (0:10)</strong></summary>

* **Files:**

  * [pgAdmin_and_Postgres_for_Mac.md](Activities/01-Evr_Installations/Resources/pgAdmin_and_Postgres_for_Mac.md)

  * [pgAdmin_and_Postgres_for_Windows.md](Activities/01-Evr_Installations/Resources/pgAdmin_and_Postgres_for_Windows.md)

* Announce to the class that they will need to install a coding environment capable of executing SQL queries.

* Send out the supplemental guides for students to use for installing pgAdmin and Postgres on their machines.

* Explain to the class that the installations are identical save for the visual components.

* Begin walking the class through the installation, explaining each step as you go:

  * Visit the download link for [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) and select the operating system appropriate for your machine.

  * After the file has been downloaded, Mac users will click on the `postgresql-11.x-osx` file.

  * **Note**: that the version in the image may not match the version on the download page; this is okay and it's because Postgres deploys updates frequently.

    ![postgresql-11.1-1-osx.png](Images/postgresql-11.1-1-osx.png)

  * Windows users will click on the `postgresql-11.x-windows-x64.exe` file.

    ![postgresql-11.1-1-windows-x64.exe](Images/postgresql-11.1-1-windows-x64.png)

  * Navigate through the Setup Wizard and install PostgreSQL. The default location is: `/Library/PostgreSQL/11`.

  * Select the components to be installed. **Be sure to un-check `Stack Builder`**.

  * Mac users will see the following window:

    ![stack_builder_mac.png](Images/stack_builder_mac.png)

  * Windows users will see the following window:

    ![stack_builder_pc.png](Images/stack_builder_pc.png)

  * Next, add your Data Directory. Keep the default location of: `/Library/PostgreSQL/11/data`.

  * When prompted, enter a password. **Be sure to record this password for future use.**

  * Keep the default port as `5432` and in the Advanced Options, locale can be set as `[Default locale]`.

  * The final screen will be the `Pre Installation Summary`.

  * Once the installation is complete, Mac users will find a folder in their Applications with these files:

    ![PostgreSQL_folder.png](Images/PostgreSQL_folder.png)

  * Windows users will be able to access the same files by clicking the start menu on their computer and scrolling to the `Postgres 11` folder.

    ![windows_files.png](Images/windows_files.png)

* **Important** if you are running the Big Sur update for Mac you will need to download the latest version of pgAdmin. Follow these steps to do so:

  * Go to the [pgAdmin download](https://www.pgadmin.org/download/pgadmin-4-macos/) and select the latest version.

  * Click the `.dmg` files to start the download.

  ![pgAdmin dmg file](Images/big_sur_pgadmin.png)

  * Once the download is complete click on the `.dmg` file in your downloads to install.

  * After it has finished installing, drag the `pgAdmin` file into your applications folder (this will take a few minutes).

  * Once the transfer completes you will now be able to use `pgAdmin`. **Note** that you will still have a version in your PostgreSQL folder, but only use the version that you copied into Applications.

* Open pgAdmin, which will open in a new browser tab, and verify that everyone is connected to a local Postgres server before moving on to the next activity.

  ![pgAdmin_browser.png](Images/pgAdmin_browser.png)

  * Students will need to input their password to connect to the server.

    ![server_connect](Images/server_connect.png)

  * **Note:** If the computer seems non-responsive when starting pgAdmin, quickly reboot the machine and try again.

* Make sure that everyone has Postgres installed and a server running before continuing the lesson.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2JBbib9)</sub>

- - -

## 2. Project Work

| Activity Time:       2:45 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 2.1 Students Do: Project Work (2:45)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1yBexCgmWs_N8gafA6guYNot4f204wKCcE4PYJxIHEtA/edit?usp=sharing) and leave slide 18 while students work on their project.

* Students have the rest of class time to work on their projects.

</details>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
