from seleniumbase import BaseCase

class TestMFALogin(BaseCase):
    def test_mfa_login(self):
        self.open("https://prezent-livestaging.myprezent.com/signin")
        self.type("#username", "intrvu_testuser_01.noreply@prezent.ai")
        self.type("#password", "kiqjemkh")
        self.enter_mfa_code("#totpcode", "GAXG2MTEOR3DMMDG")  # 6-digit
        self.assert_exact_text("Welcome!", "h1")
        self.assert_element("img#image1")
        self.click('a:contains("This Page")')
        self.save_screenshot_to_logs()
