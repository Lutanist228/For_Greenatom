from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

URL = r"https://greenatom.ru/"
chromedriver_autoinstaller.install()
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opt)
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get(URL) # подключаемся к сайту (главной странице greenatom)

total_tag = len(driver.find_elements(By.TAG_NAME, "div")) + len(driver.find_elements(By.TAG_NAME, "a")) + len(driver.find_elements(By.TAG_NAME, "li")) + len(driver.find_elements(By.TAG_NAME, "h2")) + len(driver.find_elements(By.TAG_NAME, "span")) + len(driver.find_elements(By.TAG_NAME, "br")) + len(driver.find_elements(By.TAG_NAME, "p")) + + len(driver.find_elements(By.TAG_NAME, "i")) + len(driver.find_elements(By.TAG_NAME, "b")) + len(driver.find_elements(By.TAG_NAME, "script")) + len(driver.find_elements(By.TAG_NAME, "body")) + len(driver.find_elements(By.TAG_NAME, "html")) + len(driver.find_elements(By.TAG_NAME, "img")) + len(driver.find_elements(By.TAG_NAME, "font")) + len(driver.find_elements(By.TAG_NAME, "input")) + len(driver.find_elements(By.TAG_NAME, "meta")) + len(driver.find_elements(By.TAG_NAME, "link")) + len(driver.find_elements(By.TAG_NAME, "noscript")) + len(driver.find_elements(By.TAG_NAME, "form")) + len(driver.find_elements(By.TAG_NAME, "button")) 
# total_tag ищет все тэги на странице, суммируя все результаты по определённым тэгам.  
# всего - 20 "типов" тэгов, из которых всего 15 имеют атрибуты. Ниже идёт алгоритм рассчета тэгов с атрибутами. (br\i\b\nonscript\html)

tag_div = driver.find_elements(By.TAG_NAME, "div")
tag_a = driver.find_elements(By.TAG_NAME, "a")
tag_li = driver.find_elements(By.TAG_NAME, "li")
tag_h2 = driver.find_elements(By.TAG_NAME, "h2")
tag_span = driver.find_elements(By.TAG_NAME, "span")
tag_p = driver.find_elements(By.TAG_NAME, "p")
tag_script = driver.find_elements(By.TAG_NAME, "script")
tag_image = driver.find_elements(By.TAG_NAME, "img")
tag_input = driver.find_elements(By.TAG_NAME, "input")
tag_meta = driver.find_elements(By.TAG_NAME, "meta")
tag_link = driver.find_elements(By.TAG_NAME, "link")

div_count = 0 # считает количество тэгов "div" с атрибутами
a_count = 0 # считает количество тэгов "a" с атрибутами
li_count = 0 # считает количество тэгов "li" с атрибутами
h2_count = 0 # считает количество тэгов "h2" с атрибутами
span_count = 0 # считает количество тэгов "span" с атрибутами
p_count = 0 # далее - такая же логика (кроме тех тэгов с атрибутами, количество которых наглядно)
script_count = 0 
body_count = len(driver.find_elements(By.TAG_NAME, "class"))
image_count = 0 
font_count = len(driver.find_elements(By.TAG_NAME, "size"))
input_count = 0
meta_count = 0
link_count = 0 
form_count = len(driver.find_elements(By.TAG_NAME, "action"))
button_count = len(driver.find_elements(By.TAG_NAME, "type"))

for i in range(len(tag_div)):

    class_atr = tag_div[i].get_attribute("class")
    id_attr = tag_div[i].get_attribute("id")
    style_attr = tag_div[i].get_attribute("style")

    if class_atr != "":
        if (id_attr == "" and style_attr == ""): # подсчет одиночных class
            div_count += 1
        elif (id_attr != "" or style_attr != ""): # подсчёт классов смешанных с id или style
            div_count += 1 

    if id_attr != "":
        if (style_attr == "" and class_atr == ""): # подсчет одиночных id 
            div_count += 1 
        elif (style_attr != ""): # подсчёт id смешанных с style
            div_count += 1 

    if style_attr != "":
        if (id_attr == "" and class_atr == ""): # подсчет одиночных style
            div_count += 1 
    # такая же логика подсчёта и в остальных циклах!!!!

for i in range(len(tag_a)):

    href_attr = tag_a[i].get_attribute("href")
    class_attr = tag_a[i].get_attribute("class")
    style_attr = tag_a[i].get_attribute("style")


    if href_attr != "":
        if (class_attr == "" and style_attr == ""):
            a_count += 1 
        elif (class_atr != "" or style_attr != ""): # для class и style и class_href после этого не указываем совместимость с href
            a_count += 1 
    
    if class_atr != "":
        if (style_attr == "" and href_attr == ""):
            a_count += 1 
        elif style_attr != "":
            a_count += 1
    
    if style_attr != "":
        if (class_attr == "" and href_attr == ""):
            a_count += 1 
    
for i in range(len(tag_li)):

    class_attr = tag_li[i].get_attribute("class")
    if class_attr != "":
        li_count += 1 
   
for i in range(len(tag_h2)):

    class_attr = tag_h2[i].get_attribute("class")

    if class_attr != "":
        h2_count += 1 

for i in range(len(tag_span)):
    
    class_attr = tag_span[i].get_attribute("class")

    if class_attr != "":
        span_count += 1 

for i in range(len(tag_p)):
    
    style_attr = tag_p[i].get_attribute("style")
    class_attr = tag_p[i].get_attribute("class")

    if style_attr != "":
        if class_attr == "":
            p_count += 1 
    
    if class_attr != "":
        if style_attr == "":
            p_count += 1

for i in range(len(tag_script)):
    
    src_attr = tag_script[i].get_attribute("src")
    type_attr = tag_script[i].get_attribute("type")

    if src_attr != "":
        if type_attr == "":
            script_count += 1 
        elif type_attr != "":
            script_count += 1 
    
    if type_attr != "":
        if src_attr == "":
            script_count += 1

for i in range(len(tag_image)):
    
    src_attr = tag_image[i].get_attribute("src")
    class_attr = tag_image[i].get_attribute("class")

    if src_attr != "":
        if class_attr == "":
            image_count += 1 
        elif class_attr != "":
            image_count += 1 
    
    if class_attr != "":
        if src_attr == "":
            image_count += 1

for i in range(len(tag_input)):
    
    class_attr = tag_input[i].get_attribute("class")

    if class_attr != "":
        input_count += 1 

for i in range(len(tag_meta)):
    
    content_attr = tag_meta[i].get_attribute("content")
    charset_attr = tag_meta[i].get_attribute("charset")
    lang_attr = tag_meta[i].get_attribute("lang")

    if lang_attr != "":
        meta_count += 1 

    if content_attr != "":
        if charset_attr == "" and lang_attr == "":
            meta_count += 1
        elif charset_attr != "" or lang_attr != "":
            meta_count += 1

    if charset_attr != "":
        if lang_attr == "" and content_attr == "":
            meta_count += 1

for i in range(len(tag_link)):
    
    href_attr = tag_link[i].get_attribute("href")

    if href_attr != "":
        link_count += 1 



total_tag_attr = a_count + div_count + li_count + h2_count + span_count + p_count + script_count + body_count + font_count + image_count + input_count + meta_count + link_count + form_count + button_count

print("Всего тэгов на странице: ", total_tag, end="\n\n")
print("Всего тэгов с атрибутами на странице: ", total_tag_attr)


k = input()