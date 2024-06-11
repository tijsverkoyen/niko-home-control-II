from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.const import UnitOfTime

from ..nhccoco.devices.hvacthermostat_hvac import CocoHvacthermostatHvac
from .nhc_entity import NHCBaseEntity


class Nhc2HvacthermostatHvacOverruleTimeEntity(NHCBaseEntity, SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoHvacthermostatHvac, hub, gateway):
        """Initialize a temperature sensor."""
        super().__init__(device_instance, hub, gateway)

        self._attr_unique_id = device_instance.uuid + '_overrule_time'

        self._attr_device_class = SensorDeviceClass.DURATION
        self._attr_native_value = self._device.overrule_time
        self._attr_native_unit_of_measurement = UnitOfTime.MINUTES

    @property
    def name(self) -> str:
        return 'Overrule time'

    @property
    def native_value(self) -> int:
        return self._device.overrule_time
