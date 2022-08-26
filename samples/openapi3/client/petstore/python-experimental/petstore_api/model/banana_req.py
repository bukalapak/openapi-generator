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


class BananaReq(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "lengthCm",
        }
        class properties:
            lengthCm = schemas.NumberSchema
            sweet = schemas.BoolSchema
        additional_properties = None
    
    lengthCm: MetaOapg.properties.lengthCm
    sweet: MetaOapg.properties.sweet

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        lengthCm: typing.Union[MetaOapg.properties.lengthCm, decimal.Decimal, int, float, ],
        sweet: typing.Union[MetaOapg.properties.sweet, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'BananaReq':
        return super().__new__(
            cls,
            *args,
            lengthCm=lengthCm,
            sweet=sweet,
            _configuration=_configuration,
        )
