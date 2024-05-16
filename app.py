# from locust import User, constant, task

# class MyFirstTest(User):
#     weight = 2
#     wait_time = constant(1)
    
#     @task
#     def launch(self):
#         print("Launching the URL")

#     @task
#     def search(self):
#         print("Searching")


# class MySecondTest(User):
#     weight = 2
#     wait_time = constant(1)

#     @task
#     def launch2(self):
#         print("Second Test")

#     @task
#     def search2(self):
#         print("Second Search Test")


from locust import HttpUser, task, constant

class HelloWorld(HttpUser):
    wait_time = constant(1)
    host = "https://petstore.octoperf.com"

    @task
    def test(self):
        self.client.get("/")

