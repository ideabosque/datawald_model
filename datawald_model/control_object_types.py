#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

__author__ = "bibow"


from graphene import ObjectType, InputObjectType, String, DateTime, Int, List


class TaskType(ObjectType):
    source = String()
    id = String()
    task_status = String()
    task_note = String()
    updated_at = DateTime()
    ready = Int()


class CutDateType(ObjectType):
    cut_date = DateTime()
    offset = Int()


class EntityType(ObjectType):
    source = String()
    id = String()
    task_note = String()
    task_status = String()
    updated_at = DateTime()


class SyncTaskType(ObjectType):
    task = String()
    id = String()
    source = String()
    target = String()
    table = String()
    cut_date = DateTime()
    start_date = DateTime()
    end_date = DateTime()
    offset = Int()
    sync_note = String()
    sync_status = String()
    entities = List(EntityType)


class EntityInputType(InputObjectType):
    source = String()
    id = String()
    task_note = String()
    task_status = String()
    updated_at = DateTime()
