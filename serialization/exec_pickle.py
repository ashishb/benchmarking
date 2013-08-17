import pickle
import random


def getNewStudent(i, num_courses):
	new_student = dict()
	new_student['id'] = random.randint(0, i)
	new_student['first_name'] = str(random.randint(0, i))
	new_student['last_name'] = str(random.randint(0, i))
	new_student['comments'] = str(random.randint(0, i))
	new_student['courses'] = list()
	for j in xrange(0, num_courses):
		new_course = dict()
		new_course['name'] = str(random.randint(0, i)) + str(random.randint(0, j))
		new_course['marks'] = 100 * random.randint(0, j) / num_courses
		new_student['courses'].append(new_course)
	return new_student

def serialize(student):
	return pickle.dumps(student)


def deserialize(serialized_student):
	return pickle.dumps(serialized_student)
