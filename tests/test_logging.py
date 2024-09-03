import logging

from django.test import TestCase

from django_mongoengine_logger.documents import LogDocument
from django_mongoengine_logger.logging import MongoDBHandler


class MongoDBHandlerTest(TestCase):
    def setUp(self):
        self.handler = MongoDBHandler(
            log_document_path="django_mongo_logger.documents.LogDocument"
        )
        self.logger = logging.getLogger("test_logger")
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.DEBUG)

    def test_log_message(self):
        self.logger.info("Test log message")
        log_entry = LogDocument.objects.first()
        self.assertIsNotNone(log_entry)
        self.assertEqual(log_entry.message, "Test log message")
