"""A module used for saving log entries to send them later with a server response"""

import logging
import collections
from logging import LogRecord

class StackLogger(logging.Handler):
    def __init__(self, level = logging.NOTSET) -> None:
        super().__init__(level)
        self._log_queue=collections.deque()
    def emit(self, record: LogRecord) -> None:
        self._log_queue.append(self.format(record))
    def collect(self):
        return list(self._log_queue)
    def clear(self):
        return self._log_queue.clear()