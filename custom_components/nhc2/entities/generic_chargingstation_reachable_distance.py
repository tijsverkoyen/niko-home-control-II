from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass
from homeassistant.const import UnitOfLength

from ..nhccoco.devices.generic_chargingstation import CocoGenericChargingstation
from ..nhccoco.helpers import to_int_or_none
from .nhc_entity import NHCBaseEntity


class Nhc2GenericChargingstationReachableDistanceEntity(NHCBaseEntity, SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoGenericChargingstation, hub, gateway):
        """Initialize a sensor."""
        super().__init__(device_instance, hub, gateway)

        self._attr_unique_id = device_instance.uuid + '_reachable_distance'

        self._attr_device_class = SensorDeviceClass.DISTANCE
        self._attr_native_value = to_int_or_none(self._device.reachable_distance)
        self._attr_native_unit_of_measurement = UnitOfLength.KILOMETERS
        self._attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def name(self) -> str:
        return 'Reachable Distance'

    @property
    def native_value(self) -> float:
        return to_int_or_none(self._device.reachable_distance)