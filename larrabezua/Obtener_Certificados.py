import shutil
from time import sleep
import os
import json
from winreg import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver import ChromeOptions


def here():
    """
    Obtains the current working directory

    Returns:
         (str) Current working path without file name.
    """
    return os.getcwd()


def list_files_from(directory=here()):
    """
    Return a list with the name of files contained in a especified directory.

    Parameters:
        directory (str) Is the directory from where files will be listed
    Returns:
        (list): List with the name of files contained in the directory
    """
    file_list = os.listdir(directory)
    return file_list


def different_values(list_a: list, list_b: list):
    """
    To return a list with the different elements between two lists.

    Parameters:
        list_a (list): This will be compared with list_b
        list_b (list): This will be compared with list_a

    Returns:
        differences (list): A list with the non repeated elements between two lists
    """
    differences = [item for item in list_b if item not in list_a]
    differences += [item for item in list_a if item not in list_b]
    return differences


def win_download_folder_path():
    """
    Returns a string variable with the directory of 'Donwloads' folder (Only for Microsoft Windows).

    Returns:
        download_folder_path (str): 'Downloads' folder path for Windows in a string variable
    """
    with OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        downloads_folder_path = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
    return downloads_folder_path


def move_files_to(source_folder: str, destination_folder: str, files: list):
    """
    Moves files from a source folder to a specified directory.

    Parameters:
        source_folder (str): This is the source path where files come from

        destination_folder (str): This is the path where file will be placed in

        files (list): This is a list of the files that will be moved
    """
    # Setting Absolute Path
    source_folder = os.path.abspath(source_folder)
    destination_folder = os.path.abspath(destination_folder)

    # Iterate files
    for file in files:
        # construct full file path
        source = source_folder + "/" + file
        destination = destination_folder + "/" + file
        # Per file in files Move file
        shutil.move(source, destination)
        print('Downloaded:', file)


class CertificateDownloader:
    """
    Este programa realiza la descarga de varios certificados pertenecientes a una empresa y los ,
    primero accediendo a la página donde se encuentran la lista de alumnos, a la cual se le  aplica
    tres filtros para garantizar que los certificados sean de alumnos actuales, posteriormente
    se procede a ingresar dentro de cada uno. Una vez dentro
    """

    def __init__(self):
        # Setting Printer
        pdf_printer_settings = {
            "recentDestinations": [{
                "id": "Save as PDF",
                "origin": "local",
                "account": "",
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }

        # Setting Chrome Webdriver
        self.opts = ChromeOptions()
        self.opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                               "AppleWebKit/537.36 (KHTML, like Gecko) "
                               "Chrome/80.0.3987.132 Safari/537.36")
        prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(pdf_printer_settings)}

        self.opts.add_experimental_option('prefs', prefs)
        self.opts.add_argument('--kiosk-printing')

        # opts.gpu = False
        # opts.headless = True

    def close_tab(self):
        pestanas_abiertas = self.driver.window_handles
        self.driver.switch_to.window(pestanas_abiertas[-1])
        self.driver.close()

    def switch_tab(self, tab_number):
        pestanas_abiertas = self.driver.window_handles
        self.driver.switch_to.window(pestanas_abiertas[tab_number])

    def login(self, username, password):
        """
        Detect username and password input cages, introduce credentials,

        :param username:
        :param password:
        :return:
        """
        input_user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="username"]')))
        input_pass = self.driver.find_element(By.XPATH, '//input[@name="password"]')

        input_user.send_keys(username)
        input_pass.send_keys(password)

        boton_acceder = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        boton_acceder.click()

    # Launching Chrome Webdriver
    def launch(self, usuario, password, reducir_cant=0):
        global cant_certificados_carpeta, cant_certificados_persona
        self.driver = webdriver.Chrome('./chromedriver.exe', options=self.opts)
        login_url = 'https://aprende.larrabezua.com.mx/login/index.php'
        self.driver.get(login_url)

        self.login(usuario, password)

        # Boton Lateral
        barra_lateral_principal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="sidebar-btn"]')))

        if barra_lateral_principal.get_attribute('aria-expanded') == 'false':
            barra_lateral_principal.click()

        # Ingresando a la Lista de Usuarios
        # Administracion del Sitio
        self.driver.implicitly_wait(15)
        administracion = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="Administración del sitio"]')))

        try:
            administracion.click()
        except Exception as e:
            print(e)
            self.driver.quit()

        # Pestaña Usuarios
        pestana_usuarios = self.driver.find_element_by_xpath('//a[@href="#linkusers"]')
        try:
            pestana_usuarios.click()
        except Exception as e:
            print(e)

        # Lista Usuarios
        link_lista_usuarios = self.driver.find_element_by_xpath(
            '(//a[@href="https://aprende.larrabezua.com.mx/admin/user.php"])[1]')
        try:
            link_lista_usuarios.click()
        except Exception as e:
            print(e)
            self.driver.quit()

        # Filtrar Lista de Usuarios
        # Boton Mostrar Más
        barra_lateral_usuarios = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="sidebar-btn"]')))
        if barra_lateral_usuarios.get_attribute('aria-expanded') == 'true':
            barra_lateral_usuarios.click()

        btn_mostrar_mas = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="moreless-toggler"]')))
        btn_mostrar_mas.click()

        # Cuenta suspendida = NO
        filt_cta_suspend = Select(self.driver.find_element_by_xpath('//select[@id="id_suspended"]'))
        filt_cta_suspend.select_by_value('0')

        # ID cohorte = WEC
        filt_cohorte = self.driver.find_element_by_xpath('//input[@id="id_cohort"]')
        filt_cohorte.send_keys('WEC')

        # Fecha posterior a 2019
        boton_habilitar_fecha = self.driver.find_element_by_xpath('(//span[@class="ios-switch-control-indicator"])[1]')
        boton_habilitar_fecha.click()
        seleccionar_anyo = Select(self.driver.find_element_by_xpath('//select[@id="id_firstaccess_sdt_year"]'))
        seleccionar_anyo.select_by_value('2019')

        # Boton Añadir Filtro
        agregar_filtro = self.driver.find_element_by_xpath('//input[@value="Añadir filtro"]')
        try:
            agregar_filtro.click()
        except Exception as e:
            print(e)

        # Lista de usuarios
        ventana_lista_nombres = self.driver.current_window_handle

        carpeta_alumno = input('Introduzca la ruta donde quiere almacenar las carpetas: ')

        while True:
            # Encontrar nombres:
            # self.driver.implicitly_wait(15)
            lista_nombres = self.driver.find_elements_by_xpath('//tbody//td[contains(@class, "cell c0")]/a')

            for nombre in lista_nombres:
                actual = []
                print(nombre.text)
                try:
                    # Creando carpeta de Alumno
                    os.mkdir(str(nombre.text))

                    # Generando dirección de carpeta
                    if carpeta_alumno == "":
                        carpeta_alumno = str(os.getcwd().replace('\\', '/') + "/" + nombre.text)
                        cant_certificados_carpeta = len(list_files_from(carpeta_alumno))
                        print("Carpeta del alumno:", carpeta_alumno)
                        print("Cantidad de archivos: ", cant_certificados_carpeta)
                    else:
                        carpeta_alumno = str(os.getcwd().replace('\\', '/') + "/" + nombre.text)

                except Exception:
                    # Generando dirección de carpeta
                    if carpeta_alumno == "":
                        carpeta_alumno = str(os.getcwd().replace('\\', '/') + "/" + nombre.text)
                        print("Carpeta del alumno:", carpeta_alumno)
                        cant_certificados_carpeta = len(list_files_from(carpeta_alumno))
                        print("Cantidad de archivos: ", cant_certificados_carpeta)

                        print('Carpeta', nombre.text, "ya existe")
                    if nombre == lista_nombres[-1]:
                        carpeta_alumno = str(os.getcwd().replace('\\', '/') + "/" + nombre.text)
                        print("Carpeta del alumno:", carpeta_alumno)
                        cant_certificados_carpeta = len(list_files_from(carpeta_alumno))
                        print("Cantidad de archivos: ", cant_certificados_carpeta)
                        pass
                    else:
                        carpeta_alumno = str(os.getcwd().replace('\\', '/') + "/" + nombre.text)
                        continue

                # Ingresar al perfil del Alumno
                # Abrir link en pestaña aparte
                nombre.send_keys(Keys.CONTROL + Keys.RETURN)
                pestanas_abiertas = self.driver.window_handles

                # Cambiar a pestaña perfil del Alumno
                self.driver.switch_to.window(pestanas_abiertas[-1])

                # Abrir en la misma pestaña la lista de certificados
                boton_mis_certificados = self.driver.find_element_by_xpath('(//a[text()="Mis certificados"])[1]')
                try:
                    boton_mis_certificados.send_keys(Keys.RETURN)
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located)
                except Exception as e:
                    print(e)
                    self.driver.quit()

                # Boton Descargar Certificado
                lista_certificados = self.driver.find_elements_by_xpath(
                    '//tbody//td[contains(@class, "cell c4")]/a')

                # ------------------------- Requerir x certificados -----------------------------
                if reducir_cant == 0:
                    pass
                else:
                    for x in range(len(lista_certificados) - reducir_cant):
                        if len(lista_certificados) > 0:
                            lista_certificados.pop(-1)
                # -------------------------------------------------------------------------------
                # Estado carpeta descargas
                inicial = list_files_from(win_download_folder_path())


                # Abrir link de todos los certificados del alumno y esperar un tiempo entre c/u
                for certificado in lista_certificados:
                    cant_certificados_persona = len(self.driver.find_elements_by_xpath(
                        '//tbody//tr[@class=""]/td[@class="cell c0"]'))
                    if cant_certificados_persona == cant_certificados_carpeta:
                        continue
                    else:
                        certificado.send_keys(Keys.CONTROL + Keys.RETURN)

                # Por cada certificado dirigirse a la pestaña del certificado y descargarlo
                c = -1
                for cert in lista_certificados:
                    if cant_certificados_persona == cant_certificados_carpeta:
                        continue
                    else:
                        sleep(5)
                        # Cambio a pestaña en cuestion
                        pestanas_abiertas = self.driver.window_handles
                        self.driver.switch_to.window(pestanas_abiertas[c])
                        # Esperar a que cargue el certificado
                        sleep(4)
                        # Descarga de certificado (En downloads)
                        try:
                            self.driver.execute_script('window.print();')
                        except Exception as e:
                            print(e)
                            continue
                    # Esperar a que cargue pagina
                    sleep(2)
                    c -= 1

                # Estado carpeta descargas
                actual = list_files_from(win_download_folder_path())
                # Agregar archivo a la lista de archivos a mover
                lista_de_archivos_a_mover = different_values(inicial, actual)
                # Mover archivos a la carpeta que pertenecen
                move_files_to(win_download_folder_path(), carpeta_alumno, lista_de_archivos_a_mover)

                # Por cada certificado dirigirse a la pestaña del certificado y cerrarla
                for x in lista_certificados:
                    if cant_certificados_persona == cant_certificados_carpeta:
                        continue
                    else:
                        pestanas_abiertas = self.driver.window_handles
                        self.driver.switch_to.window(pestanas_abiertas[-1])
                        self.driver.close()

                if nombre not in list_files_from():
                    # Cambiar a pestaña anterior y cerrar
                    pestanas_abiertas = self.driver.window_handles
                    self.driver.switch_to.window(pestanas_abiertas[-1])
                    self.driver.close()

                # Regresar a la lista de nombres
                self.driver.switch_to.window(ventana_lista_nombres)

                # Cambiar de página
                if lista_nombres[-1] == nombre:
                    try:
                        btn_siguiente = self.driver.find_element_by_xpath('(//a[@aria-label="Next"])[1]')
                        btn_siguiente.send_keys(Keys.RETURN)
                        WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located)
                        lista_nombres = self.driver.find_elements_by_xpath('//tbody//td[contains(@class, "cell c0")]/a')
                        continue
                    except Exception as e:
                        print(e)
                        self.driver.quit()
                        break


if __name__ == '__main__':
    # Login Credentials
    user = open('user.txt').readline().strip()
    pswd = open('pass.txt').readline().strip()

    # Initialize Donwloader
    downloader = CertificateDownloader()
    downloader.launch(user, pswd)
