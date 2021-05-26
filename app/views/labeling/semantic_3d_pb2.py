# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: semantic_3d.proto

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
    name='semantic_3d.proto',
    package='',
    syntax='proto2',
    serialized_pb=_b('\n\x11semantic_3d.proto\x1a\x0c\x63ommon.proto\"\xb7\x04\n\nSemantic3D\x12\n\n\x02id\x18\x01 \x01(\x05\x12.\n\x0fsemantic_status\x18\x02 \x01(\x0e\x32\x0c.LabelStatus:\x07UNLABEL\x12.\n\x0finstance_status\x18\x03 \x01(\x0e\x32\x0c.LabelStatus:\x07UNLABEL\x12\x33\n\rsemantic_type\x18\x04 \x03(\x0e\x32\x18.Semantic3D.SemanticTypeB\x02\x10\x01\x12\x17\n\x0binstance_id\x18\x05 \x03(\x05\x42\x02\x10\x01\x12\x15\n\tis_moving\x18\x06 \x03(\x08\x42\x02\x10\x01\"\xd7\x02\n\x0cSemanticType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07OUTLIER\x10\x01\x12\r\n\tSMALL_MOT\x10\x02\x12\x0b\n\x07\x42IG_MOT\x10\x03\x12\x0e\n\nPEDESTRIAN\x10\x04\x12\n\n\x06NONMOT\x10\x05\x12\n\n\x06GROUND\x10\x06\x12\x0b\n\x07UNLABEL\x10\x07\x12\r\n\tOTHER_MOT\x10\x08\x12\x0b\n\x07PARKING\x10\t\x12\r\n\tSIDE_WALK\x10\n\x12\x10\n\x0cOTHER_GROUND\x10\x0b\x12\x0c\n\x08\x42UILDING\x10\x0c\x12\t\n\x05\x46\x45NCE\x10\r\x12\x08\n\x04\x43ONE\x10\x0e\x12\x13\n\x0fOTHER_STRUCTURE\x10\x0f\x12\x10\n\x0cLANE_MARKING\x10\x10\x12\x0e\n\nVEGETATION\x10\x11\x12\x0b\n\x07TERRAIN\x10\x12\x12\x08\n\x04POLE\x10\x13\x12\x10\n\x0cTRAFFIC_SIGN\x10\x14\x12\n\n\x06\x41NIMAL\x10\x15\x12\x10\n\x0cOTHER_OBJECT\x10\x16'),
    dependencies=[common__pb2.DESCRIPTOR, ])


_SEMANTIC3D_SEMANTICTYPE = _descriptor.EnumDescriptor(
    name='SemanticType',
    full_name='Semantic3D.SemanticType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='OUTLIER', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='SMALL_MOT', index=2, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BIG_MOT', index=3, number=3,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PEDESTRIAN', index=4, number=4,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='NONMOT', index=5, number=5,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='GROUND', index=6, number=6,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='UNLABEL', index=7, number=7,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='OTHER_MOT', index=8, number=8,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PARKING', index=9, number=9,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='SIDE_WALK', index=10, number=10,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='OTHER_GROUND', index=11, number=11,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BUILDING', index=12, number=12,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='FENCE', index=13, number=13,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CONE', index=14, number=14,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='OTHER_STRUCTURE', index=15, number=15,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='LANE_MARKING', index=16, number=16,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='VEGETATION', index=17, number=17,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='TERRAIN', index=18, number=18,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='POLE', index=19, number=19,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='TRAFFIC_SIGN', index=20, number=20,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ANIMAL', index=21, number=21,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='OTHER_OBJECT', index=22, number=22,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=260,
    serialized_end=603,
)
_sym_db.RegisterEnumDescriptor(_SEMANTIC3D_SEMANTICTYPE)


_SEMANTIC3D = _descriptor.Descriptor(
    name='Semantic3D',
    full_name='Semantic3D',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='Semantic3D.id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='semantic_status', full_name='Semantic3D.semantic_status', index=1,
            number=2, type=14, cpp_type=8, label=1,
            has_default_value=True, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='instance_status', full_name='Semantic3D.instance_status', index=2,
            number=3, type=14, cpp_type=8, label=1,
            has_default_value=True, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='semantic_type', full_name='Semantic3D.semantic_type', index=3,
            number=4, type=14, cpp_type=8, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='instance_id', full_name='Semantic3D.instance_id', index=4,
            number=5, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='is_moving', full_name='Semantic3D.is_moving', index=5,
            number=6, type=8, cpp_type=7, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _SEMANTIC3D_SEMANTICTYPE,
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=36,
    serialized_end=603,
)

_SEMANTIC3D.fields_by_name['semantic_status'].enum_type = common__pb2._LABELSTATUS
_SEMANTIC3D.fields_by_name['instance_status'].enum_type = common__pb2._LABELSTATUS
_SEMANTIC3D.fields_by_name['semantic_type'].enum_type = _SEMANTIC3D_SEMANTICTYPE
_SEMANTIC3D_SEMANTICTYPE.containing_type = _SEMANTIC3D
DESCRIPTOR.message_types_by_name['Semantic3D'] = _SEMANTIC3D
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Semantic3D = _reflection.GeneratedProtocolMessageType('Semantic3D', (_message.Message,), dict(
    DESCRIPTOR=_SEMANTIC3D,
    __module__='semantic_3d_pb2'
    # @@protoc_insertion_point(class_scope:Semantic3D)
))
_sym_db.RegisterMessage(Semantic3D)


_SEMANTIC3D.fields_by_name['semantic_type'].has_options = True
_SEMANTIC3D.fields_by_name['semantic_type']._options = _descriptor._ParseOptions(
    descriptor_pb2.FieldOptions(), _b('\020\001'))
_SEMANTIC3D.fields_by_name['instance_id'].has_options = True
_SEMANTIC3D.fields_by_name['instance_id']._options = _descriptor._ParseOptions(
    descriptor_pb2.FieldOptions(), _b('\020\001'))
_SEMANTIC3D.fields_by_name['is_moving'].has_options = True
_SEMANTIC3D.fields_by_name['is_moving']._options = _descriptor._ParseOptions(
    descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
