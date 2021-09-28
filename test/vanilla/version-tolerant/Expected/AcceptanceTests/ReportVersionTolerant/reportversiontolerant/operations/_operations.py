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

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_get_report_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    qualifier = kwargs.pop('qualifier', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = '/report'

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if qualifier is not None:
        query_parameters['qualifier'] = _SERIALIZER.query("qualifier", qualifier, 'str')

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


def build_get_optional_report_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    qualifier = kwargs.pop('qualifier', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = '/report/optional'

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if qualifier is not None:
        query_parameters['qualifier'] = _SERIALIZER.query("qualifier", qualifier, 'str')

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
class AutoRestReportServiceOperationsMixin(object):
    @distributed_trace
    def get_report(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Dict[str, int]
        """Get test coverage report.

        :keyword qualifier: If specified, qualifies the generated report further (e.g. '2.7' vs '3.5'
         in for Python). The only effect is, that generators that run all tests several times, can
         distinguish the generated reports.
        :paramtype qualifier: str
        :return: dict mapping str to int
        :rtype: dict[str, int]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "str": 0  # Optional.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Dict[str, int]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        qualifier = kwargs.pop("qualifier", None)  # type: Optional[str]

        request = build_get_report_request(
            qualifier=qualifier,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
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

    @distributed_trace
    def get_optional_report(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Dict[str, int]
        """Get optional test coverage report.

        :keyword qualifier: If specified, qualifies the generated report further (e.g. '2.7' vs '3.5'
         in for Python). The only effect is, that generators that run all tests several times, can
         distinguish the generated reports.
        :paramtype qualifier: str
        :return: dict mapping str to int
        :rtype: dict[str, int]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "str": 0  # Optional.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Dict[str, int]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        qualifier = kwargs.pop("qualifier", None)  # type: Optional[str]

        request = build_get_optional_report_request(
            qualifier=qualifier,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
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
