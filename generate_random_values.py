#!/usr/bin/env python

# usage: ./generate_random_values.py [count] [value] [error%]
# for example, to get a set of 64 1-ohm +/-5% resistors, run this like so:
# ./generate_random_values.py 64 1 5%

import sys
import random
import pprint
import csv


def generate_random_values(count, value, fractional_percent):
	error_band = value * fractional_percent
	lower_bound = value - error_band
	upper_bound = value + error_band

	values = []
	for i in xrange(count):
		random_value = random.uniform(lower_bound, upper_bound)
		values.append(random_value)

	return values


def dump_values_to_csv_file(values):
	with open('random_values.csv','w') as csvfile:
		writer = csv.writer(csvfile)
		for value in values:
			writer.writerow([value])


if __name__ == "__main__":
	count = int(sys.argv[1])
	value = float(sys.argv[2])
	percent_error = float(sys.argv[3][:-1])
	fractional_percent = percent_error / 100.0

	values = generate_random_values(count, value, fractional_percent)
	pprint.pprint(values)
	dump_values_to_csv_file(values)
