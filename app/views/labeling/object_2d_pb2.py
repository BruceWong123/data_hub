# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_2d.proto


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
    name='object_2d.proto',
    package='',
    syntax='proto2',
    serialized_pb=_b('\n\x0fobject_2d.proto\x1a\x0c\x63ommon.proto\"l\n\x0bTrafficSign\x12$\n\tsign_type\x18\x01 \x01(\x0e\x32\x11.TrafficSign.Type\"7\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bSPEED_LIMIT\x10\x01\x12\x11\n\rPARKING_ALLOW\x10\x02\"\xce\x01\n\x0cTrafficLight\x12\"\n\x05\x63olor\x18\x01 \x01(\x0e\x32\x13.TrafficLight.Color\x12\"\n\x05shape\x18\x02 \x01(\x0e\x32\x13.TrafficLight.Shape\"C\n\x05\x43olor\x12\x11\n\rUNKNOWN_COLOR\x10\x00\x12\x07\n\x03RED\x10\x01\x12\t\n\x05GREEN\x10\x02\x12\n\n\x06YELLOW\x10\x03\x12\x07\n\x03OFF\x10\x04\"1\n\x05Shape\x12\x11\n\rUNKNOWN_SHAPE\x10\x00\x12\t\n\x05\x41RROW\x10\x01\x12\n\n\x06\x43IRCLE\x10\x02\"\xc2\x04\n\x08Object2D\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04xmin\x18\x02 \x01(\x01\x12\x0c\n\x04ymin\x18\x03 \x01(\x01\x12\x0c\n\x04xmax\x18\x04 \x01(\x01\x12\x0c\n\x04ymax\x18\x05 \x01(\x01\x12\x11\n\tcamera_id\x18\x06 \x01(\t\x12\x12\n\nis_daytime\x18\x07 \x01(\x08\x12\'\n\nbasic_type\x18\x08 \x01(\x0e\x32\x13.Object2D.BasicType\x12\x17\n\x08occluded\x18\t \x01(\x08:\x05\x66\x61lse\x12\x18\n\ttruncated\x18\n \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x10is_traffic_light\x18\x0b \x01(\x08:\x05\x66\x61lse\x12-\n\x16traffic_light_property\x18\x0c \x01(\x0b\x32\r.TrafficLight\x12\x1e\n\x0fis_traffic_sign\x18\r \x01(\x08:\x05\x66\x61lse\x12+\n\x15traffic_sign_property\x18\x0e \x01(\x0b\x32\x0c.TrafficSign\x12\x32\n\x13segmentation_status\x18\x0f \x01(\x0e\x32\x0c.LabelStatus:\x07UNLABEL\x12 \n\x0csegmentation\x18\x10 \x01(\x0b\x32\n.Polygon2d\"|\n\tBasicType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nPEDESTRIAN\x10\x01\x12\x0b\n\x07\x42ICYCLE\x10\x02\x12\x0b\n\x07VEHICLE\x10\x03\x12\t\n\x05TRUCK\x10\x04\x12\x08\n\x04\x43ONE\x10\x05\x12\x11\n\rTRAFFIC_LIGHT\x10\x06\x12\x10\n\x0cTRAFFIC_SIGN\x10\x07'),
    dependencies=[common__pb2.DESCRIPTOR, ])


_TRAFFICSIGN_TYPE = _descriptor.EnumDescriptor(
    name='Type',
    full_name='TrafficSign.Type',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='SPEED_LIMIT', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PARKING_ALLOW', index=2, number=2,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=86,
    serialized_end=141,
)
_sym_db.RegisterEnumDescriptor(_TRAFFICSIGN_TYPE)

_TRAFFICLIGHT_COLOR = _descriptor.EnumDescriptor(
    name='Color',
    full_name='TrafficLight.Color',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN_COLOR', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='RED', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='GREEN', index=2, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='YELLOW', index=3, number=3,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='OFF', index=4, number=4,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=232,
    serialized_end=299,
)
_sym_db.RegisterEnumDescriptor(_TRAFFICLIGHT_COLOR)

_TRAFFICLIGHT_SHAPE = _descriptor.EnumDescriptor(
    name='Shape',
    full_name='TrafficLight.Shape',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN_SHAPE', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ARROW', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CIRCLE', index=2, number=2,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=301,
    serialized_end=350,
)
_sym_db.RegisterEnumDescriptor(_TRAFFICLIGHT_SHAPE)

_OBJECT2D_BASICTYPE = _descriptor.EnumDescriptor(
    name='BasicType',
    full_name='Object2D.BasicType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PEDESTRIAN', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BICYCLE', index=2, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='VEHICLE', index=3, number=3,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='TRUCK', index=4, number=4,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CONE', index=5, number=5,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='TRAFFIC_LIGHT', index=6, number=6,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='TRAFFIC_SIGN', index=7, number=7,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=807,
    serialized_end=931,
)
_sym_db.RegisterEnumDescriptor(_OBJECT2D_BASICTYPE)


_TRAFFICSIGN = _descriptor.Descriptor(
    name='TrafficSign',
    full_name='TrafficSign',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='sign_type', full_name='TrafficSign.sign_type', index=0,
            number=1, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _TRAFFICSIGN_TYPE,
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=33,
    serialized_end=141,
)


_TRAFFICLIGHT = _descriptor.Descriptor(
    name='TrafficLight',
    full_name='TrafficLight',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='color', full_name='TrafficLight.color', index=0,
            number=1, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='shape', full_name='TrafficLight.shape', index=1,
            number=2, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _TRAFFICLIGHT_COLOR,
        _TRAFFICLIGHT_SHAPE,
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=144,
    serialized_end=350,
)


_OBJECT2D = _descriptor.Descriptor(
    name='Object2D',
    full_name='Object2D',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='Object2D.id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='xmin', full_name='Object2D.xmin', index=1,
            number=2, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='ymin', full_name='Object2D.ymin', index=2,
            number=3, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='xmax', full_name='Object2D.xmax', index=3,
            number=4, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='ymax', full_name='Object2D.ymax', index=4,
            number=5, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='camera_id', full_name='Object2D.camera_id', index=5,
            number=6, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='is_daytime', full_name='Object2D.is_daytime', index=6,
            number=7, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='basic_type', full_name='Object2D.basic_type', index=7,
            number=8, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='occluded', full_name='Object2D.occluded', index=8,
            number=9, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='truncated', full_name='Object2D.truncated', index=9,
            number=10, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='is_traffic_light', full_name='Object2D.is_traffic_light', index=10,
            number=11, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='traffic_light_property', full_name='Object2D.traffic_light_property', index=11,
            number=12, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='is_traffic_sign', full_name='Object2D.is_traffic_sign', index=12,
            number=13, type=8, cpp_type=7, label=1,
            has_default_value=True, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='traffic_sign_property', full_name='Object2D.traffic_sign_property', index=13,
            number=14, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='segmentation_status', full_name='Object2D.segmentation_status', index=14,
            number=15, type=14, cpp_type=8, label=1,
            has_default_value=True, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='segmentation', full_name='Object2D.segmentation', index=15,
            number=16, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _OBJECT2D_BASICTYPE,
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=353,
    serialized_end=931,
)

_TRAFFICSIGN.fields_by_name['sign_type'].enum_type = _TRAFFICSIGN_TYPE
_TRAFFICSIGN_TYPE.containing_type = _TRAFFICSIGN
_TRAFFICLIGHT.fields_by_name['color'].enum_type = _TRAFFICLIGHT_COLOR
_TRAFFICLIGHT.fields_by_name['shape'].enum_type = _TRAFFICLIGHT_SHAPE
_TRAFFICLIGHT_COLOR.containing_type = _TRAFFICLIGHT
_TRAFFICLIGHT_SHAPE.containing_type = _TRAFFICLIGHT
_OBJECT2D.fields_by_name['basic_type'].enum_type = _OBJECT2D_BASICTYPE
_OBJECT2D.fields_by_name['traffic_light_property'].message_type = _TRAFFICLIGHT
_OBJECT2D.fields_by_name['traffic_sign_property'].message_type = _TRAFFICSIGN
_OBJECT2D.fields_by_name['segmentation_status'].enum_type = common__pb2._LABELSTATUS
_OBJECT2D.fields_by_name['segmentation'].message_type = common__pb2._POLYGON2D
_OBJECT2D_BASICTYPE.containing_type = _OBJECT2D
DESCRIPTOR.message_types_by_name['TrafficSign'] = _TRAFFICSIGN
DESCRIPTOR.message_types_by_name['TrafficLight'] = _TRAFFICLIGHT
DESCRIPTOR.message_types_by_name['Object2D'] = _OBJECT2D
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrafficSign = _reflection.GeneratedProtocolMessageType('TrafficSign', (_message.Message,), dict(
    DESCRIPTOR=_TRAFFICSIGN,
    __module__='object_2d_pb2'
    # @@protoc_insertion_point(class_scope:TrafficSign)
))
_sym_db.RegisterMessage(TrafficSign)

TrafficLight = _reflection.GeneratedProtocolMessageType('TrafficLight', (_message.Message,), dict(
    DESCRIPTOR=_TRAFFICLIGHT,
    __module__='object_2d_pb2'
    # @@protoc_insertion_point(class_scope:TrafficLight)
))
_sym_db.RegisterMessage(TrafficLight)

Object2D = _reflection.GeneratedProtocolMessageType('Object2D', (_message.Message,), dict(
    DESCRIPTOR=_OBJECT2D,
    __module__='object_2d_pb2'
    # @@protoc_insertion_point(class_scope:Object2D)
))
_sym_db.RegisterMessage(Object2D)


# @@protoc_insertion_point(module_scope)
