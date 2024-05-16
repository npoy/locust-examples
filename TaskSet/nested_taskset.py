from locust import TaskSet, constant, task, HttpUser


class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get Status of 200")
        self.interrupt(reschedule=False) # Once a TaskSet is gotten, it's not going to another one so we need to interrupt it


class MyAnotherHTTPCat(TaskSet):

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Get Status of 500")
        self.interrupt(reschedule=False)

    # @task
    # class MyAnotherHTTPCat(TaskSet):
    #     @task
    #     def get_500_status(self):
    #         self.client.get("/500")
    #         print("Get Status of 500")
    #         self.interrupt(reschedule=False) # To wait instead of go right to the next task (if not, true by default)

class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPCat, MyAnotherHTTPCat]
    wait_time = constant(1)