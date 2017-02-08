# -*- coding: utf-8 -*-
"""
生成接口执行报告
"""

from xlsxwriter import *
from Scripts.APIScripts.Login import *
from GetUsers import *
from ConfigFile import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class GetReport01:
    def get_report(self):
        """
        生成excel文件
        :param id:
        :param description:
        :param request_mode:
        :param api:
        :param time:
        :param status_code:
        :param msg:
        :return:
        """
        data = self.get_login_data()
        print data
        workbook = Workbook(r"F:\app_Script\Scripts\Reports\report01.xlsx")  # 添加工作簿
        worksheet = workbook.add_worksheet("接口测试报告")  # 添加工作表：接口测试报告
        title = ["ID", "接口描述", "Post/Get", "API", "参数", "执行时间", "状态码", "执行结果"]  # 定义表头
        # 设置各列宽度
        worksheet.set_column("B:B", 50)
        worksheet.set_column("C:C", 10)
        worksheet.set_column("D:D", 100)
        worksheet.set_column("E:E", 25)
        worksheet.set_column("F:F", 10)
        worksheet.set_column("G:G", 25)

        worksheet.write_row("A1", title, self.format(workbook)[0])  # 填充表头

        # 红色字体显示失败case
        for id in range(len(GetUsers().get_users())):
            if self.get_login_data()[id][5] == 200:
                worksheet.write_row("A%s" % str(id), data[id], self.format(workbook)[1])
            else:
                worksheet.write_row("A%s" % str(id), data[id], self.format(workbook)[2])
        workbook.close()  # 关闭工作簿

    def get_login_data(self):
        login_request_mode = "post"
        api = "%s/api/member/login" % ConfigFile().host()
        users_number = len(GetUsers().get_users())
        data = []
        for id in range(users_number):
            login = Login().login(GetUsers().get_mobile(id), GetUsers().get_password(id))
            data.append([id+1, login["description"], login_request_mode,
                                api, login["mobile"], login["time"], login["status_code"],
                                login["msg"]])
        return data

    def format(self, workbook):
        """
        定义格式
        :return:[format, format_title, format_error]
        """

        # 定义单元格格式
        format = workbook.add_format()  # 定义格式对象
        format.set_border(1)  # 定义单元格边框加粗1像素
        format.set_align("left")  # 定义单元格对齐方式：居左

        # 定义表头格式
        format_title = workbook.add_format()  # 定义表头格式对象
        format_title.set_border(1)  # 定义表头边框加粗1像素
        format_title.set_bg_color("#BCD2EE")  # 定义表头背景色：湖蓝色
        format_title.set_align("center")  # 设置表头对齐方式：居中
        format_title.set_bold()  # 设置表头字体加粗

        # 定义错误接口格式
        format_error = workbook.add_format()  # 定义错误单元格格式
        format_error.set_color("#FF0000")  # 发生错误时字体为红色
        return [format_title, format, format_error]



def main():
    r = GetReport01()
    r.get_report()
    # r.get_login_data()
if __name__ == "__main__":
    main()
