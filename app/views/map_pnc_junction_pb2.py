# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map_pnc_junction.proto

from google.protobuf import descriptor_pb2
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import reflection as _reflection
from google.protobuf import message as _message
from google.protobuf import descriptor as _descriptor
import sys
_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import geometry_pb2 as geometry__pb2  # NOQA: E402


DESCRIPTOR = _descriptor.FileDescriptor(
    name='map_pnc_junction.proto',
    package='deeproute.hdmap',
    syntax='proto2',
    serialized_pb=_b(
        '\n\x16map_pnc_junction.proto\x12\x0f\x64\x65\x65proute.hdmap\x1a\x0egeometry.proto\"[\n\x0bPNCJunction\x12\n\n\x02id\x18\x01 \x01(\x05\x12,\n\x07polygon\x18\x02 \x01(\x0b\x32\x1b.deeproute.geometry.Polygon\x12\x12\n\noverlap_id\x18\x03 \x03(\x05'),
    dependencies=[geometry__pb2.DESCRIPTOR, ])


_PNCJUNCTION = _descriptor.Descriptor(
    name='PNCJunction',
    full_name='deeproute.hdmap.PNCJunction',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='deeproute.hdmap.PNCJunction.id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='polygon', full_name='deeproute.hdmap.PNCJunction.polygon', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='overlap_id', full_name='deeproute.hdmap.PNCJunction.overlap_id', index=2,
            number=3, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=59,
    serialized_end=150,
)

_PNCJUNCTION.fields_by_name['polygon'].message_type = geometry__pb2._POLYGON
DESCRIPTOR.message_types_by_name['PNCJunction'] = _PNCJUNCTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PNCJunction = _reflection.GeneratedProtocolMessageType('PNCJunction', (_message.Message,), dict(
    DESCRIPTOR=_PNCJUNCTION,
    __module__='map_pnc_junction_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.hdmap.PNCJunction)
))
_sym_db.RegisterMessage(PNCJunction)


# @@protoc_insertion_point(module_scope)
