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


class PetFood(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Can take a value of meat, or fish, or plant"""

    MEAT = "meat"
    FISH = "fish"
    PLANT = "plant"


class PetType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Can take a value of dog, or cat, or fish"""

    DOG = "dog"
    CAT = "cat"
    FISH = "fish"
