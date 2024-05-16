from locust import HttpUser, task, constant

# Clase de usuario de Locust
class UsuarioLocust(HttpUser):
    host = "https://petstore.octoperf.com"

    # Tarea para realizar login
    @task
    def login(self):
        self.client.get("/")