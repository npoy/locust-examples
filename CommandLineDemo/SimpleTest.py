from locust import HttpUser, TaskSet, task, constant

# class MyLoadTest(HttpUser):
#     wait_time = constant(1)

#     @task
#     def launch(self):
#         self.client.get("/")

# # Command: locust -f CommandLineDemo/SimpleTest.py -u 1 -r 1 -t 10s --headless --print-stats --csv Run1.csv --csv-full-history --host="https://example.com"

class FirefoxBrowserTest(TaskSet):
    @task
    def launch(self):
        print("Firefox Browser Tests")
        self.client.get("/", name=self.__class__.__name__)
        self.interrupt(reschedule=False)

class ChromeBrowserTest(TaskSet):
    @task
    def launch(self):
        print("Chrome Browser Tests")
        self.client.get("/", name=self.__class__.__name__)
        self.interrupt(reschedule=False)

class EdgeBrowserTest(TaskSet):
    @task
    def launch(self):
        print("Edge Browser Tests")
        self.client.get("/", name=self.__class__.__name__)
        self.interrupt(reschedule=False)

class MyLoadTest(HttpUser):
    wait_time = constant(1)
    tasks = [ChromeBrowserTest, FirefoxBrowserTest, EdgeBrowserTest]

# Command: locust -f CommandLineDemo/SimpleTest.py -u 1 -r 1 -t 10s --headless --print-stats --host="https://example.com" -L DEBUG --logfile mylog.log --html Run1