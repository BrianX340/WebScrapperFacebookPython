from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from webdriver_manager.chrome import ChromeDriverManager
import wget
import os
import time
import getpass



#Defina un usuario y clave
user = input('Ingrese su usuario de facebook: ')
passw = getpass.getpass("Ingrese su contraseña: ")

#Objetivo scrapear fotos
objetive = input("Ingrese usuario objetivo: ")


enlaces_descarga = []
lista_albumes = []

album_name = []


PWD = os.path.abspath(os.curdir)



try:
    os.stat(objetive)
except:
    os.mkdir(objetive)

def scroll(driver):
    asd = 3

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)

        # Wait to load page
        time.sleep(asd)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height 
    
                                
#Comenzamos
with webdriver.Chrome(executable_path=r'.\chromedriver.exe') as driver:
    wait = driver.implicitly_wait(3)
    driver.get("https://mbasic.facebook.com/login/?ref=dbl&fl")
    driver.find_element_by_id("m_login_email").send_keys(user)
    driver.find_element_by_name('pass').send_keys(passw)
    driver.find_element_by_name('login').click()
    
    time.sleep(3)
    
    driver.get(f"https://m.facebook.com/{objetive}/photos")
    #Hasta aqui logeamos y entramos al perfil fotos

    #con esto buscamos en cada album
    albumes = driver.find_elements_by_xpath("//div[@id='rootcontainer']/div/div/div/div/div/a")
    for album in albumes:
        lista_albumes.append(album.get_attribute("href"))
        
    
    albumes_nombre = driver.find_elements_by_xpath("//div[@id='rootcontainer']/div/div/div/div/div/a/div/div/div/strong")
    for album in albumes_nombre:
        album_name.append(album.text)
        try:
            os.stat('{}\\{}'.format(objetive,album.text))
        except:
            os.mkdir('{}\\{}'.format(objetive,album.text))
    
    

    
    for indice, album in enumerate(lista_albumes):
        lista_fotos = []
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[1])
    
    
        driver.get(album)
        scroll(driver)

        elemento_fotos = driver.find_elements_by_css_selector('#rootcontainer #root div span a')
        
        
        for elem in elemento_fotos:
            href = elem.get_attribute('href')
            lista_fotos.append(href)
        
                                
        for foto in lista_fotos: 
            driver.execute_script("window.open()")
            driver.switch_to.window(driver.window_handles[2])
            driver.get(foto)
            
            enlaces = driver.find_elements_by_css_selector('.desc .fcg .atb span a')
            
            for enlace in enlaces:
                if enlace.get_attribute('target') == "_blank":
                    #aca buscamos el enlace para ver imagen completa
                    image_url = enlace.get_attribute("href")
                    driver.get(image_url)

                    image_url_final = driver.find_element_by_css_selector('img').get_attribute("src")
                    wget.download(image_url_final, PWD+'\\{}\\{}\\'.format(objetive,album_name[indice]))
                    print(lista_albumes)
                    enlaces_descarga.append(image_url_final)
                    
                    driver.close()
                    driver.switch_to.window(driver.window_handles[1])
                     break
    
    driver.back()







"""
#Si algun album no se descarga correctamente podemos usar este codigo para extraer el album aparte, solo debemos pegar el enlace al album...

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from webdriver_manager.chrome import ChromeDriverManager
import wget
import os
import time
import getpass



#Defina un usuario y clave
user = 
passw = 

#Objetivo scrapear fotos
objetive = 


enlaces_descarga = []
lista_albumes = []

album_name = []


PWD = os.path.abspath(os.curdir)



try:
    os.stat(objetive)
except:
    os.mkdir(objetive)

def scroll(driver):
    asd = 3

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)

        # Wait to load page
        time.sleep(asd)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height 
    
                                
#Comenzamos
with webdriver.Chrome(executable_path=r'.\chromedriver.exe') as driver:
    wait = driver.implicitly_wait(3)
    driver.get("https://mbasic.facebook.com/login/?ref=dbl&fl")
    driver.find_element_by_id("m_login_email").send_keys(user)
    driver.find_element_by_name('pass').send_keys(passw)
    driver.find_element_by_name('login').click()
    
    time.sleep(3)
    

    lista_fotos = []
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])

    album  = input("url")
    driver.get(album)
    scroll(driver)

    elemento_fotos = driver.find_elements_by_css_selector('#rootcontainer div div div div div a')
    
    print(elemento_fotos)
    input()
    for elem in elemento_fotos:
        href = elem.get_attribute('href')
        lista_fotos.append(href)

    print(lista_fotos)
    
    for foto in lista_fotos: 
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[2])
        driver.get(foto)

        enlaces = driver.find_elements_by_css_selector('#rootcontainer div div div div div')

        for enlace in enlaces:
            if enlace.get_attribute('target') == "_blank":
                #aca buscamos el enlace para ver imagen completa
                image_url = enlace.get_attribute("href")
                driver.get(image_url)

                image_url_final = driver.find_element_by_css_selector('img').get_attribute("src")
                wget.download(image_url_final, PWD+'\\{}\\{}\\'.format(objetive,album_name[indice]))
                print(lista_albumes)
                enlaces_descarga.append(image_url_final)

                driver.close()
                driver.switch_to.window(driver.window_handles[1])
                break

    driver.back()
"""