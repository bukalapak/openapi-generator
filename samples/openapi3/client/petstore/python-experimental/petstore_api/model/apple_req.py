# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401
import uuid  # noqa: F401

from petstore_api import schemas  # noqa: F401


class AppleReq(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "cultivar",
        }
        class properties:
            cultivar = schemas.StrSchema
            mealy = schemas.BoolSchema
        additional_properties = None
    
    cultivar: MetaOapg.properties.cultivar
    mealy: MetaOapg.properties.mealy

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        cultivar: typing.Union[MetaOapg.properties.cultivar, str, ],
        mealy: typing.Union[MetaOapg.properties.mealy, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AppleReq':
        return super().__new__(
            cls,
            *args,
            cultivar=cultivar,
            mealy=mealy,
            _configuration=_configuration,
        )
