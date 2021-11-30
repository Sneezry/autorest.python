# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

from ..._vendor import _format_url_section, _get_from_dict

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional, TypeVar

    T = TypeVar("T")
    JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_get_by_pet_id_request(
    pet_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """get pet by id.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param pet_id: Pet id.
    :type pet_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet. Possible values include: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday". Default value: "Friday".
                "IntEnum": "str",  # Required. Possible values include: "1", "2", "3".
                "name": "str"  # Optional. name.
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = '/extensibleenums/pet/{petId}'
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=_headers,
        **kwargs
    )


def build_add_pet_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """add pet.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. pet param.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). pet param.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet. Possible values include: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday". Default value: "Friday".
                "IntEnum": "str",  # Required. Possible values include: "1", "2", "3".
                "name": "str"  # Optional. name.
            }

            # response body for status code(s): 200
            response.json() == {
                "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet. Possible values include: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday". Default value: "Friday".
                "IntEnum": "str",  # Required. Possible values include: "1", "2", "3".
                "name": "str"  # Optional. name.
            }
    """

    _headers = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]

    content_type = kwargs.pop('content_type', _get_from_dict(_headers, 'Content-Type') or None)  # type: Optional[str]

    accept = _get_from_dict(_headers, 'Accept') or "application/json"

    # Construct URL
    url = '/extensibleenums/pet/addPet'

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=_headers,
        **kwargs
    )
