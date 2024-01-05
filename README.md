# Data Representation Project

Kenneth Linehan, Winter 23/24

This project is a CRUD (Create, Read, Update, Delete) web application that manages information about countries. It includes a Flask web server, a MySQL database, and integration with OpenWeatherMap API for weather information.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [WampServer](https://www.wampserver.com/) - A Windows web development environment that allows you to create web applications with Apache2, PHP, and a MySQL database.
- [Anaconda](https://www.anaconda.com/) - A distribution of Python for data science and machine learning.
- [Python](https://www.python.org/) - The programming language used for the web server.
- [Visual Studio Code](https://code.visualstudio.com/) - An integrated development environment (IDE) used for code editing and debugging. I also used this for coding the html.
- [Flask](https://flask.palletsprojects.com/) - A web framework for Python.
- [OpenWeatherMap API Key](https://openweathermap.org/) - An API key is required for accessing weather information.

## Website Host

I have hosted the website on:
https://kennethlinehan132.pythonanywhere.com/

This will allow a user to use the website without cloning and setting up the database to work. 


## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/KenLin765/data-representation-project.git
   cd data-representation-project

2. **Install WampServer:**
   - Install WampServer and set up the MySQL database. Test creating a database to ensure it's working.

3. **Import API Data (Optional):**
   - The JSON data from [https://restcountries.com/v3.1/all](https://restcountries.com/v3.1/all) is included in the API code folder.

4. **Run Database_Create.py:**
   - This script will create and extract the database to MySQL for use with the website.

5. **Create a Connection to the Database:**
   - Create a file named `db_connection.py` for the database connection. Example connection:
     ```python
     import pymysql

     def get_db_connection():
         conn = pymysql.connect(
             host="localhost",
             user="root",
             password="INPUT YOUR PASSWORD",
             database="countries",
             charset="utf8mb4"
         )
     ```

     Double-check the import in `app.py`:
     ```python
     from db_connection import get_db_connection
     ```

6. **Create an Account on OpenWeatherMap:**
   - Request an API key from [OpenWeatherMap](https://openweathermap.org/api) and add it to `config.py`:
     ```python
     OPENWEATHERMAP_API_KEY = "COPY KEY HERE"
     ```
     Import it into `app.py` securely:
     ```python
     from config import OPENWEATHERMAP_API_KEY
     ```

7. **Setup a Virtual Environment:**
   - On the command prompt, navigate to the folder you have cloned from my GitHub repository. Run the following commands:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

   - Install required packages:
     ```bash
     pip install pymysql flask requests
     ```

8. **Run app.py on Command Prompt:**
   - This should connect now to your database, allowing you to use the project.

9. **On your web browser, visit http://127.0.0.1:5000/:**
   - This will allow you to run my website, which effectively is a way to manage all the countries in the world. It will allow you to create, read, update, and delete details in the database. I also included code that would allow you to check the weather in a capital city.





## Usage

- Visit http://localhost:5000/ to interact with the CRUD web application.

- Explore different functionalities such as creating, reading, updating, and deleting country information.

- The weather functionality requires a valid country name and an API key from OpenWeatherMap.



## Future Improvements

I'd like to do more with this project as I really enjoyed working with the database. I found a separate database which has a countries capital expenditure and other financial aspects and I wanted to introduce this in and combine the data, but I ran out of time. I will try and work on this over the next few weeks as I think I can learn even more this. I also had aims to include more data in the database as I wanted to create a quick quiz, but also ran out of time. I also think the website could look better, I aimed more for performance to get all code working as opposed to design but this is something I will improve.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)