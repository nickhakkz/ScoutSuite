# -*- coding: utf-8 -*-

import abc

from ScoutSuite.providers.base.configs.resources import SimpleResources
from ScoutSuite.providers.base.configs.resources import CompositeResources


class AzureSimpleResources(SimpleResources, metaclass=abc.ABCMeta):

    async def fetch_all(self, credentials):
        raw_resource = await self.get_resources_from_api(credentials)
        name, resource = self.parse_resource(raw_resource)
        self[name] = resource


class AzureCompositeResources(CompositeResources, metaclass=abc.ABCMeta):

    # TODO: get rid of the credentials.
    async def fetch_children(self, parent, credentials, **kwargs):
        for child_class in self.children:
            child = child_class(**kwargs)
            await child.fetch_all(credentials)
            parent.update(child)