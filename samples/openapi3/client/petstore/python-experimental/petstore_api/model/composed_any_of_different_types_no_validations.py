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


class ComposedAnyOfDifferentTypesNoValidations(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        additional_properties = schemas.AnyTypeSchema
        any_of_0 = schemas.DictSchema
        any_of_1 = schemas.DateSchema
        any_of_2 = schemas.DateTimeSchema
        any_of_3 = schemas.BinarySchema
        any_of_4 = schemas.StrSchema
        any_of_5 = schemas.StrSchema
        any_of_6 = schemas.DictSchema
        any_of_7 = schemas.BoolSchema
        any_of_8 = schemas.NoneSchema
        
        
        class any_of_9(
            schemas.ListSchema
        ):
        
        
            class MetaOapg:
                items = schemas.AnyTypeSchema
        any_of_10 = schemas.NumberSchema
        any_of_11 = schemas.Float32Schema
        any_of_12 = schemas.Float64Schema
        any_of_13 = schemas.IntSchema
        any_of_14 = schemas.Int32Schema
        any_of_15 = schemas.Int64Schema
        
        @classmethod
        @property
        @functools.cache
        def any_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.any_of_0,
                cls.any_of_1,
                cls.any_of_2,
                cls.any_of_3,
                cls.any_of_4,
                cls.any_of_5,
                cls.any_of_6,
                cls.any_of_7,
                cls.any_of_8,
                cls.any_of_9,
                cls.any_of_10,
                cls.any_of_11,
                cls.any_of_12,
                cls.any_of_13,
                cls.any_of_14,
                cls.any_of_15,
            ]

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'ComposedAnyOfDifferentTypesNoValidations':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
