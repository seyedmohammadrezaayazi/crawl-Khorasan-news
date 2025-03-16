from selenium import webdriver
import pandas as pd
import time
import excel
from selenium.common.exceptions import NoSuchElementException


class Scape():

    def __init__(self, urls, nameexcel):
        self.urls = urls
        self.numberrow = 1
        # 'http://khorasannews.com/?nid=' + str(id) + '&pid=5&type=0'
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('window-size=1920x1480')
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=r"D:/work/chromedriver")
        # self.driver.get(url)
        self.excel = excel.Excel(nameexcel)
        self.excel.write_by_list_in_next_row(["تاریخ", "موضوع", "سرتیتر", "نویسنده", "اسم روزنامه", "صفحه", "قالب"])

    def checkExistsClassName(self, classname, element):
        try:
            text = element.find_element_by_class_name(classname).text
        except NoSuchElementException:
            return ""
        if text == '':
            return ""
        return text

    def run(self):
        print("start")
        for url in self.urls:
            for VersionNumber in range(url.downVersionNumber, url.UpVersionNumber + 1):
                for page in url.pages:
                    localURL = url.baseUrl + '/?nid=' + str(VersionNumber) + '&pid=' + str(page) + '&type=0'
                    try:
                        self.driver.get(localURL)
                        self.el = self.driver.find_element_by_class_name("close")
                        element = self.driver.find_elements_by_class_name('menu-item')
                        elm = [el.text for el in element]
                        self.getDataPage(elm[1], page, url.name)
                    except Exception as e:
                        print(e, "page", page, ' version=', VersionNumber,' '+url.name)
                        continue
                    # print(elm[1])

    def final(self):
        self.excel.final()
        self.driver.quit()

    def getDataPage(self, date, page, name):
        elements = self.driver.find_elements_by_class_name("nblock")
        block = self.driver.find_elements_by_class_name("blockcontent")
        el = self.driver.find_element_by_class_name("close")
        for x in range(len(elements)):
            try:
                elements[x].click()
            except:
                continue
            time.sleep(.6)
            title = self.checkExistsClassName("newsbodytitr", block[x])
            author = self.checkExistsClassName("newsauthor", block[x])
            author = author.replace("نویسنده :", "")
            titr = self.checkExistsClassName("newsbodyrotitr", block[x])
            removetitle = ['پیشخوان بین الملل', 'نمای روز', 'چهره روز', 'چهره ها', 'چهره ها و خبر ها', 'اظهارنظر روز',
                           'چهره ها و خبر ها', 'توئیت روز', 'هوش منطقی', 'بازی با کلمات', 'چالش ذهن', 'اختلاف تصاویر',
                           'عددیاب', 'خفن استریپ', 'بازی ریاضی', 'تست هوش', 'سودوکو', 'حل‌جداول‌ومعماها']
            removetitr = ['سینمای جهان', 'شاخص', 'تلویزیون', 'چهره', 'توییت سیاسی']
            removetitle1 = ['حرف مردم', 'اخبار', 'از میان خبر ها', 'بدون شرح', 'ما و شما', 'پیامک روز', 'تیتر روز',
                            'چند خط خبر', 'رویداد', 'نگاه سوم']
            if (title != "" and title not in removetitle and titr not in removetitr):
                if (not (title in removetitle1 and titr == '')):
                    try:
                        # print("-------------")
                        if titr == "تحلیل روز" or titr == "یادداشت روز":
                            self.excel.write_by_list_in_next_row([date, title, titr, author, name, page, 'تحلیلی'])
                            # print(self.numberrow,[date, title, titr, author, name, page, 'تحلیلی'])
                        else:
                            self.excel.write_by_list_in_next_row([date, title, titr, author, name, page])
                            # print(self.numberrow,[date, title, titr, author, name, page])
                        self.numberrow += 1
                        # print()
                    except Exception as e:
                        print(e)

            try:
                self.el.click()
            except:
                pass
