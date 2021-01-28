import random
import functools


@functools.lru_cache(maxsize=None)
def knapsack(capacity, n):
	'''
	A Dynamic Programming based Python
	Program for 0-1 Knapsack problem
	Returns the maximum value that can
	be put in a knapsack of given capacity
	'''
	if not n or not capacity:
		return 0
	elif weights[n-1] > capacity:
		return knapsack(capacity, n - 1)
	else:
		case_no = knapsack(capacity, n - 1)
		case_yes = values[n-1] + knapsack(capacity - weights[n-1], n - 1)
		return max(case_no, case_yes)


def random_test(N, *, seed=None):
	random.seed(seed)
	weights, values = {}, {0}
	while len(weights) != len(values):
		weights = {random.randint(0, 100) for _ in range(N)}
		values = {random.randint(0, 1000) for _ in range(N)}

	return list(weights), list(values)


def main():
	global weights, values
	weights, values = random_test(20, seed=1)
	capacity = 200
	print(f'C: {capacity}')
	print(f'W: {weights}')
	print(f'V: {values}')
	print(f'MAX: {knapsack(capacity, len(values))}')


if __name__ == '__main__':
	main()