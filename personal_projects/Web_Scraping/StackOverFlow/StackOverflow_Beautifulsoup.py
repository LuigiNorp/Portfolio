import requests
from bs4 import BeautifulSoup

encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.149 Safari/537.36 "
}
url = "https://stackoverflow.com/questions"
respuesta = requests.get(url, headers=encabezados)
soup = BeautifulSoup(respuesta.text)  # <-- En vez de parser ahora es soup

# Find para Buscar el (único) Id "Questions"
contenedor_de_preguntas = soup.find(id="questions")

# Se usa find_all() para Buscar varias preguntas en Stackoverflow
"""
contenedor_de_preguntas.find_all(class="questions-summary") <-- Error porque class es keyword
contenedor_de_preguntas.find_all(class_="questions-summary")<-- Lo correcto es class_
"""

# Para asegurarse de que el elemento encontrado es el que quiero podemos verificar
# que su tag sea "div"
# [Añadir imagen de árbol HTML]
"""
También pudo escribirse en la línea anterior: 
    contenedor_de_preguntas = soup.find("div", id="questions")
"""
lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="question-summary")

for pregunta in lista_de_preguntas:
    """
    # Para obtener el 'Título de la Pregunta' se usa H3 porque es la única que no se repite
    # en el árbol, se usa text para obtener texto
    # [Añadir imagen de árbol HTML]
    texto_pregunta = pregunta.find("h3").text
    
    # El texto del título en realidad está dentro del tag <a>, hijo del tag <h3>. Sin embargo, 
    # hacer .text en Beautifulsoup implica sacar todo el texto contenido en el tag, incluyendo 
    # el de sus hijos.
    

    # Para obtener la 'Descripción de la Pregunta' se usa excerpt, ya que en el arbol se observa
    # que el div que contiene la descripción es de clase excerpt
    # [Añadir imagen de árbol HTML]
    descripcion_pregunta = pregunta.find(class_="excerpt").text
    # Se le da un formato más legible a lo obtenido con lo siguiente:
    descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '').strip()

    # Imprimir datos
    print(texto_pregunta)
    print(descripcion_pregunta)
    print()
    """
# La ventaja de Beautifulsoup frente a LXML es que puede moverse a su primo siguiente, en caso de
# que no tuviera ninguna clase que podamos usar:

    elemento_texto_pregunta = pregunta.find('h3')

    texto_pregunta = elemento_texto_pregunta.text

# Avanza de h3 a su siguiente primo que sea 'div'
    descripcion_pregunta = elemento_texto_pregunta.find_next_sibling('div').text
    descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '').strip()

    # Imprimir datos
    print(texto_pregunta)
    print(descripcion_pregunta)
    print()