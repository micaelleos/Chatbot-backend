from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Dict, List, Optional

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import (
    BaseMessage,
    message_to_dict,
    messages_from_dict,
    messages_to_dict,
)

logger = logging.getLogger(__name__)

class StoreServiceChatMessageHistory(BaseChatMessageHistory):
    """Chat message history that stores history in AWS DynamoDB.

    This class expects that a DynamoDB table exists with name `table_name`

    """

    def __init__(
        self,
        table_name: str,
        session_id: str,
        endpoint_url: Optional[str] = None,
        primary_key_name: str = "SessionId",
        key: Optional[Dict[str, str]] = None,
        boto3_session: Optional[Session] = None,
        kms_key_id: Optional[str] = None,
        ttl: Optional[int] = None,
        ttl_key_name: str = "expireAt",
        history_size: Optional[int] = None,
    ):
        if boto3_session:
            client = boto3_session.resource("dynamodb", endpoint_url=endpoint_url)
        else:
            try:
                import boto3
            except ImportError as e:
                raise ImportError(
                    "Unable to import boto3, please install with `pip install boto3`."
                ) from e
            if endpoint_url:
                client = boto3.resource("dynamodb", endpoint_url=endpoint_url)
            else:
                client = boto3.resource("dynamodb")
        self.table = client.Table(table_name)
        self.session_id = session_id
        self.key: Dict = key or {primary_key_name: session_id}
        self.ttl = ttl
        self.ttl_key_name = ttl_key_name
        self.history_size = history_size

    @property
    def messages(self) -> List[BaseMessage]:
        """Retrieve the messages from DynamoDB"""

        response = None
        try:
            response = self.table.get_item(Key=self.key)
        except ClientError as error:
            if error.response["Error"]["Code"] == "ResourceNotFoundException" :
                logger.warning("No record found with session id: %s", self.session_id)
            else:
                logger.error(error)

        if response and "Item" in response:
            items = response["Item"]["History"]
        else:
            items = []

        messages = messages_from_dict(items)
        return messages

    @messages.setter
    def messages(self, messages: List[BaseMessage]) -> None:
        raise NotImplementedError(
            "Direct assignment to 'messages' is not allowed."
            " Use the 'add_messages' instead."
        )

    def add_message(self, message: BaseMessage) -> None:
        """Append the message to the record in DynamoDB"""
        try:
            from botocore.exceptions import ClientError
        except ImportError as e:
            raise ImportError(
                "Unable to import botocore, please install with `pip install botocore`."
            ) from e

        messages = messages_to_dict(self.messages)
        _message = message_to_dict(message)
        messages.append(_message)

        if self.history_size:
            messages = messages[-self.history_size :]

        try:
            self.table.put_item(Item={**self.key, "History": messages})
        except ClientError as err:
            logger.error(err)


    def clear(self) -> None:
        """Clear session memory from DynamoDB"""
        try:
            from botocore.exceptions import ClientError
        except ImportError as e:
            raise ImportError(
                "Unable to import botocore, please install with `pip install botocore`."
            ) from e

        try:
            self.table.delete_item(Key=self.key)
        except ClientError as err:
            logger.error(err)