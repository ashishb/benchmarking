import os
import random
import sys

sys.path.append(os.path.join(os.getcwd(), 'gen-py'))
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport

# Generated using 
# thrift -o . --gen py:new_style student.thrift 
from student.ttypes import Course
from student.ttypes import Student

# Based on http://wiki.apache.org/thrift/ThriftUsagePython

def getNewStudent(i, num_courses):
	new_student = Student()
	new_student.id = random.randint(0, i)
	new_student.first_name = str(random.randint(0, i))
	new_student.last_name = str(random.randint(0, i))
	new_student.comments = str(random.randint(0, i))
	new_student.courses = list()
	for j in xrange(0, num_courses):
		new_course = Course()
		new_course.name = str(random.randint(0, i)) + str(random.randint(0, j))
		new_course.marks = 100 * random.randint(0, j) / num_courses
		new_student.courses.append(Course)
	return new_student


def serialize(student):
	transport_out = TTransport.TMemoryBuffer()
	protocol_out = TBinaryProtocol.TBinaryProtocol(transport_out)
	student.write(protocol_out)
	bytes = transport_out.getvalue()
	return bytes


def deserialize(serialized_student):
	transport_in = TTransport.TMemoryBuffer(serialized_student)
	protocol_in = TBinaryProtocol.TBinaryProtocol(transport_in)
	student = Student()
	student.read(protocol_in)
	return student
