from splinter import Browser
import time
import os
import sys

exp_name = "emotion" # 实验名称
campus = "紫金港校区" # 预约校区（紫金港校区，西溪校区，华家池校区）
classroom_list = ["524A", "525A", "534C", "534D"] # 要预约的实验室
start_date = ["2019", "12", "26"] # 开始日期 [yyyy, mm, dd]
start_time = "22:30" # 开始时间
end_date = ["2019", "12", "26"] # 结束日期
end_time = "23:15" # 结束时间
exp_duration = "40" # 实验
exp_interval = "10" # 实验间隔
exp_hc = "10" # 预计实验人数
exp_type = "emotion" # 实验类型
exp_bonus_type = "奖金" # 实验奖励类型（奖金/学分）
exp_bonus_number = "10" # 实验奖励费用/学分
additional_info = "实验1"
# is_restrict_exp_cond = False # 是否限制实验条件（是/否）

acc_phone = "13588760515" # 登录手机号
acc_pwd = "123456" #登录密码

url_login = "http://106.12.13.13:8087/#/login"

class Orderer:
    """ 
    Classroom Orderer Class
    """
    
    def __init__(self, browser):
        self.browser = browser
        pass

    def login(self):
        """
        login
        """
        # 填入手机号和密码
        self.browser.visit(url_login)
        ele_inputs =  self.browser.find_by_tag('INPUT')
        phone_input_ele = ele_inputs[3]
        pwd_input_ele = ele_inputs[4]
        vc_input_ele = ele_inputs[5]
        phone_input_ele.fill(acc_phone)
        pwd_input_ele.fill(acc_pwd)
        # 填入验证码
        get_vc_button_ele = self.browser.find_by_tag('BUTTON')[2]
        # print(len(self.browser.find_by_tag('BUTTON')))
        get_vc_button_ele.click()
        vc_code = input("请输入验证码：")
        if(len(vc_code) > 0):
            vc_input_ele.fill(vc_code)
            login_button_ele = self.browser.find_by_text('登陆')[1]
            login_button_ele.click()
        time.sleep(1)
    
    def order_one_day(self):
        """ 
        order classrooms in 1 day
        """
        delay = 1.0
        start_date_str = start_date[0] + "-" + start_date[1] + '-' + start_date[2]
        end_date_str = end_date[0] + "-" + end_date[1] + '-' + end_date[2]
        self.browser.visit("http://106.12.13.13:8087/#/sendInfo-add")
        success = False
        while(not success):
            self.browser.reload()
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            input_eles =  self.browser.find_by_tag('INPUT')            
            input_eles[0].fill(exp_name)
            campus_ele = input_eles[1]
            campus_ele.click()
            time.sleep(delay)
            campus_item_ele = self.browser.find_by_text(campus)[0]
            campus_item_ele.click()
            time.sleep(delay)
            # 选择房间
            for room in classroom_list:
                room_ele = self.browser.find_by_text(room)
                room_ele.click()
            # 输入开始日期
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            input_eles[2].fill(start_date_str)
            input_eles[3].fill(start_time)
            input_eles[3].click()
            time.sleep(delay)
            if(input_eles[2].value != start_date_str or input_eles[3].value != start_time):
                continue
            time.sleep(delay)
            input_eles[6].click()

            input_eles[4].fill(end_date_str)
            time.sleep(delay)
            input_eles[5].fill(end_time)
            input_eles[5].click()
            if(input_eles[4].value != end_date_str or input_eles[5].value != end_time):
                continue
            time.sleep(delay)
            input_eles[6].click()

            input_eles[6].fill(exp_duration)
            input_eles[7].fill(exp_interval)
            input_eles[8].fill(exp_hc)
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            input_eles[9].click()
            time.sleep(delay)
            self.browser.find_by_text(exp_type)[0].click()
            time.sleep(delay)
            self.browser.find_by_text(exp_bonus_type)[0].click()
            input_eles[12].fill(exp_bonus_number)
            self.browser.find_by_tag('TEXTAREA')[0].fill(additional_info)
            self.browser.find_by_text('立即创建')[0].click()
            time.sleep(delay)
            if(len(self.browser.find_by_text('立即创建')) > 0):
                continue
            else:
                success = True
            while(len(self.browser.find_by_text('立即创建')) > 0) :
                self.browser.find_by_text('立即创建')[0].click()
        print("发布成功！")

    def run(self):
        """
        Run program.
        """
        self.login()
        self.order_one_day()
        window = browser.windows[0]
        while(window.is_current):
            time.sleep(1)
            pass
            
    

if __name__ == "__main__":
    with Browser("chrome") as browser:
        orderer = Orderer(browser)
        orderer.run()