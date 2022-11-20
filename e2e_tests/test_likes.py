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
import datetime

x =datetime.datetime.now(tz=datetime.timezone.utc)

class TestLikes(StaticLiveServerTestCase):

    def setUp(self):
        self.browser =  webdriver.Chrome('e2e_tests/chromedriver.exe')

        self.usuario = User.objects.create(username='usuario')
        self.usuario.set_password('cesar123')
        self.usuario.save()
        self.c = Client()
        logged_in = self.c.login(username='usuario', password='cesar123')

        Post.objects.create(usuario=self.usuario, image='sample.png', caption='post teste', created=x)
        self.browser.get("http://localhost:8000/feed/")

    def tearDown(self):
        self.browser.close()
    
    def teste_like(self):
        self.browser.find_element(By.XPATH, '/html/body/div/p/a').click()
        self.browser.find_element(By.XPATH, '/html/body/div/form[1]/button').click()

        assert '1 curtidas' in self.browser.page_source
    
    def teste_like_multiplas_vezes_mesmo_user(self):
        self.browser.find_element(By.XPATH, '/html/body/div/p/a').click()
        self.browser.find_element(By.XPATH, '/html/body/div/form[1]/button').click()
        self.browser.find_element(By.XPATH, '/html/body/div/form[1]/button').click()
        self.browser.find_element(By.XPATH, '/html/body/div/form[1]/button').click()

        assert '1 curtidas' in self.browser.page_source
    
    def teste_like_multiplas_vezes_user_diferente(self):
        self.browser.find_element(By.XPATH, '/html/body/div/p/a').click()
        self.browser.find_element(By.XPATH, '/html/body/div/form[1]/button').click()

        self.c.logout()

        self.usuario2 = User.objects.create(username='usuario2')
        self.usuario2.set_password('cesar123')
        self.usuario2.save()
        self.c2 = Client()
        self.c2.login(username='usuario2', password='cesar123')

        self.browser.get("http://localhost:8000/feed/")

        self.browser.find_element(By.XPATH, '/html/body/div/p/a').click()
        self.browser.find_element(By.XPATH, '/html/body/div/form[1]/button').click()

        assert '2 curtidas' in self.browser.page_source