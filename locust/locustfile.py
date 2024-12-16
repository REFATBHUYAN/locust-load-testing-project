from locust import HttpUser, task, between

class JsonPlaceholderUser(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def get_posts(self):
        self.client.get("/posts")

    @task(2)
    def create_post(self):
        self.client.post("/posts", json={"title": "Test Post", "body": "This is a test post.", "userId": 1})

    @task(3)
    def update_post(self):
        self.client.put("/posts/1", json={"title": "Updated Post", "body": "Updated content.", "userId": 1})

    @task(4)
    def delete_post(self):
        self.client.delete("/posts/1")