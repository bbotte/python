# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_replication_controller_list import V1ReplicationControllerList


class TestV1ReplicationControllerList(unittest.TestCase):
    """ V1ReplicationControllerList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ReplicationControllerList(self):
        """
        Test V1ReplicationControllerList
        """
        model = kubernetes.client.models.v1_replication_controller_list.V1ReplicationControllerList()


if __name__ == '__main__':
    unittest.main()
