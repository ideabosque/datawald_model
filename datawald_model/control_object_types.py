#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = "bibow"


from graphene import ObjectType, String, DateTime, Int


class TaskType(ObjectType):
    source = String()
    id = String()
    task_status = String()
    task_note = String()
    updated_at = DateTime()
    ready = Int()