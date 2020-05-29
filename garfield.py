import os
import sys
from datetime import datetime
import random

list_of_errors = [
	KeyError,
	NameError,
	MemoryError,
	NotImplementedError,
]

def get_current_day() -> datetime:
	"""
	This is what my class does

	:return: Integer day of week, 0 is Monday, 6 is Sunday.
	"""
	return datetime.now().weekday()


def monday_error():
	day = get_current_day()

	if day == 0:
		# Get a list of different error types
		# Randomly pick one
		rand_err = random.sample(list_of_errors, n=1)
		raise rand_err

	else:
		print("No Error")
		pass

monday_error()

if __name__ == '__main__':

	monday_error()
