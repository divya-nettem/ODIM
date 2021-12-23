# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: composition_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='composition_service.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=
    b'\n\x19\x63omposition_service.proto\"W\n\x1cGetCompositionServiceRequest\x12\x14\n\x0csessionToken\x18\x01 \x01(\t\x12\x14\n\x0crequestParam\x18\x02 \x01(\t\x12\x0b\n\x03URL\x18\x03 \x01(\t\"l\n\x1dGetCompositionResourceRequest\x12\x14\n\x0csessionToken\x18\x01 \x01(\t\x12\x14\n\x0crequestParam\x18\x02 \x01(\t\x12\x0b\n\x03URL\x18\x03 \x01(\t\x12\x12\n\nresourceID\x18\x04 \x01(\t\"Z\n CreateCompositionResourceRequest\x12\x14\n\x0cSessionToken\x18\x01 \x01(\t\x12\x0b\n\x03URL\x18\x02 \x01(\t\x12\x13\n\x0bRequestBody\x18\x03 \x01(\x0c\"E\n DeleteCompositionResourceRequest\x12\x14\n\x0cSessionToken\x18\x01 \x01(\t\x12\x0b\n\x03URL\x18\x02 \x01(\t\"H\n\x0e\x43omposeRequest\x12\x14\n\x0csessionToken\x18\x01 \x01(\t\x12\x0b\n\x03URL\x18\x02 \x01(\t\x12\x13\n\x0bRequestBody\x18\x03 \x01(\x0c\"\xbd\x01\n\x1a\x43ompositionServiceResponse\x12\x12\n\nstatusCode\x18\x01 \x01(\x05\x12\x15\n\rstatusMessage\x18\x02 \x01(\t\x12\x37\n\x06header\x18\x03 \x03(\x0b\x32\'.CompositionServiceResponse.HeaderEntry\x12\x0c\n\x04\x62ody\x18\x04 \x01(\x0c\x1a-\n\x0bHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xb6\x03\n\x0b\x43omposition\x12U\n\x15GetCompositionService\x12\x1d.GetCompositionServiceRequest\x1a\x1b.CompositionServiceResponse\"\x00\x12W\n\x16GetCompositionResource\x12\x1e.GetCompositionResourceRequest\x1a\x1b.CompositionServiceResponse\"\x00\x12]\n\x19\x43reateCompositionResource\x12!.CreateCompositionResourceRequest\x1a\x1b.CompositionServiceResponse\"\x00\x12]\n\x19\x44\x65leteCompositionResource\x12!.DeleteCompositionResourceRequest\x1a\x1b.CompositionServiceResponse\"\x00\x12\x39\n\x07\x43ompose\x12\x0f.ComposeRequest\x1a\x1b.CompositionServiceResponse\"\x00\x62\x06proto3'
)

_GETCOMPOSITIONSERVICEREQUEST = _descriptor.Descriptor(
    name='GetCompositionServiceRequest',
    full_name='GetCompositionServiceRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='sessionToken',
            full_name='GetCompositionServiceRequest.sessionToken',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='requestParam',
            full_name='GetCompositionServiceRequest.requestParam',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='URL',
            full_name='GetCompositionServiceRequest.URL',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=29,
    serialized_end=116,
)

_GETCOMPOSITIONRESOURCEREQUEST = _descriptor.Descriptor(
    name='GetCompositionResourceRequest',
    full_name='GetCompositionResourceRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='sessionToken',
            full_name='GetCompositionResourceRequest.sessionToken',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='requestParam',
            full_name='GetCompositionResourceRequest.requestParam',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='URL',
            full_name='GetCompositionResourceRequest.URL',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='resourceID',
            full_name='GetCompositionResourceRequest.resourceID',
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=118,
    serialized_end=226,
)

_CREATECOMPOSITIONRESOURCEREQUEST = _descriptor.Descriptor(
    name='CreateCompositionResourceRequest',
    full_name='CreateCompositionResourceRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='SessionToken',
            full_name='CreateCompositionResourceRequest.SessionToken',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='URL',
            full_name='CreateCompositionResourceRequest.URL',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='RequestBody',
            full_name='CreateCompositionResourceRequest.RequestBody',
            index=2,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=228,
    serialized_end=318,
)

_DELETECOMPOSITIONRESOURCEREQUEST = _descriptor.Descriptor(
    name='DeleteCompositionResourceRequest',
    full_name='DeleteCompositionResourceRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='SessionToken',
            full_name='DeleteCompositionResourceRequest.SessionToken',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='URL',
            full_name='DeleteCompositionResourceRequest.URL',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=320,
    serialized_end=389,
)

_COMPOSEREQUEST = _descriptor.Descriptor(
    name='ComposeRequest',
    full_name='ComposeRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='sessionToken',
            full_name='ComposeRequest.sessionToken',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='URL',
            full_name='ComposeRequest.URL',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='RequestBody',
            full_name='ComposeRequest.RequestBody',
            index=2,
            number=3,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=391,
    serialized_end=463,
)

_COMPOSITIONSERVICERESPONSE_HEADERENTRY = _descriptor.Descriptor(
    name='HeaderEntry',
    full_name='CompositionServiceResponse.HeaderEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='CompositionServiceResponse.HeaderEntry.key',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='CompositionServiceResponse.HeaderEntry.value',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b'8\001',
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=610,
    serialized_end=655,
)

_COMPOSITIONSERVICERESPONSE = _descriptor.Descriptor(
    name='CompositionServiceResponse',
    full_name='CompositionServiceResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='statusCode',
            full_name='CompositionServiceResponse.statusCode',
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='statusMessage',
            full_name='CompositionServiceResponse.statusMessage',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='header',
            full_name='CompositionServiceResponse.header',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='body',
            full_name='CompositionServiceResponse.body',
            index=3,
            number=4,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[
        _COMPOSITIONSERVICERESPONSE_HEADERENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=466,
    serialized_end=655,
)

_COMPOSITIONSERVICERESPONSE_HEADERENTRY.containing_type = _COMPOSITIONSERVICERESPONSE
_COMPOSITIONSERVICERESPONSE.fields_by_name[
    'header'].message_type = _COMPOSITIONSERVICERESPONSE_HEADERENTRY
DESCRIPTOR.message_types_by_name[
    'GetCompositionServiceRequest'] = _GETCOMPOSITIONSERVICEREQUEST
DESCRIPTOR.message_types_by_name[
    'GetCompositionResourceRequest'] = _GETCOMPOSITIONRESOURCEREQUEST
DESCRIPTOR.message_types_by_name[
    'CreateCompositionResourceRequest'] = _CREATECOMPOSITIONRESOURCEREQUEST
DESCRIPTOR.message_types_by_name[
    'DeleteCompositionResourceRequest'] = _DELETECOMPOSITIONRESOURCEREQUEST
DESCRIPTOR.message_types_by_name['ComposeRequest'] = _COMPOSEREQUEST
DESCRIPTOR.message_types_by_name[
    'CompositionServiceResponse'] = _COMPOSITIONSERVICERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCompositionServiceRequest = _reflection.GeneratedProtocolMessageType(
    'GetCompositionServiceRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _GETCOMPOSITIONSERVICEREQUEST,
        '__module__': 'composition_service_pb2'
        # @@protoc_insertion_point(class_scope:GetCompositionServiceRequest)
    })
_sym_db.RegisterMessage(GetCompositionServiceRequest)

GetCompositionResourceRequest = _reflection.GeneratedProtocolMessageType(
    'GetCompositionResourceRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _GETCOMPOSITIONRESOURCEREQUEST,
        '__module__': 'composition_service_pb2'
        # @@protoc_insertion_point(class_scope:GetCompositionResourceRequest)
    })
_sym_db.RegisterMessage(GetCompositionResourceRequest)

CreateCompositionResourceRequest = _reflection.GeneratedProtocolMessageType(
    'CreateCompositionResourceRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _CREATECOMPOSITIONRESOURCEREQUEST,
        '__module__': 'composition_service_pb2'
        # @@protoc_insertion_point(class_scope:CreateCompositionResourceRequest)
    })
_sym_db.RegisterMessage(CreateCompositionResourceRequest)

DeleteCompositionResourceRequest = _reflection.GeneratedProtocolMessageType(
    'DeleteCompositionResourceRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _DELETECOMPOSITIONRESOURCEREQUEST,
        '__module__': 'composition_service_pb2'
        # @@protoc_insertion_point(class_scope:DeleteCompositionResourceRequest)
    })
_sym_db.RegisterMessage(DeleteCompositionResourceRequest)

ComposeRequest = _reflection.GeneratedProtocolMessageType(
    'ComposeRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _COMPOSEREQUEST,
        '__module__': 'composition_service_pb2'
        # @@protoc_insertion_point(class_scope:ComposeRequest)
    })
_sym_db.RegisterMessage(ComposeRequest)

CompositionServiceResponse = _reflection.GeneratedProtocolMessageType(
    'CompositionServiceResponse',
    (_message.Message, ),
    {
        'HeaderEntry':
        _reflection.GeneratedProtocolMessageType(
            'HeaderEntry',
            (_message.Message, ),
            {
                'DESCRIPTOR': _COMPOSITIONSERVICERESPONSE_HEADERENTRY,
                '__module__': 'composition_service_pb2'
                # @@protoc_insertion_point(class_scope:CompositionServiceResponse.HeaderEntry)
            }),
        'DESCRIPTOR':
        _COMPOSITIONSERVICERESPONSE,
        '__module__':
        'composition_service_pb2'
        # @@protoc_insertion_point(class_scope:CompositionServiceResponse)
    })
_sym_db.RegisterMessage(CompositionServiceResponse)
_sym_db.RegisterMessage(CompositionServiceResponse.HeaderEntry)

_COMPOSITIONSERVICERESPONSE_HEADERENTRY._options = None

_COMPOSITION = _descriptor.ServiceDescriptor(
    name='Composition',
    full_name='Composition',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=658,
    serialized_end=1096,
    methods=[
        _descriptor.MethodDescriptor(
            name='GetCompositionService',
            full_name='Composition.GetCompositionService',
            index=0,
            containing_service=None,
            input_type=_GETCOMPOSITIONSERVICEREQUEST,
            output_type=_COMPOSITIONSERVICERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='GetCompositionResource',
            full_name='Composition.GetCompositionResource',
            index=1,
            containing_service=None,
            input_type=_GETCOMPOSITIONRESOURCEREQUEST,
            output_type=_COMPOSITIONSERVICERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='CreateCompositionResource',
            full_name='Composition.CreateCompositionResource',
            index=2,
            containing_service=None,
            input_type=_CREATECOMPOSITIONRESOURCEREQUEST,
            output_type=_COMPOSITIONSERVICERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='DeleteCompositionResource',
            full_name='Composition.DeleteCompositionResource',
            index=3,
            containing_service=None,
            input_type=_DELETECOMPOSITIONRESOURCEREQUEST,
            output_type=_COMPOSITIONSERVICERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='Compose',
            full_name='Composition.Compose',
            index=4,
            containing_service=None,
            input_type=_COMPOSEREQUEST,
            output_type=_COMPOSITIONSERVICERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_COMPOSITION)

DESCRIPTOR.services_by_name['Composition'] = _COMPOSITION

# @@protoc_insertion_point(module_scope)
