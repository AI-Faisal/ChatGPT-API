from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def chat_with_gpt(command):
    # Firefox profile
    profile_path = 'C:/Users/profile/AppData/Roaming/Mozilla/Firefox/Profiles/gmmsn0a8.profile'  # Firefox profile path
    options = webdriver.FirefoxOptions()
    options.profile = webdriver.FirefoxProfile(profile_path)

    options.add_argument('--headless')
    
    # Initialize the WebDriver
    driver = webdriver.Firefox(options=options)
    
    try:
        driver.get('https://chatgpt.com/') 
        
        # Wait for the text area visible, indicate page is ready
        wait = WebDriverWait(driver, 30)
        input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#prompt-textarea')))
        
        # Locate the input field and send the command
        input_field = driver.find_element(By.CSS_SELECTOR, '#prompt-textarea')
        input_field.send_keys(command)
        input_field.send_keys(Keys.RETURN)
        
        # Wait for the response until display copy button
        copy_button = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/span[1]/button')))
        
        # Locate and extract the response
        response = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div/div[1]/div/div/div')
        #response = driver.find_element(By.CSS_SELECTOR, '.markdown > p:nth-child(1)')
        print('\n')
        print(response.text)
        print('\n')

    except Exception as e:
        print (f"Error occured: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    import sys
    command = " ".join(sys.argv[1:])
    chat_with_gpt(command)
