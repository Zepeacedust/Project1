import pytest

from Code.structured_logging.processors.timestamp_processor import TimestampProcessor
def test_handle():
    test_processor = TimestampProcessor()
    data = {"some_key": "some_data"}
    test_processor.handle(data)
    assert "timestamp" in data