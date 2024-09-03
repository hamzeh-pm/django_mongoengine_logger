import json
import logging

import pytest

from django_mongoengine_logger.documents import LogDocument
from django_mongoengine_logger.logging import MongoDBHandler


@pytest.fixture
def logger():
    logger = logging.getLogger("mongo_log")
    return logger


@pytest.mark.django_db
def test_log_message(logger):
    logger.info("Test log message")
    log_entry = LogDocument.objects.first()
    assert log_entry is not None
    assert log_entry.message == "Test log message"

    logger.info(json.dumps({"message": "test"}))
    log_entry = LogDocument.objects.order_by("-id").first()  # Get the last log entry
    assert log_entry.message["message"] == "test"
