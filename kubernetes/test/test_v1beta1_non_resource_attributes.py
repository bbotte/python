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
from kubernetes.client.models.v1beta1_non_resource_attributes import V1beta1NonResourceAttributes


class TestV1beta1NonResourceAttributes(unittest.TestCase):
    """ V1beta1NonResourceAttributes unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1NonResourceAttributes(self):
        """
        Test V1beta1NonResourceAttributes
        """
        model = kubernetes.client.models.v1beta1_non_resource_attributes.V1beta1NonResourceAttributes()


if __name__ == '__main__':
    unittest.main()
