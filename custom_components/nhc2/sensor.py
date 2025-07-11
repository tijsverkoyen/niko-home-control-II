import logging

from homeassistant.const import CONF_USERNAME

from .nhccoco.coco import CoCo

from .entities.accesscontrol_action_basicstate import Nhc2AccesscontrolActionBasicStateEntity
from .entities.audiocontrol_action_speaker import Nhc2AudiocontrolActionSpeakerEntity
from .entities.alarms_action_basicstate import Nhc2AlarmsActionBasicStateEntity
from .entities.bellbutton_action_basicstate import Nhc2BellbuttonActionBasicStateEntity
from .entities.electricity_clamp_centralmeter_electrical_power import \
    Nhc2ElectricityClampCentralmeterElectricalPowerEntity
from .entities.electricity_clamp_centralmeter_electrical_power1 import \
    Nhc2ElectricityClampCentralmeterElectricalPower1Entity
from .entities.electricity_clamp_centralmeter_electrical_power2 import \
    Nhc2ElectricityClampCentralmeterElectricalPower2Entity
from .entities.electricity_clamp_centralmeter_electrical_power3 import \
    Nhc2ElectricityClampCentralmeterElectricalPower3Entity
from .entities.electricity_clamp_centralmeter_electrical_power_consumption import \
    Nhc2ElectricityClampCentralmeterElectricalPowerConsumptionEntity
from .entities.electricity_clamp_centralmeter_electrical_power_production import \
    Nhc2ElectricityClampCentralmeterElectricalPowerProductionEntity
from .entities.electricity_clamp_centralmeter_clamp_type import Nhc2ElectricityClampCentralmeterClampTypeEntity
from .entities.electricity_clamp_centralmeter_flow import Nhc2ElectricityClampCentralmeterFlowEntity
from .entities.electricity_clamp_centralmeter_inverter_type import Nhc2ElectricityClampCentralmeterInverterTypeEntity
from .entities.electricity_clamp_centralmeter_segment import Nhc2ElectricityClampCentralmeterSegmentEntity
from .entities.garagedoor_action_basicstate import Nhc2GaragedoorActionBasicStateEntity
from .entities.generic_chargingstation_charging_status import Nhc2GenericChargingstationChargingStatusEntity
from .entities.generic_chargingstation_coupling_status import Nhc2GenericChargingstationCouplingStatusEntity
from .entities.generic_chargingstation_electrical_power import Nhc2GenericChargingstationElectricalPowerEntity
from .entities.generic_chargingstation_ev_status import Nhc2GenericChargingstationEvStatusEntity
from .entities.generic_chargingstation_next_charging_time import Nhc2GenericChargingstationNextChargingTimeEntity
from .entities.generic_domestichotwaterunit_coupling_status import Nhc2GenericDomestichotwaterunitCouplingStatusEntity
from .entities.generic_energyhome_electrical_power_consumption import \
    Nhc2GenericEnergyhomeElectricalPowerConsumptionEntity
from .entities.generic_energyhome_electrical_power_from_grid import Nhc2GenericEnergyhomeElectricalPowerFromGridEntity
from .entities.generic_energyhome_electrical_power_production import \
    Nhc2GenericEnergyhomeElectricalPowerProductionEntity
from .entities.generic_energyhome_electrical_power_self_consumption import \
    Nhc2GenericEnergyhomeElectricalPowerSelfConsumptionEntity
from .entities.generic_energyhome_electrical_power_to_grid import Nhc2GenericEnergyhomeElectricalPowerToGridEntity
from .entities.generic_fan_co2 import Nhc2GenericFanCo2Entity
from .entities.generic_fan_coupling_status import Nhc2GenericFanCouplingStatusEntity
from .entities.generic_fan_humidity import Nhc2GenericFanHumidityEntity
from .entities.generic_hvac_coupling_status import Nhc2GenericHvacCouplingStatusEntity
from .entities.generic_inverter_coupling_status import Nhc2GenericInverterCouplingStatusEntity
from .entities.generic_inverter_electrical_power_production import Nhc2GenericInverterElectricalPowerProductionEntity
from .entities.generic_smartplug_electrical_power import Nhc2GenericSmartplugElectricalPowerEntity
from .entities.generic_thermometer_ambient_temperature import Nhc2GenericThermometerAmbientTemperatureEntity
from .entities.hvacthermostat_hvac_setpoint_temperature import Nhc2HvacthermostatHvacSetpointTemperatureEntity
from .entities.hvacthermostat_hvac_overrule_setpoint import Nhc2HvacthermostatHvacOverruleSetpointEntity
from .entities.hvacthermostat_hvac_overrule_time import Nhc2HvacthermostatHvacOverruleTimeEntity
from .entities.motor_action_last_direction import Nhc2MotorActionLastDirectionEntity
from .entities.naso_smartplug_electrical_power import Nhc2NasoSmartplugElectricalPowerEntity
from .entities.playerstatus_action_feedback_message import Nhc2PlayerstatusActionFeedbackMessageEntity
from .entities.reynaers_action_status import Nhc2ReynaersActionStatusEntity
from .entities.robinsip_videodoorstation_call_status import Nhc2RobinsipVideodoorstationCallStatusEntity
from .entities.robinsip_videodoorstation_ip_address import Nhc2RobinsipVideodoorstationIpAddressEntity
from .entities.robinsip_videodoorstation_status import Nhc2RobinsipVideodoorstationStatusEntity
from .entities.simulation_action_basicstate import Nhc2SimulationActionBasicStateEntity
from .entities.thermostat_hvac_setpoint_temperature import Nhc2ThermostatHvacSetpointTemperatureEntity
from .entities.thermostat_hvac_overrule_time import Nhc2ThermostatHvacOverruleTimeEntity
from .entities.thermostat_hvac_overrule_setpoint import Nhc2ThermostatHvacOverruleSetpointEntity
from .entities.thermostat_thermostat_setpoint_temperature import Nhc2ThermostatThermostatSetpointTemperatureEntity
from .entities.thermostat_thermostat_overrule_time import Nhc2ThermostatThermostatOverruleTimeEntity
from .entities.thermostat_thermostat_overrule_setpoint import Nhc2ThermostatThermostatOverruleSetpointEntity
from .entities.thermoswitchx_multisensor_ambient_temperature import Nhc2ThermoswitchxMultisensorAmbientTemperatureEntity
from .entities.thermoswitchx_multisensor_heat_index import Nhc2ThermoswitchxMultisensorHeatIndexEntity
from .entities.thermoswitchx_multisensor_humidity import Nhc2ThermoswitchxMultisensorHumidityEntity
from .entities.velux_action_feedback import Nhc2VeluxActionFeedbackEntity
from .entities.virtual_hvac_setpoint_temperature import Nhc2VirtualHvacSetpointTemperatureEntity
from .entities.virtual_hvac_overrule_time import Nhc2VirtualHvacOverruleTimeEntity
from .entities.virtual_hvac_overrule_setpoint import Nhc2VirtualHvacOverruleSetpointEntity
from .nhccoco.devices.accesscontrol_action import CocoAccesscontrolAction
from .nhccoco.devices.audiocontrol_action import CocoAudiocontrolAction
from .nhccoco.devices.alarms_action import CocoAlarmsAction
from .nhccoco.devices.battery_clamp_centralmeter import CocoBatteryClampCentralmeter
from .nhccoco.devices.bellbutton_action import CocoBellbuttonAction
from .nhccoco.devices.generic_chargingstation import CocoGenericChargingstation
from .nhccoco.devices.electricity_clamp_centralmeter import CocoElectricityClampCentralmeter
from .nhccoco.devices.gate_action import CocoGateAction
from .nhccoco.devices.garagedoor_action import CocoGaragedoorAction
from .nhccoco.devices.generic_domestichotwaterunit import CocoGenericDomestichotwaterunit
from .nhccoco.devices.generic_energyhome import CocoGenericEnergyhome
from .nhccoco.devices.generic_fan import CocoGenericFan
from .nhccoco.devices.generic_hvac import CocoGenericHvac
from .nhccoco.devices.generic_inverter import CocoGenericInverter
from .nhccoco.devices.generic_smartplug import CocoGenericSmartplug
from .nhccoco.devices.generic_thermometer import CocoGenericThermometer
from .nhccoco.devices.hvacthermostat_hvac import CocoHvacthermostatHvac
from .nhccoco.devices.naso_smartplug import CocoNasoSmartplug
from .nhccoco.devices.playerstatus_action import CocoPlayerstatusAction
from .nhccoco.devices.reynaers_action import CocoReynaersAction
from .nhccoco.devices.robinsip_videodoorstation import CocoRobinsipVideodoorstation
from .nhccoco.devices.rolldownshutter_action import CocoRolldownshutterAction
from .nhccoco.devices.simulation_action import CocoSimulationAction
from .nhccoco.devices.sunblind_action import CocoSunblindAction
from .nhccoco.devices.thermostat_hvac import CocoThermostatHvac
from .nhccoco.devices.thermostat_thermostat import CocoThermostatThermostat
from .nhccoco.devices.thermoswitchx_multisensor import CocoThermoswitchxMultisensor
from .nhccoco.devices.touchswitch_hvac import CocoTouchswitchHvac
from .nhccoco.devices.velux_action import CocoVeluxAction
from .nhccoco.devices.venetianblind_action import CocoVenetianblindAction
from .nhccoco.devices.virtual_hvac import CocoVirtualHvac
from .nhccoco.devices.virtual_thermostat import CocoVirtualThermostat

from .const import DOMAIN, KEY_GATEWAY

KEY_ENTITY = 'nhc2_sensors'

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, config_entry, async_add_entities):
    _LOGGER.info('Configuring sensors')

    hass.data.setdefault(KEY_ENTITY, {})[config_entry.entry_id] = []

    gateway: CoCo = hass.data[KEY_GATEWAY][config_entry.entry_id]
    hub = (DOMAIN, config_entry.data[CONF_USERNAME])

    device_instances = gateway.get_device_instances(CocoAccesscontrolAction)
    _LOGGER.info('→ Found %s NHC Access Control Actions', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            if device_instance.supports_basicstate:
                entities.append(Nhc2AccesscontrolActionBasicStateEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoAudiocontrolAction)
    _LOGGER.info('→ Found %s NHC Audio Control Actions', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2AudiocontrolActionSpeakerEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoAlarmsAction)
    _LOGGER.info('→ Found %s NHC Basic Alarm Actions', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2AlarmsActionBasicStateEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoBellbuttonAction)
    _LOGGER.info('→ Found %s NHC BellButton Actions', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2BellbuttonActionBasicStateEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoGaragedoorAction)
    _LOGGER.info('→ Found %s NHC Garage Door Actions', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2GaragedoorActionBasicStateEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoHvacthermostatHvac)
    _LOGGER.info('→ Found %s NHC HVAC Thermostats', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2HvacthermostatHvacSetpointTemperatureEntity(device_instance, hub, gateway))
            entities.append(Nhc2HvacthermostatHvacOverruleTimeEntity(device_instance, hub, gateway))
            entities.append(Nhc2HvacthermostatHvacOverruleSetpointEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoThermostatHvac)
    _LOGGER.info('→ Found %s NHC Thermostat (thermostat/touchswitch)', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2ThermostatHvacSetpointTemperatureEntity(device_instance, hub, gateway))

            if device_instance.supports_overrule_setpoint:
                entities.append(Nhc2ThermostatHvacOverruleSetpointEntity(device_instance, hub, gateway))

            if device_instance.supports_overrule_time:
                entities.append(Nhc2ThermostatHvacOverruleTimeEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoThermostatThermostat)
    _LOGGER.info('→ Found %s NHC Touch Switch', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2ThermostatThermostatSetpointTemperatureEntity(device_instance, hub, gateway))
            entities.append(Nhc2ThermostatThermostatOverruleSetpointEntity(device_instance, hub, gateway))
            entities.append(Nhc2ThermostatThermostatOverruleTimeEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoGateAction)
    device_instances += gateway.get_device_instances(CocoRolldownshutterAction)
    device_instances += gateway.get_device_instances(CocoSunblindAction)
    device_instances += gateway.get_device_instances(CocoVenetianblindAction)
    _LOGGER.info('→ Found %s NHC Motor Actions', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            if device_instance.supports_last_direction:
                entities.append(Nhc2MotorActionLastDirectionEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoSimulationAction)
    _LOGGER.info('→ Found %s NHC Presence Simulation Actions', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2SimulationActionBasicStateEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoReynaersAction)
    _LOGGER.info('→ Found %s NHC Reynaers Actions', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2ReynaersActionStatusEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoVeluxAction)
    _LOGGER.info('→ Found %s NHC Velux Actions', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            if device_instance.supports_feedback:
                entities.append(Nhc2VeluxActionFeedbackEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoNasoSmartplug)
    _LOGGER.info('→ Found %s NHC Zigbee Smart plugs', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2NasoSmartplugElectricalPowerEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoGenericSmartplug)
    _LOGGER.info('→ Found %s Generic Zigbee Smart plugs', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2GenericSmartplugElectricalPowerEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoElectricityClampCentralmeter)
    _LOGGER.info('→ Found %s Battery Metering Clamp/Electricity Metering modules', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            if device_instance.supports_electrical_power:
                entities.append(Nhc2ElectricityClampCentralmeterElectricalPowerEntity(device_instance, hub, gateway))
            if device_instance.supports_electrical_power1:
                entities.append(Nhc2ElectricityClampCentralmeterElectricalPower1Entity(device_instance, hub, gateway))
            if device_instance.supports_electrical_power2:
                entities.append(Nhc2ElectricityClampCentralmeterElectricalPower2Entity(device_instance, hub, gateway))
            if device_instance.supports_electrical_power3:
                entities.append(Nhc2ElectricityClampCentralmeterElectricalPower3Entity(device_instance, hub, gateway))
            entities.append(
                Nhc2ElectricityClampCentralmeterElectricalPowerConsumptionEntity(device_instance, hub, gateway)
            )
            entities.append(
                Nhc2ElectricityClampCentralmeterElectricalPowerProductionEntity(device_instance, hub, gateway)
            )
            if device_instance.supports_flow:
                entities.append(Nhc2ElectricityClampCentralmeterFlowEntity(device_instance, hub, gateway))
            if device_instance.supports_segment:
                entities.append(Nhc2ElectricityClampCentralmeterSegmentEntity(device_instance, hub, gateway))
            if device_instance.supports_clamp_type:
                entities.append(Nhc2ElectricityClampCentralmeterClampTypeEntity(device_instance, hub, gateway))
            if device_instance.supports_inverter_type:
                entities.append(Nhc2ElectricityClampCentralmeterInverterTypeEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoGenericEnergyhome)
    _LOGGER.info('→ Found %s Energy Home\'s', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            if device_instance.supports_electrical_power_to_grid:
                entities.append(Nhc2GenericEnergyhomeElectricalPowerToGridEntity(device_instance, hub, gateway))
            if device_instance.supports_electrical_power_from_grid:
                entities.append(Nhc2GenericEnergyhomeElectricalPowerFromGridEntity(device_instance, hub, gateway))
            if device_instance.supports_electrical_power_production:
                entities.append(Nhc2GenericEnergyhomeElectricalPowerProductionEntity(device_instance, hub, gateway))
            if device_instance.supports_electrical_power_self_consumption:
                entities.append(
                    Nhc2GenericEnergyhomeElectricalPowerSelfConsumptionEntity(device_instance, hub, gateway)
                )
            if device_instance.supports_electrical_power_consumption:
                entities.append(Nhc2GenericEnergyhomeElectricalPowerConsumptionEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoGenericFan)
    _LOGGER.info('→ Found %s Generic Ventilation Implementation', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            if device_instance.supports_co2:
                entities.append(Nhc2GenericFanCo2Entity(device_instance, hub, gateway))
            if device_instance.supports_coupling_status:
                entities.append(Nhc2GenericFanCouplingStatusEntity(device_instance, hub, gateway))
            if device_instance.supports_humidity:
                entities.append(Nhc2GenericFanHumidityEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoGenericHvac)
    _LOGGER.info('→ Found %s Generic Heating/Cooling Implementations', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            if device_instance.supports_coupling_status:
                entities.append(Nhc2GenericHvacCouplingStatusEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoGenericDomestichotwaterunit)
    _LOGGER.info('→ Found %s Generic Warm Water Implementations', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            if device_instance.supports_coupling_status:
                entities.append(Nhc2GenericDomestichotwaterunitCouplingStatusEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoPlayerstatusAction)
    _LOGGER.info('→ Found %s NHC Player status action', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2PlayerstatusActionFeedbackMessageEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoThermoswitchxMultisensor)
    _LOGGER.info('→ Found %s NHC Thermo switch', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            if device_instance.supports_heat_index:
                entities.append(Nhc2ThermoswitchxMultisensorHeatIndexEntity(device_instance, hub, gateway))

            if device_instance.supports_ambient_temperature:
                entities.append(Nhc2ThermoswitchxMultisensorAmbientTemperatureEntity(device_instance, hub, gateway))

            if device_instance.supports_humidity:
                entities.append(Nhc2ThermoswitchxMultisensorHumidityEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoVirtualHvac)
    device_instances += gateway.get_device_instances(CocoVirtualThermostat)
    _LOGGER.info('→ Found %s NHC Virtual Thermostat, Virtual Thermostat', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2VirtualHvacSetpointTemperatureEntity(device_instance, hub, gateway))

            if device_instance.supports_overrule_time:
                entities.append(Nhc2VirtualHvacOverruleTimeEntity(device_instance, hub, gateway))

            if device_instance.supports_overrule_setpoint:
                entities.append(Nhc2VirtualHvacOverruleSetpointEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoRobinsipVideodoorstation)
    _LOGGER.info('→ Found %s Robinsip Videodoorstations (undocumented)', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2RobinsipVideodoorstationCallStatusEntity(device_instance, hub, gateway, 1))
            entities.append(Nhc2RobinsipVideodoorstationIpAddressEntity(device_instance, hub, gateway))
            entities.append(Nhc2RobinsipVideodoorstationStatusEntity(device_instance, hub, gateway))

            if device_instance.supports_call_status_02:
                entities.append(Nhc2RobinsipVideodoorstationCallStatusEntity(device_instance, hub, gateway, 2))
            if device_instance.supports_call_status_03:
                entities.append(Nhc2RobinsipVideodoorstationCallStatusEntity(device_instance, hub, gateway, 3))
            if device_instance.supports_call_status_04:
                entities.append(Nhc2RobinsipVideodoorstationCallStatusEntity(device_instance, hub, gateway, 4))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoGenericInverter)
    _LOGGER.info('→ Found %s Generic Inverter Implementations (undocumented)', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            if device_instance.supports_coupling_status:
                entities.append(Nhc2GenericInverterCouplingStatusEntity(device_instance, hub, gateway))
            if device_instance.supports_electrical_power_production:
                entities.append(Nhc2GenericInverterElectricalPowerProductionEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoGenericChargingstation)
    _LOGGER.info('→ Found %s Generic Chargingstation Implementation', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            if device_instance.supports_coupling_status:
                entities.append(Nhc2GenericChargingstationCouplingStatusEntity(device_instance, hub, gateway))
            if device_instance.supports_electrical_power:
                entities.append(Nhc2GenericChargingstationElectricalPowerEntity(device_instance, hub, gateway))
            if device_instance.supports_ev_status:
                entities.append(Nhc2GenericChargingstationEvStatusEntity(device_instance, hub, gateway))
            if device_instance.supports_charging_status:
                entities.append(Nhc2GenericChargingstationChargingStatusEntity(device_instance, hub, gateway))
            if device_instance.supports_next_charging_time:
                entities.append(Nhc2GenericChargingstationNextChargingTimeEntity(device_instance, hub, gateway))

        async_add_entities(entities)

    device_instances = gateway.get_device_instances(CocoGenericThermometer)
    _LOGGER.info('→ Found %s Generic Thermometer Implementations (undocumented)', len(device_instances))
    if len(device_instances) > 0:
        entities = []
        for device_instance in device_instances:
            entities.append(Nhc2GenericThermometerAmbientTemperatureEntity(device_instance, hub, gateway))

        async_add_entities(entities)
