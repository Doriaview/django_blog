# django_blog

 Este es un proyecto de blog simple realizado con Django. Permite listar publicaciones, ver los detalles y agregar nuevas publicaciones a través de un formulario web.

 ## Instalación

1. Clona el repositorio:
   git clone <URL_del_repositorio>
   cd blog

2. Crea un entorno virtual y actívalo:

    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows

3. Instala las dependencias:

    pip install -r requirements.txt

4. Realiza las migraciones:

    python manage.py migrate

5. Inicia el servidor de desarrollo:

    python manage.py runserver
    Accede a http://127.0.0.1:8000/ en tu navegador.
