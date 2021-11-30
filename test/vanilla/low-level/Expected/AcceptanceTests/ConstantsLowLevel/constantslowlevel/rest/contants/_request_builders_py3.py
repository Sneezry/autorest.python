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

from ..._vendor import _format_url_section, _get_from_dict

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_put_no_model_as_string_no_required_two_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putNoModelAsStringNoRequiredTwoValueNoDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_no_model_as_string_no_required_two_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putNoModelAsStringNoRequiredTwoValueDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_no_model_as_string_no_required_one_value_no_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: The default value is "value1".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putNoModelAsStringNoRequiredOneValueNoDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_no_model_as_string_no_required_one_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: The default value is "value1".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putNoModelAsStringNoRequiredOneValueDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_no_model_as_string_required_two_value_no_default_request(*, input: str, **kwargs: Any) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putNoModelAsStringRequiredTwoValueNoDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_no_model_as_string_required_two_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putNoModelAsStringRequiredTwoValueDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_no_model_as_string_required_one_value_no_default_request(**kwargs: Any) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: The default value is "value1". Note that overriding this default value may
     result in unsupported behavior.
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    input = kwargs.pop("input", _get_from_dict(_params, "input") or "value1")  # type: str

    # Construct URL
    url = "/constants/putNoModelAsStringRequiredOneValueNoDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_no_model_as_string_required_one_value_default_request(**kwargs: Any) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: The default value is "value1". Note that overriding this default value may
     result in unsupported behavior.
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    input = kwargs.pop("input", _get_from_dict(_params, "input") or "value1")  # type: str

    # Construct URL
    url = "/constants/putNoModelAsStringRequiredOneValueDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_model_as_string_no_required_two_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putModelAsStringNoRequiredTwoValueNoDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_model_as_string_no_required_two_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putModelAsStringNoRequiredTwoValueDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_model_as_string_no_required_one_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: "value1"
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putModelAsStringNoRequiredOneValueNoDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_model_as_string_no_required_one_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: "value1"
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putModelAsStringNoRequiredOneValueDefault"

    # Construct parameters
    if input is not None:
        _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_model_as_string_required_two_value_no_default_request(*, input: str, **kwargs: Any) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putModelAsStringRequiredTwoValueNoDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_model_as_string_required_two_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putModelAsStringRequiredTwoValueDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_model_as_string_required_one_value_no_default_request(*, input: str, **kwargs: Any) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: "value1"
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putModelAsStringRequiredOneValueNoDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_model_as_string_required_one_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: "value1"
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    # Construct URL
    url = "/constants/putModelAsStringRequiredOneValueDefault"

    # Construct parameters
    _params["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=_params, **kwargs)


def build_put_client_constants_request(**kwargs: Any) -> HttpRequest:
    """Pass constants from the client to this function. Will pass in constant path, query, and header
    parameters.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword header_constant: Constant header property on the client that is a required parameter
     for operation 'constants_putClientConstants'. The default value is True. Note that overriding
     this default value may result in unsupported behavior.
    :paramtype header_constant: bool
    :keyword query_constant: Constant query property on the client that is a required parameter for
     operation 'constants_putClientConstants'. The default value is 100. Note that overriding this
     default value may result in unsupported behavior.
    :paramtype query_constant: int
    :keyword path_constant: Constant path property on the client that is a required parameter for
     operation 'constants_putClientConstants'. The default value is "path". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype path_constant: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    _params = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]

    header_constant = kwargs.pop("header_constant", _get_from_dict(_headers, "header-constant") or True)  # type: bool
    query_constant = kwargs.pop("query_constant", _get_from_dict(_params, "query-constant") or 100)  # type: int
    path_constant = kwargs.pop("path_constant", "path")  # type: str

    # Construct URL
    url = "/constants/clientConstants/{path-constant}"
    path_format_arguments = {
        "path-constant": _SERIALIZER.url("path_constant", path_constant, "str"),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    _params["query-constant"] = _SERIALIZER.query("query_constant", query_constant, "int")

    # Construct headers
    _headers["header-constant"] = _SERIALIZER.header("header_constant", header_constant, "bool")

    return HttpRequest(method="PUT", url=url, params=_params, headers=_headers, **kwargs)
