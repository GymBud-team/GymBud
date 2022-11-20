from main.models import Post
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class TestLandingPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser =  webdriver.Chrome('e2e_tests/chromedriver.exe')
        self.usuario = User.objects.create_user(username='usuario')
        self.usuario.set_password('cesar123') 
        self.usuario.save()
        self.browser.get("http://localhost:8000/")

    def tearDown(self):
        self.browser.close()

    def test_login_invalido(self):

        user = self.browser.find_element(By.XPATH, '/html/body/section[2]/form/div/div[1]/input')
        passw = self.browser.find_element(By.XPATH, '/html/body/section[2]/form/div/div[2]/input')
        submit = self.browser.find_element(By.XPATH, '/html/body/section[2]/form/div/div[3]/button')

        user.send_keys('teste')
        passw.send_keys('cesar123')
        submit.send_keys(Keys.RETURN)

        assert 'incorretos' in self.browser.page_source
    
    def test_login_valido(self):

        user = self.browser.find_element(By.XPATH, '/html/body/section[2]/form/div/div[1]/input')
        passw = self.browser.find_element(By.XPATH, '/html/body/section[2]/form/div/div[2]/input')
        submit = self.browser.find_element(By.XPATH, '/html/body/section[2]/form/div/div[3]/button')

        user.send_keys('usuario')
        passw.send_keys('cesar123')
        submit.send_keys(Keys.RETURN)

        add_url = 'http://localhost:8000/confirmed/'
        self.assertEquals(self.browser.current_url, add_url )
    
    def test_cadastro_button_redirects_to_cadastro_page(self):

        cadastro = self.browser.find_element(By.XPATH, '/html/body/section[1]/header/div/div[2]/a')
        cadastro.click()
        add_url = 'http://localhost:8000/register/'
        self.assertEquals(self.browser.current_url, add_url )
    
    def test_cadastro_a_redirects_to_cadastro_page(self):

        cadastro = self.browser.find_element(By.XPATH, '/html/body/section[2]/form/div/p/a')
        cadastro.click()
        add_url = 'http://localhost:8000/register/'
        self.assertEquals(self.browser.current_url, add_url )
