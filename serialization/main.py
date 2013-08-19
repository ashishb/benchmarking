import pickle
import random
import sys

import common
import exec_pickle
import exec_proto_buf
import exec_thrift


if __name__ == '__main__':
	num_students = 100 * 1000
	num_courses = 5
	assert len(sys.argv) >= 1, 'Please pass pickle, proto or thrift as second argument.'
	class_to_test = sys.argv[1]
	if class_to_test == 'proto':
		getNewStudent = exec_proto_buf.getNewStudent
		serialize = exec_proto_buf.serialize
		deserialize = exec_proto_buf.deserialize
	elif class_to_test == 'thrift':
		getNewStudent = exec_thrift.getNewStudent
		serialize = exec_thrift.serialize
		deserialize = exec_thrift.deserialize
	elif class_to_test == 'pickle':
		getNewStudent = exec_pickle.getNewStudent
		serialize = exec_pickle.serialize
		deserialize = exec_pickle.deserialize
	else:
		print 'ERROR'
		sys.exit(1)
	

	students, serialized_length = common.createStudents(num_students, num_courses, getNewStudent, serialize)
	common.getStudents(students, deserialize)
	print 'Created %d students, length %d KiB' % (len(students), serialized_length/1024)
