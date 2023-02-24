# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import arizon_usb_apiserver.grpc.force_packet_pb2 as force__packet__pb2


class ForcePacketServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetFIFOStatus = channel.unary_unary(
                '/protocol.ForcePacketService/SetFIFOStatus',
                request_serializer=force__packet__pb2.ForceSetFIFOStatusRequest.SerializeToString,
                response_deserializer=force__packet__pb2.ForceStatusResponse.FromString,
                )
        self.GetFIFOStatus = channel.unary_unary(
                '/protocol.ForcePacketService/GetFIFOStatus',
                request_serializer=force__packet__pb2.ForceGetFIFOStatusRequest.SerializeToString,
                response_deserializer=force__packet__pb2.ForceStatusResponse.FromString,
                )
        self.GetPacket = channel.unary_unary(
                '/protocol.ForcePacketService/GetPacket',
                request_serializer=force__packet__pb2.ForcePacketRequest.SerializeToString,
                response_deserializer=force__packet__pb2.ForcePacketResponse.FromString,
                )
        self.GetPacketStream = channel.unary_stream(
                '/protocol.ForcePacketService/GetPacketStream',
                request_serializer=force__packet__pb2.ForcePacketRequest.SerializeToString,
                response_deserializer=force__packet__pb2.ForcePacketResponse.FromString,
                )
        self.ResetPacketCache = channel.unary_unary(
                '/protocol.ForcePacketService/ResetPacketCache',
                request_serializer=force__packet__pb2.ForceResetCacheRequest.SerializeToString,
                response_deserializer=force__packet__pb2.ForceStatusResponse.FromString,
                )
        self.ToggleRecording = channel.unary_unary(
                '/protocol.ForcePacketService/ToggleRecording',
                request_serializer=force__packet__pb2.ForceToggleRecordingRequest.SerializeToString,
                response_deserializer=force__packet__pb2.ForceStatusResponse.FromString,
                )


class ForcePacketServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetFIFOStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFIFOStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPacket(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPacketStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetPacketCache(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ToggleRecording(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ForcePacketServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetFIFOStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SetFIFOStatus,
                    request_deserializer=force__packet__pb2.ForceSetFIFOStatusRequest.FromString,
                    response_serializer=force__packet__pb2.ForceStatusResponse.SerializeToString,
            ),
            'GetFIFOStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFIFOStatus,
                    request_deserializer=force__packet__pb2.ForceGetFIFOStatusRequest.FromString,
                    response_serializer=force__packet__pb2.ForceStatusResponse.SerializeToString,
            ),
            'GetPacket': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPacket,
                    request_deserializer=force__packet__pb2.ForcePacketRequest.FromString,
                    response_serializer=force__packet__pb2.ForcePacketResponse.SerializeToString,
            ),
            'GetPacketStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetPacketStream,
                    request_deserializer=force__packet__pb2.ForcePacketRequest.FromString,
                    response_serializer=force__packet__pb2.ForcePacketResponse.SerializeToString,
            ),
            'ResetPacketCache': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetPacketCache,
                    request_deserializer=force__packet__pb2.ForceResetCacheRequest.FromString,
                    response_serializer=force__packet__pb2.ForceStatusResponse.SerializeToString,
            ),
            'ToggleRecording': grpc.unary_unary_rpc_method_handler(
                    servicer.ToggleRecording,
                    request_deserializer=force__packet__pb2.ForceToggleRecordingRequest.FromString,
                    response_serializer=force__packet__pb2.ForceStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protocol.ForcePacketService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ForcePacketService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetFIFOStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protocol.ForcePacketService/SetFIFOStatus',
            force__packet__pb2.ForceSetFIFOStatusRequest.SerializeToString,
            force__packet__pb2.ForceStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFIFOStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protocol.ForcePacketService/GetFIFOStatus',
            force__packet__pb2.ForceGetFIFOStatusRequest.SerializeToString,
            force__packet__pb2.ForceStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPacket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protocol.ForcePacketService/GetPacket',
            force__packet__pb2.ForcePacketRequest.SerializeToString,
            force__packet__pb2.ForcePacketResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPacketStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/protocol.ForcePacketService/GetPacketStream',
            force__packet__pb2.ForcePacketRequest.SerializeToString,
            force__packet__pb2.ForcePacketResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetPacketCache(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protocol.ForcePacketService/ResetPacketCache',
            force__packet__pb2.ForceResetCacheRequest.SerializeToString,
            force__packet__pb2.ForceStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ToggleRecording(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protocol.ForcePacketService/ToggleRecording',
            force__packet__pb2.ForceToggleRecordingRequest.SerializeToString,
            force__packet__pb2.ForceStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
