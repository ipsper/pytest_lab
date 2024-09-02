"""collection of locust api functions"""

import locust

class UsersTest(locust.TaskSet):
    """UsersTest class"""
    @locust.seq_task(1)
    def api_get_task(self):
        self.client.get("/api", name="GET /api")

    @locust.seq_task(2)
    def api_post_task(self):
        payload = {"username": "user1", "password": "123456"}
        self.client.post("/api", data=payload, name="POST /api")

class SituationTest(locust.HttpLocust):
    """SituationTest class"""
    task_set = UsersTest 
    min_wait = 1000 
    max_wait = 2000
    host = "http://127.0.0.1:3000"
