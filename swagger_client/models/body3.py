# coding: utf-8

"""
    Broker API.

    the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec. There are no TOS at this moment, use at your own risk we take no responsibility  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: support@cexbro.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Body3(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'contingency_type': 'str',
        'orders': 'list[str]'
    }

    attribute_map = {
        'contingency_type': 'contingency_type',
        'orders': 'orders'
    }

    def __init__(self, contingency_type=None, orders=None):  # noqa: E501
        """Body3 - a model defined in Swagger"""  # noqa: E501

        self._contingency_type = None
        self._orders = None
        self.discriminator = None

        if contingency_type is not None:
            self.contingency_type = contingency_type
        if orders is not None:
            self.orders = orders

    @property
    def contingency_type(self):
        """Gets the contingency_type of this Body3.  # noqa: E501

        Contingency type of order group to cancel. Will appeared when create if-then order One of the following values (case-insensitive):  OCO – orders in the group are OCO orders. Once one order gets into a final state, the other ones are cancelled. For this group OPEN position effect and nonzero quantity should be set for both orders. Quantity equal for both orders. Note, OCO orders pair can be either traditional Limit/Stop pair with same side or pair with different sides, like Stop-Buy + Stop+Sell.  IF-THEN – orders in the group are parent and contingents. The first order is considered a parent(IF order) and the other ones become active after parent is filled. IF order should have OPEN position effect and nonzero quantity. THEN order(s) should have CLOSE position effect and either zero quantity (\"position attached\") or quantity, equal by absolute value to IF order. The THEN orders should have opposite SIDE from the IF order.  # noqa: E501

        :return: The contingency_type of this Body3.  # noqa: E501
        :rtype: str
        """
        return self._contingency_type

    @contingency_type.setter
    def contingency_type(self, contingency_type):
        """Sets the contingency_type of this Body3.

        Contingency type of order group to cancel. Will appeared when create if-then order One of the following values (case-insensitive):  OCO – orders in the group are OCO orders. Once one order gets into a final state, the other ones are cancelled. For this group OPEN position effect and nonzero quantity should be set for both orders. Quantity equal for both orders. Note, OCO orders pair can be either traditional Limit/Stop pair with same side or pair with different sides, like Stop-Buy + Stop+Sell.  IF-THEN – orders in the group are parent and contingents. The first order is considered a parent(IF order) and the other ones become active after parent is filled. IF order should have OPEN position effect and nonzero quantity. THEN order(s) should have CLOSE position effect and either zero quantity (\"position attached\") or quantity, equal by absolute value to IF order. The THEN orders should have opposite SIDE from the IF order.  # noqa: E501

        :param contingency_type: The contingency_type of this Body3.  # noqa: E501
        :type: str
        """

        self._contingency_type = contingency_type

    @property
    def orders(self):
        """Gets the orders of this Body3.  # noqa: E501

        Comma-separated list of order codes  # noqa: E501

        :return: The orders of this Body3.  # noqa: E501
        :rtype: list[str]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this Body3.

        Comma-separated list of order codes  # noqa: E501

        :param orders: The orders of this Body3.  # noqa: E501
        :type: list[str]
        """

        self._orders = orders

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Body3, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
