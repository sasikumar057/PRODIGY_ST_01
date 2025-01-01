from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  
driver.get("https://dunizb.github.io/sCalc/")

def perform_calculation(sequence, expected_result):
    try:
        print(f"Testing sequence: {sequence}")
        driver.find_element(By.ID, "reset").click()
        time.sleep(1)  

        for char in sequence:
            button = driver.find_element(By.XPATH, f"//span[@data-number='{char}']")
            button.click()
            time.sleep(0.5)
        
        driver.find_element(By.ID, "equals").click()
        time.sleep(1)

        result_display = driver.find_element(By.ID, "res").text

        if str(result_display) == str(expected_result):
            print(f"PASS: {sequence} = {result_display}")
        else:
            print(f"FAIL: {sequence}. Expected {expected_result}, Got {result_display}")
    except Exception as e:
        print(f"Error testing sequence '{sequence}': {e}")

test_cases = [
    ("5+3", 8),          
    ("10-4", 6),         
    ("7*3", 21),        
    ("12/4", 3),       
    ("10/0", "Infinity"),
    ("0/10", 0),         
    ("0*5", 0),           
    ("5+0", 5),          
    ("5-0", 5),          
    ("-5+3", -2),        
    ("-7*-3", 21),       
    ("-12/4", -3),      
    ("5.5+3.2", 8.7),   
    ("10.0-4.5", 5.5),  
    ("7.2*3.1", 22.32),   
    ("12.6/2.1", 6.0),   
    ("5+3*2", 11),    
    ("10-4/2", 8),     
    ("7*3-2", 19),       
    ("12/4+5", 8),       
]

for sequence, expected in test_cases:
    perform_calculation(sequence, expected)

time.sleep(2) 
driver.quit()
