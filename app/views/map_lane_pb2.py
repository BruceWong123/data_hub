# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map_lane.proto


import os
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

curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
# sys.path.append("/home/bruce/datahub/data_hub/app/views")

import map_overlap_pb2 as map__overlap__pb2   # NOQA: E402
import map_geometry_pb2 as map__geometry__pb2  # NOQA: E402
import geometry_pb2 as geometry__pb2   # NOQA: E402

DESCRIPTOR = _descriptor.FileDescriptor(
    name='map_lane.proto',
    package='deeproute.hdmap',
    syntax='proto2',
    serialized_pb=_b('\n\x0emap_lane.proto\x12\x0f\x64\x65\x65proute.hdmap\x1a\x12map_geometry.proto\x1a\x11map_overlap.proto\x1a\x0egeometry.proto\"\xce\x01\n\x10LaneBoundaryType\x12\t\n\x01s\x18\x01 \x01(\x01\x12\x35\n\x05types\x18\x02 \x03(\x0e\x32&.deeproute.hdmap.LaneBoundaryType.Type\"x\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rDOTTED_YELLOW\x10\x01\x12\x10\n\x0c\x44OTTED_WHITE\x10\x02\x12\x10\n\x0cSOLID_YELLOW\x10\x03\x12\x0f\n\x0bSOLID_WHITE\x10\x04\x12\x11\n\rDOUBLE_YELLOW\x10\x05\x12\x08\n\x04\x43URB\x10\x06\"\x88\x03\n\x0cLaneBoundary\x12%\n\x05\x63urve\x18\x01 \x01(\x0b\x32\x16.deeproute.hdmap.Curve\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12\x0f\n\x07virtual\x18\x03 \x01(\x08\x12\x38\n\rboundary_type\x18\x04 \x03(\x0b\x32!.deeproute.hdmap.LaneBoundaryType\x12\n\n\x02id\x18\x05 \x01(\x05\x12.\n\x08\x62oundary\x18\x06 \x01(\x0b\x32\x1c.deeproute.geometry.Polyline\x12:\n\tcrossable\x18\x07 \x01(\x0e\x32\'.deeproute.hdmap.LaneBoundary.Crossable\x12\x0c\n\x04\x63ost\x18\x08 \x01(\x01\x12\x0e\n\x06layers\x18\t \x03(\x05\"`\n\tCrossable\x12\x12\n\x0ePHYSICALLY_NOT\x10\x00\x12\x0f\n\x0bLEGALLY_NOT\x10\x01\x12\x11\n\rRIGHT_TO_LEFT\x10\x02\x12\x11\n\rLEFT_TO_RIGHT\x10\x03\x12\x08\n\x04\x42OTH\x10\x04\"1\n\x15LaneSampleAssociation\x12\t\n\x01s\x18\x01 \x01(\x01\x12\r\n\x05width\x18\x02 \x01(\x01\"f\n\x08\x45ntrance\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07lane_id\x18\x02 \x01(\x05\x12-\n\x08location\x18\x03 \x01(\x0b\x32\x1b.deeproute.geometry.Point3D\x12\x0e\n\x06layers\x18\x04 \x03(\x05\"\xe3\r\n\x04Lane\x12\n\n\x02id\x18\x01 \x01(\x05\x12-\n\rcentral_curve\x18\x02 \x01(\x0b\x32\x16.deeproute.hdmap.Curve\x12\x34\n\rleft_boundary\x18\x03 \x01(\x0b\x32\x1d.deeproute.hdmap.LaneBoundary\x12\x35\n\x0eright_boundary\x18\x04 \x01(\x0b\x32\x1d.deeproute.hdmap.LaneBoundary\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\x1f\n\x0bspeed_limit\x18\x06 \x01(\x02:\n11.1111107\x12\x12\n\noverlap_id\x18\x07 \x03(\x05\x12\x16\n\x0epredecessor_id\x18\x08 \x03(\x05\x12\x14\n\x0csuccessor_id\x18\t \x03(\x05\x12%\n\x1dleft_neighbor_forward_lane_id\x18\n \x01(\x05\x12&\n\x1eright_neighbor_forward_lane_id\x18\x0b \x01(\x05\x12,\n\x04type\x18\x0c \x01(\x0e\x32\x1e.deeproute.hdmap.Lane.LaneType\x12,\n\x04turn\x18\r \x01(\x0e\x32\x1e.deeproute.hdmap.Lane.LaneTurn\x12%\n\x1dleft_neighbor_reverse_lane_id\x18\x0e \x01(\x05\x12&\n\x1eright_neighbor_reverse_lane_id\x18\x0f \x01(\x05\x12\x13\n\x0bjunction_id\x18\x10 \x01(\x05\x12;\n\x0bleft_sample\x18\x11 \x03(\x0b\x32&.deeproute.hdmap.LaneSampleAssociation\x12<\n\x0cright_sample\x18\x12 \x03(\x0b\x32&.deeproute.hdmap.LaneSampleAssociation\x12\x36\n\tdirection\x18\x13 \x01(\x0e\x32#.deeproute.hdmap.Lane.LaneDirection\x12@\n\x10left_road_sample\x18\x14 \x03(\x0b\x32&.deeproute.hdmap.LaneSampleAssociation\x12\x41\n\x11right_road_sample\x18\x15 \x03(\x0b\x32&.deeproute.hdmap.LaneSampleAssociation\x12\x1c\n\x14self_reverse_lane_id\x18\x16 \x03(\x05\x12\x30\n\ncenterline\x18\x17 \x01(\x0b\x32\x1c.deeproute.geometry.Polyline\x12\x18\n\x0c\x63\x65nterline_s\x18\x18 \x03(\x02\x42\x02\x10\x01\x12\x18\n\x10left_boundary_id\x18\x19 \x01(\x05\x12\x19\n\x11right_boundary_id\x18\x1a \x01(\x05\x12\x43\n\x12\x62oundary_direction\x18\x1b \x01(\x0e\x32\'.deeproute.hdmap.Lane.BoundaryDirection\x12*\n\x08overlaps\x18\x1c \x03(\x0b\x32\x18.deeproute.hdmap.Overlap\x12\x0c\n\x04\x63ost\x18\x1d \x01(\x01\x12.\n\x05merge\x18\x1e \x01(\x0e\x32\x1f.deeproute.hdmap.Lane.MergeType\x12\x18\n\x10merge_to_lane_id\x18\x1f \x01(\x05\x12\x1a\n\x12merge_from_lane_id\x18  \x03(\x05\x12\x0e\n\x06layers\x18! \x03(\x05\"\xbc\x01\n\x08LaneType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07HIGHWAY\x10\x01\x12\n\n\x06STREET\x10\x02\x12\x11\n\rBIDIRECTIONAL\x10\x03\x12\x0c\n\x08SHOULDER\x10\x04\x12\n\n\x06\x42IKING\x10\x05\x12\x0c\n\x08SIDEWALK\x10\x06\x12\x0e\n\nRESTRICTED\x10\x07\x12\x0b\n\x07PARKING\x10\x08\x12\x0c\n\x08ROADWORK\x10\t\x12\x0b\n\x07OFFRAMP\x10\n\x12\n\n\x06ONRAMP\x10\x0b\x12\x0b\n\x07\x42USLANE\x10\x0c\"]\n\x08LaneTurn\x12\x0b\n\x07INVALID\x10\x00\x12\x0c\n\x08STRAIGHT\x10\x01\x12\x08\n\x04LEFT\x10\x02\x12\t\n\x05RIGHT\x10\x04\x12\x0f\n\x0bU_TURN_LEFT\x10\x08\x12\x10\n\x0cU_TURN_RIGHT\x10\x10\";\n\rLaneDirection\x12\x0b\n\x07\x46ORWARD\x10\x01\x12\x0c\n\x08\x42\x41\x43KWARD\x10\x02\x12\x0f\n\x0b\x42IDIRECTION\x10\x03\"T\n\x11\x42oundaryDirection\x12\x08\n\x04SAME\x10\x00\x12\x10\n\x0cLEFT_REVERSE\x10\x01\x12\x11\n\rRIGHT_REVERSE\x10\x02\x12\x10\n\x0c\x42OTH_REVERSE\x10\x03\"4\n\tMergeType\x12\x08\n\x04NONE\x10\x00\x12\r\n\tFROM_LEFT\x10\x01\x12\x0e\n\nFROM_RIGHT\x10\x02'),
    dependencies=[map__geometry__pb2.DESCRIPTOR, map__overlap__pb2.DESCRIPTOR, geometry__pb2.DESCRIPTOR, ])


_LANEBOUNDARYTYPE_TYPE = _descriptor.EnumDescriptor(
    name='Type',
    full_name='deeproute.hdmap.LaneBoundaryType.Type',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='DOTTED_YELLOW', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='DOTTED_WHITE', index=2, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='SOLID_YELLOW', index=3, number=3,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='SOLID_WHITE', index=4, number=4,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='DOUBLE_YELLOW', index=5, number=5,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CURB', index=6, number=6,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=177,
    serialized_end=297,
)
_sym_db.RegisterEnumDescriptor(_LANEBOUNDARYTYPE_TYPE)

_LANEBOUNDARY_CROSSABLE = _descriptor.EnumDescriptor(
    name='Crossable',
    full_name='deeproute.hdmap.LaneBoundary.Crossable',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='PHYSICALLY_NOT', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='LEGALLY_NOT', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='RIGHT_TO_LEFT', index=2, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='LEFT_TO_RIGHT', index=3, number=3,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BOTH', index=4, number=4,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=596,
    serialized_end=692,
)
_sym_db.RegisterEnumDescriptor(_LANEBOUNDARY_CROSSABLE)

_LANE_LANETYPE = _descriptor.EnumDescriptor(
    name='LaneType',
    full_name='deeproute.hdmap.Lane.LaneType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='HIGHWAY', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='STREET', index=2, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BIDIRECTIONAL', index=3, number=3,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='SHOULDER', index=4, number=4,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BIKING', index=5, number=5,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='SIDEWALK', index=6, number=6,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='RESTRICTED', index=7, number=7,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PARKING', index=8, number=8,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ROADWORK', index=9, number=9,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='OFFRAMP', index=10, number=10,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ONRAMP', index=11, number=11,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BUSLANE', index=12, number=12,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=2129,
    serialized_end=2317,
)
_sym_db.RegisterEnumDescriptor(_LANE_LANETYPE)

_LANE_LANETURN = _descriptor.EnumDescriptor(
    name='LaneTurn',
    full_name='deeproute.hdmap.Lane.LaneTurn',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='INVALID', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='STRAIGHT', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='LEFT', index=2, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='RIGHT', index=3, number=4,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='U_TURN_LEFT', index=4, number=8,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='U_TURN_RIGHT', index=5, number=16,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=2319,
    serialized_end=2412,
)
_sym_db.RegisterEnumDescriptor(_LANE_LANETURN)

_LANE_LANEDIRECTION = _descriptor.EnumDescriptor(
    name='LaneDirection',
    full_name='deeproute.hdmap.Lane.LaneDirection',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='FORWARD', index=0, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BACKWARD', index=1, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BIDIRECTION', index=2, number=3,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=2414,
    serialized_end=2473,
)
_sym_db.RegisterEnumDescriptor(_LANE_LANEDIRECTION)

_LANE_BOUNDARYDIRECTION = _descriptor.EnumDescriptor(
    name='BoundaryDirection',
    full_name='deeproute.hdmap.Lane.BoundaryDirection',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='SAME', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='LEFT_REVERSE', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='RIGHT_REVERSE', index=2, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BOTH_REVERSE', index=3, number=3,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=2475,
    serialized_end=2559,
)
_sym_db.RegisterEnumDescriptor(_LANE_BOUNDARYDIRECTION)

_LANE_MERGETYPE = _descriptor.EnumDescriptor(
    name='MergeType',
    full_name='deeproute.hdmap.Lane.MergeType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='NONE', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='FROM_LEFT', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='FROM_RIGHT', index=2, number=2,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=2561,
    serialized_end=2613,
)
_sym_db.RegisterEnumDescriptor(_LANE_MERGETYPE)


_LANEBOUNDARYTYPE = _descriptor.Descriptor(
    name='LaneBoundaryType',
    full_name='deeproute.hdmap.LaneBoundaryType',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='s', full_name='deeproute.hdmap.LaneBoundaryType.s', index=0,
            number=1, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='types', full_name='deeproute.hdmap.LaneBoundaryType.types', index=1,
            number=2, type=14, cpp_type=8, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _LANEBOUNDARYTYPE_TYPE,
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=91,
    serialized_end=297,
)


_LANEBOUNDARY = _descriptor.Descriptor(
    name='LaneBoundary',
    full_name='deeproute.hdmap.LaneBoundary',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='curve', full_name='deeproute.hdmap.LaneBoundary.curve', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='length', full_name='deeproute.hdmap.LaneBoundary.length', index=1,
            number=2, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='virtual', full_name='deeproute.hdmap.LaneBoundary.virtual', index=2,
            number=3, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='boundary_type', full_name='deeproute.hdmap.LaneBoundary.boundary_type', index=3,
            number=4, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='id', full_name='deeproute.hdmap.LaneBoundary.id', index=4,
            number=5, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='boundary', full_name='deeproute.hdmap.LaneBoundary.boundary', index=5,
            number=6, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='crossable', full_name='deeproute.hdmap.LaneBoundary.crossable', index=6,
            number=7, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='cost', full_name='deeproute.hdmap.LaneBoundary.cost', index=7,
            number=8, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='layers', full_name='deeproute.hdmap.LaneBoundary.layers', index=8,
            number=9, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _LANEBOUNDARY_CROSSABLE,
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=300,
    serialized_end=692,
)


_LANESAMPLEASSOCIATION = _descriptor.Descriptor(
    name='LaneSampleAssociation',
    full_name='deeproute.hdmap.LaneSampleAssociation',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='s', full_name='deeproute.hdmap.LaneSampleAssociation.s', index=0,
            number=1, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='width', full_name='deeproute.hdmap.LaneSampleAssociation.width', index=1,
            number=2, type=1, cpp_type=5, label=1,
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
    serialized_start=694,
    serialized_end=743,
)


_ENTRANCE = _descriptor.Descriptor(
    name='Entrance',
    full_name='deeproute.hdmap.Entrance',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='deeproute.hdmap.Entrance.id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='lane_id', full_name='deeproute.hdmap.Entrance.lane_id', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='location', full_name='deeproute.hdmap.Entrance.location', index=2,
            number=3, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='layers', full_name='deeproute.hdmap.Entrance.layers', index=3,
            number=4, type=5, cpp_type=1, label=3,
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
    serialized_start=745,
    serialized_end=847,
)


_LANE = _descriptor.Descriptor(
    name='Lane',
    full_name='deeproute.hdmap.Lane',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='deeproute.hdmap.Lane.id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='central_curve', full_name='deeproute.hdmap.Lane.central_curve', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='left_boundary', full_name='deeproute.hdmap.Lane.left_boundary', index=2,
            number=3, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='right_boundary', full_name='deeproute.hdmap.Lane.right_boundary', index=3,
            number=4, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='length', full_name='deeproute.hdmap.Lane.length', index=4,
            number=5, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='speed_limit', full_name='deeproute.hdmap.Lane.speed_limit', index=5,
            number=6, type=2, cpp_type=6, label=1,
            has_default_value=True, default_value=float(11.1111107),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='overlap_id', full_name='deeproute.hdmap.Lane.overlap_id', index=6,
            number=7, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='predecessor_id', full_name='deeproute.hdmap.Lane.predecessor_id', index=7,
            number=8, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='successor_id', full_name='deeproute.hdmap.Lane.successor_id', index=8,
            number=9, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='left_neighbor_forward_lane_id', full_name='deeproute.hdmap.Lane.left_neighbor_forward_lane_id', index=9,
            number=10, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='right_neighbor_forward_lane_id', full_name='deeproute.hdmap.Lane.right_neighbor_forward_lane_id', index=10,
            number=11, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='type', full_name='deeproute.hdmap.Lane.type', index=11,
            number=12, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='turn', full_name='deeproute.hdmap.Lane.turn', index=12,
            number=13, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='left_neighbor_reverse_lane_id', full_name='deeproute.hdmap.Lane.left_neighbor_reverse_lane_id', index=13,
            number=14, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='right_neighbor_reverse_lane_id', full_name='deeproute.hdmap.Lane.right_neighbor_reverse_lane_id', index=14,
            number=15, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='junction_id', full_name='deeproute.hdmap.Lane.junction_id', index=15,
            number=16, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='left_sample', full_name='deeproute.hdmap.Lane.left_sample', index=16,
            number=17, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='right_sample', full_name='deeproute.hdmap.Lane.right_sample', index=17,
            number=18, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='direction', full_name='deeproute.hdmap.Lane.direction', index=18,
            number=19, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=1,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='left_road_sample', full_name='deeproute.hdmap.Lane.left_road_sample', index=19,
            number=20, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='right_road_sample', full_name='deeproute.hdmap.Lane.right_road_sample', index=20,
            number=21, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='self_reverse_lane_id', full_name='deeproute.hdmap.Lane.self_reverse_lane_id', index=21,
            number=22, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='centerline', full_name='deeproute.hdmap.Lane.centerline', index=22,
            number=23, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='centerline_s', full_name='deeproute.hdmap.Lane.centerline_s', index=23,
            number=24, type=2, cpp_type=6, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='left_boundary_id', full_name='deeproute.hdmap.Lane.left_boundary_id', index=24,
            number=25, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='right_boundary_id', full_name='deeproute.hdmap.Lane.right_boundary_id', index=25,
            number=26, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='boundary_direction', full_name='deeproute.hdmap.Lane.boundary_direction', index=26,
            number=27, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='overlaps', full_name='deeproute.hdmap.Lane.overlaps', index=27,
            number=28, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='cost', full_name='deeproute.hdmap.Lane.cost', index=28,
            number=29, type=1, cpp_type=5, label=1,
            has_default_value=False, default_value=float(0),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='merge', full_name='deeproute.hdmap.Lane.merge', index=29,
            number=30, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='merge_to_lane_id', full_name='deeproute.hdmap.Lane.merge_to_lane_id', index=30,
            number=31, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='merge_from_lane_id', full_name='deeproute.hdmap.Lane.merge_from_lane_id', index=31,
            number=32, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='layers', full_name='deeproute.hdmap.Lane.layers', index=32,
            number=33, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _LANE_LANETYPE,
        _LANE_LANETURN,
        _LANE_LANEDIRECTION,
        _LANE_BOUNDARYDIRECTION,
        _LANE_MERGETYPE,
    ],
    options=None,
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=850,
    serialized_end=2613,
)

_LANEBOUNDARYTYPE.fields_by_name['types'].enum_type = _LANEBOUNDARYTYPE_TYPE
_LANEBOUNDARYTYPE_TYPE.containing_type = _LANEBOUNDARYTYPE
_LANEBOUNDARY.fields_by_name['curve'].message_type = map__geometry__pb2._CURVE
_LANEBOUNDARY.fields_by_name['boundary_type'].message_type = _LANEBOUNDARYTYPE
_LANEBOUNDARY.fields_by_name['boundary'].message_type = geometry__pb2._POLYLINE
_LANEBOUNDARY.fields_by_name['crossable'].enum_type = _LANEBOUNDARY_CROSSABLE
_LANEBOUNDARY_CROSSABLE.containing_type = _LANEBOUNDARY
_ENTRANCE.fields_by_name['location'].message_type = geometry__pb2._POINT3D
_LANE.fields_by_name['central_curve'].message_type = map__geometry__pb2._CURVE
_LANE.fields_by_name['left_boundary'].message_type = _LANEBOUNDARY
_LANE.fields_by_name['right_boundary'].message_type = _LANEBOUNDARY
_LANE.fields_by_name['type'].enum_type = _LANE_LANETYPE
_LANE.fields_by_name['turn'].enum_type = _LANE_LANETURN
_LANE.fields_by_name['left_sample'].message_type = _LANESAMPLEASSOCIATION
_LANE.fields_by_name['right_sample'].message_type = _LANESAMPLEASSOCIATION
_LANE.fields_by_name['direction'].enum_type = _LANE_LANEDIRECTION
_LANE.fields_by_name['left_road_sample'].message_type = _LANESAMPLEASSOCIATION
_LANE.fields_by_name['right_road_sample'].message_type = _LANESAMPLEASSOCIATION
_LANE.fields_by_name['centerline'].message_type = geometry__pb2._POLYLINE
_LANE.fields_by_name['boundary_direction'].enum_type = _LANE_BOUNDARYDIRECTION
_LANE.fields_by_name['overlaps'].message_type = map__overlap__pb2._OVERLAP
_LANE.fields_by_name['merge'].enum_type = _LANE_MERGETYPE
_LANE_LANETYPE.containing_type = _LANE
_LANE_LANETURN.containing_type = _LANE
_LANE_LANEDIRECTION.containing_type = _LANE
_LANE_BOUNDARYDIRECTION.containing_type = _LANE
_LANE_MERGETYPE.containing_type = _LANE
DESCRIPTOR.message_types_by_name['LaneBoundaryType'] = _LANEBOUNDARYTYPE
DESCRIPTOR.message_types_by_name['LaneBoundary'] = _LANEBOUNDARY
DESCRIPTOR.message_types_by_name['LaneSampleAssociation'] = _LANESAMPLEASSOCIATION
DESCRIPTOR.message_types_by_name['Entrance'] = _ENTRANCE
DESCRIPTOR.message_types_by_name['Lane'] = _LANE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LaneBoundaryType = _reflection.GeneratedProtocolMessageType('LaneBoundaryType', (_message.Message,), dict(
    DESCRIPTOR=_LANEBOUNDARYTYPE,
    __module__='map_lane_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.hdmap.LaneBoundaryType)
))
_sym_db.RegisterMessage(LaneBoundaryType)

LaneBoundary = _reflection.GeneratedProtocolMessageType('LaneBoundary', (_message.Message,), dict(
    DESCRIPTOR=_LANEBOUNDARY,
    __module__='map_lane_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.hdmap.LaneBoundary)
))
_sym_db.RegisterMessage(LaneBoundary)

LaneSampleAssociation = _reflection.GeneratedProtocolMessageType('LaneSampleAssociation', (_message.Message,), dict(
    DESCRIPTOR=_LANESAMPLEASSOCIATION,
    __module__='map_lane_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.hdmap.LaneSampleAssociation)
))
_sym_db.RegisterMessage(LaneSampleAssociation)

Entrance = _reflection.GeneratedProtocolMessageType('Entrance', (_message.Message,), dict(
    DESCRIPTOR=_ENTRANCE,
    __module__='map_lane_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.hdmap.Entrance)
))
_sym_db.RegisterMessage(Entrance)

Lane = _reflection.GeneratedProtocolMessageType('Lane', (_message.Message,), dict(
    DESCRIPTOR=_LANE,
    __module__='map_lane_pb2'
    # @@protoc_insertion_point(class_scope:deeproute.hdmap.Lane)
))
_sym_db.RegisterMessage(Lane)


_LANE.fields_by_name['centerline_s'].has_options = True
_LANE.fields_by_name['centerline_s']._options = _descriptor._ParseOptions(
    descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
