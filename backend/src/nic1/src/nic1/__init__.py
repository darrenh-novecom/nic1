"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "nic1"

_ = MessageFactory("nic1")

logger = logging.getLogger("nic1")
