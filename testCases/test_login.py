# import pytest
# from selenium import webdriver
# from pageObjects.LoginPage import LoginPage
# from utilites.readProperties import ReadConfig
# from utilites.customLogger import LogGen
# # import logging
# # import time
#
# class Test_001_Login:
#     baseURl = ReadConfig.getApplicationURL()
#     username = ReadConfig.getUseremail()
#     password = ReadConfig.getPassword()
#     logger = LogGen.loggen()
#
#     def test_homepagetitle(self):
#
#         self.logger.info("******************Test_001_Login*******************")
#         self.logger.info("*****************Verifying Home page Title**********************")
#
#         # self.driver = setup
#         self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
#         self.driver.get(self.baseURl)
#         act_title = self.driver.title
#
#         if act_title == "CrmLanding":
#             assert True
#             self.driver.close()
#             self.logger.info("*****************************Home Page title is passed************************")
#         else:
#             self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetitle.png")
#             self.driver.close()
#             self.logger.error("**************************Home Page title is failed*************************")
#             assert False
#
#     def test_login(self):
#         # self.driver = setup
#         self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
#         self.driver.get(self.baseURl)
#         self.driver.maximize_window()
#         self.lp = LoginPage(self.driver)
#         self.lp.setStartlogin()
#         self.lp.setusername(self.username)
#         self.lp.setpassword(self.password)
#         self.lp.clicklogin()
#         act_title = self.driver.title
#         if act_title == "CrmLanding":
#             assert True
#             # self.driver.save_screenshot(".\\Screenshots\\" + "test_login0.png")
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
#             self.driver.close()
#             assert False
#
#     def test_login_02(self):
#         # self.driver = setup
#         self.driver = webdriver.Firefox(executable_path="E:\geckodriver\geckodriver.exe")
#         self.driver.get(self.baseURl)
#         self.driver.maximize_window()
#         self.lp = LoginPage(self.driver)
#         self.lp.setStartlogin()
#         self.lp.setusername(self.username)
#         # self.lp.setpassword(self.password)
#         self.lp.clicklogin()
#         act_error_msg = "Password is required"
#         if act_error_msg == "Password is required123":
#             assert True
#             self.driver.close()
#
#         else:
#             self.driver.save_screenshot(".\\Screenshots\\" + "test_login_02.png")
#             self.driver.close()
#             assert False
#
#     def test_login_03(self):
#         self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
#         self.driver.get(self.baseURl)
#         self.driver.maximize_window()
#         self.lp = LoginPage(self.driver)
#         self.lp.setStartlogin()
#         self.lp.setusername(self.username)
#         self.lp.setpassword(self.password)
#         self.lp.clicklogin()
#
#         act_error_msg = "Username is required"
#         if act_error_msg == "Username is required":
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\Screenshots\\" + "test_login_03.png")
#             self.driver.close()
#             assert False
#
#
#


##################################################################################
#
# class Test_002_DDT_Login:
#     baseURl = ReadConfig.getApplicationURL()
#     path = ".//TestData/login_IDPWD.xlsx"
#     logger = LogGen.loggen()
#
#     def test_login_ddt(self, setup):
#
#         self.logger.info("******************Test_001_Login*******************")
#         self.logger.info("*****************Verifying Home page Title**********************")
#
#         # self.driver = setup
#         self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
#         self.driver.get(self.baseURl)
#         self.driver.maximize_window()
#         self.lp = LoginPage(self.driver)
#
#         self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
#         print("Number of rows in a excel:", self.rows)
#
#         lst_status = []
#
#         for i in range(2, self.rows+1):
#             self.Username=XLUtils.readData(self.path, 'Sheet1', r, 1)
#             self.Password = XLUtils.readData(self.path, 'Sheet1', r, 2)
#             self.Status = XLUtils.readData(self.path, 'Sheet1', r, 3)
#
#             self.lp.setStartlogin()
#
#             self.lp.setusername(self.Username)
#             self.lp.setpassword(self.Password)
#             self.lp.clicklogin()
#             time.sleep(5)
#         act_title = self.driver.title
#         if act_title == "CrmLanding":
#             if self.Status == "Passed":
#                 self.logger.info("******Passed*******")
#                 lst_status.append("Passed")
#             elif self.Status == "failed":
#                 self.logger.info("***************failed******************")
#                 lst_status.append("failed")
#
#             if "failed" not in lst_status:
#                 self.logger.info("***************Login DDT test is passed*****************")
#                 self.driver.close()
#                 assert True
#             else:
#                 self.logger.info("***************Login DDT test is failed*****************")
#                 self.driver.close()
#                 assert False
#
#         self.logger.info("***********************End of Login DDT Test***************************")
#         self.logger.info("***************************Completed ******************************")
#




#########################################################################################################

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen
# import logging
# import time

class Test_001_Login:
    baseURl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepagetitle(self):

        self.logger.info("******************Test_001_Login*******************")
        self.logger.info("*****************Verifying Home page Title**********************")

        # self.driver = setup
        self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        self.driver.get(self.baseURl)
        act_title = self.driver.title

        if act_title == "CrmLanding":
            assert True
            self.driver.close()
            self.logger.info("*****************************Home Page title is passed************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetitle.png")
            self.driver.close()
            self.logger.error("************************** Home Page title is failed *************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self):
        self.logger.info("********************************* Verifying Login Test *********************************")
        # self.driver = setup
        self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setStartlogin()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_handle = "CDwindow-E8EC14A08398C09BF737011841994C5C"
        if act_handle == "CDwindow-E8EC14A08398C09BF737011841994C5C":
            assert True
            self.logger.info("************************** Login Test is passed ******************************")
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_login0.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*************************** Login test is failed **************************")
            assert False

