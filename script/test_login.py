# 导包
import logging
import unittest


from api.login_api import LoginApi

# 创建测试类
class TestIHRMLogin(unittest.TestCase):
    # 进行实例化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 定义登录成功的测试用例函数
    def test01_login_success(self):
        jsonData = {"mobile":"13800000002","password":"123456"}
        headers = {"Content-type":"application/json"}
        response = self.login_api.login(jsonData=jsonData,headers=headers)

        # 打印响应数据
        logging.info("登录成功的结果为:{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))