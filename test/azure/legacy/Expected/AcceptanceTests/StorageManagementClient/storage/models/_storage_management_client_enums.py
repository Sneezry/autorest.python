# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AccountStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the status indicating whether the primary location of the storage account is available or
    unavailable.
    """

    AVAILABLE = "Available"
    UNAVAILABLE = "Unavailable"


class AccountType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the account type."""

    STANDARD_LRS = "Standard_LRS"
    STANDARD_ZRS = "Standard_ZRS"
    STANDARD_GRS = "Standard_GRS"
    STANDARD_RAGRS = "Standard_RAGRS"
    PREMIUM_LRS = "Premium_LRS"


class KeyName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    KEY1 = "key1"
    KEY2 = "key2"


class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the status of the storage account at the time the operation was called."""

    CREATING = "Creating"
    RESOLVING_DNS = "ResolvingDNS"
    SUCCEEDED = "Succeeded"


class Reason(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the reason that a storage account name could not be used. The Reason element is only
    returned if NameAvailable is false.
    """

    ACCOUNT_NAME_INVALID = "AccountNameInvalid"
    ALREADY_EXISTS = "AlreadyExists"


class UsageUnit(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the unit of measurement."""

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNTS_PER_SECOND = "CountsPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"
