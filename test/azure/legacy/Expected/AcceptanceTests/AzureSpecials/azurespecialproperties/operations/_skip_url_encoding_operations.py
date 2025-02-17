# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_get_method_path_valid_request(
    unencoded_path_param,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/azurespecials/skipUrlEncoding/method/path/valid/{unencodedPathParam}')
    path_format_arguments = {
        "unencodedPathParam": _SERIALIZER.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_path_valid_request(
    unencoded_path_param,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/azurespecials/skipUrlEncoding/path/path/valid/{unencodedPathParam}')
    path_format_arguments = {
        "unencodedPathParam": _SERIALIZER.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_swagger_path_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    unencoded_path_param = kwargs.pop('unencoded_path_param', "path1/path2/path3")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/azurespecials/skipUrlEncoding/swagger/path/valid/{unencodedPathParam}')
    path_format_arguments = {
        "unencodedPathParam": _SERIALIZER.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_method_query_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    q1 = kwargs.pop('q1')  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/azurespecials/skipUrlEncoding/method/query/valid')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['q1'] = _SERIALIZER.query("q1", q1, 'str', skip_quote=True)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_method_query_null_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    q1 = kwargs.pop('q1', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/azurespecials/skipUrlEncoding/method/query/null')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if q1 is not None:
        query_parameters['q1'] = _SERIALIZER.query("q1", q1, 'str', skip_quote=True)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_path_query_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    q1 = kwargs.pop('q1')  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/azurespecials/skipUrlEncoding/path/query/valid')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['q1'] = _SERIALIZER.query("q1", q1, 'str', skip_quote=True)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_swagger_query_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    q1 = kwargs.pop('q1', "value1&q2=value2&q3=value3")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/azurespecials/skipUrlEncoding/swagger/query/valid')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['q1'] = _SERIALIZER.query("q1", q1, 'str', skip_quote=True)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class SkipUrlEncodingOperations(object):
    """SkipUrlEncodingOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azurespecialproperties.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_method_path_valid(
        self,
        unencoded_path_param,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get method with unencoded path parameter with value 'path1/path2/path3'.

        :param unencoded_path_param: Unencoded path parameter with value 'path1/path2/path3'.
        :type unencoded_path_param: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_method_path_valid_request(
            unencoded_path_param=unencoded_path_param,
            template_url=self.get_method_path_valid.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_method_path_valid.metadata = {"url": "/azurespecials/skipUrlEncoding/method/path/valid/{unencodedPathParam}"}  # type: ignore

    @distributed_trace
    def get_path_valid(
        self,
        unencoded_path_param,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get method with unencoded path parameter with value 'path1/path2/path3'.

        :param unencoded_path_param: Unencoded path parameter with value 'path1/path2/path3'.
        :type unencoded_path_param: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_path_valid_request(
            unencoded_path_param=unencoded_path_param,
            template_url=self.get_path_valid.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_path_valid.metadata = {"url": "/azurespecials/skipUrlEncoding/path/path/valid/{unencodedPathParam}"}  # type: ignore

    @distributed_trace
    def get_swagger_path_valid(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get method with unencoded path parameter with value 'path1/path2/path3'.

        :keyword unencoded_path_param: An unencoded path parameter with value 'path1/path2/path3'. The
         default value is "path1/path2/path3". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype unencoded_path_param: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        unencoded_path_param = kwargs.pop("unencoded_path_param", "path1/path2/path3")  # type: str

        request = build_get_swagger_path_valid_request(
            unencoded_path_param=unencoded_path_param,
            template_url=self.get_swagger_path_valid.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_swagger_path_valid.metadata = {"url": "/azurespecials/skipUrlEncoding/swagger/path/valid/{unencodedPathParam}"}  # type: ignore

    @distributed_trace
    def get_method_query_valid(
        self,
        q1,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

        :param q1: Unencoded query parameter with value 'value1&q2=value2&q3=value3'.
        :type q1: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_method_query_valid_request(
            q1=q1,
            template_url=self.get_method_query_valid.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_method_query_valid.metadata = {"url": "/azurespecials/skipUrlEncoding/method/query/valid"}  # type: ignore

    @distributed_trace
    def get_method_query_null(
        self,
        q1=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get method with unencoded query parameter with value null.

        :param q1: Unencoded query parameter with value null.
        :type q1: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_method_query_null_request(
            q1=q1,
            template_url=self.get_method_query_null.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_method_query_null.metadata = {"url": "/azurespecials/skipUrlEncoding/method/query/null"}  # type: ignore

    @distributed_trace
    def get_path_query_valid(
        self,
        q1,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

        :param q1: Unencoded query parameter with value 'value1&q2=value2&q3=value3'.
        :type q1: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_path_query_valid_request(
            q1=q1,
            template_url=self.get_path_query_valid.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_path_query_valid.metadata = {"url": "/azurespecials/skipUrlEncoding/path/query/valid"}  # type: ignore

    @distributed_trace
    def get_swagger_query_valid(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

        :keyword q1: An unencoded query parameter with value 'value1&q2=value2&q3=value3'. The default
         value is "value1&q2=value2&q3=value3". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype q1: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        q1 = kwargs.pop("q1", "value1&q2=value2&q3=value3")  # type: str

        request = build_get_swagger_query_valid_request(
            q1=q1,
            template_url=self.get_swagger_query_valid.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_swagger_query_valid.metadata = {"url": "/azurespecials/skipUrlEncoding/swagger/query/valid"}  # type: ignore
