#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = "bibow"

from graphene import ObjectType, String, Decimal, DateTime, List, Field
from .common_object_types import TransactionType


class OrderItemType(ObjectType):
    price = Decimal()
    qty = Decimal()
    sku = String()


class AddressType(ObjectType):
    address = String()
    city = String()
    company = String()
    country = String()
    email = String()
    firstname = String()
    lastname = String()
    postcode = String()
    region = String()
    telephone = String()


class AddressesType(ObjectType):
    billto = Field(AddressType)
    shipto = Field(AddressType)


class OrderDataType(ObjectType):
    tgt_id = String()
    updated_at = DateTime()
    order_status = String()
    addresses = Field(AddressesType)
    items = List(OrderItemType)


class OrderType(ObjectType):
    class Meta:
        interfaces = (TransactionType,)

    data = Field(OrderDataType)
    history = List(OrderDataType)