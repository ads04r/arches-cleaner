import random

def random_result(instance, *args, **kwargs):
	return random.randint(0, 1) == 1

def always_return_true(instance, *args, **kwargs):
	"""Always returns true, so should never fail."""
	return True
