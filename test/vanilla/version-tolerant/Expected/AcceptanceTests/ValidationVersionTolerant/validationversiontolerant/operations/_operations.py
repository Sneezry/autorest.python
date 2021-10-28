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
from msrest import Serializer

from .._vendor import _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()


def _param_not_set(param_dict, rest_api_name_lower):
    return not any(k for k in param_dict if k.lower() == rest_api_name_lower)


# fmt: off

def build_validation_of_method_parameters_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    id,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "1.0.0")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/fakepath/{subscriptionId}/{resourceGroupName}/{id}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=10, min_length=3, pattern=r'[a-zA-Z0-9\']+'),
        "id": _SERIALIZER.url("id", id, 'int', maximum=1000, minimum=100, multiple=10),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(query_parameters, "apiversion"):
        query_parameters['apiVersion'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_validation_of_body_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    id,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "1.0.0")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/fakepath/{subscriptionId}/{resourceGroupName}/{id}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=10, min_length=3, pattern=r'[a-zA-Z0-9]+'),
        "id": _SERIALIZER.url("id", id, 'int', maximum=1000, minimum=100, multiple=10),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(query_parameters, "apiversion"):
        query_parameters['apiVersion'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "content-type") and content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_with_constant_in_path_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    constant_param = kwargs.pop('constant_param', "constant")  # type: str

    # Construct URL
    url = kwargs.pop("template_url", '/validation/constantsInPath/{constantParam}/value')
    path_format_arguments = {
        "constantParam": _SERIALIZER.url("constant_param", constant_param, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    return HttpRequest(
        method="GET",
        url=url,
        **kwargs
    )


def build_post_with_constant_in_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    constant_param = kwargs.pop('constant_param', "constant")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/validation/constantsInPath/{constantParam}/value')
    path_format_arguments = {
        "constantParam": _SERIALIZER.url("constant_param", constant_param, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "content-type") and content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class AutoRestValidationTestOperationsMixin(object):
    @distributed_trace
    def validation_of_method_parameters(
        self,
        resource_group_name,  # type: str
        id,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> Any
        """Validates input parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :keyword api_version: Api Version. The default value is "1.0.0". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                        "constProperty2": "constant2"  # Default value is "constant2". Constant string2. Has constant value: "constant2".
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                    "constString": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is "constant_string_as_enum". Constant string as Enum. The only acceptable values to pass in are None and "constant_string_as_enum". The default value is None.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6 elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        api_version = kwargs.pop("api_version", "1.0.0")  # type: str

        request = build_validation_of_method_parameters_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            id=id,
            api_version=api_version,
            template_url=self.validation_of_method_parameters.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    validation_of_method_parameters.metadata = {"url": "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"}  # type: ignore

    @distributed_trace
    def validation_of_body(
        self,
        resource_group_name,  # type: str
        id,  # type: int
        body=None,  # type: Any
        **kwargs  # type: Any
    ):
        # type: (...) -> Any
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :param body:
        :type body: Any
        :keyword api_version: Api Version. The default value is "1.0.0". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                        "constProperty2": "constant2"  # Default value is "constant2". Constant string2. Has constant value: "constant2".
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                    "constString": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is "constant_string_as_enum". Constant string as Enum. The only acceptable values to pass in are None and "constant_string_as_enum". The default value is None.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6 elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }

                # response body for status code(s): 200
                response.json() == {
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                        "constProperty2": "constant2"  # Default value is "constant2". Constant string2. Has constant value: "constant2".
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                    "constString": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is "constant_string_as_enum". Constant string as Enum. The only acceptable values to pass in are None and "constant_string_as_enum". The default value is None.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6 elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        api_version = kwargs.pop("api_version", "1.0.0")  # type: str
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if body is not None:
            json = body
        else:
            json = None

        request = build_validation_of_body_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            id=id,
            api_version=api_version,
            content_type=content_type,
            json=json,
            template_url=self.validation_of_body.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    validation_of_body.metadata = {"url": "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"}  # type: ignore

    @distributed_trace
    def get_with_constant_in_path(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """get_with_constant_in_path.

        :keyword constant_param: The default value is "constant". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype constant_param: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        constant_param = kwargs.pop("constant_param", "constant")  # type: str

        request = build_get_with_constant_in_path_request(
            constant_param=constant_param,
            template_url=self.get_with_constant_in_path.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    get_with_constant_in_path.metadata = {"url": "/validation/constantsInPath/{constantParam}/value"}  # type: ignore

    @distributed_trace
    def post_with_constant_in_body(
        self,
        body=None,  # type: Any
        **kwargs  # type: Any
    ):
        # type: (...) -> Any
        """post_with_constant_in_body.

        :param body:
        :type body: Any
        :keyword constant_param: The default value is "constant". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype constant_param: str
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                        "constProperty2": "constant2"  # Default value is "constant2". Constant string2. Has constant value: "constant2".
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                    "constString": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is "constant_string_as_enum". Constant string as Enum. The only acceptable values to pass in are None and "constant_string_as_enum". The default value is None.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6 elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }

                # response body for status code(s): 200
                response.json() == {
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                        "constProperty2": "constant2"  # Default value is "constant2". Constant string2. Has constant value: "constant2".
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                    "constString": "constant",  # Default value is "constant". Constant string. Has constant value: "constant".
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is "constant_string_as_enum". Constant string as Enum. The only acceptable values to pass in are None and "constant_string_as_enum". The default value is None.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6 elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        constant_param = kwargs.pop("constant_param", "constant")  # type: str
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if body is not None:
            json = body
        else:
            json = None

        request = build_post_with_constant_in_body_request(
            constant_param=constant_param,
            content_type=content_type,
            json=json,
            template_url=self.post_with_constant_in_body.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    post_with_constant_in_body.metadata = {"url": "/validation/constantsInPath/{constantParam}/value"}  # type: ignore
