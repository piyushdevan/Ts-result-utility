from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

text_to_find = input("Name to be Searched  : ").upper()
x = int(input("Enter Starting Value of Range: "))
y = int(input("Enter Ending   Value of Range: "))
year = input("Enter Year of Study: ")

driver = webdriver.Chrome() 
driver.get("https://tsbie.cgg.gov.in/ResultMemorandum.do")


# ITERATION
for hallticket_no in range(x, y):

    # Select the desired option of Year in the dropdown
    select = Select(driver.find_element(By.NAME, "property(pass_year)"))  
    select.select_by_value(year)  

    # Find the radio button by its name attribute
    radio_button1 = driver.find_element(By.ID,"year2")  
    radio_button1.click()
    
    # check value of IPE
    radio_button_xpath = f"//input[@value='3']"
    radio_button = driver.find_element(By.XPATH, radio_button_xpath)
    radio_button.click()

    # Input field with HallTicket number
    input_field = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.NAME, 'hallticket_no')))
    input_field.send_keys(str(hallticket_no))
   
    
    # Submit the form
    submit_button = driver.find_element(By.CLASS_NAME, "button")
    submit_button.click()

    # Stop when the result match
    
    if text_to_find in driver.page_source:
        print(f"Found the text: {text_to_find}")
        print(f"Hallticket_no:  {hallticket_no}")

        # print Dialogue appear
        printing_button = driver.find_element(By.ID, "4")
        printing_button.click()
        time.sleep(8)
        break


driver.quit()
