# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, TypeVar

from azure.core.rest import HttpRequest
from msrest import Serializer

from ..._vendor import _format_url_section, _get_from_dict

T = TypeVar("T")
JSONType = Any

_SERIALIZER = Serializer()


def build_post_required_request(
    path: str,
    *,
    json: JSONType = None,
    content: Any = None,
    custom_header: Optional[str] = None,
    query: Optional[int] = 30,
    **kwargs: Any
) -> HttpRequest:
    """Post a bunch of required parameters grouped.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param path: Path parameter.
    :type path: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input).
    :paramtype content: any
    :keyword custom_header:
    :paramtype custom_header: str
    :keyword query: Query parameter with default.
    :paramtype query: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = 0  # Optional.
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop("content_type", _get_from_dict(_headers, "Content-Type") or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/parameterGrouping/postRequired/{path}"
    path_format_arguments = {
        "path": _SERIALIZER.url("path", path, "str"),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    if query is not None:
        _params["query"] = _SERIALIZER.query("query", query, "int")

    # Construct headers
    if custom_header is not None:
        _headers["customHeader"] = _SERIALIZER.header("custom_header", custom_header, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=_params, headers=_headers, json=json, content=content, **kwargs)


def build_post_optional_request(
    *, custom_header: Optional[str] = None, query: Optional[int] = 30, **kwargs: Any
) -> HttpRequest:
    """Post a bunch of optional parameters grouped.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword custom_header:
    :paramtype custom_header: str
    :keyword query: Query parameter with default.
    :paramtype query: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/parameterGrouping/postOptional"

    # Construct parameters
    if query is not None:
        _params["query"] = _SERIALIZER.query("query", query, "int")

    # Construct headers
    if custom_header is not None:
        _headers["customHeader"] = _SERIALIZER.header("custom_header", custom_header, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=_params, headers=_headers, **kwargs)


def build_post_reserved_words_request(
    *, from_parameter: Optional[str] = None, accept_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    """Post a grouped parameters with reserved words.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword from_parameter: 'from' is a reserved word. Pass in 'bob' to pass.
    :paramtype from_parameter: str
    :keyword accept_parameter: 'accept' is a reserved word. Pass in 'yes' to pass.
    :paramtype accept_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/parameterGrouping/postReservedWords"

    # Construct parameters
    if from_parameter is not None:
        _params["from"] = _SERIALIZER.query("from_parameter", from_parameter, "str")
    if accept_parameter is not None:
        _params["accept"] = _SERIALIZER.query("accept_parameter", accept_parameter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=_params, headers=_headers, **kwargs)


def build_post_multi_param_groups_request(
    *,
    header_one: Optional[str] = None,
    query_one: Optional[int] = 30,
    header_two: Optional[str] = None,
    query_two: Optional[int] = 30,
    **kwargs: Any
) -> HttpRequest:
    """Post parameters from multiple different parameter groups.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword header_one:
    :paramtype header_one: str
    :keyword query_one: Query parameter with default.
    :paramtype query_one: int
    :keyword header_two:
    :paramtype header_two: str
    :keyword query_two: Query parameter with default.
    :paramtype query_two: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/parameterGrouping/postMultipleParameterGroups"

    # Construct parameters
    if query_one is not None:
        _params["query-one"] = _SERIALIZER.query("query_one", query_one, "int")
    if query_two is not None:
        _params["query-two"] = _SERIALIZER.query("query_two", query_two, "int")

    # Construct headers
    if header_one is not None:
        _headers["header-one"] = _SERIALIZER.header("header_one", header_one, "str")
    if header_two is not None:
        _headers["header-two"] = _SERIALIZER.header("header_two", header_two, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=_params, headers=_headers, **kwargs)


def build_post_shared_parameter_group_object_request(
    *, header_one: Optional[str] = None, query_one: Optional[int] = 30, **kwargs: Any
) -> HttpRequest:
    """Post parameters with a shared parameter group object.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword header_one:
    :paramtype header_one: str
    :keyword query_one: Query parameter with default.
    :paramtype query_one: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, "Accept") or "application/json"

    # Construct URL
    url = "/parameterGrouping/sharedParameterGroupObject"

    # Construct parameters
    if query_one is not None:
        _params["query-one"] = _SERIALIZER.query("query_one", query_one, "int")

    # Construct headers
    if header_one is not None:
        _headers["header-one"] = _SERIALIZER.header("header_one", header_one, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=_params, headers=_headers, **kwargs)
