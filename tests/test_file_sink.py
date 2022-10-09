import pytest

from unittest.mock import patch, mock_open, call

from Code.structured_logging.sinks.file_sink import FileSink


def test_write_stuff_to_file():
    open_mock = mock_open()
    with patch("builtins.open", open_mock, create=True):
        test_sink = FileSink("output.json")
        test_sink.sink_data({"some_key":"some_data"})

    calls = [call('{'),call('"some_key"'),call(': '), call('"some_data"'),call('}')]
    
    open_mock.assert_called_with("output.json", "a")
    open_mock.return_value.write.assert_has_calls(calls)