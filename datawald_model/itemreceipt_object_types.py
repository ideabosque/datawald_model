#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = "bibow"

from graphene import (
    ObjectType,
    String,
    Decimal,
    DateTime,
    List,
    Field,
    DateTime,
)
from .common_object_types import TransactionType


class ItemreceiptItemType(ObjectType):
    internal_id = String()
    item_no = String()
    qty = Decimal()


class ShipToType(ObjectType):
    address = String()
    city = String()
    contact = String()
    country_code = String()
    name = String()
    shipping = String()
    state = String()
    zip = String()


class ItemreceiptDataType(ObjectType):
    tgt_id = String()
    updated_at = DateTime()
    internal_id = String()
    items = List(ItemreceiptItemType)
    key = String()
    order_date = String()
    ref_no = List(String)
    ship_to = Field(ShipToType)
    status = String()
    tran_ids = List(String)
    update_date = String()


class ItemreceiptType(ObjectType):
    class Meta:
        interfaces = (TransactionType,)

    data = Field(ItemreceiptDataType)
    history = List(ItemreceiptDataType)