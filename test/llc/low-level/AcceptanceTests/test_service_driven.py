
# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import pytest

from llcservicedriveninitiallowlevel import LLCClient as LLCClientInitial
from llcservicedrivenupdateonelowlevel import LLCClient as LLCClientUpdateOne

from llcservicedriveninitiallowlevel.rest import params as params_initial
from llcservicedrivenupdateonelowlevel.rest import params as params_update_one


@pytest.fixture
def initial_client():
    with LLCClientInitial() as client:
        yield client

@pytest.fixture
def update_one_client():
    with LLCClientUpdateOne() as client:
        yield client

@pytest.fixture
def initial_send_request(initial_client, base_send_request):
    def _send_request(request):
        return base_send_request(initial_client, request)
    return _send_request

@pytest.fixture
def update_one_send_request(update_one_client, base_send_request):
    def _send_request(request):
        return base_send_request(update_one_client, request)
    return _send_request


def test_required_to_optional(initial_send_request, update_one_send_request):
    request = params_initial.build_get_required_request(parameter="foo")
    initial_send_request(request)

    request = params_update_one.build_get_required_request(parameter="foo", new_parameter="bar")
    update_one_send_request(request)
