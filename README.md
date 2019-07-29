
# django-backend
---

Aplicación desarrollada con **Python** y el Framework **Django** para proporcionar administración básica de entrega de comida.

El sistema cuenta con el apartado de administración y el de empleados, a continuación, se especificará las características de cada una.

## Administrador:
	•	Administrador de empleados: el usuario de tipo administrador puede crear, editar y eliminar empleados.
	•	Administrador de Menús: el usuario de tipo administrador puede crear, editar y eliminar menús.
	•	Administrador de Órdenes: el usuario de tipo administrador puede ver, editar y eliminar órdenes.
	•	Envió de notificaciones: el usuario puede enviar recordatorios vía correo electrónico a todos los empleados del menú 	diario disponible en el sistema.
## Validaciones:
	•	El sistema cuenta con las siguientes restricciones para el administrador:
	•	Solo se pueden registrar menús con fecha de hoy o posterior
	•	Solo se pueden crear menús hasta las 11:00 AM. (Esta validación no afecta a registro con fechas posteriores a la fecha actual)
	•	Solo se puede editar el menú hasta a las 10:00 AM. (esto con el fin que los empleados tengan un tiempo necesario para ordenar)
	•	Las notificaciones se pueden enviar hasta las 10:00 AM.

## Empleados:
	•	Registrar y editar ordenes: los empleados pueden registrar y editar una orden de una de las opciones de menús diarias disponible en el sistema.
	•	Ver listado de menús: los empleados pueden ver las opciones de menú diarias, disponibles en el sistema.
	•	Ver historial de ordenes: los empleados pueden ver el historial de órdenes que realizaron en el sistema.

## Validaciones:
	El sistema cuenta con las siguientes restricciones para los empleados:
	o	Solo se puede registrar una orden diaria.
	o	Solo se pueden registrar las órdenes hasta las 11:00 AM.
	o	Solo se puede editar la orden hasta a las 10:00 AM. (esto con el fin que el administrado tengan un tiempo necesario para considerar las modificaciones)

El sistema no tiene límite de creación de menús diarios, automáticamente agrupa todos los menús que contenga la fecha actual y los presenta como opciones a los empleados.


## Proceso de instalación

## INSTALACIÓN
Ejecuta el siguiente comando para instalar las dependencias y ejecución:

- Crear y activar entorno
``` shell virtualenv env --python=python3 
source env/bin/activate ```

NOTA: debes tener instalado *virtualenv* para poder crear el entorno virtual

* Instalar depdenceias

```shell
pip install -r requirements.txt
```

* Migraciones:

	```shell
	python manage.py makemigrations
	python manage.py migrate

	```

* Crear superusuario:

	```shell
	python manage.py createsuperuser
	```
NOTA: se debe crear un super usuario para poder crear un Menús y empleados

* Correr aplicación:
	```shell
	python manage.py runserver
	```
* Correr tarea celery:
	```shell
	celery -A cornershop worker -l info
	```

## IMPORTANTE

Debes tener instalado en tu sistema RabbitMQ y ejecutar:

* instalar RabbitMQ en ubuntu:
	```shell
	apt-get install -y erlang
    apt-get install rabbitmq-server
    systemctl enable rabbitmq-server
	```

* configuración settings:

  debes configurar el correo, para las notificaciones de menu:

    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'example@gmail.com'
    EMAIL_HOST_PASSWORD = 'herepass'
    EMAIL_PORT = 587


## TEST

Se realizaron test de validación de URL y de creación de objetos de los modelos de:
•	Menu
•	Order
Para ejecutar las pruebas, se debe ejecutar el siguiente comando:

	```shell
	python manage.py test
	```









