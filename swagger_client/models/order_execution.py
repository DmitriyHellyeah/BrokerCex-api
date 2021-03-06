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


class OrderExecution(object):
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
        'account': 'str',
        'action_code': 'str',
        'client_order_id': 'str',
        'execution_code': 'str',
        'filled_quantity': 'float',
        'final_status': 'bool',
        'order_code': 'str',
        'status': 'str',
        'transaction_time': 'datetime',
        'update_order_id': 'int',
        'version': 'int'
    }

    attribute_map = {
        'account': 'account',
        'action_code': 'actionCode',
        'client_order_id': 'clientOrderId',
        'execution_code': 'executionCode',
        'filled_quantity': 'filledQuantity',
        'final_status': 'finalStatus',
        'order_code': 'orderCode',
        'status': 'status',
        'transaction_time': 'transactionTime',
        'update_order_id': 'updateOrderId',
        'version': 'version'
    }

    def __init__(self, account=None, action_code=None, client_order_id=None, execution_code=None, filled_quantity=None, final_status=None, order_code=None, status=None, transaction_time=None, update_order_id=None, version=None):  # noqa: E501
        """OrderExecution - a model defined in Swagger"""  # noqa: E501

        self._account = None
        self._action_code = None
        self._client_order_id = None
        self._execution_code = None
        self._filled_quantity = None
        self._final_status = None
        self._order_code = None
        self._status = None
        self._transaction_time = None
        self._update_order_id = None
        self._version = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if action_code is not None:
            self.action_code = action_code
        if client_order_id is not None:
            self.client_order_id = client_order_id
        if execution_code is not None:
            self.execution_code = execution_code
        if filled_quantity is not None:
            self.filled_quantity = filled_quantity
        if final_status is not None:
            self.final_status = final_status
        if order_code is not None:
            self.order_code = order_code
        if status is not None:
            self.status = status
        if transaction_time is not None:
            self.transaction_time = transaction_time
        if update_order_id is not None:
            self.update_order_id = update_order_id
        if version is not None:
            self.version = version

    @property
    def account(self):
        """Gets the account of this OrderExecution.  # noqa: E501


        :return: The account of this OrderExecution.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this OrderExecution.


        :param account: The account of this OrderExecution.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def action_code(self):
        """Gets the action_code of this OrderExecution.  # noqa: E501


        :return: The action_code of this OrderExecution.  # noqa: E501
        :rtype: str
        """
        return self._action_code

    @action_code.setter
    def action_code(self, action_code):
        """Sets the action_code of this OrderExecution.


        :param action_code: The action_code of this OrderExecution.  # noqa: E501
        :type: str
        """

        self._action_code = action_code

    @property
    def client_order_id(self):
        """Gets the client_order_id of this OrderExecution.  # noqa: E501


        :return: The client_order_id of this OrderExecution.  # noqa: E501
        :rtype: str
        """
        return self._client_order_id

    @client_order_id.setter
    def client_order_id(self, client_order_id):
        """Sets the client_order_id of this OrderExecution.


        :param client_order_id: The client_order_id of this OrderExecution.  # noqa: E501
        :type: str
        """

        self._client_order_id = client_order_id

    @property
    def execution_code(self):
        """Gets the execution_code of this OrderExecution.  # noqa: E501


        :return: The execution_code of this OrderExecution.  # noqa: E501
        :rtype: str
        """
        return self._execution_code

    @execution_code.setter
    def execution_code(self, execution_code):
        """Sets the execution_code of this OrderExecution.


        :param execution_code: The execution_code of this OrderExecution.  # noqa: E501
        :type: str
        """

        self._execution_code = execution_code

    @property
    def filled_quantity(self):
        """Gets the filled_quantity of this OrderExecution.  # noqa: E501


        :return: The filled_quantity of this OrderExecution.  # noqa: E501
        :rtype: float
        """
        return self._filled_quantity

    @filled_quantity.setter
    def filled_quantity(self, filled_quantity):
        """Sets the filled_quantity of this OrderExecution.


        :param filled_quantity: The filled_quantity of this OrderExecution.  # noqa: E501
        :type: float
        """

        self._filled_quantity = filled_quantity

    @property
    def final_status(self):
        """Gets the final_status of this OrderExecution.  # noqa: E501


        :return: The final_status of this OrderExecution.  # noqa: E501
        :rtype: bool
        """
        return self._final_status

    @final_status.setter
    def final_status(self, final_status):
        """Sets the final_status of this OrderExecution.


        :param final_status: The final_status of this OrderExecution.  # noqa: E501
        :type: bool
        """

        self._final_status = final_status

    @property
    def order_code(self):
        """Gets the order_code of this OrderExecution.  # noqa: E501


        :return: The order_code of this OrderExecution.  # noqa: E501
        :rtype: str
        """
        return self._order_code

    @order_code.setter
    def order_code(self, order_code):
        """Sets the order_code of this OrderExecution.


        :param order_code: The order_code of this OrderExecution.  # noqa: E501
        :type: str
        """

        self._order_code = order_code

    @property
    def status(self):
        """Gets the status of this OrderExecution.  # noqa: E501


        :return: The status of this OrderExecution.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrderExecution.


        :param status: The status of this OrderExecution.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def transaction_time(self):
        """Gets the transaction_time of this OrderExecution.  # noqa: E501


        :return: The transaction_time of this OrderExecution.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """Sets the transaction_time of this OrderExecution.


        :param transaction_time: The transaction_time of this OrderExecution.  # noqa: E501
        :type: datetime
        """

        self._transaction_time = transaction_time

    @property
    def update_order_id(self):
        """Gets the update_order_id of this OrderExecution.  # noqa: E501


        :return: The update_order_id of this OrderExecution.  # noqa: E501
        :rtype: int
        """
        return self._update_order_id

    @update_order_id.setter
    def update_order_id(self, update_order_id):
        """Sets the update_order_id of this OrderExecution.


        :param update_order_id: The update_order_id of this OrderExecution.  # noqa: E501
        :type: int
        """

        self._update_order_id = update_order_id

    @property
    def version(self):
        """Gets the version of this OrderExecution.  # noqa: E501


        :return: The version of this OrderExecution.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OrderExecution.


        :param version: The version of this OrderExecution.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(OrderExecution, dict):
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
        if not isinstance(other, OrderExecution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
