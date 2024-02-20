"""
Home Assistant bileşeni olarak Namaz Vakitleri Sensörü.
"""

import logging
import requests
from datetime import datetime, timedelta
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'hacs_namaz_vakitleri'

CONF_CITY = 'city'
CONF_CITY_CODE = 'city_code'
CONF_API_KEY = 'api_key'

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_CITY): cv.string,
        vol.Required(CONF_CITY_CODE): cv.string,
        vol.Required(CONF_API_KEY): cv.string,
    })
}, extra=vol.ALLOW_EXTRA)

def setup_platform(hass, config, add_entities, discovery_info=None):
    city = config[DOMAIN].get(CONF_CITY)
    city_code = config[DOMAIN].get(CONF_CITY_CODE)
    api_key = config[DOMAIN].get(CONF_API_KEY)
    
    if city is None or city_code is None or api_key is None:
        _LOGGER.error("City, city code, or API key is missing. Please provide all required parameters.")
        return
    
    url = f"https://api.crm10.de/vakitler.php?sehir={city}&sehir_kodu={city_code}&api_key={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()['Namazvakitleri']
        entities = []
        for prayer_time, time_value in data.items():
            entities.append(NamazVaktiSensor(prayer_time, time_value))
        add_entities(entities)
    except Exception as e:
        _LOGGER.error("Error fetching data from API: %s", e)

class NamazVaktiSensor(Entity):
    def __init__(self, prayer_time, time_value):
        self._prayer_time = prayer_time
        self._state = time_value
        self._unit_of_measurement = None
        self._attributes = {}

    @property
    def name(self):
        return f"{self._prayer_time} Vakti"

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement

    @property
    def device_state_attributes(self):
        return self._attributes

    def update(self):
        pass
