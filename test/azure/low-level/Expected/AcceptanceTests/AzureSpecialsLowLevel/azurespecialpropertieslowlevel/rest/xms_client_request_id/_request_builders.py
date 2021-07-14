# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

_SERIALIZER = Serializer()

# fmt: off

def build_get_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get method that overwrites x-ms-client-request header with value
    9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = kwargs.pop("template_url", '/azurespecials/overwrite/x-ms-client-request-id/method/')

    return HttpRequest(
        method="GET",
        url=url,
        **kwargs
    )


def build_param_get_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get method that overwrites x-ms-client-request header with value
    9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder into your
    code flow.

    :keyword x_ms_client_request_id: This should appear as a method parameter, use value
     '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'.
    :paramtype x_ms_client_request_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    x_ms_client_request_id = kwargs.pop('x_ms_client_request_id')  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/azurespecials/overwrite/x-ms-client-request-id/via-param/method/')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['x-ms-client-request-id'] = _SERIALIZER.header("x_ms_client_request_id", x_ms_client_request_id, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )
