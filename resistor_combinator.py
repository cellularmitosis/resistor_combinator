#!/usr/bin/env python

# usage: ./resistor_combinator.py [size] [desired_value] [csvfile]
# where size is the "edge" size.  i.e., for a 4x4 resistor block, size=4.
# for example, ./resistor_combinator.py 4 1.0 foo.csv


import itertools
import sys
import csv
import pprint
import math
import copy


def parse_csv_file(filename):
	values = []
	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			value = float(row[0])
			values.append(value)
	return set(values)


def inverse(value):
	return 1.0 / value


def parallel_resistors_value(resistors):
	return inverse(sum(map(inverse, resistors)))


def parallel_resistor_columns_value(columns):
	column_values = map(sum, columns)
	return parallel_resistors_value(column_values)


def iterate_towards_best_value(values, edge_size, desired_value):
	columns = []
	level = 0
	best_value = 0.0
	return recursive_iterate_towards_best_value(columns, values, edge_size, desired_value, best_value, level)


def recursive_iterate_towards_best_value(columns, remaining_values, edge_size, desired_value, best_value, level):
	if (level == edge_size):
		combined_value = parallel_resistor_columns_value(columns)

		error = math.fabs(desired_value - combined_value)
		best_error = math.fabs(desired_value - best_value)

		# for absolute closest value:
		# if (error < best_error):
		# 	best_value = combined_value
		# 	print best_value

		# for closest value without going over:
		if (error < best_error and combined_value < desired_value):
			best_value = combined_value
			print best_value

	else:
		for next_column in itertools.combinations(remaining_values, edge_size):
			next_column = set(next_column)
			next_column_value = sum(next_column)

			next_columns = copy.copy(columns)
			next_columns.append(next_column)

			next_remaining_values = remaining_values - next_column

			best_value = recursive_iterate_towards_best_value(next_columns, next_remaining_values, edge_size, desired_value, best_value, level+1)

	return best_value


if __name__ == "__main__":
	edge_size = int(sys.argv[1])
	desired_value = float(sys.argv[2])
	csv_filename = sys.argv[3]
	values = parse_csv_file(csv_filename)

	# print_all_combinations_for_column_one(values, edge_size)

	# print "calculating 2x2:"
	# best = best_value_two_by_two(values)
	# print "best 2x2:", best

	# print "calculating 3x3:"
	# best = best_value_three_by_three(values)
	# print "best 3x3:", best

	best = iterate_towards_best_value(values, edge_size, desired_value)
	print "best value:", best




# ---------- old code

# def print_all_combinations_for_column_one(values, edge_size):
# 	combos = []
# 	count = 0
# 	for combo in itertools.combinations(values, edge_size):
# #		pprint.pprint(combo)
# #		combos.append(combo)
# 		count += 1
# 	print "%d combinations" % count


# def best_value_three_by_three(values):
# 	best_value = 0.0

# 	edge_size = 3
# 	for column_one in itertools.combinations(values, edge_size):
# 		column_one_set = set(column_one)
# 		column_one_value = sum(column_one_set)

# 		remaining_values_1 = values - column_one_set
# 		for column_two in itertools.combinations(remaining_values_1, edge_size):
# 			column_two_set = set(column_two)
# 			column_two_value = sum(column_two_set)

# 			remaining_values_2 = remaining_values_1 - column_two_set
# 			for column_three in itertools.combinations(remaining_values_2, edge_size):
# 				column_three_set = set(column_three)
# 				column_three_value = sum(column_three_set)

# 				combined_value = 1.0 / ((1.0 / column_one_value) + (1.0 / column_two_value) + (1.0 / column_three_value))

# 				error = math.fabs(desired_value - combined_value)
# 				best_error = math.fabs(desired_value - best_value)
# 				if (error < best_error):
# 					best_value = combined_value
# 					print best_value
# 	return best_value


# def best_value_two_by_two(values):
# 	best_value = 0.0

# 	edge_size = 2
# 	for column_one in itertools.combinations(values, edge_size):
# 		column_one_set = set(column_one)
# 		column_one_value = sum(column_one_set)

# 		remaining_values_1 = values - column_one_set
# 		for column_two in itertools.combinations(remaining_values_1, edge_size):
# 			column_two_set = set(column_two)
# 			column_two_value = sum(column_two_set)

# 			combined_value = 1.0 / ((1.0 / column_one_value) + (1.0 / column_two_value))

# 			error = math.fabs(desired_value - combined_value)
# 			best_error = math.fabs(desired_value - best_value)
# 			if (error < best_error):
# 				best_value = combined_value
# 				print best_value
# 	return best_value

