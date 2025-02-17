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

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional, TypeVar

    T = TypeVar("T")
    JSONType = Any

_SERIALIZER = Serializer()

# fmt: off

def build_get_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get complex types that extend others.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "breed": "str",  # Optional.
                "color": "str",  # Optional.
                "hates": [
                    {
                        "food": "str",  # Optional.
                        "id": 0,  # Optional.
                        "name": "str"  # Optional.
                    }
                ],
                "id": 0,  # Optional.
                "name": "str"  # Optional.
            }
    """

    accept = "application/json"
    # Construct URL
    url = '/complex/inheritance/valid'

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_put_valid_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put complex types that extend others.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Please put a siamese with id=2, name="Siameee",
     color=green, breed=persion, which hates 2 dogs, the 1st one named "Potato" with id=1 and
     food="tomato", and the 2nd one named "Tomato" with id=-1 and food="french fries".
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Please put a siamese with id=2, name="Siameee", color=green,
     breed=persion, which hates 2 dogs, the 1st one named "Potato" with id=1 and food="tomato", and
     the 2nd one named "Tomato" with id=-1 and food="french fries".
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "breed": "str",  # Optional.
                "color": "str",  # Optional.
                "hates": [
                    {
                        "food": "str",  # Optional.
                        "id": 0,  # Optional.
                        "name": "str"  # Optional.
                    }
                ],
                "id": 0,  # Optional.
                "name": "str"  # Optional.
            }
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = '/complex/inheritance/valid'

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **kwargs
    )
