from main.models import Post
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from django.test import Client
import os

class TestFeedPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser =  webdriver.Chrome('e2e_tests/chromedriver.exe')

        self.usuario = User.objects.create(username='usuario')
        self.usuario.set_password('cesar123')
        self.usuario.save()
        c = Client()
        logged_in = c.login(username='usuario', password='cesar123')

        self.browser.get("http://localhost:8000/feed/")

    def tearDown(self):
        self.browser.close()
    
    def test_post(self):
        criar = self.browser.find_element(By.XPATH, '/html/body/div/h4/a').click()
        file = self.browser.find_element(By.XPATH, '/html/body/form/p[1]/input').send_keys(os.getcwd()+ "/sample.png")
        caption = self.browser.find_element(By.XPATH, '/html/body/form/p[2]/textarea').send_keys("post teste")
        submit = self.browser.find_element(By.XPATH, '/html/body/form/input[2]').send_keys(Keys.RETURN)

        assert 'post teste' in self.browser.page_source
    
    def test_post_sem_imagem(self):
        criar = self.browser.find_element(By.XPATH, '/html/body/div/h4/a').click()
        caption = self.browser.find_element(By.XPATH, '/html/body/form/p[2]/textarea').send_keys("post teste")
        submit = self.browser.find_element(By.XPATH, '/html/body/form/input[2]').send_keys(Keys.RETURN)

        add_url = 'http://localhost:8000/createpost/'
        
        self.assertEquals(self.browser.current_url, add_url)
    
    def teste_ver_post(self):
        criar = self.browser.find_element(By.XPATH, '/html/body/div/h4/a').click()
        file = self.browser.find_element(By.XPATH, '/html/body/form/p[1]/input').send_keys(os.getcwd()+ "/sample.png")
        caption = self.browser.find_element(By.XPATH, '/html/body/form/p[2]/textarea').send_keys("post teste")
        submit = self.browser.find_element(By.XPATH, '/html/body/form/input[2]').send_keys(Keys.RETURN)
        self.browser.find_element(By.XPATH, '/html/body/div/p/a').click()

        add_url = 'http://localhost:8000/post/1/'
        self.assertEquals(add_url, self.browser.current_url)