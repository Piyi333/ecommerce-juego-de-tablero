Proyecto E-commerce Django - Juegos de Mesa



- Aplicación web de e-commerce desarrollada con Django que permite a los usuarios registrarse, iniciar sesión, explorar un catálogo de productos, gestionar un carrito de compras y realizar pedidos.

- El proyecto está enfocado en la temática de juegos de mesa y fue desarrollado como proyecto final de un curso de Full Stack con Python.



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


✮⋆˙Enlace al repositorio publico:

https://github.com/Piyi333/ecommerce-juego-de-tablero.git



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


✮⋆˙ Funcionalidades:

> Usuarios (clientes):

- Registro e inicio de sesión
- Visualización del catálogo de productos
- Agregar productos al carrito
- Eliminar productos del carrito
- Visualizar total de compra
- Confirmar pedido


> Administrador:

- Crear productos
- Editar productos
- Eliminar productos
- Gestión completa desde la aplicación



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


✮⋆˙ Tecnologías utilizadas:

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap
- Git y GitHub



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


✮⋆˙ Estructura del proyecto:

ecommerce/
│── products/
│── users/
│── templates/
│── static/
│── manage.py


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


✮⋆˙ Instalación y ejecución

- Sigue estos pasos para ejecutar el proyecto en local:


1. Clonar repositorio:

git clone https://github.com/Piyi333/ecommerce-juego-de-tablero.git
cd ecommerce


2. Crear entorno virtual:

python -m venv env


3. Activar entorno virtual:

- En Windows:

env\Scripts\activate

- En Mac/Linux:

source env/bin/activate


4.- Instalar dependencias:

pip install -r requirements.txt


5. Aplicar migraciones:

python manage.py migrate


6. Crear superusuario:

python manage.py createsuperuser


7. Ejecutar servidor:

python manage.py runserver



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


✮⋆˙ Rutas principales:

> Públicas:

/ → inicio
/login/ → login
/register/ → registro

> Ecommerce:

/products/ → lista de productos
/cart/ → carrito
/add/<id>/ → agregar producto
/remove/<id>/ → eliminar producto
/checkout/ → finalizar compra

> Admin:

/admin/


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

✮⋆˙ Credenciales de prueba:

> Administrador:

- User: admin
- Pass: admin


> Clientes:

- User: cliente1
- Pass: charmander1

- User: cliente2
- Pass: pikachu1!

- User: cliente3
- Pass: squirtle1!
