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

class TestRequestWorkoutPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser =  webdriver.Chrome('e2e_tests/chromedriver.exe')

        self.usuario = User.objects.create(username='usuario')
        self.usuario.set_password('cesar123')
        self.usuario.save()
        c = Client()
        c.login(username='usuario', password='cesar123')

        self.browser.get("http://localhost:8000/requestworkout/")
    
    def tearDown(self):
        self.browser.close()

    def solicitar_treino(self):
        horas = self.browser.find_element(By.XPATH, '/html/body/form/p[2]/textarea').send_keys(1)
        condicao = self.browser.find_element(By.XPATH, '/html/body/form/p[3]/textarea').send_keys('nada')
        submit = self.browser.find_element(By.XPATH, '/html/body/form/input[2]').send_keys(Keys.RETURN)

        assert 'Sua solicitação já foi recebida' in self.browser.page_source

    def solicitar_treino_sem_condicao(self):
        horas = self.browser.find_element(By.XPATH, '/html/body/form/p[2]/textarea').send_keys(1)
        submit = self.browser.find_element(By.XPATH, '/html/body/form/input[2]').send_keys(Keys.RETURN)

        add_url = 'http://localhost:8000/requestworkout/'
        self.assertEquals(self.browser.current_url, add_url)
    
    def solicitar_treino_duas_vezes(self):
        horas = self.browser.find_element(By.XPATH, '/html/body/form/p[2]/textarea').send_keys(1)
        condicao = self.browser.find_element(By.XPATH, '/html/body/form/p[3]/textarea').send_keys('nada')
        submit = self.browser.find_element(By.XPATH, '/html/body/form/input[2]').send_keys(Keys.RETURN)

        voltar = self.browser.find_element(By.XPATH, '/html/body/p/a').send_keys(Keys.RETURN)

        self.browser.get("http://localhost:8000/requestworkout/")

        horas = self.browser.find_element(By.XPATH, '/html/body/form/p[2]/textarea').send_keys(2)
        condicao = self.browser.find_element(By.XPATH, '/html/body/form/p[3]/textarea').send_keys('nothing')
        submit = self.browser.find_element(By.XPATH, '/html/body/form/input[2]').send_keys(Keys.RETURN)


        assert 'Sua solicitação já foi recebida' in self.browser.page_source
       