import random


def createStudents(num_students, num_courses, get_new_student_func, serialize_func):
	students = list()
	total_serialized_length = 0
	for i in xrange(0, num_students):
		new_student = get_new_student_func(i, num_courses)
		serialized_string = serialize_func(new_student)
		students.append(serialized_string)
		total_serialized_length += len(serialized_string)
	return students, total_serialized_length


def getStudents(students, deserialize_func):
	students_obj = list()
	count = 0
	for serialized_student in students:
		students_obj.append(deserialize_func(serialized_student))
		count += 1
	return students_obj
