

# 🏥 Medical Inventory Management System
This Python project is a console-based application for managing a medical inventory, patient records, and doctor details. It's designed to simulate the core functionalities of a hospital or a medical store's administrative system. The application uses a MySQL database to store all data and provides an interactive command-line interface for users to perform various operations.

-----

## 📋 Features

  * **Database Management:** Automatically creates four interconnected tables on the first run: `doc_det` (doctors), `pat_det` (patients), `room_det` (rooms), and `billgenerator` (billing).
  * **CRUD Operations:** Allows for the creation, retrieval, updating, and deletion of records for doctors, patients, and rooms.
  * **User Roles:** Implements a simple login system with two distinct user roles:
      * **Admin:** Has full access to all CRUD operations, as well as the ability to generate graphs, admit patients, and discharge patients.
      * **Staff:** Can only view and search records, and has the ability to admit and discharge patients.
  * **Patient Admissions & Billing:**
      * Manages patient admissions by linking a patient to an available room and a doctor.
      * Generates a bill for a patient upon discharge, calculating the total cost based on the number of days and room price.
  * **Data Visualization:** Generates a bar graph using `matplotlib` to visualize the number of different types of rooms occupied by patients, providing a quick overview of hospital occupancy.
  * **Interactive Interface:** Guides the user through a menu-driven interface to select and execute different functions.

-----

## ⚙️ Requirements

To run this project, you need to have the following installed:

  * **Python 3.x**
  * **MySQL Database**
  * **Python Libraries:**
      * `mysql-connector-python`: To connect Python with your MySQL database.
      * `matplotlib`: For generating the data visualization graphs.

You can install the required Python libraries using pip:

```bash
pip install mysql-connector-python matplotlib
```

-----

## 🖥️ Database Setup

1.  **Create a Database:** First, create a database in your MySQL server. For example, you can name it `med`.

    ```sql
    CREATE DATABASE med;
    ```

2.  **Update Connection Details:** Open the Python script and update the database connection details in the `mysql.connector.connect()` function with your own credentials.

    ```python
    mydb = mysql.connector.connect(
      host="your_host_name",      # e.g., "localhost"
      user="your_username",      # e.g., "root"
      password="your_password",  # your MySQL password
      database="med"             # your database name
    )
    ```

3.  **Run the Script:** The first time you run the script, it will automatically create the necessary tables (`doc_det`, `pat_det`, `room_det`, `billgenerator`) within your `med` database.

-----

## ▶️ How to Run

1.  Ensure you have completed the **Database Setup** steps.

2.  Navigate to the directory containing the Python file in your terminal.

3.  Run the script with the following command:

    ```bash
    python your_file_name.py
    ```

4.  The program will start and prompt you to log in.

-----

## 🔐 User Credentials

The application has a simple login system with hardcoded credentials for demonstration purposes.

| Role  | Username | Password |
| :---- | :------- | :------- |
| **Admin** | `admin`    | `admin1`   |
| **Staff** | `staff`    | `staff2`   |