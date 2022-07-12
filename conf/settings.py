# -*- coding: utf-8 -*-
__author__ = 'Guibin'

import os
import sys
import datetime
# 根目录：
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_PATH)

# ---------------- 日志相关 --------------------
# 日志级别：
LOG_LEVEL = 'debug'
LOG_STREAM_LEVEL = 'debug'  # 屏幕输出流
LOG_FILE_LEVEL = 'info'   # 文件输出流
# 日志文件夹命名：
LOG_FILE_NAME = os.path.join(BASE_PATH, 'logs', datetime.datetime.now().strftime('%Y-%m-%d') + '.log')
#print(LOG_FILE_NAME)

# ---------------- Excel相关 --------------------
# Excel数据文件夹命名：
DATA_PATH = os.path.join(BASE_PATH, 'data')
#print(DATA_PATH)
# 切换data文件时，只需要更改文件名即可：
EXCEL_FILE_NAME = 'crm-api.xlsx'
EXCEL_FILE_PATH = os.path.join(DATA_PATH, EXCEL_FILE_NAME)
if __name__ == '__main__':
    # 添加顶级目录：
    sys.path.insert(0, BASE_PATH)
    print(sys.path)

# ---------------- Allure相关 ----------------------
# 报告路径：
REPORT_PATH = os.path.join(BASE_PATH, 'report')
#print(REPORT_PATH)
# Allure的json文件夹命名：
ALLURE_JSON_DIR_NAME = 'allure_json'
# Allure的json文件路径：
ALLURE_JSON_DIR_PATH = os.path.join(REPORT_PATH, ALLURE_JSON_DIR_NAME)
#print(ALLURE_JSON_DIR_PATH)
# allure的html文件夹命名：
ALLURE_REPORT_DIR_NAME = os.path.join(REPORT_PATH, 'allure_report')
#print(ALLURE_REPORT_DIR_NAME)
# allure的html报告路径
ALLURE_REPORT_DIR_PATH = os.path.join(REPORT_PATH, ALLURE_REPORT_DIR_NAME)
#print(ALLURE_REPORT_DIR_PATH)
# 压缩包路径：
ZIP_FILE_PATH = os.path.join(REPORT_PATH, 'report.zip')
#print(ZIP_FILE_PATH)
# 生成报告命令：
ALLURE_COMMAND = "allure generate {} -o {}".format(ALLURE_JSON_DIR_PATH, ALLURE_REPORT_DIR_PATH)
#print(ALLURE_COMMAND)

# ------------------- 邮件相关 -----------------
# 第三方 SMTP 服务：
MAIL_HOST = "smtp.qq.com"
MAIL_USERNAME = "1558365217@qq.com"
MAIL_TOKEN = "xxxxxxxxx"
# 邮件主题、收件人、发件人：
MAIL_SUBJECT = 'Python通过第三方发邮件'
# 可修改：设置收件人和发件人
SENDER = '1558365217@qq.com' # 发件人
# 收件人，收件人可以有多个，以列表形式存放：
RECEIVERS  = ['1297891880@qq.com','1558365217@qq.com']
# 邮件正文
MAIN_CONTENT = 'Hi man：\r\n这是今日的{excel_file_name}测试报告\r\n详情请下载附件查看\r\n具体方法请在终端执行 allure open report\r\n测试人:{execute_tests_name},联系电话：{execute_tests_phone} \r\n{execute_tests_date}'.format(
    excel_file_name= EXCEL_FILE_NAME,
    execute_tests_name="羊羊",
    execute_tests_phone=13185845341,
    execute_tests_date=datetime.datetime.date(datetime.datetime.now())
)

###找openapi
#https://srv.jk.cn/
#https://api.ucloud.cn/

