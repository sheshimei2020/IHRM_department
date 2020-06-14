# 导包
import logging
import unittest
import app
from api.department_api import DepartmentApi

from api.login_api import LoginApi

# 创建测试类
from utils import assert_common


class TestIHRMDepartment(unittest.TestCase):
    # 初始化unittest的函数
    def setUp(self):
        # 实例化登录api
        self.login_api = LoginApi()
        # 实例化部门管理api
        self.dept_api = DepartmentApi()

    def tearDown(self):
        pass

    # 实现登录成功的接口
    def test01_login_success(self):
        # 发送登录的接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData, {"Content-Type": "application/json"})
        # 打印登录接口返回的结果
        logging.info("登录接口返回的结果为:{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 打印请求体
        logging.info("保存到全局变量中的请求头为:{}".format(app.HEADERS))
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        assert_common(self, 200, True, 10000, "操作成功", response)

    def test02_add_dept(self):
        # 发送添加部门的接口请求
        jsonData = {"name": "国际资源部001",
                    "code": "DEPT-GJZY",
                    "manager": "Yilisarou",
                    "introduce": "牛逼洋气的部门",
                    "pid": None}
        response = self.dept_api.add_dept(jsonData,app.HEADERS)
        # 打印添加部门的结果
        logging.info("添加部门的结果是:{}".format(response.json()))
        # 提取部门的id并保存到全局变量
        app.DEPT_ID= response.json().get("data").get("id")
        # 打印保存的部门id
        logging.info("保存到全局变量的部门id是:{}".format(response.json()))
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        assert_common(self, 200, True, 10000, "操作成功", response)

    def test03_modify_dept(self):
        jsonData={"name":"国际资源部002",
                  "code":"DEPT-GJZY",
                  "manager":"",
                  "introduce":""}
        # 发送修改部门接口的请求
        response = self.dept_api.modify_dept(app.DEPT_ID,jsonData,app.HEADERS)
        # 打印修改员工的结果
        logging.info("修改员工的结果为:{}".format(response.json()))
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        assert_common(self, 200, True, 10000, "操作成功", response)

    def test04_query_dept(self):
        # 发送查询部门接口的请求
        response = self.dept_api.query_dept(app.DEPT_ID,app.HEADERS)
        # 打印查询部门的结果
        logging.info("查询部门的结果为:{}".format(response.json()))
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        assert_common(self, 200, True, 10000, "操作成功", response)

    def test05_delete_dept(self):
        # 发送删除部门接口的请求
        response = self.dept_api.delete_dept(app.DEPT_ID,app.HEADERS)
        # 打印删除部门的结果
        logging.info("删除部门的结果为:{}".format(response.json()))
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        assert_common(self, 200, True, 10000, "操作成功", response)
