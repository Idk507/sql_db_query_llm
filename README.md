SQL Query Assistant with Gemini AI
A Streamlit-based web application that converts natural language questions into SQL queries using Google's Gemini AI model. The application allows users to query a SQLite database using simple English questions.
Features

Natural language to SQL query conversion
Interactive web interface built with Streamlit
Integration with Google's Gemini Pro AI model
SQLite database support
Real-time query execution and result display

Prerequisites
Before running this application, make sure you have the following:

Python 3.7 or higher
Google Cloud API key for Gemini AI
SQLite database named "student.db" with the following schema:
sqlCopyCREATE TABLE STUDENT (
    NAME TEXT,
    CLASS TEXT,
    SECTION TEXT
);


Installation

Clone the repository:

bashCopygit clone <repository-url>
cd sql-query-assistant

Install the required dependencies:

bashCopypip install streamlit python-dotenv google-generativeai sqlite3

Create a .env file in the project root and add your Google Cloud API key:

CopyGOOGLE_API_KEY=your_api_key_here
Usage

Start the Streamlit application:

bashCopystreamlit run app.py

Open your web browser and navigate to the provided local URL (typically http://localhost:8501)
Enter your question in natural language (e.g., "How many students are in Data Science class?")
Click the "Ask the question" button to get your results

Example Questions

"How many entries of records are present?"
"Tell me all the students studying in Data Science class"
"List all students in Section A"

Application Structure

app.py: Main application file containing the Streamlit interface and core functionality
student.db: SQLite database file containing student records
.env: Environment variables file (create this yourself)

Functions
get_gemini_response(question, prompt)
Converts natural language questions to SQL queries using the Gemini AI model.
read_sql_query(sql, db)
Executes SQL queries on the SQLite database and returns the results.
Database Schema
The application uses a SQLite database with the following structure:
sqlCopyCREATE TABLE STUDENT (
    NAME TEXT,      -- Student's full name
    CLASS TEXT,     -- Class/Course name
    SECTION TEXT    -- Section identifier
);
Contributing

Fork the repository
Create a new branch (git checkout -b feature/improvement)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/improvement)
Create a Pull Request

Error Handling
The application includes basic error handling for:

Invalid SQL queries
Database connection issues
Missing API keys
Invalid user inputs

Security Notes

Never commit your .env file or expose your API keys
The application currently accepts all user inputs - implement proper input validation for production use
Consider implementing user authentication for production deployment

Future Improvements

Add support for more complex SQL queries
Implement query history
Add export functionality for query results
Support for multiple database types
Add unit tests and integration tests

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

Google Gemini AI for natural language processing
Streamlit for the web interface
SQLite for database management