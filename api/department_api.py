# 导包
import requests

# 创建要封装的类
class DepartmentApi:
    def __init__(self):
        # 定义部门管理模块的URL
        self.dept_url = "http://ihrm-test.itheima.net/api/company/department"

    # 定义新增部门的函数
    def add_dept(self,jsonData,headers):
        return requests.post(url=self.dept_url,json=jsonData,headers=headers)

    # 定义修改部门的函数
    def modify_dept(self,dept_id,jsonData,headers):
        modify_url = self.dept_url +"/"+ dept_id
        return requests.put(url=modify_url,json= jsonData, headers=headers)

    # 定义查询部门的函数
    def query_dept(self,dept_id,headers):
        query_url = self.dept_url + "/"+dept_id
        return requests.get(url=query_url,headers=headers)

    # 定义删除部门的函数
    def delete_dept(self,dept_id,headers):
        delete_url= self.dept_url + "/" +dept_id
        return requests.delete(url=delete_url,headers=headers)