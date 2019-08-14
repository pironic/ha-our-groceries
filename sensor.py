"""Support for Our Groceries."""
import logging

from homeassistant.helpers.entity import Entity

from .const import DOMAIN, VERSION, NAME_LONG, PROJECT_URL


_LOGGER = logging.getLogger(__name__)


ATTR_RECIPES = 'recipes'
ATTR_SHOPPING_LISTS = 'shopping_lists'


async def async_setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the OurGroceries sensor platform."""
    _LOGGER.debug('add_entities')
    og = hass.data[DOMAIN]
    add_entities([OurGroceriesSensor(og)], True)


class OurGroceriesSensor(Entity):
    """Representation of an Our Groceries sensor."""

    def __init__(self, og):
        """Initialize the sensor."""
        self._og = og
        self._lists = []

    @property
    def unique_id(self):
        """Return a unique ID to use for this sensor."""
        return (
            "07g5g-74gc-48fd-9b16-c854365f-fd42-4a5vv8-a072-adeh4544cd"
        )

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'our_groceries'

    @property
    def state(self):
        """Return the state of the sensor."""
        shopping_lists = len(self._lists.get('shoppingLists', []))
        recipes = len(self._lists.get('recipes', []))
        return shopping_lists + recipes

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            ATTR_RECIPES: self._lists.get('recipes'),
            ATTR_SHOPPING_LISTS: self._lists.get('shoppingLists')
        }

    @property
    def icon(self):
        """Return the icon to use in the frontend."""
        return 'mdi:format-list-bulleted'

    async def async_update(self):
        """Update data from API."""
        _LOGGER.debug('updating og state')
        self._lists = await self._og.get_my_lists()
    
    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": NAME_LONG,
            "sw_version": VERSION,
            "manufacturer": PROJECT_URL,
        }

