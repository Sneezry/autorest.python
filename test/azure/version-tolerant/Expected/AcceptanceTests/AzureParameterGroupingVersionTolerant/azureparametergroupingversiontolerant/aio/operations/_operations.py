# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ...operations._operations import (
    build_parameter_grouping_post_multi_param_groups_request,
    build_parameter_grouping_post_optional_request,
    build_parameter_grouping_post_required_request,
    build_parameter_grouping_post_reserved_words_request,
    build_parameter_grouping_post_shared_parameter_group_object_request,
)

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ParameterGroupingOperations:
    """ParameterGroupingOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def post_required(
        self, path: str, body: int, *, custom_header: Optional[str] = None, query: Optional[int] = 30, **kwargs: Any
    ) -> None:
        """Post a bunch of required parameters grouped.

        :param path: Path parameter.
        :type path: str
        :param body:
        :type body: int
        :keyword custom_header:
        :paramtype custom_header: str
        :keyword query: Query parameter with default.
        :paramtype query: int
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = body

        request = build_parameter_grouping_post_required_request(
            path=path,
            content_type=content_type,
            json=_json,
            custom_header=custom_header,
            query=query,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    post_required.metadata = {"url": "/parameterGrouping/postRequired/{path}"}  # type: ignore

    @distributed_trace_async
    async def post_optional(
        self, *, custom_header: Optional[str] = None, query: Optional[int] = 30, **kwargs: Any
    ) -> None:
        """Post a bunch of optional parameters grouped.

        :keyword custom_header:
        :paramtype custom_header: str
        :keyword query: Query parameter with default.
        :paramtype query: int
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_parameter_grouping_post_optional_request(
            custom_header=custom_header,
            query=query,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    post_optional.metadata = {"url": "/parameterGrouping/postOptional"}  # type: ignore

    @distributed_trace_async
    async def post_reserved_words(
        self, *, from_parameter: Optional[str] = None, accept_parameter: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Post a grouped parameters with reserved words.

        :keyword from_parameter: 'from' is a reserved word. Pass in 'bob' to pass.
        :paramtype from_parameter: str
        :keyword accept_parameter: 'accept' is a reserved word. Pass in 'yes' to pass.
        :paramtype accept_parameter: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_parameter_grouping_post_reserved_words_request(
            from_parameter=from_parameter,
            accept_parameter=accept_parameter,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    post_reserved_words.metadata = {"url": "/parameterGrouping/postReservedWords"}  # type: ignore

    @distributed_trace_async
    async def post_multi_param_groups(
        self,
        *,
        header_one: Optional[str] = None,
        query_one: Optional[int] = 30,
        header_two: Optional[str] = None,
        query_two: Optional[int] = 30,
        **kwargs: Any
    ) -> None:
        """Post parameters from multiple different parameter groups.

        :keyword header_one:
        :paramtype header_one: str
        :keyword query_one: Query parameter with default.
        :paramtype query_one: int
        :keyword header_two:
        :paramtype header_two: str
        :keyword query_two: Query parameter with default.
        :paramtype query_two: int
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_parameter_grouping_post_multi_param_groups_request(
            header_one=header_one,
            query_one=query_one,
            header_two=header_two,
            query_two=query_two,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    post_multi_param_groups.metadata = {"url": "/parameterGrouping/postMultipleParameterGroups"}  # type: ignore

    @distributed_trace_async
    async def post_shared_parameter_group_object(
        self, *, header_one: Optional[str] = None, query_one: Optional[int] = 30, **kwargs: Any
    ) -> None:
        """Post parameters with a shared parameter group object.

        :keyword header_one:
        :paramtype header_one: str
        :keyword query_one: Query parameter with default.
        :paramtype query_one: int
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_parameter_grouping_post_shared_parameter_group_object_request(
            header_one=header_one,
            query_one=query_one,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    post_shared_parameter_group_object.metadata = {"url": "/parameterGrouping/sharedParameterGroupObject"}  # type: ignore
