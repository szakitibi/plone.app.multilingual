# -*- coding: utf-8 -*-
import logging

import pkg_resources
from zope.i18nmessageid import MessageFactory

try:
    pkg_resources.get_distribution("Products.LinguaPlone")
except pkg_resources.DistributionNotFound:
    isLPinstalled = False
else:
    isLPinstalled = True

logger = logging.getLogger("plone.app.multilingual")
_ = MessageFactory("plone")
