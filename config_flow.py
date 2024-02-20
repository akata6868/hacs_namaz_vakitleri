"""Namaz Vakitleri bileşenin yapılandırma akışı."""

import logging

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_CITY, CONF_CITY_CODE, CONF_API_KEY
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DOMAIN = "hacs_namaz_vakitleri"

DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_CITY): cv.string,
    vol.Required(CONF_CITY_CODE): cv.string,
    vol.Required(CONF_API_KEY): cv.string,
})


async def validate_input(hass, data):
    """Kullanıcının sağladığı verileri doğrula."""
    # Verileri doğrulama işlemleri burada yapılabilir
    return {"title": f"Namaz Vakitleri ({data[CONF_CITY]})"}


class NamazVakitleriConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Namaz Vakitleri bileşenin yapılandırma akışı sınıfı."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_UNKNOWN

    async def async_step_user(self, user_input=None):
        """Yapılandırma akışının başlangıç adımı."""
        if user_input is not None:
            return self.async_create_entry(title=user_input[CONF_CITY], data=user_input)

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA)

    async def async_step_import(self, user_input):
        """Yapılandırma akışının içe aktarma adımı."""
        return await self.async_step_user(user_input)
