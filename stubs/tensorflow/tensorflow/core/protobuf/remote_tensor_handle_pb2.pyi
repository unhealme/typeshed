"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import tensorflow.core.framework.tensor_shape_pb2
import tensorflow.core.framework.types_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ResourceDtypeAndShape(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DTYPE_FIELD_NUMBER: builtins.int
    SHAPE_FIELD_NUMBER: builtins.int
    dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
    @property
    def shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto: ...
    def __init__(
        self,
        *,
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
        shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["shape", b"shape"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["dtype", b"dtype", "shape", b"shape"]) -> None: ...

global___ResourceDtypeAndShape = ResourceDtypeAndShape

@typing.final
class RemoteTensorHandle(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OP_ID_FIELD_NUMBER: builtins.int
    OUTPUT_NUM_FIELD_NUMBER: builtins.int
    DEVICE_FIELD_NUMBER: builtins.int
    OP_DEVICE_FIELD_NUMBER: builtins.int
    DTYPE_FIELD_NUMBER: builtins.int
    RESOURCE_DTYPES_AND_SHAPES_FIELD_NUMBER: builtins.int
    op_id: builtins.int
    """The ID of the operation that produced this tensor."""
    output_num: builtins.int
    """The index into the outputs of the operation that produced this tensor."""
    device: builtins.str
    """Device where the tensor is located. Cannot be empty.
    For multi-device functions, it's the default device passed to placer.
    """
    op_device: builtins.str
    """Device of the operation producing this tensor. Can be empty if the
    operation producing this tensor is a multi-device function.
    """
    dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
    """Tensor type."""
    @property
    def resource_dtypes_and_shapes(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ResourceDtypeAndShape]:
        """Optional data types and shapes of a remote resource variable."""

    def __init__(
        self,
        *,
        op_id: builtins.int | None = ...,
        output_num: builtins.int | None = ...,
        device: builtins.str | None = ...,
        op_device: builtins.str | None = ...,
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
        resource_dtypes_and_shapes: collections.abc.Iterable[global___ResourceDtypeAndShape] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "device",
            b"device",
            "dtype",
            b"dtype",
            "op_device",
            b"op_device",
            "op_id",
            b"op_id",
            "output_num",
            b"output_num",
            "resource_dtypes_and_shapes",
            b"resource_dtypes_and_shapes",
        ],
    ) -> None: ...

global___RemoteTensorHandle = RemoteTensorHandle
