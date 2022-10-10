from time import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def login(self, username, password):    
        username_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_polje.clear()
        username_polje.click()
        username_polje.send_keys(username)
        password_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_polje.clear()
        password_polje.click()
        password_polje.send_keys(password)
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
    
    def get_title_text(self):
        welcome_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='title']")))
        return welcome_element.text

    def products(self,n1,n2):
        addTocard = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//button[text()='Add to cart']")))
        sviNazivi = self.wait.until(EC.visibility_of_any_elements_located((By.XPATH,"//div[@class='inventory_item_name']")))
        addTocard[n1].click()
        addTocard[n2].click()
        prvi = sviNazivi[n1].text
        drugi = sviNazivi[n2].text
        kolica = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']")))
        kolica.click()
        return [prvi, drugi]
        

    def provjera(self):
        items = self.wait.until(EC.visibility_of_any_elements_located((By.XPATH, "//div[@class ='inventory_item_name']")))
        return [items[0].text, items[1].text]

    def checkout(self,ime, prezime, kod):
        dugmeCheckout = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        dugmeCheckout.click()
        assert self.get_title_text() == "CHECKOUT: YOUR INFORMATION"
        firstname = self.wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        firstname.clear()
        firstname.click()
        firstname.send_keys(ime)
        lastname = self.wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        lastname.clear()
        lastname.click()
        lastname.send_keys(prezime)
        zipKod = self.wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
        zipKod.clear()
        zipKod.click()
        zipKod.send_keys(kod)
        continueButton = self.driver.find_element(By.ID, "continue")
        continueButton.click()

    def kraj(self):
        dugmeKraj = self.wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        dugmeKraj.click()
        assert self.get_title_text() == "CHECKOUT: COMPLETE!"
        menuButton = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menuButton.click()
        logout_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text() ='Logout']")))
        logout_element.click()
        username_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))



    


