from locust import User, task, constant, between, constant_pacing
import time

class MyUser(User):
    wait_time = constant_pacing(3)

    @task
    def launch(self):
        time.sleep(5)
        print("This will inject 2 to 5 second delay")