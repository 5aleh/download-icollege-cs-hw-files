from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# If there are errors not related to 'element not found', try to increase the sleep timer...
# ...prior to place of error before trying other solutions.

# To download the files to student specific folders on your computer, uncomment the two os.renames() functions during the...
# ...'Download the first submitted homework file...' section

# Currently as it stands, only the first file submitted by a student is downloaded
# Future versions will download all student submitted files

# Set the default download directory the homework files will be downloaded to
downloaddir = # Insert download directory here

# Set the iCollege username and password login credentials
username = # Insert iCollege username here
password = # Insert iCollege password here

# Set the homework number (as a String '') whose files will be downloaded
HW_NUM = # Insert homework number here

# Testing area...........ignore...............#
# print(os.listdir("C:/seltest/"))
# i = 1
# for file in os.listdir("C:/seltest/"):
#     newdir = "C:/seltest/student"+ str(i)
#     # os.makedirs(newdir)
#     os.renames("C:/seltest/"+file, newdir + "/" + file)
#     i+=1

# timestr = time.strftime("%Y%m%d-%H%M%S")
# print(timestr)
# End of testing area........................#

options = webdriver.ChromeOptions()

# Set preferences like default directory where the files will be downloaded to
# Add preferences to chrome driver
prefs = {
    "download.default_directory": downloaddir, # Place path to download directory here
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}

options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options)

# Open Georgia State University iCollege login page
driver.get("https://gastate.view.usg.edu/")

# Enter login credentials and login
menu = driver.find_element_by_xpath("//button[@type= 'submit']")
ActionChains(driver).click(menu).perform()
driver.find_element_by_name("loginForm:username").send_keys(username)
driver.find_element_by_name("loginForm:password").send_keys(password)
menu = driver.find_element_by_name("loginForm:loginButton")
menu.click()
time.sleep(2)

# Navigate to CSC1302 class from the course menu and click the class
btn = driver.find_element_by_css_selector("div.d2l-navigation-s-course-menu")
btn.click()
time.sleep(2)
btn = driver.find_element_by_xpath("//div[contains(@title, 'PRINCIPLES OF COMPUTER SCI II')]//a[@class='d2l-link d2l-datalist-item-actioncontrol']")
btn.click()
time.sleep(2)

# Navigate to assignments from the menu and click the assignments link
btn = driver.find_element_by_xpath("//div[@class='d2l-navigation-s-main-wrapper']/div[3]")
btn.click()
btn = driver.find_element_by_xpath("//d2l-menu-item-link[@text='Assignments']")
btn.click()
time.sleep(2)

# Navigate to and click the wanted homework submissions
# To change to a different homework, change the value of the HW_NUM variable at the top of the file
# For example, to download homework 4 submissions, you set the value of HW_NUM to '4'
btn = driver.find_element_by_xpath("//a[@title='View Homework#" + HW_NUM + " submissions']")
btn.click()
time.sleep(2)

# Navigate to and click the first student
btn = driver.find_element_by_xpath("//td[@class='dlay_l']/a")
btn.click()
time.sleep(2)

# Retrieve the total number of students that submitted their assignment
stdnum = driver.find_element_by_xpath("//td[@class='d_tc d_tm d_tn']/label").text
print(stdnum)
newstdnum = stdnum[10:]
print("Total number of students that submitted their HW: " + str(newstdnum))
print(int(newstdnum)-1)

# Download the first submitted homework file from the all students that submitted their assignment
btn = driver.find_element_by_xpath("//a[contains(@onclick, 'DownloadFile')]")
btn.click()
time.sleep(2)
stdname = driver.find_element_by_xpath("//td[@class='d_tl d_tm d_tn']/label/strong").text
print("1: " + stdname)
numfiles = driver.find_elements_by_xpath("//td[@class='dlay_l']//a[contains(@onclick, 'DownloadFile')]")
print("Number of files submitted: " + str(len(numfiles)))
print("")
filename = driver.find_element_by_xpath("//a[contains(@onclick, 'DownloadFile')]/span").text
newdir = downloaddir + stdname
# os.renames(downloaddir + filename, newdir + "/" + filename)
for i in range(int(newstdnum)-1):
    btn = driver.find_element_by_xpath("//a[@title='Next Student']")
    btn.click()
    time.sleep(2)
    btn = driver.find_element_by_xpath("//a[contains(@onclick, 'DownloadFile')]")
    btn.click()
    time.sleep(2)
    stdname = driver.find_element_by_xpath("//td[@class='d_tl d_tm d_tn']/label/strong").text
    print(str(i+2) + ": " + stdname)
    numfiles = driver.find_elements_by_xpath("//td[@class='dlay_l']//a[contains(@onclick, 'DownloadFile')]")
    print("Number of files submitted: " + str(len(numfiles)))
    print("")
    filename = driver.find_element_by_xpath("//a[contains(@onclick, 'DownloadFile')]/span").text
    newdir = downloaddir + stdname
    # os.renames(downloaddir + filename, newdir + "/" + filename)
    time.sleep(2)


driver.close()
