# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map_parking_space.proto

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
    name='map_parking_space.proto',
    package='deeproute.hdmap',
    syntax='proto2',
    serialized_pb=_b('\n\x17map_parking_space.proto\x12\x0f\x64\x65\x65proute.hdmap\x1a\x0egeometry.proto\"m\n\x0cParkingSpace\x12\n\n\x02id\x18\x01 \x01(\x05\x12,\n\x07polygon\x18\x02 \x01(\x0b\x32\x1b.deeproute.geometry.Polygon\x12\x12\n\noverlap_id\x18\x03 \x03(\x05\x12\x0f\n\x07heading\x18\x04 \x01(\x01\"Z\n\nParkingLot\x12\n\n\x02id\x18\x01 \x01(\x05\x12,\n\x07polygon\x18\x02 \x01(\x0b\x32\x1b.deeproute.geometry.Polygon\x12\x12\n\noverlap_id\x18\x03 \x03(\x05'),
    dependencies=[geometry__pb2.DESCRIPTOR, ])


_PARKINGSPACE = _descriptor.Descriptor(
    name='ParkingSpace',
    full_name='deeproute.hdmap.ParkingSpace',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='deeproute.hdmap.ParkingSpace.id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='polygon', full_name='deeproute.hdmap.ParkingSpace.polygon', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='overlap_id', full_name='deeproute.hdmap.ParkingSpace.overlap_id', index=2,
            number=3, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='heading', full_name='deeproute.hdmap.ParkingSpace.heading', index=3,
            number=4, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
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
    serialized_start=60,
    serialized_end=169,
)


_PARKINGLOT = _descriptor.Descriptor(
    name='ParkingLot',
    full_name='deeproute.hdmap.ParkingLot',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='deeproute.hdmap.ParkingLot.id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='polygon', full_name='deeproute.hdmap.ParkingLot.polygon', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='overlap_id', full_name='deeproute.hdmap.ParkingLot.overlap_id', index=2,
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
    serialized_start=171,
    serialized_end=261,
)

_PARKINGSPACE.fields_by_name['polygon'].message_type = geometry__pb2._POLYGON
_PARKINGLOT.fields_by_name['polygon'].message_type = geometry__pb2._POLYGON
DESCRIPTOR.message_types_by_name['ParkingSpace'] = _PARKINGSPACE
DESCRIPTOR.message_types_by_name['ParkingLot'] = _PARKINGLOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParkingSpace = _reflection.GeneratedProtocolMessageType('ParkingSpace', (_message.Message,), dict(
    DESCRIPTOR=_PARKINGSPACE,
    __module__='map_parking_space_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.hdmap.ParkingSpace)
))
_sym_db.RegisterMessage(ParkingSpace)

ParkingLot = _reflection.GeneratedProtocolMessageType('ParkingLot', (_message.Message,), dict(
    DESCRIPTOR=_PARKINGLOT,
    __module__='map_parking_space_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.hdmap.ParkingLot)
))
_sym_db.RegisterMessage(ParkingLot)


# @@protoc_insertion_point(module_scope)
