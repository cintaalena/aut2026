import os, sys, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AutTest(unittest.TestCase):
    def setUp(self):
        browser_name = os.environ.get("BROWSER", "firefox").lower()

        server = os.environ.get("SELENIUM_URL", "http://localhost:4444/wd/hub")

        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
        elif browser_name == "edge":
            options = webdriver.EdgeOptions()
        else:
            options = webdriver.FirefoxOptions()

        options.add_argument("--ignore-certificate-errors")

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def test_homepage(self):
        url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost"
        self.browser.get(url)

        # Screenshot untuk bukti/debug
        self.browser.save_screenshot("screenshot.png")

        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, "p").text
        self.assertIn(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], verbosity=2, warnings="ignore")
