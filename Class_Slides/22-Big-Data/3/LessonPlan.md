# 22.3 Cloud ETL

## Overview

Today's class will introduce students to the extract, transform, and load process, also referred to as ETL. Students will learn how to perform ETL both locally and with data stored in the cloud via Amazon Web Services.

## Class Objectives
By the end of today's class, students will be able to:

* Use Amazon Web Services (AWS) to host data using their RDS and S3 services.

* Create and use databases in the cloud.

* Define and create ETL pipelines in the cloud.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</summary></strong>

* You may find that this lesson falls on a weekday due to a holiday shifting the course schedule. In this case, we have provided notes within the LP that will allow you to **easily adjust the length of the lesson to fit into a weekday class**.

  * Be on the lookout for a ⏰**3-Hour Adjustment** note at the top of activities in this Lesson Plan. If this class is being taught on a weekday, please utilize the directions found in the note. Keep in mind that breaks will be reduced from 40 minutes to the typical 15 minutes for a weekday class as well.

  * Shortening these activities could potentially limit the students' ability to finish them, so please remind them to utilize office hours to clear up any questions they may have.

* **Important!** Sends out the disclaimer for [AWS Free Tier](Activities/00-AWS_Free_Tier/AWS-Free-Tier.pdf) services prior to class. Take some time at the beginning of class to explain that while we are only using free tier services in class, students should review this documentation in order to avoid accidentally incurring charges. **Note**: If the free trial for your personal AWS account has expired, it may be best to create a new account that has access to all free tier options.

* Today's class should be a fun one. Students will put together many different technologies covered so far and learn how they can interact with cloud services.

* There are a few activities that require setup. Have the class follow along and ask questions as you go.

* The students will need to the pgAdmin 4 UI to interact with Postgres database they create in AWS. Be sure everyone has downloaded and installed from [pgAdmin download](https://www.pgadmin.org/download/). **Note** a local psql server is NOT needed.

* Today's class introduces students to ETL with cloud storage. ETL is a critical job skill for data engineers, and students will get a taste of how to manually perform ETL using Python and Amazon Web Services (AWS). Note that this unit focuses on manual ETL with Python and AWS Free Tier, but the concepts can be applied to automated processes and processing pipelines.

* AWS Free Tier is available for 12 months after signing up. This will include free RDS storage up to 25 GB, 750 hours of operational RDS a month (over 31 days), 5 GB of S3 storage, and much more. Visit [https://aws.amazon.com/free/](https://aws.amazon.com/free/) for a more detailed breakdown.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-22-big-data) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Have your TAs keep track of the time with the [Time Tracker](TimeTracker.xlsx).

* Lastly, as a reminder these slideshows are for instructor use only - when distributing slides to students, please first export the slides to a PDF file. You may then send out the PDF file.

</details>

<details>
  <summary><strong>Class Video</strong></summary>

View an example class lecture here: [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=82d67391-968a-46db-9bf3-aa46001e81db). (Note that this video may not reflect the latest lesson plan.)

</details>

- - -
# Class Activities

## 1. Instructor Presentation & Create a PostgreSQL Database

| Activity Time:       0:35 |  Elapsed Time:      0:35  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 1.1 Instructor Do: Welcome Class (0:05) </strong></summary>

* Welcome the class and explain that today's lesson will cover the data pipeline process of ETL, working strictly with cloud services.

</details>

<details>
  <summary><strong> 📣 1.2 Instructor Do: Review Class Objectives (Slide 2) (0:05) </strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/16LqVD9Dgh1YpXMEw_ZwvlML3vqPleH_d4PXQgCW4Z0c/edit?usp=sharing).

* Take a moment to review the objectives for today's class with students. (Slide 2)

</details>

<details>
  <summary><strong> 🎉 1.3 Everyone Do: Create a PostgreSQL Database in RDS (0:15)</strong></summary>

* **Files:**

  * [AWS Free Tier](Activities/00-AWS_Free_Tier/AWS-Free-Tier.pdf)

  * [AWS_RDS_guide.pdf](Supplemental/AWS_RDS_guide.pdf)

* **Important!** Send out the disclaimer for [AWS Free Tier](Activities/00-AWS_Free_Tier/AWS-Free-Tier.pdf) services prior to class. Take some time at the beginning of class to explain that while we are only using free tier services in class, students should review this documentation in order to avoid accidentally incurring charges. **Note**: If the free trial for your personal AWS account has expired, it may be best to create a new account that has access to all free tier options.

* Students can follow this activity along with a PDF guide. Send it out: [AWS_RDS_guide.pdf](Supplemental/AWS_RDS_guide.pdf)

* Send out the following link to [AWS Free Tier](https://aws.amazon.com/free/) and ask students to create a Free Tier account.

* Explain to students that today's class will utilize Amazon Web Services. Everything used in class will be available under Amazon's Free Tier program, but students should be careful not to choose any options that have a cost associated with it. Students should also delete their RDS databases after class so that no further costs are incurred. We will cover the steps for deleting RDS databases at the end of class.

* Log in to the AWS Management Console and navigate to the **RDS** section under **Database**.

  ![rds_console](Images/rds_console.png)

* Click **Create database** from the **Create database** section to the right. This button will take you to the **Engine options** page, which brings up a menu of different relational databases. **Note** AWS may have a different screen than the one pictured below. If this is the first time using the service, the orange **Create database** will still be on the right.

  ![create_db_button](Images/create_db_button.png)

  **Note**: There may be an option to create a database with Amazon Aurora, which is a paid database. We will not be using this in today's lesson.

* Check the box next to **Only enable options eligible for RDS Free Usage Tier** at the bottom of the menu.

* Select **PostgreSQL**.

  ![postgres_select](Images/postgres_select.png)

* Under **Templates** select **Free Tier**.

  ![Free Tier](Images/free_tier.png)

* Fill out the fields under Settings. Use **myPostgresDB** as the database instance identifier and **root** as the master username.

  **Note**: While the database instance identifier and master username can be anything, we recommend sticking to these settings in this case for consistency.

* Uncheck the **Auto generate password** box. Enter a password and be sure to record it somewhere. The other settings will be accessible in the future, but the password will not.

  ![db settings](Images/db_settings.png)

* Under **Connectivity** click the down arrow next to **Additional connectivity configuration**. Select **Yes** under the **Public accessibility** option. Explain that this does not mean anyone can access the database, as a password is still required, but it allows connections from outside sources like pgAdmin.

  ![public accessible](Images/public_accessible.png)

* Under **Additional configuration**, click the down arrow and make the database name **my_data_class_db**. (Use this name for the sake of consistency. In the future, any name can be used.) Keep the default settings in the other fields.

  ![database_options](Images/database_options.png)

* Uncheck the boxes for **Enable automatic backups**, **Enable performance insights**, and **Enable auto minor version upgrade**.

  ![additional options](Images/additional_options.png)

* Leave everything else as is and be sure to mention to students the **Estimated monthly costs** at the end. Send out the link to [AWS Free Tier Link](https://aws.amazon.com/rds/free/) and explain:

  * Free tier was selected so these costs will not occur.

  * We will clean up the database at the end of class to make sure nothing is left running.

* Click **Create Database** followed by **View DB Instance details** to navigate to the instance console page. The database creation on AWS's end will take anywhere from 10 to 15 minutes.

</details>

<details>
  <summary><strong> 📣 1.4 Instructor Do: Cloud ETL Slideshow (Slides 3–6) (0:10)</strong></summary>

* Go through the slideshow and explain the following:

  * The data is stored in AWS S3 buckets. A cloud connection is made to a Colab notebook, and the data is extracted into a PySpark DataFrame. (Slide 4)

  * Using the cloud notebook Colab, PySpark is used to transform the DataFrame. (Slide 5)

  * Once the transformations are complete, Colab will create a connection to an RDS instance and load in the data. (Slide 6)

  </details>


<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2VcrPYr)</sub>


## 2. AWS S3

| Activity Time:       0:25 |  Elapsed Time:      1:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 2.1 Instructor Do: AWS S3 Intro (Slides 7–10) (0:10) </strong></summary>

* Go through the slideshow and explain the following:

  * Simple Storage Service, or S3, is Amazon's cloud file storage service that uses key-value pairs. Files are stored on multiple servers and have a high rate of availability. (Slide 8)

  * S3 uses *buckets* to store files, which are similar to computer folders or directories. Buckets can contain additional folders and files. Each bucket must have a unique name. (Slide 9)

  * S3 has fine-grained control over files, such as read and write permissions. Buckets can assign individual access or total public access. (Slide 10)

</details>

<details>
  <summary><strong> 🎉 2.2 Everyone Do: Cloud Storage with S3 (0:15) </strong></summary>

* **Files:**

  * [dog.png](Activities/01-Evr_S3/Resources/dog.png)

  * [S3_guide.pdf](Supplemental/S3_guide.pdf)

* Send out the PDF guide for students.

* Explain the following points:

  * AWS's S3 is a cloud-based file storage service.

  * Files are stored on multiple servers, providing redundancy for data.

  * Amazon guarantees an uptime, or availability, of over 99.99% for S3 files.

  * On S3, files are organized by buckets.

  * The S3 bucket structure is somewhat similar to a GitHub repository, which also holds files and folders.

  * Each S3 bucket must have a URL that is unique across AWS.

  * An S3 bucket can contain files, but it cannot contain another bucket.

  * In this case, the region precedes `amazonaws.com`, followed by the bucket name and the filename.

    ![Images/s300.png](Images/s300.png)

  * S3 provides a high level of control over the files. At both the bucket and file levels, it is possible to control read and write access to different individuals and organizations.

* Tell students to follow along for the rest of the activity.

  * Go to console.aws.amazon.com and select S3 under Storage.

    ![s3 console](Images/s3_console.png)

  * Click **Create bucket**.

    ![click create](Images/create_bucket.png)

  * Create a bucket name and choose the region.

  * **Note:** The bucket name must be unique across all existing bucket names in Amazon S3. Buckets cannot be renamed or created inside of another bucket.

  * Leave the region as the default `US East (N. Virginia)`. Changing the region will change the object Url used in all examples today.

    ![Images/s301.png](Images/s301.png)

  * Most of the options on the **Configure Options** tab can be left as the default values.

  * Tags are user-defined key-value pairs of information that can help keep track of buckets.

  * Click **Next**.

    ![Images/s302.png](Images/s302.png)

  * The **Set Permissions** page is where we grant others permission to access buckets.

    * A number of [security breaches](https://securityboulevard.com/2018/01/leaky-buckets-10-worst-amazon-s3-breaches/) were caused by unsecured S3 buckets.
    * Public access is denied by default.

  * Leave the boxes checked and click **Next**.

    ![Images/s303.png](Images/s303.png)

  * The **Review** page is a summary of the bucket configurations. Click **Create bucket**. The bucket name now appears in the S3 console.

    ![Images/s304.png](Images/s304.png)

    ![Images/s305.png](Images/s305.png)

  * Explain that we'll now upload a file to the newly created bucket. Click the bucket name and then click **Upload**.

  * A file can be dragged to the screen. Demonstrate by uploading [dog.png](Activities/01-Evr_S3/Resources/dog.png) into the S3 bucket.

  * Click **Upload**.

    ![Images/s315.png](Images/s315.png)

    ![Images/s316.png](Images/s316.png)

  * Click the filename.

    ![Images/s317.png](Images/s317.png)

  * Explain why clicking the link leads to an error message.

    ![Images/s308.png](Images/s308.png)

    ![Images/s309.png](Images/s309.png)

  * By default, the permission for the file denies access to everyone, so it needs to be changed.

  * Navigate back to the dashboard by clicking **Amazon S3** on the top left.

    ![Images/s3_dashboard](Images/s3_dashboard.png)

  * Check the box next to your bucket and click **Edit public access settings**.

    ![Images/edit_public.png](Images/edit_public.png)

  * Make sure all boxes are unchecked on the next screen. Even though these were checked in the initial setup, they will not be now.

    ![Images/bucket_public.png](Images/bucket_policy.png)

  * Click **Save**. Then type **confirm** and click **Confirm**.

    ![Images/confirm_policy.png](Images/confirm_policy.png)

  * Next, navigate back into your bucket and check the box next to the image. Click the **Actions** box on the top and select **Make public**.

    ![Images/bucket_public.png](Images/bucket_public.png)

  * Now the image will be displayed when you click on the link.

* Tell students that they can explore various settings at the bucket level and the file level. Use the tabs at the bucket level to illustrate the available settings, such as tags:

  ![Images/s306.png](Images/s306.png)

* **Note:** Students can remove public access anytime by repeating the steps above and checking all the boxes in **Edit public access settings**.

</details>


<sub>[Having issues with this activity? Report a bug!](https://bit.ly/39Uf1eT)</sub>


## 3. PostgreSQL

| Activity Time:       0:40 |  Elapsed Time:      1:40  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 3.1 Instructor Do: PostgreSQL on RDS Introduction (0:10)</strong></summary>

* First make sure that everyone has a database to use. Database creation was initiated at the beginning of class. Students whose databases are not yet running should follow along with a partner until their database is available.

* Explain the following about the new RDS database:

  * RDS stands for Relational Database Service. This is what Amazon uses to host a variety of relational databases in the cloud.

  * These databases can have different dialects, such as MySQL, PostgreSQL, and Amazon's own Aurora database.

  * The database that was created at the beginning of class uses PostgreSQL.

* Navigate to the DB instance in the console created earlier. There will be a lot of information available, but we'll use only a few points of interest. Go over the console page, explaining these key points:

  * The **Summary** section shows the kind of database the instance is and whether it is available.

    ![db summary](Images/db_summary.png)

  * The database metrics can largely be ignored for now.

  * The **Connectivity** tab lists the endpoint, port, and security groups associated with the instance. The endpoint will be used to connect to the database.

    ![db connection](Images/db_connection.png)

  * The rest of the tabs contain more information about the instance, such as backups and logs, but students will not need to be concerned with this for class.

  </details>

<details>
  <summary><strong> 🎉 3.2 Everyone Do: RDS PostgreSQL and pgAdmin (0:15)</strong></summary>

* **File:**

  * [RDS_pgAdmin_guide.pdf](Supplemental/RDS_pgAdmin_guide.pdf)

* Sends out the PDF guide, which students can use to follow along.

* Make sure everyone has the pgAdmin 4 UI installed. Direct students who do not have it installed to the [pgAdmin download page](https://www.pgadmin.org/download/) to download the appropriate version for their operating system.

* Open up the pgAdmin UI. Explain the following to students:

  * pgAdmin can connect to a cloud-based database, such as AWS, as well as local databases.

  * pgAdmin offers a visual interface for managing data.

* Log in to the AWS console and navigate to **RDS** under **Database**.

  ![RDS console](Images/rds_console.png)

* Navigate to **Instances** in the **Resources** section to the right.

  ![instance_menu.png](Images/instance_menu.png)

* Go to the database created earlier, `mypostgresdb`.

* Navigate to the **Security Group** rules section on the right and explain the following:

  * These security groups tell the RDS instance what traffic is allowed into and out of the database.

  * The security settings can range from restrictive to open.

  * In this activity, the database will be open to all traffic; however, this is not recommended for production code.

* Click the security group for type **CIDR/IP - Inbound**.

  ![security_inbound](Images/security_indbound.png)

* This will navigate to a new page. Follow these steps to give the database access to all inbound traffic:

  * From the management console, navigate to the Inbound tab on the bottom part of the screen, and then click **Edit**. This will bring up a menu to set rules for the security group.

    ![inbound_edit](Images/inbound_edit.png)

  * Change the Source to **Anywhere** and click **Save**. The RDS instance will now accept a connection from anywhere. This isn't completely open to the world because the endpoint, username, and password are still needed to connect.

      ![ip_source](Images/ip_source.png)

* Navigate back to the instance console and have the class find the endpoint, which is found in the **Connectivity** tab.

  ![db connection](Images/db_connection.png))

* Open up pgAdmin, right-click on **Servers**, and then go to **Create - Server**. Then walk through the following steps to create a connection to the AWS RDS instance:

  * Under the **General** tab, enter the server name as **my_aws_postgres_rds**.

    ![server name](Images/general_tab.png)

  * Under the **Connection** tab, do the following:

    * Enter the Endpoint in the **Hostname/address** field. This is unique to the instance.

    * Enter 'postgres' in the **Maintenance database** field. This is the default for all postgres RDS instances.

    * Enter the Username in the **Username** field, which is `root` in this case.

    * Enter the password that was created for your RDS instance.

    * Check the box next to **Save Password**.

  * Click **Save**. If all information is entered correctly, this will set up the connection and not return an error.

    ![connection tab](Images/connection_tab.png).

* Have the TAs verify that every student has a working connection in pgAdmin. Since the class should be using the same username and DB name, the biggest issue could be passwords.

</details>

<details>
  <summary><strong> 🎉 3.3 Everyone Do: Create, Read, Update, and Delete (CRUD) with RDS (0:15)</summary></strong>

* Open up pgAdmin and send out [schema.sql](Activities/02-Evr_RDS_CRUD/Solved/schema.sql). Before running the code, explain the following:

  * The four basic functions of persistent data storage are created, read, update, and delete (CRUD).

  * This schema consists of the first part of CRUD, create.

  * The schema will create the tables. The insertion creates the data.

  * A foreign key is used in the `patients` table to reference the `doctor` table.

* Create a new database named `medical`, open a query tool, and then run the schema. This creates two tables and uploads the data.

* Sends out and open [query.sql](Activities/02-Evr_RDS_CRUD/Solved/query.sql). Run through the queries one at a time, explaining the following points:

  * The read functions of a database are run with `SELECT` statements.

  * An error will occur after running the first `INSERT`. This is because the `doctor_id` key 22 does not exist in the `doctor` table.

  * The second `INSERT` statement will run because the foreign key is located in the `doctor` table.

  * The update functions are run with `UPDATE`.

  * The delete functions are run with `DELETE`.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/39OxmK8)</sub>

## 4. ETL with S3, PySpark and RD

| Activity Time:       0:40 |  Elapsed Time:      2:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 4.1 Instructor Do: ETL with S3, PySpark, and RDS (0:10)</summary></strong>

* Before navigating to AWS open up pgAdmin and navigate to the AWS connection on the left hand side and create a database called `my_data_class_db` within our RDS instance.

* Open the AWS console and navigate to S3 under **Storage**.

* Create a bucket and upload [user_data.csv](Activities/03-Ins_ETL_S3_RDS/Resources/user_data.csv) and [user_payment.csv](Activities/03-Ins_ETL_S3_RDS/Resources/user_data.csv), making sure they are made public.

* Return to pgAdmin and run [schema.sql](Activities/03-Ins_ETL_S3_RDS/Solved/schema.sql) in `my_data_class_db` RDS database. Review the schema and explain the following:

  * The schema defines three unique tables.

  * Each table is normalized and represents, or models, different data.

  * This schema is only being used to create and simulate a production database.

  * The ETL process will need to `extract` the necessary data from the CSVs, `transform` it, and then `load` the data into these tables.

* Open [etl_s3_rds](Activities/03-Ins_ETL_S3_RDS/Solved/ins_etl_s3_rds.ipynb) in Colab. Update `<bucket name>` with the name of your bucket just created. **Note:** some buckets will add the location to Object URL, such as `https://s3.us-east-2.amazonaws.com/<bucket name>/user_data.csv`. If an error is returned, grab the object URL from the file and use that instead. Go through the code, explaining the following:

  * Colab needs to install a postgres driver in order for the notebook to load our end result in an RDS. Then it will store the driver into the Spark application.

  ```python
    !wget https://jdbc.postgresql.org/download/postgresql-42.2.9.jar

    from pyspark.sql import SparkSession
    spark = SparkSession.builder.appName("CloudETL").config("spark.driver.extraClassPath","/content/postgresql-42.2.9.jar").getOrCreate()
  ```

  * The Colab notebook reads in the file from S3 and stores it into a PySpark DataFrame. The   argument `inferSchema` will assign the correct data types; otherwise, everything will be returned as a string.

    ```python
    from pyspark import SparkFiles
    # Load in user_data.csv from S3 into a DataFrame
    url = "https://<bucket name>.s3.amazonaws.com/user_data.csv"
    spark.sparkContext.addFile(url)

    user_data_df = spark.read.option('header', 'true').csv(SparkFiles.get("user_data.csv"), inferSchema=True, sep=',')
    user_data_df.show(10)
    ```

* Pulling this file from S3 is part of the `extract` process of ETL.

* The PySpark DataFrame will be used to help `transform` the data.

* The next step is to merge the two DataFrames before beginning the cleanup process.

* In this case, part of the `transform` step in the ETL process is to clean the data and remove duplicate or incomplete entries. This can be accomplished with `dropna()` in Pandas.

* The next step creates three new DataFrames that store the information needed to populate the existing tables in the production database. The DataFrame columns should match the table column names.

* Refer back to the schema for the three tables that were created earlier: `active_user`, `billing_info`, and `payment_info`.

* To push the DataFrames up to the database, the mode is set to `append`, the URL is set, and a configuration with the database details is stored into a dictionary.

* PySpark then uses the configuration dictionary to connect to RDS and writes the DataFrame contents to the database.

  ```python
  # Append DataFrame to active_user table in RDS
  mode = "append"
  jdbc_url="jdbc:postgresql://<endpoint>:5432/my_data_class_db"
  config = {"user":"root", "password": "<password>", "driver":"org.postgresql.Driver"}
  clean_user_df.write.jdbc(url=jdbc_url, table='active_user', mode=mode, properties=config)
  ```

* The queries in [query.sql](Activities/03-Ins_ETL_S3_RDS/Solved/query.sql) can be used with pgAdmin to check that data has successfully loaded to their tables.

</details>

<details>
  <summary><strong> ✏️ 4.2 Student Do: ETL with S3, PySpark, and RDS (0:20)</summary></strong>

* **⏰ 3-Hour Adjustment**: Reduce activity time to 15 minutes.

* **Files:**

  * [employees.csv](Activities/04-Stu_ETL_S3_Colab/Resources/employees.csv)

  * [stu_etl_s3_rds.ipynb](Activities/04-Stu_ETL_S3_Colab/Unsolved/stu_etl_s3_rds.ipynb)

* **Instructions:**

  * [README.md](Activities/04-Stu_ETL_S3_Colab/README.md)

  </details>

<details>
  <summary><strong> ⭐ 4.3 Review Activity (0:10)</summary></strong>

* **Files:**

  * [stu_etl_s3_rds.ipynb](Activities/04-Stu_ETL_S3_Colab/Solved/stu_etl_s3_rds.ipynb)

  * [query.sql](Activities/04-Stu_ETL_S3_Colab/Solved/query.sql)

  * [schema.sql](Activities/04-Stu_ETL_S3_Colab/Resources/schema.sql)

* Before walking through the code, emphasize that students are already familiar with most of the processes used in the activity. The new ETL process involves extracting data from S3, transforming the data with PySpark, and loading the data into RDS.

* Explain to students that the first requirement of the activity is to upload the CSV file to S3.

  * Students should already have an existing bucket, but they are free to create a new one.

  * If a student asks why we're uploading and downloading the same file, respond that we're assuming the data is already stored in the cloud.

  * The AWS resources used fall well below the free tier threshold. However, as a safety measure, it is best to clean up resources by deleting them after use. AWS does not cap resource usage and will auto-scale if needed. If usage ever goes beyond the free tier, you will be charged for those resources.

* In Colab upload the unsolved Jupyter Notebook file:

  ![Images/colab00.png](Images/colab00.png)

* The first two Colab cells install Spark and start a Spark Session..

* Explain that the next cell reads in the data source from S3:

```python
from pyspark import SparkFiles
# Load in employee.csv from S3 into a DataFrame
url = "https://<INSERT_BUCKET>.amazonaws.com/employees.csv"
spark.sparkContext.addFile(url)

df = spark.read.option('header', 'true').csv(SparkFiles.get("employees.csv"), inferSchema=True, sep=',')
df.show(10)
```

* You will have to replace the bucket name.

* Preview the first 10 rows of the DataFrame:

  ![Images/colab03.png](Images/colab03.png)

* Open the [SQL schema](Activities/04-Stu_ETL_S3_Colab/Resources/schema.sql):

  ```sql
  CREATE TABLE employee_personal_info (
      employee_id INTEGER PRIMARY KEY NOT NULL,
      email VARCHAR,
      marital_status VARCHAR,
      gender VARCHAR,
      salaried VARCHAR
  );

  CREATE TABLE employee_password (
      employee_id INT PRIMARY KEY NOT NULL,
      password TEXT
  );
  ```

* Contrast the desired data output of the SQL table schema with the current input seen in the DataFrames.

  * The DataFrames have multiple unnecessary columns.

  * The column names in the SQL tables are lowercase.

* Pause for a moment to go over the steps that might be taken with Spark to achieve our goal.

  * Clean the data by deleting unnecessary columns.

  * Clean the data by deleting rows that contain incomplete or duplicate data.

  * Rename the DataFrame columns to match those in the SQL tables.

  * Create new DataFrames with rows that will be inserted in the two SQL tables.

  * Load the DataFrames into the SQL database.

* In the next steps, use the `dropna()` and `dropDuplicates()` methods to drop rows containing junk data:

  ![Images/colab04.png](Images/colab04.png)

* Open pgAdmin and explain that the table schema are loaded into RDS. The actual rows of data from the DataFrames will be loaded into these tables on RDS.

  ![Images/etl05.png](Images/etl05.png)

* Examine the DataFrame schema.

  ![Images/colab06.png](Images/colab06.png)

* Explain that the columns that will be exported into SQL are renamed in lowercase letters. Also, following convention, spaces are replaced with underscores.

  ![Images/colab07.png](Images/colab07.png)

* Explain that a new DataFrame called `employee_personal_info` is created with the columns needed for its SQL counterpart.

  ![Images/colab08.png](Images/colab08.png)

* Explain that this cell sets the configuration for the Postgres database.

  ![Images/colab09.png](Images/colab09.png)

  * The endpoint and password will need to be inserted here.

  * Since the schema for the SQL table `employee_personal_info` was already created in Postgres, the `mode` here is `append` rather than `overwrite`.

* Explain that this cell inserts the data from the DataFrame into a SQL table.

  ![Images/colab10.png](Images/colab10.png)

* Verify that the table has been populated in pgAdmin with a query:

  ```sql
  SELECT * FROM employee_personal_info;
  ```

* Repeat the above steps for the `employee_password` DataFrame and table.

  * First select the columns.

  ![Images/colab11.png](Images/colab11.png)

  * Write to the database.

  ![Images/colab12.png](Images/colab12.png)

* A new DataFrame is created and loaded into RDS.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2RpNADg)</sub>

- - -

## Break

| Activity Time:       0:40 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

⏰ **3-Hour Adjustment**: Reduce break time to 15 minutes.

- - -

## 5. RDS to Google Colab & AWS Cleanup

| Activity Time:       1:00 |  Elapsed Time:       4:00 |
|---------------------------|---------------------------|


<details>
  <summary><strong> 🎉 5.1 Everyone Do: AWS Cleanup (0:20)</summary></strong>

* **⏰ 3-Hour Adjustment**: Reduce activity time to 15 minutes.

* Explain to students that everything we have done today will fall under the AWS Free Tier. However, as a precaution, we will delete everything we created. Let students know that they can recreate everything using the processes learned today.

* To delete the RDS database, follow these steps:

  * Log in to the AWS management console and navigate to the **RDS** dashboard. Click **DB Instances**.

    ![DB instance](Images/db_instance.png)

  * Select **DB Name** and click **Modify**.

    ![Modify DB](Images/modify_db.png)

  * Scroll down to Deletion Protection and un-check the box next to **Enable deletion protection**. Then click **Continue** and **Modify DB Instance**.

    ![deletion protection](Images/delete_proc.png)

  * Next, on the database dashboard, make sure the database is checked and then click **Actions** followed by **Delete**.

    ![delete DB](Images/delete_db.png)

  * **Important:** Un-check **Create final snapshot?** and check the acknowledgement box. Type **delete me** and click **Delete**. If you do not un check this box, your databases will create a back up that could accrue additional costs so be sure not to skip over this step.

    ![final delete](Images/final_delete.png)

  * This will take a few minutes to fully delete.

* To delete any S3 buckets, navigate to S3 dashboard and follow these steps:

  * **Note:** This process will delete the whole bucket with all its contents. For sake of time, this will be the process. Mention to students that individual files inside a bucket might be deleted as well.

  * Check the box next to the bucket you want to delete and click **Delete**.

  ![select bucket](Images/select_bucket.png)

  * Type the name of the bucket and click **Confirm**.

  ![delete bucket](Images/delete_bucket.png)

  * The bucket and all of its files are now deleted.

  * Sends out the [AWS Billing Check](AWS_check_billing.pdf) that instructs students how to double their billing costs.

</details>

<details>
  <summary><strong> ✏️ 5.2 Student Do: PySpark Review (0:20)</strong></summary>

* ⏰**3-Hour Adjustment**: Skip this **Student Do** activity and continue on to the review activity.

* In this activity, students will review PySpark by working with sample datasets.

* **Files:**

  * [Q1_unsolved.ipynb](Activities/05-Stu_Big_Data_Review/Unsolved/Q1_unsolved.ipynb)

  * [Q2_unsolved.ipynb](Activities/05-Stu_Big_Data_Review/Unsolved/Q2_unsolved.ipynb)

  * [Q3_unsolved.ipynb](Activities/05-Stu_Big_Data_Review/Unsolved/Q3_unsolved.ipynb)

  * [Q4_unsolved.ipynb](Activities/05-Stu_Big_Data_Review/Unsolved/Q4_unsolved.ipynb)

* **Instructions**

  * [README.md](Activities/05-Stu_Big_Data_Review/README.md)

</details>

<details>
  <summary><strong> ⭐ 5.3 Review Activity (0:20)</strong></summary>

* ⏰**3-Hour Adjustment**: This review activity is now an **Everyone Do**.

* Review the previous activity with the class.

* **Files:**

  * [Q1_solved.ipynb](Activities/05-Stu_Big_Data_Review/Solved/Q1_solved.ipynb)

  * [Q2_solved.ipynb](Activities/05-Stu_Big_Data_Review/Solved/Q2_solved.ipynb)

  * [Q3_solved.ipynb](Activities/05-Stu_Big_Data_Review/Solved/Q3_solved.ipynb)

  * [Q4_solved.ipynb](Activities/05-Stu_Big_Data_Review/Solved/Q4_solved.ipynb)

* Open `Q1_unsolved` in Google Colab and ask for a volunteer to explain the solution. Code along to solve the question using `Q1_solved.ipynb` as guidance. Explain the solution:

  * First, select the columns `coffee_shop_name` and `num_rating`.

  * Use `groupby("coffee_shop_name")` and aggregate the average rating and count of coffee shops.

  * Finally, order the results in descending order to find the coffee shop with the most reviews.

  * The answer is 3.8125 for Epoch Coffee.

* Next, open `Q2_unsolved` in Google Colab and and ask for a volunteer to explain the solution. Code along to solve the question using `Q2_solved` as guidance. Explain the solution:

  * Group the data by `coffee_shop_name` while aggregating the count of coffee shops.

  * Order the results by count to find the shop with the fewest reviews.

  * The answer is Lola Savannah Coffee Downtown.

* Next, open `Q3_unsolved` in Google Colab and and ask for a volunteer to explain the solution. Code along to solve the question using `Q3_solved` as guidance. Explain the solution:

  * Here, `df.count()` is used to find the rows and `len(df.columns)` is used to find the number of columns.

  * The answer is 7616 rows and 2 columns.

* Finally, open `Q4_unsolved` in Google Colab and and ask for a volunteer to explain the solution. Code along to solve the question using `Q4_solved` as guidance. Explain the solution:

  * The DataFrame is grouped by date and then aggregates the count of each date.

  * The resulting DataFrame is sorted in descending order to find the date with most reviews.

  * The answer is "2016-01-09".

* Answer any questions that students may have before ending class.

</details>

<sub>[Having issues with this activity? Report a bug!](https://bit.ly/2URB7du)</sub>

- - -

# End Class

- - -

## 6. Structured Office Hours

| Activity Time:       0:30 |  Elapsed Time:       4:30 |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 6.1 Instructor Do: Structured Office Hours-Review ETL in the Cloud (0:30)</strong></summary>
* Go over the following exercise for students looking for extra practice with ETL in the cloud.

* **Files:**

  * [ratings_and_sentiments.csv](Activities/06-Stu_Cloud_ETL_Project/Resources/ratings_and_sentiments.csv)

  * [cloud_etl_analysis.ipynb](Activities/06-Stu_Cloud_ETL_Project/Solved/cloud_etl_analysis.ipynb)

  * [cloud_etl_nlp.ipynb](Activities/06-Stu_Cloud_ETL_Project/Solved/cloud_etl_nlp.ipynb)

* Import the [cloud_etl_analysis.ipynb](Activities/06-Stu_Cloud_ETL_Project/Solved/cloud_etl_analysis.ipynb) notebook into Google Colab. Go through the code and explain the following:

  * Data is imported from an S3 bucket and stored in a DataFrame.

  * The first table calls for the coffee shop's name, average rating, and the total amount of ratings.

  * The columns `coffee_shop_name` and `num_rating` will correspond to this and are selected.

  * The selected data is then grouped by `coffee_shop_name` and aggregated with the average of the ratings and the count of `coffee_shop_name`.

  * To finish, the columns are renamed and ordered by descending values. Note `desc` coming from `from pyspark.sql.functions import desc`.

  * The next data has its information in the `review_text` column and is selected.

  * The `withColumn` method allows manipulation of columns. The regex extraction function will create two new columns from `review_text`: one column with the date and the other with the text.

* Alert students that `regexp_extract` is an advanced command that is being used here to separate data; it is nothing to overthink. If students are curious about regex, encourage them to learn more on their own.

  * The new columns are selected, and any null rows are dropped.

  * The next DataFrame groups by the date and aggregates the data by getting the total number of times each date appeared using `count`. The DataFrame is then renamed and reordered in descending order.

* Answer any questions about the previous steps, and then import [cloud_etl_nlp.ipynb](Activities/06-Stu_Cloud_ETL_Project/Solved/cloud_etl_nlp.ipynb) into Google Colab. Go through the code and explain the following:

  * Like the `review_text` cleanup from earlier, data is read in and cleaned up. This time, the `num_rating` column needs to be renamed `label` to be passed into the model later.

  ```python
  from pyspark.sql.functions import regexp_extract, length
  review_df = new_df.withColumn("date", regexp_extract("review_text", "\d+/\d+/\d+", 0))\
      .withColumn("review_text", regexp_extract("review_text", "\d+/\d+/\d+(?:\s)(.*)", 1))\
      .withColumnRenamed("num_rating", "label")\
      .select(["label", "date", "review_text"])
  ```

  * A length column is also created, and null values are dropped.

  ```python
  review_df = review_df.withColumn('review)length', length(review_df['review_text'])).dropna()
  ```

  * The first part of the pipeline is to convert the text into something the computer can read by tokenizing, removing stop words, hashing, and fitting to the IDF model.

    Note: `string indexer` is not needed here because the label is already a number.

  ```python
    from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF
    # Create all the features to the data set
    tokenizer = Tokenizer(inputCol="review_text", outputCol="token_text")
    stopremove = StopWordsRemover(inputCol='token_text',outputCol='stop_tokens')
    hashingTF = HashingTF(inputCol="token_text", outputCol='hash_token')
    idf = IDF(inputCol='hash_token', outputCol='idf_token')
  ```

  * The features are created from the `idf_token` and `review_length` using `VectorAssembler`. Everything is then passed into the pipeline.

  * After the pipeline, the data is fit and transformed.

  * The transformed data is split into a test set and training set, and then fit into the Naive Bayes model.

  ```python
  from pyspark.ml.classification import NaiveBayes
  # Break data down into a training set and a testing set
  training, testing = cleaned.randomSplit([0.7, 0.3])

  # Create a Naive Bayes model and fit training data
  nb = NaiveBayes()
  predictor = nb.fit(training)
  ```

  * The testing is transformed.

  * Finally, using `MulticlassClassificationEvaluator`, the accuracy of the model can be predicted.

* Explain that the result is that the model was not very accurate at predicting the rating.

  * The features passed in were the length of reviews and a natural language breakdown of the review.

  * These features weren't strong enough to determine which are more likely to be negative or positive reviews.

  * The length of a review does not indicate whether a review will be positive or negative.

  * Word choice also does not necessarily indicate whether a review is positive or negative. Words that you think might only appear in a positive review, like great (e.g., "Coffee was great") can also appear in negative reviews (e.g., "It would be great if they got my order correct").

  </details>

- - -

## References

Mockaroo, LLC. (2021). Realistic Data Generator. [https://www.mockaroo.com/](https://www.mockaroo.com/)

Microsoft. (2017). Adventure Works sql Server Sample. [https://github.com/microsoft/sql-server-samples/blob/master/samples/databases/adventure-works/oltp-install-script/Employee.csv](https://github.com/microsoft/sql-server-samples/blob/master/samples/databases/adventure-works/oltp-install-script/Employee.csv)

Woods, Rachel. (2016). Austin Coffee Shop Yelp Reviews. [https://data.world/rdowns26/austin-coffee-yelp-reviews](https://data.world/rdowns26/austin-coffee-yelp-reviews)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
