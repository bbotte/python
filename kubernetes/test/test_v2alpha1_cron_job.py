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
from kubernetes.client.models.v2alpha1_cron_job import V2alpha1CronJob


class TestV2alpha1CronJob(unittest.TestCase):
    """ V2alpha1CronJob unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV2alpha1CronJob(self):
        """
        Test V2alpha1CronJob
        """
        model = kubernetes.client.models.v2alpha1_cron_job.V2alpha1CronJob()


if __name__ == '__main__':
    unittest.main()
