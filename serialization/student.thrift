struct Course {
	1: required string name;
	2: optional i32 marks;
}

struct Student {
	1: required i32 id;
	2: required string first_name;
	3: required string last_name;
	4: optional string comments;
	5: list<Course> courses;
}

