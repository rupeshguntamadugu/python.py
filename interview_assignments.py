from seleniumbase import BaseCase


class InterviewAssignments(BaseCase):
    def test_assignment_task1(self):
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

        # Assert for submit button and click
        self._print("Waiting for Login button and clicking it")
        self.assert_element("#submit")
        self.click("#submit")
        
        # Assert for profile icon element and click it
        self._print("Waiting for profile icon and clicking it")
        self.assert_element("div.profile-user-avatar", timeout=15)
        self.click("div.profile-user-avatar")

        # Assert for logout button and click
        self._print("Waiting for Signout button and clicking it") 
        self.assert_element("button.log-out-button")
        self.click("button.log-out-button")
        
        self._print("Waiting for Signout to complete and username field to appear")
        self.assert_element("#username", timeout=15)


        #self.hover_and_click("#myDropdown", "#dropOption2", timeout=1)
        # self.js_click("#dropOption2")
        # self.click('button:contains("Click Me")')
