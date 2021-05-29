# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: semantic_2d.proto


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
import labeling.common_pb2 as common__pb2  # NOQA: E402

DESCRIPTOR = _descriptor.FileDescriptor(
    name='semantic_2d.proto',
    package='',
    syntax='proto2',
    serialized_pb=_b('\n\x11semantic_2d.proto\x1a\x0c\x63ommon.proto\"g\n\x04Lane\x12\x0f\n\x07lane_id\x18\x01 \x01(\x05\x12\x1c\n\x04type\x18\x02 \x01(\x0e\x32\x0e.Lane.LaneType\x12\x19\n\x04line\x18\x03 \x01(\x0b\x32\x0b.Polyline3d\"\x15\n\x08LaneType\x12\t\n\x05SOLID\x10\x00\"N\n\nSemantic2D\x12*\n\x0blane_status\x18\x01 \x01(\x0e\x32\x0c.LabelStatus:\x07UNLABEL\x12\x14\n\x05lanes\x18\x02 \x03(\x0b\x32\x05.Lane'),
    dependencies=[common__pb2.DESCRIPTOR, ])


_LANE_LANETYPE = _descriptor.EnumDescriptor(
    name='LaneType',
    full_name='Lane.LaneType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='SOLID', index=0, number=0,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=117,
    serialized_end=138,
)
_sym_db.RegisterEnumDescriptor(_LANE_LANETYPE)


_LANE = _descriptor.Descriptor(
    name='Lane',
    full_name='Lane',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='lane_id', full_name='Lane.lane_id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='type', full_name='Lane.type', index=1,
            number=2, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='line', full_name='Lane.line', index=2,
            number=3, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _LANE_LANETYPE,
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=35,
    serialized_end=138,
)


_SEMANTIC2D = _descriptor.Descriptor(
    name='Semantic2D',
    full_name='Semantic2D',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='lane_status', full_name='Semantic2D.lane_status', index=0,
            number=1, type=14, cpp_type=8, label=1,
            has_default_value=True, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='lanes', full_name='Semantic2D.lanes', index=1,
            number=2, type=11, cpp_type=10, label=3,
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
    serialized_start=140,
    serialized_end=218,
)

_LANE.fields_by_name['type'].enum_type = _LANE_LANETYPE
_LANE.fields_by_name['line'].message_type = common__pb2._POLYLINE3D
_LANE_LANETYPE.containing_type = _LANE
_SEMANTIC2D.fields_by_name['lane_status'].enum_type = common__pb2._LABELSTATUS
_SEMANTIC2D.fields_by_name['lanes'].message_type = _LANE
DESCRIPTOR.message_types_by_name['Lane'] = _LANE
DESCRIPTOR.message_types_by_name['Semantic2D'] = _SEMANTIC2D
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Lane = _reflection.GeneratedProtocolMessageType('Lane', (_message.Message,), dict(
    DESCRIPTOR=_LANE,
    __module__='semantic_2d_pb2'
    # @@protoc_insertion_point(class_scope:Lane)
))
_sym_db.RegisterMessage(Lane)

Semantic2D = _reflection.GeneratedProtocolMessageType('Semantic2D', (_message.Message,), dict(
    DESCRIPTOR=_SEMANTIC2D,
    __module__='semantic_2d_pb2'
    # @@protoc_insertion_point(class_scope:Semantic2D)
))
_sym_db.RegisterMessage(Semantic2D)


# @@protoc_insertion_point(module_scope)