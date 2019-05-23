# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from azure.core import HttpResponseError


class CloudError(Model):
    """CloudError.

    :param status:
    :type status: int
    :param message:
    :type message: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, status: int=None, message: str=None, **kwargs) -> None:
        super(CloudError, self).__init__(**kwargs)
        self.status = status
        self.message = message


class CloudErrorException(HttpResponseError):
    """Server responsed with exception of type: 'CloudError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, response, deserialize, *args):

      model_name = 'CloudError'
      self.error = deserialize(model_name, response)
      if self.error is None:
          self.error = deserialize.dependencies[model_name]()
      super(CloudErrorException, self).__init__(response=response)


class HttpResponseError(Model):
    """HttpResponseError.
    """

    _attribute_map = {
    }


class OperationResult(Model):
    """OperationResult.

    :param status: The status of the request. Possible values include:
     'Succeeded', 'Failed', 'canceled', 'Accepted', 'Creating', 'Created',
     'Updating', 'Updated', 'Deleting', 'Deleted', 'OK'
    :type status: str or ~lro.models.enum
    :param error:
    :type error: ~lro.models.OperationResultError
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'error': {'key': 'error', 'type': 'OperationResultError'},
    }

    def __init__(self, *, status=None, error=None, **kwargs) -> None:
        super(OperationResult, self).__init__(**kwargs)
        self.status = status
        self.error = error


class OperationResultError(Model):
    """OperationResultError.

    :param code: The error code for an operation failure
    :type code: int
    :param message: The detailed arror message
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: int=None, message: str=None, **kwargs) -> None:
        super(OperationResultError, self).__init__(**kwargs)
        self.code = code
        self.message = message


class Resource(Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar type: Resource Type
    :vartype type: str
    :param tags:
    :type tags: dict[str, str]
    :param location: Resource Location
    :type location: str
    :ivar name: Resource Name
    :vartype name: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, tags=None, location: str=None, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.tags = tags
        self.location = location
        self.name = None


class Product(Resource):
    """Product.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar type: Resource Type
    :vartype type: str
    :param tags:
    :type tags: dict[str, str]
    :param location: Resource Location
    :type location: str
    :ivar name: Resource Name
    :vartype name: str
    :param provisioning_state:
    :type provisioning_state: str
    :ivar provisioning_state_values: Possible values include: 'Succeeded',
     'Failed', 'canceled', 'Accepted', 'Creating', 'Created', 'Updating',
     'Updated', 'Deleting', 'Deleted', 'OK'
    :vartype provisioning_state_values: str or ~lro.models.enum
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'provisioning_state_values': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'provisioning_state_values': {'key': 'properties.provisioningStateValues', 'type': 'str'},
    }

    def __init__(self, *, tags=None, location: str=None, provisioning_state: str=None, **kwargs) -> None:
        super(Product, self).__init__(tags=tags, location=location, **kwargs)
        self.provisioning_state = provisioning_state
        self.provisioning_state_values = None


class Sku(Model):
    """Sku.

    :param name:
    :type name: str
    :param id:
    :type id: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, id: str=None, **kwargs) -> None:
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.id = id


class SubResource(Model):
    """SubResource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Sub Resource Id
    :vartype id: str
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(SubResource, self).__init__(**kwargs)
        self.id = None


class SubProduct(SubResource):
    """SubProduct.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Sub Resource Id
    :vartype id: str
    :param provisioning_state:
    :type provisioning_state: str
    :ivar provisioning_state_values: Possible values include: 'Succeeded',
     'Failed', 'canceled', 'Accepted', 'Creating', 'Created', 'Updating',
     'Updated', 'Deleting', 'Deleted', 'OK'
    :vartype provisioning_state_values: str or ~lro.models.enum
    """

    _validation = {
        'id': {'readonly': True},
        'provisioning_state_values': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'provisioning_state_values': {'key': 'properties.provisioningStateValues', 'type': 'str'},
    }

    def __init__(self, *, provisioning_state: str=None, **kwargs) -> None:
        super(SubProduct, self).__init__(**kwargs)
        self.provisioning_state = provisioning_state
        self.provisioning_state_values = None
