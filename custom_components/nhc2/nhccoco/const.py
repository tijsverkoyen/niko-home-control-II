import paho.mqtt.client as mqtt

MQTT_PROTOCOL = mqtt.MQTTv311
MQTT_TRANSPORT = 'tcp'
MQTT_CERT_FILE = '/coco_ca.pem'

DEVICE_CONTROL_BUFFER_SIZE = 16
DEVICE_CONTROL_BUFFER_COMMAND_SIZE = 32

MQTT_DATA_METHOD = 'Method'
MQTT_DATA_METHOD_SYSINFO_PUBLISH = 'systeminfo.publish'
MQTT_DATA_METHOD_SYSINFO_PUBLISHED = 'systeminfo.published'
MQTT_DATA_METHOD_DEVICES_LIST = 'devices.list'
MQTT_DATA_METHOD_DEVICES_CONTROL = 'devices.control'
MQTT_DATA_METHOD_DEVICES_STATUS = 'devices.status'
MQTT_DATA_METHOD_DEVICES_CHANGED = 'devices.changed'
MQTT_DATA_PARAMS = 'Params'
MQTT_DATA_PARAMS_DEVICES = 'Devices'
MQTT_DATA_PARAMS_DEVICES_PROPERTIES = 'Properties'
MQTT_DATA_PARAMS_DEVICES_UUID = 'Uuid'
MQTT_DATA_PARAMS_SYSTEMINFO = 'SystemInfo'
MQTT_DATA_PARAMS_SYSTEMINFO_SWVERSIONS = 'SWversions'
MQTT_DATA_PARAMS_SYSTEMINFO_SWVERSIONS_COCO_IMAGE = 'CocoImage'
MQTT_DATA_PARAMS_SYSTEMINFO_SWVERSIONS_NHC_VERSION = 'NhcVersion'

MQTT_RC_CODES = [
    '',
    'Connection refused - incorrect protocol version',
    'Connection refused - invalid client identifier',
    'Connection refused - server unavailable',
    'Connection refused - bad username or password',
    'Connection refused - not authorised'
]

MQTT_TOPIC_PUBLIC_AUTH_CMD = 'public/authentication/cmd'
MQTT_TOPIC_PUBLIC_AUTH_RSP = 'public/authentication/rsp'
MQTT_TOPIC_SUFFIX_SYS_EVT = '/system/evt'
MQTT_TOPIC_PUBLIC_CMD = '/system/cmd'
MQTT_TOPIC_PUBLIC_RSP = '/system/rsp'
MQTT_TOPIC_SUFFIX_CMD = '/control/devices/cmd'
MQTT_TOPIC_SUFFIX_RSP = '/control/devices/rsp'
MQTT_TOPIC_SUFFIX_EVT = '/control/devices/evt'

DEVICE_DESCRIPTOR_UUID = 'Uuid'
DEVICE_DESCRIPTOR_TYPE = 'Type'
DEVICE_DESCRIPTOR_TECHNOLOGY = 'Technology'
DEVICE_DESCRIPTOR_TECHNOLOGY_NIKOHOMECONTROL = 'nikohomecontrol'
DEVICE_DESCRIPTOR_MODEL = 'Model'
DEVICE_DESCRIPTOR_IDENTIFIER = 'Identifier'
DEVICE_DESCRIPTOR_NAME = 'Name'
DEVICE_DESCRIPTOR_TRAITS = 'Traits'
DEVICE_DESCRIPTOR_PARAMETERS = 'Parameters'
DEVICE_DESCRIPTOR_PROPERTIES = 'Properties'
DEVICE_DESCRIPTOR_PROPERTY_DEFINITIONS = 'PropertyDefinitions'
DEVICE_DESCRIPTOR_PROPERTY_DEFINITIONS_DESCRIPTION = 'Description'
DEVICE_DESCRIPTOR_ONLINE = 'Online'
DEVICE_DESCRIPTOR_ONLINE_VALUE_TRUE = 'True'

PARAMETER_ACTION = 'Action'
PARAMETER_BUTTON_ID = 'ButtonId'
PARAMETER_CLAMP_TYPE = 'ClampType'
PARAMETER_CLAMP_TYPE_VALUE_63A = '63A'
PARAMETER_CLAMP_TYPE_VALUE_120A = '120A'
PARAMETER_DECLINE_CALL_APPLIED_ON_ALL_DEVICES = 'DeclineCallAppliedOnAllDevices'
PARAMETER_DECLINE_CALL_APPLIED_ON_ALL_DEVICES_VALUE_TRUE = 'true'
PARAMETER_FEEDBACK_ENABLED = 'FeedbackEnabled'
PARAMETER_FEEDBACK_ENABLED_VALUE_TRUE = 'True'
PARAMETER_FLOW = 'Flow'
PARAMETER_FLOW_VALUE_PRODUCER = 'Producer'
PARAMETER_FLOW_VALUE_CONSUMER = 'Consumer'
PARAMETER_MANUFACTURER = 'Manufacturer'
PARAMETER_MEASURING_ONLY = 'MeasuringOnly'
PARAMETER_MEASURING_ONLY_VALUE_TRUE = 'True'
PARAMETER_MJPEG_URI = 'MjpegUri'
PARAMETER_RINGTONE = 'Ringtone'
PARAMETER_SEGMENT = 'Segment'
PARAMETER_SEGMENT_VALUE_CENTRAL = 'Central'
PARAMETER_SEGMENT_VALUE_SUBSEGMENT = 'Subsegment'
PARAMETER_SPEAKER = 'Speaker'
PARAMETER_TN_URI = 'TnUri'

PROPERTY_ACTION = 'Action'
PROPERTY_ACTION_VALUE_CLOSE = 'Close'
PROPERTY_ACTION_VALUE_OPEN = 'Open'
PROPERTY_ACTION_VALUE_STOP = 'Stop'
PROPERTY_ACTIVE = 'Active'
PROPERTY_ACTIVE_VALUE_TRUE = 'True'
PROPERTY_ALIGNED = 'Aligned'
PROPERTY_ALIGNED_VALUE_TRUE = 'True'
PROPERTY_ALL_OFF_ACTIVE = 'AllOffActive'
PROPERTY_ALL_OFF_ACTIVE_VALUE_TRUE = 'True'
PROPERTY_ALL_STARTED = 'AllStarted'
PROPERTY_ALL_STARTED_VALUE_TRUE = 'True'
PROPERTY_AMBIENT_TEMPERATURE = 'AmbientTemperature'
PROPERTY_BASIC_STATE = 'BasicState'
PROPERTY_BASIC_STATE_VALUE_INTERMEDIATE = 'Intermediate'
PROPERTY_BASIC_STATE_VALUE_ON = 'On'
PROPERTY_BASIC_STATE_VALUE_OFF = 'Off'
PROPERTY_BASIC_STATE_VALUE_TRIGGERED = 'Triggered'
PROPERTY_BOOST = 'Boost'
PROPERTY_BOOST_VALUE_FALSE = 'False'
PROPERTY_BOOST_VALUE_TRUE = 'True'
PROPERTY_BRIGHTNESS = 'Brightness'
PROPERTY_CALL_ANSWERED = 'CallAnswered'
PROPERTY_CALL_ANSWERED_VALUE_TRUE = 'True'
PROPERTY_CALL_PENDING = 'CallPending'
PROPERTY_CALL_PENDING_VALUE_TRUE = 'True'
PROPERTY_CALL_STATUS_01 = 'CallStatus01'
PROPERTY_CO2 = 'CO2'
PROPERTY_COOLING_MODE = 'CoolingMode'
PROPERTY_COOLING_MODE_VALUE_TRUE = 'True'
PROPERTY_CONNECTED = 'Connected'
PROPERTY_CONNECTED_VALUE_TRUE = 'True'
PROPERTY_COUPLING_STATUS = 'CouplingStatus'
PROPERTY_DEMAND = 'Demand'
PROPERTY_DEMAND_VALUE_COOLING = 'Cooling'
PROPERTY_DEMAND_VALUE_HEATING = 'Heating'
PROPERTY_DEMAND_VALUE_NONE = 'None'
PROPERTY_DOMESTIC_HOT_WATER_TEMPERATURE = 'DomesticHotWaterTemperature'
PROPERTY_DOORLOCK = 'Doorlock'
PROPERTY_DOORLOCK_VALUE_OPEN = 'Open'
PROPERTY_DOORLOCK_VALUE_CLOSED = 'Closed'
PROPERTY_ECOSAVE = 'EcoSave'
PROPERTY_ECOSAVE_VALUE_FALSE = 'False'
PROPERTY_ECOSAVE_VALUE_TRUE = 'True'
PROPERTY_ELECTRICAL_POWER = 'ElectricalPower'
PROPERTY_ELECTRICAL_POWER_CONSUMPTION = 'ElectricalPowerConsumption'
PROPERTY_ELECTRICAL_POWER_FROM_GRID = 'ElectricalPowerFromGrid'
PROPERTY_ELECTRICAL_POWER_PRODUCTION = 'ElectricalPowerProduction'
PROPERTY_ELECTRICAL_POWER_PRODUCTION_THRESHOLD_EXCEEDED = 'ElectricalPowerProductionThresholdExceeded'
PROPERTY_ELECTRICAL_POWER_PRODUCTION_THRESHOLD_EXCEEDED_VALUE_TRUE = 'True'
PROPERTY_ELECTRICAL_POWER_SELF_CONSUMPTION = 'ElectricalPowerSelfConsumption'
PROPERTY_ELECTRICAL_POWER_TO_GRID = 'ElectricalPowerToGrid'
PROPERTY_FAN_SPEED = 'FanSpeed'
PROPERTY_FAN_SPEED_VALUE_AUTO = 'Auto'
PROPERTY_FAN_SPEED_VALUE_BOOST = 'Boost'
PROPERTY_FAN_SPEED_VALUE_HIGH = 'High'
PROPERTY_FAN_SPEED_VALUE_LOW = 'Low'
PROPERTY_FAN_SPEED_VALUE_MEDIUM = 'Medium'
PROPERTY_FAN_SPEED_VALUE_OFF = 'Off'
PROPERTY_FEEDBACK = 'Feedback'
PROPERTY_FEEDBACK_MESSAGE = 'FeedbackMessage'
PROPERTY_HEAT_INDEX = 'HeatIndex'
PROPERTY_HEATING_MODE = 'HeatingMode'
PROPERTY_HEATING_MODE_VALUE_TRUE = 'True'
PROPERTY_HUMIDITY = 'Humidity'
PROPERTY_HVAC_ON = 'HvacOn'
PROPERTY_HVAC_ON_VALUE_TRUE = 'True'
PROPERTY_IP_ADDRESS = 'IpAddress'
PROPERTY_LAST_DIRECTION = 'LastDirection'
PROPERTY_LAST_DIRECTION_VALUE_OPEN = 'Open'
PROPERTY_LAST_DIRECTION_VALUE_CLOSE = 'Close'
PROPERTY_MOOD_ACTIVE = 'MoodActive'
PROPERTY_MOOD_ACTIVE_VALUE_TRUE = 'True'
PROPERTY_MOVING = 'Moving'
PROPERTY_MOVING_VALUE_TRUE = 'True'
PROPERTY_MUTED = 'Muted'
PROPERTY_MUTED_VALUE_FALSE = 'False'
PROPERTY_MUTED_VALUE_TRUE = 'True'
PROPERTY_OPERATION_MODE = 'OperationMode'
PROPERTY_OPERATION_MODE_VALUE_AUTO = 'Auto'
PROPERTY_OPERATION_MODE_VALUE_COOL = 'Cool'
PROPERTY_OPERATION_MODE_VALUE_COOLING = 'Cooling'
PROPERTY_OPERATION_MODE_VALUE_DRY = 'Dry'
PROPERTY_OPERATION_MODE_VALUE_FAN = 'Fan'
PROPERTY_OPERATION_MODE_VALUE_HEATING = 'Heating'
PROPERTY_OPERATION_MODE_VALUE_HEAT = 'Heat'
PROPERTY_OVERRULE_ACTIVE = 'OverruleActive'
PROPERTY_OVERRULE_ACTIVE_VALUE_FALSE = 'False'
PROPERTY_OVERRULE_ACTIVE_VALUE_TRUE = 'True'
PROPERTY_OVERRULE_SETPOINT = 'OverruleSetpoint'
PROPERTY_OVERRULE_TIME = 'OverruleTime'
PROPERTY_OUTDOOR_TEMPERATURE = 'OutdoorTemperature'
PROPERTY_PLAYBACK = 'Playback'
PROPERTY_PLAYBACK_VALUE_BUFFERING = 'Buffering'
PROPERTY_PLAYBACK_VALUE_PAUSED = 'Paused'
PROPERTY_PLAYBACK_VALUE_PLAYING = 'Playing'
PROPERTY_PORT_CLOSED = 'PortClosed'
PROPERTY_PORT_CLOSED_VALUE_TRUE = 'True'
PROPERTY_POSITION = 'Position'
PROPERTY_PROGRAM = 'Program'
PROPERTY_PROGRAM_VALUE_AWAY = 'Away'
PROPERTY_PROGRAM_VALUE_CUSTOM = 'Custom'
PROPERTY_PROGRAM_VALUE_DAY = 'Day'
PROPERTY_PROGRAM_VALUE_ECO = 'Eco'
PROPERTY_PROGRAM_VALUE_HOME = 'Home'
PROPERTY_PROGRAM_VALUE_NIGHT = 'Night'
PROPERTY_PROGRAM_VALUE_OFF = 'Off'
PROPERTY_PROGRAM_VALUE_PROG_1 = 'Prog1'
PROPERTY_PROGRAM_VALUE_PROG_2 = 'Prog2'
PROPERTY_PROGRAM_VALUE_PROG_3 = 'Prog3'
PROPERTY_PROTECT_MODE = 'ProtectMode'
PROPERTY_PROTECT_MODE_VALUE_TRUE = 'True'
PROPERTY_PROTECT_MODE_VALUE_FALSE = 'False'
PROPERTY_REPORT_INSTANT_USAGE = 'ReportInstantUsage'
PROPERTY_REPORT_INSTANT_USAGE_VALUE_TRUE = 'True'
PROPERTY_REPORT_INSTANT_USAGE_VALUE_FALSE = 'False'
PROPERTY_SETPOINT_TEMPERATURE = 'SetpointTemperature'
PROPERTY_START_ACTIVE = 'StartActive'
PROPERTY_START_ACTIVE_VALUE_TRUE = 'True'
PROPERTY_STATUS = 'Status'
PROPERTY_STATUS_VALUE_FALSE = 'False'
PROPERTY_STATUS_VALUE_OFF = 'Off'
PROPERTY_STATUS_VALUE_ON = 'On'
PROPERTY_STATUS_VALUE_TRUE = 'True'
PROPERTY_STATUS_VALUE_FIXED_CLOSED = 'FixedClosed'
PROPERTY_TITLE = 'Title'
PROPERTY_TITLE_ALIGNED = 'TitleAligned'
PROPERTY_TITLE_ALIGNED_VALUE_TRUE = 'True'
PROPERTY_THERMOSTAT_ON = 'ThermostatOn'
PROPERTY_THERMOSTAT_ON_VALUE_FALSE = 'False'
PROPERTY_THERMOSTAT_ON_VALUE_TRUE = 'True'
PROPERTY_VOLUME = 'Volume'
PROPERTY_VOLUME_ALIGNED = 'VolumeAligned'
PROPERTY_VOLUME_ALIGNED_VALUE_TRUE = 'True'

GARAGE_DOOR_STATUS_OPENING = 'Opening'
GARAGE_DOOR_STATUS_CLOSING = 'Closing'
