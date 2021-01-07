from locust import between, HttpUser, task, TaskSet


class WebsiteTasks(TaskSet):

    @task
    def index(self):
        self.client.get("/uk")

    @task
    def about(self):
        self.client.get("/invest")


class WebsiteUser(HttpUser):
    tasks = [WebsiteTasks]
    wait_time = between(0.5, 15)
