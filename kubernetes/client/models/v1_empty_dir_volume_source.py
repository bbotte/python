# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1EmptyDirVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, medium=None):
        """
        V1EmptyDirVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'medium': 'str'
        }

        self.attribute_map = {
            'medium': 'medium'
        }

        self._medium = medium

    @property
    def medium(self):
        """
        Gets the medium of this V1EmptyDirVolumeSource.
        What type of storage medium should back this directory. The default is \"\" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir

        :return: The medium of this V1EmptyDirVolumeSource.
        :rtype: str
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """
        Sets the medium of this V1EmptyDirVolumeSource.
        What type of storage medium should back this directory. The default is \"\" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir

        :param medium: The medium of this V1EmptyDirVolumeSource.
        :type: str
        """

        self._medium = medium

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
