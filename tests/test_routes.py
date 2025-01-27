import unittest

from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        """Set up the test client and environment before each test runs"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_get_routes(self):
        """Testing that routes return a 200 or 302 status code"""
        for rule in self.app.url_map.iter_rules():
            if "<" in rule.rule or ">" in rule.rule:
                continue

            allowed_methods = rule.methods
            if allowed_methods and "GET" in allowed_methods:
                response = self.client.get(rule.rule)
            else:
                continue

            response = self.client.get(rule.rule)
            self.assertIn(response.status_code, [200, 302])

    def test_post_routes(self):
        """Testing that post routes return a 200 or 302 status code"""
        for rule in self.app.url_map.iter_rules():
            if "<" in rule.rule or ">" in rule.rule:
                continue

            allowed_methods = rule.methods
            if allowed_methods and "POST" in allowed_methods:
                response = self.client.post(rule.rule, data = {})
            else:
                continue

            self.assertIn(response.status_code, [200, 302])

    def test_404_route(self):
        """Test that invalid routes return 404"""
        response = self.client.get('/nonexistent-route')
        self.assertEqual(response.status_code, 404)
        self.assertIn("Oops!", response.data.decode('utf-8'))
