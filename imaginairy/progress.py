import logging

logger = logging.getLogger(__name__)


class ProgressReporter:
    def __init__(self, l, length):
        self.i = -1
        self.l = l
        self.max_length = length

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        if self.i < self.max_length - 1:
            self.i += 1
            try:
                logger.progress("{0}/{1}".format(self.i + 1, self.max_length))
            except AttributeError:
                logger.warning("Logger initialized incorrectly?")
            return self.l[self.i]
        else:
            raise StopIteration