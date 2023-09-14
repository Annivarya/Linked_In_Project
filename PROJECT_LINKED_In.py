from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By for locating elements
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

# Set the path to the Firefox WebDriver executable
driver_path = "D:\\geckodriver\\geckodriver.exe"

# Create a FirefoxOptions instance and set the executable path
options = webdriver.FirefoxOptions()
options.binary_location = "path/to/firefox.exe"  # Path to Firefox binary (if needed)

# Initialize the WebDriver with options
driver = webdriver.Firefox(options=options)
class LinkedIN:

    def LOGIN(self):
        print("-1")

        driver.get("https://www.linkedin.com/login")
        print("-2")
        username_field = driver.find_element(By.ID, "username")  # Use By.ID to locate by ID
        print("-3")
        password_field = driver.find_element(By.ID, "password")  # Use By.ID to locate by ID
        print("4")
        username_field.send_keys("octaneimposter86@gmail.com")
        password_field.send_keys("Imposter86")
        sign_in_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')  # Use By.CSS_SELECTOR to locate by CSS selector
        sign_in_button.click()
        time.sleep(5)
        print("Login successful!")
        driver.get("https://www.linkedin.com/search/results/people/?keywords=data%20scientist&origin=CLUSTER_EXPANSION&searchId=aa6c0022-9174-4075-9eb7-916e830d6b01&sid=HSC")
        
        # Wait for the search results page to load (you may need to adjust the wait time)
        time.sleep(5)
        names=[]
        headlines=[]
        locations=[]
        html=page_source = driver.page_source
        name_elements = driver.find_elements(By.CSS_SELECTOR, "span.entity-result__title-text a")
        for name_element in name_elements:
            temp=''
            temp=" ".join(name_element.text.split(' ')[:2])
            names.append(temp)
            print("--------------------------")
        print(names)
        soup = BeautifulSoup(html, 'html.parser')

        # Find the element by class and extract the text
        headline_elements = soup.find_all('div', class_='entity-result__primary-subtitle')

        # Loop through the elements and extract their text
        for headline_element in headline_elements:
            headline = headline_element.text.strip()
            headlines.append(headline)
        print("Headline:", headlines)


        location_elements = soup.find_all('div', class_='entity-result__secondary-subtitle t-14 t-normal')

        # Loop through the elements and extract their text
        for location_element in location_elements:
            location = location_element.text.strip()
            locations.append(location)
        print("Location:", locations)
    
        df = pd.DataFrame({'Name': names, 'Location': locations, 'Headline': headlines})

        # Print the DataFrame
        print(df)

        # Save the DataFrame to a CSV file (optional)
        df.to_csv("linkedin_data.csv", index=False)


        print("---")  # Separating profiles with dashes

        # Close the webdriver
        driver.get("https://www.linkedin.com/m/logout/")
        driver.quit()
        

obj = LinkedIN()
obj.LOGIN()
