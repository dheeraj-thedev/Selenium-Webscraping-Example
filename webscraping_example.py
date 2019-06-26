#*•	1st import: Allows you to launch/initialise a browser.
#*•	2nd import: Allows you to search for things using specific parameters.
#*•	3rd import: Allows you to wait for a page to load.
#*•	4th import: Specify what you are looking for on a specific page
# in order to determine that the webpage has loaded.
#*•	5th import: Handling a timeout situation

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# Create new Instance of Chrome in incognito mode

driverPath=r'chromedriver.exe'

#browser = webdriver.Chrome(executable_path='/Library/Application Support/Google/chromedriver', chrome_options=option)
browser = webdriver.Chrome(executable_path=driverPath, chrome_options=option)

# Go to desired website
browser.get("https://github.com/dheeraj-thedev")

# Wait 20 seconds for page to load
timeout = 40
try:
    # Wait until the final element [Avatar link] is loaded.
    # Assumption: If Avatar link is loaded, the whole page would be relatively loaded because it is among
    # the last things to be loaded.
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="js-pjax-container"]')))
except TimeoutException as toe:
    print("Timed out waiting for page to load {}".format(toe))
    browser.quit()

# Get all of the titles for the pinned repositories
# We are not just getting pure titles but we are getting a selenium object
# with selenium elements of the titles.

# find_elements_by_xpath - Returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath("//a[@class='text-bold']")

# List Comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]

#for x in titles_element:
 #   print(x.text)

# print response in terminal
print('TITLES:')
print(titles, '\n')


# Get all of the pinned repo languages
language_element = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
languages = [x.text for x in language_element] # same concept as for-loop/ list-comprehension above.

# print response in terminal
print("LANGUAGES:")
print(languages, '\n')

# Pair each title with its corresponding language using zip function and print each pair
for title, language in zip(titles, languages):
    print("RepoName : Language")
    print(title + ": " + language, '\n')
