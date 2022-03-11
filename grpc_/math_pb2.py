# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: math.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmath.proto\"\x1d\n\x0bSqrtRequest\x12\x0e\n\x06number\x18\x01 \x01(\x01\"\x1c\n\x0cSqrtResponse\x12\x0c\n\x04sqrt\x18\x01 \x01(\x01\"\x1c\n\nStdRequest\x12\x0e\n\x06number\x18\x01 \x01(\x01\"\x1a\n\x0bStdResponse\x12\x0b\n\x03std\x18\x01 \x01(\x01\"$\n\x12MultipliersRequest\x12\x0e\n\x06number\x18\x01 \x01(\x05\"%\n\x13MultipliersResponse\x12\x0e\n\x06number\x18\x01 \x01(\x05\"\x1c\n\nMaxRequest\x12\x0e\n\x06number\x18\x01 \x01(\x05\"\x1a\n\x0bMaxResponse\x12\x0b\n\x03max\x18\x01 \x01(\x05\x32\xc9\x01\n\x04Math\x12)\n\x08get_sqrt\x12\x0c.SqrtRequest\x1a\r.SqrtResponse\"\x00\x12(\n\x07get_std\x12\x0b.StdRequest\x1a\x0c.StdResponse\"\x00(\x01\x12@\n\x0fget_multipliers\x12\x13.MultipliersRequest\x1a\x14.MultipliersResponse\"\x00\x30\x01\x12*\n\x07get_max\x12\x0b.MaxRequest\x1a\x0c.MaxResponse\"\x00(\x01\x30\x01\x62\x06proto3')



_SQRTREQUEST = DESCRIPTOR.message_types_by_name['SqrtRequest']
_SQRTRESPONSE = DESCRIPTOR.message_types_by_name['SqrtResponse']
_STDREQUEST = DESCRIPTOR.message_types_by_name['StdRequest']
_STDRESPONSE = DESCRIPTOR.message_types_by_name['StdResponse']
_MULTIPLIERSREQUEST = DESCRIPTOR.message_types_by_name['MultipliersRequest']
_MULTIPLIERSRESPONSE = DESCRIPTOR.message_types_by_name['MultipliersResponse']
_MAXREQUEST = DESCRIPTOR.message_types_by_name['MaxRequest']
_MAXRESPONSE = DESCRIPTOR.message_types_by_name['MaxResponse']
SqrtRequest = _reflection.GeneratedProtocolMessageType('SqrtRequest', (_message.Message,), {
  'DESCRIPTOR' : _SQRTREQUEST,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:SqrtRequest)
  })
_sym_db.RegisterMessage(SqrtRequest)

SqrtResponse = _reflection.GeneratedProtocolMessageType('SqrtResponse', (_message.Message,), {
  'DESCRIPTOR' : _SQRTRESPONSE,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:SqrtResponse)
  })
_sym_db.RegisterMessage(SqrtResponse)

StdRequest = _reflection.GeneratedProtocolMessageType('StdRequest', (_message.Message,), {
  'DESCRIPTOR' : _STDREQUEST,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:StdRequest)
  })
_sym_db.RegisterMessage(StdRequest)

StdResponse = _reflection.GeneratedProtocolMessageType('StdResponse', (_message.Message,), {
  'DESCRIPTOR' : _STDRESPONSE,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:StdResponse)
  })
_sym_db.RegisterMessage(StdResponse)

MultipliersRequest = _reflection.GeneratedProtocolMessageType('MultipliersRequest', (_message.Message,), {
  'DESCRIPTOR' : _MULTIPLIERSREQUEST,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:MultipliersRequest)
  })
_sym_db.RegisterMessage(MultipliersRequest)

MultipliersResponse = _reflection.GeneratedProtocolMessageType('MultipliersResponse', (_message.Message,), {
  'DESCRIPTOR' : _MULTIPLIERSRESPONSE,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:MultipliersResponse)
  })
_sym_db.RegisterMessage(MultipliersResponse)

MaxRequest = _reflection.GeneratedProtocolMessageType('MaxRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAXREQUEST,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:MaxRequest)
  })
_sym_db.RegisterMessage(MaxRequest)

MaxResponse = _reflection.GeneratedProtocolMessageType('MaxResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAXRESPONSE,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:MaxResponse)
  })
_sym_db.RegisterMessage(MaxResponse)

_MATH = DESCRIPTOR.services_by_name['Math']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SQRTREQUEST._serialized_start=14
  _SQRTREQUEST._serialized_end=43
  _SQRTRESPONSE._serialized_start=45
  _SQRTRESPONSE._serialized_end=73
  _STDREQUEST._serialized_start=75
  _STDREQUEST._serialized_end=103
  _STDRESPONSE._serialized_start=105
  _STDRESPONSE._serialized_end=131
  _MULTIPLIERSREQUEST._serialized_start=133
  _MULTIPLIERSREQUEST._serialized_end=169
  _MULTIPLIERSRESPONSE._serialized_start=171
  _MULTIPLIERSRESPONSE._serialized_end=208
  _MAXREQUEST._serialized_start=210
  _MAXREQUEST._serialized_end=238
  _MAXRESPONSE._serialized_start=240
  _MAXRESPONSE._serialized_end=266
  _MATH._serialized_start=269
  _MATH._serialized_end=470
# @@protoc_insertion_point(module_scope)
