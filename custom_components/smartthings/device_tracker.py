"""
Support for Samsung SmartTag and SmartTag+ devices in SmartThings integration as device_tracker platform.
"""

import logging
from homeassistant.components.device_tracker import SourceType, TrackerEntity
from .const import DOMAIN
from pysmartthings import Category
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from . import FullDevice, SmartThingsConfigEntry


_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant,
    config_entry: SmartThingsConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
):
    _LOGGER.info("Setting up SmartTag device tracker entities...")
    data = hass.data[DOMAIN][config_entry.entry_id]
    devices = data.devices
    entities = []
    for device_id, full_device in devices.items():
        device = full_device.device
        if getattr(device, "category", None) == Category.BLUETOOTH_TRACKER:
            _LOGGER.info(f"Discovered SmartTag: {device.label or device.name} ({device.device_id})")
            entities.append(SmartTagDeviceTracker(full_device))
    async_add_entities(entities, True)
    _LOGGER.info(f"Added {len(entities)} SmartTag device tracker entities.")

class SmartTagDeviceTracker(TrackerEntity):
    _attr_icon = "mdi:bluetooth"
    _attr_should_poll = False

    def __init__(self, full_device):
        self._full_device = full_device
        device = full_device.device
        self._attr_name = device.label or device.name
        self._attr_unique_id = device.device_id
        self._attr_source_type = SourceType.GPS
        _LOGGER.info(f"Initialized SmartTagDeviceTracker entity: {self._attr_name} ({self._attr_unique_id})")

    @property
    def latitude(self):
        return self._full_device.status.get("latitude")

    @property
    def longitude(self):
        return self._full_device.status.get("longitude")

    @property
    def battery_level(self):
        return self._full_device.status.get("battery")

    @property
    def is_connected(self):
        return self._full_device.online

    @property
    def extra_state_attributes(self):
        # Add any extra attributes you want to expose
        return {}

    async def async_update(self):
        _LOGGER.debug(f"Updating SmartTagDeviceTracker entity: {self._attr_name} ({self._attr_unique_id})")
        # Optionally refresh device status
        pass

    async def async_beep(self):
        _LOGGER.info(f"Beep command sent to SmartTag: {self._attr_name} ({self._attr_unique_id})")
        # If SmartTag supports beeping via SmartThings
        await self._full_device.device.command("beep")
