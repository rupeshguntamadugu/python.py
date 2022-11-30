#####################################
##  FILENAME   : interview_assignments_v2.py
##  DESCRIPTION: This Python/SeleniumBase program is to solve below assignment tasks
##                1. Task1 - Login to given Url and Logout
##                2. Task2 - GoTo Slides, Expand a slide and Download pptx
##                3. Task3 - Profile -> Fingerprint, Complete Re-take Fingerprint flow
##  AUTHOR      : Rupesh G
##  DATE        : 25/11/2022
#####################################
from seleniumbase import BaseCase

class InterviewAssignmentsV3(BaseCase):

    def _login(self):
        # Open a web page in the active browser window
        self._print("\nOpening url for livestaging")
        self.open("https://prezent-livestaging.myprezent.com/home/main")
        self.maximize_window()

        # Assert the title of the current web page
        self.assert_title("Prezent")
        
        # Assert for username entry field and type email
        self._print("Waiting for username field and typing user email")
        self.assert_element("#username")
        self.type("#username", "intrvu_testuser_01.noreply@prezent.ai")

        # Assert for continue button and click it
        self._print("Waiting for continue button and clicking it")
        self.assert_element("#continue")
        self.click("#continue")

        # Assert for password entry field and type password
        self._print("Waiting for password field and typing password")
        self.assert_element("#password")
        self.type("#password", "kiqjemkh")
        self.wait(2)

        # Assert for submit button and click
        self._print("Waiting for Login button and clicking it")
        self.assert_element("#submit")
        self.click("#submit")
        self.wait(2)
        
        # Assert for profile icon element and click it
        self._print("Waiting for profile icon and clicking it")
        self.assert_element("div.profile-user-avatar", timeout=15)
        self.wait(2)

    def _logout(self):
        self._print("Waiting for profile icon and clicking it")
        self.assert_element("div.profile-user-avatar", timeout=20)
        self.click("div.profile-user-avatar")
        self.wait(2)
        
        # Assert for logout button and click
        self._print("Waiting for Signout button and clicking it") 
        self.assert_element("button.log-out-button")
        self.click("button.log-out-button")
        
        self._print("Waiting for Signout to complete and username field to appear")
        self.assert_element("#username", timeout=15)
    
    # Login to URL and do Logout
    def test_assignment_task1(sb):
        sb._login()
        sb._logout()

    # Download a slide
    def test_assignment_task2(self):
        self._login()
        
        # Go to slides page 
        self._print("Finding Slides element and clicking it")
        self.assert_element("//div[@class='v-list-item__title' and text()='Slides']")
        self.click("//div[@class='v-list-item__title' and text()='Slides']")
        self.wait(10)

        # Find a slide thumbnail and expand it
        self._print("Selecting a slide at position '1' and expanding it by clicking")
        self.assert_element('div.slides-wrapper.row .slide-wrapper.col-sm-6', timeout = 10)
        self.click_nth_visible_element('div.slides-wrapper.row .slide-wrapper.col-sm-6', 1)

        # Go to download button and click on it
        self._print("Waiting for download button and clicking it")
        self.assert_element("#download-btn")
        self.click("#download-btn")

        self._print("Waiting for pptx download option and selecting it")
        self.assert_element("#download-btn-from-list")
        self.click("#download-btn-from-list")
        self.sleep(5)

        self._logout()

    # Go to fingerprint tab and click on Re-take fingerprint
    def test_assignment_task3(self):
        self._login()

        # Assert for profile icon element and click on it
        self._print("Waiting for profile icon and clicking it")
        self.assert_element("div.profile-user-avatar", timeout=15)
        self.click("div.profile-user-avatar", timeout=15)
        self.wait(2)
        self.wait(2)

        # Go to fingerprint page
        self._print("Finding fingerprint element and clicking it")
        self.assert_element("a#fingerprint-tab")
        self.click("a#fingerprint-tab")
        self.wait(2)

        # Go to Re-take fingerprint test button and click on it
        self._print("Waiting for Re-take fingerprint test button and clicking it")
        self.assert_element("div.btn-retake")
        self.click("div.btn-retake")
        self.wait(2)

        # Find Discover My Fingerprint button and click on it
        self._print("Finding Discover My Fingerprint button and clicking it")
        self.assert_element("#discover", timeout=15)
        self.click("#discover")
        self.wait(2)

        self.assert_element("div.question-content-header .header", timeout=10)
        self._print(self.get_text("div.question-content-header .header")) 

        # left,right,left,right,left,right 
        self.click_nth_visible_element('div.images-wrapper .question-image', 1)
        self.assert_element("div.question-buttons .primary-button")
        self.click("div.question-buttons .primary-button")
        self.wait(2)

        self.click_nth_visible_element('div.images-wrapper .question-image', 2)
        self.assert_element("div.question-buttons .primary-button")
        self.click("div.question-buttons .primary-button")
        self.wait(2)

        self.click_nth_visible_element('div.images-wrapper .question-image', 1)
        self.assert_element("div.question-buttons .primary-button")
        self.click("div.question-buttons .primary-button")
        self.wait(2)

        self.click_nth_visible_element('div.images-wrapper .question-image', 2)
        self.assert_element("div.question-buttons .primary-button")
        self.click("div.question-buttons .primary-button")
        self.wait(2)

        self.click_nth_visible_element('div.images-wrapper .question-image', 1)
        self.assert_element("div.question-buttons .primary-button")
        self.click("div.question-buttons .primary-button")
        self.wait(2)

        self.click_nth_visible_element('div.images-wrapper .question-image', 2)
        self.assert_element("div.question-buttons .primary-button")
        self.click("div.question-buttons .primary-button")
        self.wait(2)
 
        self.assert_element("div.question-content-header .header", timeout=10)
        self._print(self.get_text("div.question-content-header .header"))

        self.click_nth_visible_element('div.selections .selection', 3)
        self.click_nth_visible_element('div.selections .selection', 5)
        self.click_nth_visible_element('div.selections .selection', 9)
        self.wait(2)

        self.assert_element('#show-fingerprint-for-btn--auto')
        self.click('#show-fingerprint-for-btn--auto')
        self.wait(2)

        self._print(self.get_text("div.result-wrapper .result-title"))

        self.assert_element("button.primary.primary-button")
        self.click("button.primary.primary-button")
        self.wait(2)

        self._logout()

        
        

