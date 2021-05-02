#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = "bibow"

from graphene import Interface, String, DateTime


class TransactionType(Interface):
    id = String()
    source = String()
    src_id = String()
    tgt_id = String()
    tx_type = String()
    created_at = DateTime()
    updated_at = DateTime()
    tx_note = String()
    tx_status = String()