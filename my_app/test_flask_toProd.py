import pytest
import mysql.connector
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


# Run before to the tests
# =======================
@pytest.fixture
def setup():
    chrome_driver_path = ChromeDriverManager().install()
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--headless")
    service_obj = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    yield driver
    driver.quit()


# ======  Test 1  ======
def test_signup_1(setup):
    driver = setup
    driver.get("http://54.84.147.134:5000/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "(//button[normalize-space()='Sign-in'])[1]").click()
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Bruce Springsteen")
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    message = driver.find_element(By.XPATH, "//h1[normalize-space()]").text

    # Establish connection to database
    connection = connect_to_database()
    cursor = connection.cursor()
    # Prepare the SQL statement
    sql = """
    INSERT INTO proj2_tests_results (id, test_name, test_status, datetime)
    SELECT COALESCE(MAX(id), 0) + 1, %s, %s, NOW()
    FROM proj2_tests_results
    """

    try:
        assert "Welcome Bruce Springsteen" in message
        print("Test result: Success")

        # Execute the SQL statement
        TestName = 'test_signup_1'
        TestStatus = 'Success'
        cursor.execute(sql, (TestName, TestStatus))
        connection.commit()
    except AssertionError:
        print("Test result: ERROR !!!")

        # Execute the SQL statement
        TestName = 'test_signup_1'
        TestStatus = '*** FAILURE ***'
        cursor.execute(sql, (TestName, TestStatus))
        connection.commit()
    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()


# ======  Test 2  ======
def test_signup_2(setup):
    driver = setup
    driver.get("http://54.84.147.134:5000/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "(//button[normalize-space()='Sign-in'])[1]").click()
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Bruce Springsteen")
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    message = driver.find_element(By.XPATH, "//h1[normalize-space()]").text

    # Establish connection to database
    connection = connect_to_database()
    cursor = connection.cursor()
    # Prepare the SQL statement
    sql = """
    INSERT INTO proj2_tests_results (id, test_name, test_status, datetime)
    SELECT COALESCE(MAX(id), 0) + 1, %s, %s, NOW()
    FROM proj2_tests_results
    """

    try:
        assert "Welcome Bruce Springsteen" in message
        print("Test result: Success")

        # Execute the SQL statement
        TestName = 'test_signup_2'
        TestStatus = 'Success'
        cursor.execute(sql, (TestName, TestStatus))
        connection.commit()
    except AssertionError:
        print("Test result: ERROR !!!")

        # Execute the SQL statement
        TestName = 'test_signup_2'
        TestStatus = '*** FAILURE ***'
        cursor.execute(sql, (TestName, TestStatus))
        connection.commit()
    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()


def connect_to_database():
    connection = mysql.connector.connect(
        host='proj2-db-dockerhub-image-tags.cvojwwnpfgmu.us-east-1.rds.amazonaws.com',
        user='skaufma',
        password='Aa123456',
        database='PROJ2'
    )
    return connection