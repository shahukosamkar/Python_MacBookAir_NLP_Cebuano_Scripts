#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Glenn Abastillas
# December 14, 2015
# Distance.py

import math, numpy

class Distance(object):

	def euclidean(self, point1, point2):
		""" counts the euclidean distance between point1 and point2. Returns a scalar integer. 

			point1:	first point of data to compare against point2
			point2:	second point of data to compare against point1
		"""
		return math.sqrt(sum((b - a)**2 for a, b in zip(point1, point2)))

	def manhattan(self, point1, point2):
		""" counts the manhattan distance between point1 and point2. Returns a scalar integer. 

			point1:	first point of data to compare against point2
			point2:	second point of data to compare against point1
		"""
		return sum(abs(b - a) for a, b in zip(point1, point2))

	def chebyshev(self, point1, point2):
		""" counts the chebyshev distance between point1 and point2. Returns a scalar integer. 

			point1:	first point of data to compare against point2
			point2:	second point of data to compare against point1
		"""
		return max(abs(b - a) for a, b in zip(point1, point2))

	def hamming(self, point1, point2):
		""" counts the hamming distance between point1 and point2. Returns a scalar integer. 

			point1:	first point of data to compare against point2
			point2:	second point of data to compare against point1
		"""
		if len(point1) != len(point2):
			raise ValueError("Undefined for strings of unequal lengths.")
		return sum((bool(ord(b)-ord(a)) for a, b in zip(point1, point2)))

	def levenshtein(self, point1, point2):
		""" counts the levenshtein distance between point1 and point2. Returns a scalar integer. 

			point1:	first point of data to compare against point2
			point2:	second point of data to compare against point1
		"""
		points = sorted((point1, point2), key = len)

		point1Length = len(points[0])
		point2Length = len(points[1])

		# If the first data vector is empty, maximum errors is equal to the length of the second vector.
		if point2Length == 0: 
			return point2Length

		if point2Length == point2Length: 
			# Initialize this vector to be used for the following inner loop.
			previous_row = range(point2Length) + [0]
		else:
			previous_row = range(point2Length)

		# Loop through the first data vector, which should be the longer one.
		for i, c1 in enumerate(points[1]):

			# Initialize this vector have i+1 as the first integer
			current_row = [i+1]

			# Loop through the second data vector, which should be the shorter one.
			for j, c2 in enumerate(points[0]):
				#print j, j+1, previous_row

				deletion = previous_row[j+1] + 1
				insertion = current_row[j] + 1
				substitution = previous_row[j] + (c1 != c2)
				current_row.append(min(deletion, insertion, substitution))

			#print current_row, previous_row
			previous_row = current_row

		return previous_row[-1]

	def cosine(self, point1, point2):
		return numpy.dot(point1, point2)/(numpy.sqrt(numpy.dot(point1, point1)) * numpy.sqrt(numpy.dot(point2, point2)))

if __name__ == "__main__":
	d = Distance()

	f1 = [1, 9, 10, 100, 77, 1]
	f2 = [2, 8, 13, 105, 70, 1]
	f3 = [3, 7, 16, 110, 63, 1]
	f4 = [4, 6, 19, 115, 56, 1]
	f5 = [5, 5, 22, 120, 49, 1]
	f6 = [6, 4, 25, 125, 42, 0]
	f7 = [7, 3, 28, 130, 35, 0]
	f8 = [8, 2, 31, 135, 28, 0]
	f9 = [9, 1, 34, 140, 21, 0]

	fa = [57, 56, 54, 56, 55, 48, 51, 56, 56, 53]
	fb = [36, 106, 121, 111, 116, 105, 49, 57, 57, 48]

	f0 = [f1,f2,f3,f4,f5,f6,f7,f8,f9]
	fn = list()

	fu = [8,3,31,120,49]

	a = d.euclidean(f1, f2)
	b = d.manhattan(f1, f2)
	c = d.chebyshev(f1, f2)
	f = d.hamming("f1", "f2")
	#e = d.levenshtein(f1, f2)

	print "{0}:\t{1}".format("euclidean", a)
	print "{0}:\t{1}".format("manhattan", b)
	print "{0}:\t{1}".format("chebyshev", c)
	print "{0}:\t{1}".format("hamming", f)
	#print "{0}:\t{1}".format("levenshtein", e)


	print "levenshtein distance", d.levenshtein("water", "aterw")
	print "hamming distance", d.hamming("blogs", "logsb")
	#print "LEVENT", d.levenshtein(fb, fa)

	print "cosine", d.cosine([1,2,1,3], [1,2,2,2])

	"""
	for f in f0:
		a = d.euclidean(fu, f[:-1])
		b = d.manhattan(fu, f[:-1])
		c = d.chebyshev(fu, f[:-1])

		print round(a, 2), b, c
		fn.append(c)

	print "class", f0[fn.index(min(fn))][-1]

	print "hamming", d.hamming("ddzz", "best")

	#print a
	#print b
	#print c

	for f in f0:
		print
		for ff in f0:
				a = d.euclidean(f, ff)
				b = d.manhattan(f, ff)
				c = d.chebyshev(f, ff)

				#print f[-1]
				#print "euclidean distance: {0}".format(a)
				#print "manhattan distance: {0}".format(b)
				#print "chebyshev distance: {0}\n".format(c)
				fn.append(min([a,b,c]))

		print f0[fn.index(min(fn))], fn
		fn = list()
	"""