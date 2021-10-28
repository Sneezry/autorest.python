# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional

from azure.core.rest import HttpRequest
from msrest import Serializer

from ..._vendor import _format_url_section

_SERIALIZER = Serializer()


def _param_not_set(param_dict, rest_api_name_lower):
    return not any(k for k in param_dict if k.lower() == rest_api_name_lower)


def build_get_method_global_valid_request(**kwargs: Any) -> HttpRequest:
    """GET method with api-version modeled in global settings.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: Api Version. The default value is "2015-07-01-preview". Note that
     overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop("api_version", "2015-07-01-preview")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/apiVersion/method/string/none/query/global/2015-07-01-preview")

    # Construct parameters
    query_parameters = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(query_parameters, "api-version"):
        query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_get_method_global_not_provided_valid_request(**kwargs: Any) -> HttpRequest:
    """GET method with api-version modeled in global settings.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: Api Version. The default value is "2015-07-01-preview". Note that
     overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop("api_version", "2015-07-01-preview")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop(
        "template_url", "/azurespecials/apiVersion/method/string/none/query/globalNotProvided/2015-07-01-preview"
    )

    # Construct parameters
    query_parameters = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(query_parameters, "api-version"):
        query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_get_path_global_valid_request(**kwargs: Any) -> HttpRequest:
    """GET method with api-version modeled in global settings.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: Api Version. The default value is "2015-07-01-preview". Note that
     overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop("api_version", "2015-07-01-preview")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/apiVersion/path/string/none/query/global/2015-07-01-preview")

    # Construct parameters
    query_parameters = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(query_parameters, "api-version"):
        query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_get_swagger_global_valid_request(**kwargs: Any) -> HttpRequest:
    """GET method with api-version modeled in global settings.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: Api Version. The default value is "2015-07-01-preview". Note that
     overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop("api_version", "2015-07-01-preview")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/apiVersion/swagger/string/none/query/global/2015-07-01-preview")

    # Construct parameters
    query_parameters = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(query_parameters, "api-version"):
        query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)
