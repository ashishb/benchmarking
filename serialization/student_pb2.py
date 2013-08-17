# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='student.proto',
  package='',
  serialized_pb='\n\rstudent.proto\"h\n\x07Student\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x12\n\nfirst_name\x18\x02 \x02(\t\x12\x11\n\tlast_name\x18\x03 \x02(\t\x12\x10\n\x08\x63omments\x18\x04 \x01(\t\x12\x18\n\x07\x63ourses\x18\x05 \x03(\x0b\x32\x07.Course\"%\n\x06\x43ourse\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05marks\x18\x02 \x01(\x05')




_STUDENT = descriptor.Descriptor(
  name='Student',
  full_name='Student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='Student.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='first_name', full_name='Student.first_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_name', full_name='Student.last_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='comments', full_name='Student.comments', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='courses', full_name='Student.courses', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=17,
  serialized_end=121,
)


_COURSE = descriptor.Descriptor(
  name='Course',
  full_name='Course',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='Course.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='marks', full_name='Course.marks', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=123,
  serialized_end=160,
)

_STUDENT.fields_by_name['courses'].message_type = _COURSE
DESCRIPTOR.message_types_by_name['Student'] = _STUDENT
DESCRIPTOR.message_types_by_name['Course'] = _COURSE

class Student(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STUDENT
  
  # @@protoc_insertion_point(class_scope:Student)

class Course(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COURSE
  
  # @@protoc_insertion_point(class_scope:Course)

# @@protoc_insertion_point(module_scope)
