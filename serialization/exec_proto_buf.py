import random

# This was generated using
# protoc student.proto --python_out=.
from student_pb2 import Student


def getNewStudent(i, num_courses):
	new_student = Student()
	new_student.id = random.randint(0, i)
	new_student.first_name = str(random.randint(0, i))
	new_student.last_name = str(random.randint(0, i))
	new_student.comments = str(random.randint(0, i))
	for j in xrange(0, num_courses):
		new_course = new_student.courses.add()
		new_course.name = str(random.randint(0, i)) + str(random.randint(0, j))
		new_course.marks = 100 * random.randint(0, j) / num_courses
	return new_student


def serialize(student):
	return student.SerializeToString()


def deserialize(serialized_student):
	student = Student()
	student.ParseFromString(serialized_student)
	return student
