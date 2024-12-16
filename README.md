# Load Testing Project with Locust and Docker Compose

## **Project Overview**
This project demonstrates load testing using **Locust** and **Docker Compose**. We use the public JSONPlaceholder API to perform CRUD operations (`GET`, `POST`, `PUT`, and `DELETE`) on the `/posts` endpoint. The test simulates real-world user behavior with Locust tasks.

---

## **Project Structure**
```
locust-load-testing-project/
├── docker-compose.yml
├── locust/
│   ├── Dockerfile
│   └── locustfile.py
├── images/
│   ├── locust_dashboard.png
│   └── test_summary.png
└── README.md
```

---

## **Technologies Used**
- **Locust:** For load testing.
- **JSONPlaceholder API:** A free testing API.
- **Docker & Docker Compose:** For container orchestration.

---

## **Features**
- Perform API testing with simulated traffic.
- CRUD operations on JSONPlaceholder API endpoints.
- Scalable with multiple workers using Docker Compose.
- HTML test reports for better test analysis.

---

## **How to Run the Project**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/REFATBHUYAN/locust-load-testing-project.git
   cd locust-load-testing-project
   ```

2. **Run the Project:**
   ```bash
   docker-compose up --build
   ```

3. **Access Locust Web UI:**
   Open `http://localhost:8089` in your browser.

4. **Start the Test:**
   - Set the target number of users and spawn rate.
   - Click **Start Swarming**.

5. **Monitor Test Results:**
   - View requests per second, response time, and failure rates.
   - Download detailed HTML reports.

---

## **CRUD Operations Tested**
1. **GET /posts:** Fetch all posts.
2. **POST /posts:** Create a new post.
3. **PUT /posts/1:** Update an existing post.
4. **DELETE /posts/1:** Delete an existing post.

---

## **Screenshots**

### **Locust Web UI Charts
![Locust Web UI](https://github.com/REFATBHUYAN/locust-load-testing-project/blob/main/images/locust_dashboard.png?raw=true)

### **Test Metrics Summary:**
![Test Summary](https://github.com/REFATBHUYAN/locust-load-testing-project/blob/main/images/test_summary.png?raw=true)

---

## **HTML Test Report**
Download the HTML report after running tests by clicking the **Download Report** button in Locust's web interface.

---

## **Why This Project?**
- **Recruiter Appeal:** Demonstrates real-world testing skills.
- **Performance Expertise:** Shows knowledge of load testing and performance monitoring.
- **Scalable Solution:** Uses modern tools like Docker Compose for scalable architecture.

---

## **Files Overview**

### **docker-compose.yml**
```yaml
version: '3.8'

services:
  locust-master:
    build: ./locust
    ports:
      - "8089:8089"
    environment:
      - LOCUST_MODE=master
    command: >
      locust -f locustfile.py --master --host=https://jsonplaceholder.typicode.com

  locust-worker:
    build: ./locust
    environment:
      - LOCUST_MODE=worker
    depends_on:
      - locust-master
    command: >
      locust -f locustfile.py --worker --master-host=locust-master
```

### **Dockerfile**
```dockerfile
FROM python:3.9-slim
WORKDIR /locust
COPY locustfile.py ./
RUN pip install locust requests
CMD ["locust"]
```

### **locustfile.py**
```python
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
```

---
