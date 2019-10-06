'''
Brad Bosak
SWDV 660 Week 6 Assignment
10/5/2019
'''
import logging
import logstash
import sys
import time
import random

test_logger = logging.getLogger('python-application-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler('18.208.203.182',5959,version=1))

for x in range(50):
  if x % 4:
    print("info")
    test_logger.info('python-logstash: This is an info message.')
  elif x % 5:
    print("warning")
    test_logger.warning('python-logstash: This is an warning message.')
  else:
    print("error")
    test_logger.error('python-logstash: Uh oh, this is an error.')

extra = {
    'test_string': 'python-version: ' + repr(sys.version_info),
    'test_boolean': 'True',
    'test_integer': 123,
}

test_logger.info('python-logstash: test extra fields', extra=extra)