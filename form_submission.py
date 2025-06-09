from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pymysql
import time
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up Chrome options
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Uncomment for headless mode if desired
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver (Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Navigate to the practice login page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    print("Page title:", driver.title)
    time.sleep(2)

    # Find and fill the username field
    input_name = driver.find_element(By.ID, "username")
    input_name.send_keys("student")

    # Find and fill the password field
    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys("Password123")

    # Find and click the form submit button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # Wait for the page to load after submission
    time.sleep(2)

    # Connect to the RDS MySQL database
    conn = pymysql.connect(
        host=os.getenv('RDS_HOST'),
        user=os.getenv('RDS_USER'),
        password=os.getenv('RDS_PASSWORD'),
        database=os.getenv('RDS_DATABASE'),
        port=3306
    )

    # Create a cursor to execute SQL queries
    cursor = conn.cursor()

    # Create a table to store form submissions
    create_table_query = """
    CREATE TABLE IF NOT EXISTS form_submissions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR(255),
        submission_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    cursor.execute(create_table_query)

    # Insert the form data into the table
    sql = "INSERT INTO form_submissions (username, password) VALUES (%s, %s)"
    values = ("student", "Password123")
    cursor.execute(sql, values)

    # Save the changes to the database
    conn.commit()
    print("Data inserted into RDS successfully")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the database connection
    if 'conn' in locals():
        conn.close()
        print("Database connection closed")

    # Close the browser
    driver.quit()
    print("Browser closed")