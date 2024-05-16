import csv
import random
from locust import task, HttpUser

# Función para leer datos de usuario del archivo CSV
def leer_datos_usuario(archivo_csv):
    with open(archivo_csv, 'r') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            yield fila

# Clase de usuario de Locust
class UsuarioLocust(HttpUser):
    # Leer datos de usuario desde el archivo CSV
    datos_usuario = list(leer_datos_usuario('TestCw\\user-data-demo2.csv'))

    # Tarea para realizar login
    @task
    def login(self):
        # Obtener datos de usuario aleatorio
        usuario = random.choice(self.datos_usuario)

        # Enviar solicitud POST para login
        print("self.client:", self.client)
        response = self.client.post(
            url='https://int-achieve-iam.mldev.cloud/login?retURL=https://int-achieve-courseware-frontend.mldev.cloud/courses',
            data={
                'email': usuario['email'],
                'password': 'Passw0rd!'
            }
        )

        # Validar respuesta de login
        if response.status_code != 200:
            self.error(f"Error al iniciar sesión: {response.status_code}")

    # Tarea para ingresar a un curso
    @task
    def ingresar_curso(self):
        # Obtener datos de usuario y curso aleatorios
        usuario = random.choice(self.datos_usuario)
        course_id = usuario['short']

        # Construir URL del curso
        curso_url = f"https://int-achieve-courseware.mldev.cloud/api/v1/courseid/{course_id}"

        # Enviar solicitud GET para ingresar al curso
        response = self.client.get(url=curso_url)

        # Validar respuesta de ingreso a curso
        if response.status_code != 200:
            self.error(f"Error al ingresar al curso {course_id}: {response.status_code}")

# Ejecutar la prueba de carga
if __name__ == "__main__":
    user_load = HttpUser.load_test(
        user_class=UsuarioLocust,
        target_user_count=10  # Ajustar la cantidad de usuarios simulados
    )

    user_load.run()