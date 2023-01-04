# An Eloquent Home

Hello!  This repo contains the configuration for our [Home Assistant](https://www.home-assistant.io/) setup.  What started as a curiosity to while away the time during Covid lockdowns in 2020 is now the primary way in which we interact with and control our home.  We follow a few principles in our setup:
1. __Automation first__: Things should just adjust themselves in response to changes in the environment, without needing user intervention
2. __Maximum flexibility__: Devices, user interfaces and even the automation logic are as modular as possible, so it is easy to modify one part without affecting the whole
3. __Maximum redundancy__: Aside from automated control, devices can be controlled by app, ZigBee remote controls or voice assistant.  The only things built into our walls are data and power cables.  All smart devices can be moved or removed easily.  All devices can function locally regardless of cloud connectivity.  A non-smart fallback option is always available.
4. __Subtle helpfulness__: Other than reporting the current state, the platform recommends states based on context.  UI allows users to interpret the state of the whole system at a glance, including relationships between different devices.

## Hub
* Refurbished [Lenovo Thinkcentre M93p Tiny](https://support.lenovo.com/sg/en/solutions/pd027573-detailed-specifications-for-thinkcentre-m93-m93p-tiny-form-factor)
* [Home Assistant Operating System](https://www.home-assistant.io/installation/alternative) [9.4](https://github.com/home-assistant/operating-system/releases/tag/9.4) running in a [Proxmox VM](https://www.proxmox.com/)
* [Home Assistant Core 2022.12.8](https://github.com/home-assistant/core/releases/tag/2022.12.8)
* 4 cores, 4GB RAM, 32GB storage

## Entities

Domain | Quantity
-- | --
[`automation`](https://www.home-assistant.io/components/automation) | 82
[`binary_sensor`](https://www.home-assistant.io/components/binary_sensor) | 86
[`button`](https://www.home-assistant.io/components/button) | 120
[`camera`](https://www.home-assistant.io/components/camera) | 1
[`climate`](https://www.home-assistant.io/components/climate) | 6
[`cover`](https://www.home-assistant.io/components/cover) | 8
[`device_tracker`](https://www.home-assistant.io/components/device_tracker) | 2
[`fan`](https://www.home-assistant.io/components/fan) | 6
[`input_boolean`](https://www.home-assistant.io/components/input_boolean) | 16
[`input_datetime`](https://www.home-assistant.io/components/input_datetime) | 14
[`input_number`](https://www.home-assistant.io/components/input_number) | 25
[`input_select`](https://www.home-assistant.io/components/input_select) | 7
[`input_text`](https://www.home-assistant.io/components/input_text) | 29
[`light`](https://www.home-assistant.io/components/light) | 56
[`media_player`](https://www.home-assistant.io/components/media_player) | 4
[`number`](https://www.home-assistant.io/components/number) | 164
[`person`](https://www.home-assistant.io/components/person) | 3
[`remote`](https://www.home-assistant.io/components/remote) | 6
[`script`](https://www.home-assistant.io/components/script) | 30
[`select`](https://www.home-assistant.io/components/select) | 48
[`sensor`](https://www.home-assistant.io/components/sensor) | 333
[`sun`](https://www.home-assistant.io/components/sun) | 1
[`switch`](https://www.home-assistant.io/components/switch) | 21
[`update`](https://www.home-assistant.io/components/update) | 10
[`vacuum`](https://www.home-assistant.io/components/vacuum) | 1
[`weather`](https://www.home-assistant.io/components/weather) | 1
[`zone`](https://www.home-assistant.io/components/zone) | 1
Total | 1081

## Core Integrations
- [<img src="https://brands.home-assistant.io/_/broadlink/icon.png" height="24"/>](https://home-assistant.io/integrations/broadlink) [Broadlink](https://home-assistant.io/integrations/broadlink)
- [<img src="https://brands.home-assistant.io/_/generic_thermostat/icon.png" height="24"/>](https://home-assistant.io/integrations/generic_thermostat) [Generic Thermostat](https://home-assistant.io/integrations/generic_thermostat)
- [<img src="https://brands.home-assistant.io/_/google_assistant/icon.png" height="24"/>](https://home-assistant.io/integrations/google_assistant) [Google Assistant](https://home-assistant.io/integrations/google_assistant)
- [<img src="https://brands.home-assistant.io/_/cast/icon.png" height="24"/>](https://home-assistant.io/integrations/cast) [Google Cast](https://home-assistant.io/integrations/cast)
- [<img src="https://brands.home-assistant.io/_/mobile_app/icon.png" height="24"/>](https://home-assistant.io/integrations/mobile_app) [Home Assistant Companion](https://home-assistant.io/integrations/mobile_app)
- [<img src="https://brands.home-assistant.io/_/mqtt/icon.png" height="24"/>](https://home-assistant.io/integrations/mqtt) [MQTT](https://home-assistant.io/integrations/mqtt)
- [<img src="https://brands.home-assistant.io/_/neato/icon.png" height="24"/>](https://home-assistant.io/integrations/neato) [Neato](https://home-assistant.io/integrations/neato)
- [<img src="https://brands.home-assistant.io/_/rest/icon.png" height="24"/>](https://home-assistant.io/integrations/sensor.rest) [RESTful Sensor](https://home-assistant.io/integrations/sensor.rest)
- [<img src="https://brands.home-assistant.io/_/tasmota/icon.png" height="24"/>](https://home-assistant.io/integrations/tasmota) [Tasmota](https://home-assistant.io/integrations/tasmota)
- [<img src="https://brands.home-assistant.io/_/template/icon.png" height="24"/>](https://home-assistant.io/integrations/template) [Template Binary Sensors & Sensors](https://home-assistant.io/integrations/template)
- [<img src="https://brands.home-assistant.io/_/template/icon.png" height="24"/>](https://home-assistant.io/integrations/cover.template) [Template Cover](https://home-assistant.io/integrations/cover.template)
- [<img src="https://brands.home-assistant.io/_/template/icon.png" height="24"/>](https://home-assistant.io/integrations/fan.template) [Template Fan](https://home-assistant.io/integrations/fan.template)
- [<img src="https://brands.home-assistant.io/_/template/icon.png" height="24"/>](https://home-assistant.io/integrations/switch.template) [Template Switch](https://home-assistant.io/integrations/switch.template)
- [<img src="https://brands.home-assistant.io/_/zha/icon.png" height="24"/>](https://home-assistant.io/integrations/zha) [ZigBee Home Automation](https://home-assistant.io/integrations/zha)
## Extensions:

### Add-ons
- Duck DNS
- Home Assistant Google Drive Backup
- MariaDB
- Mosquitto broker
- Samba share
- SSH & Web Terminal
- Studio Code Server

### Custom integrations
- [Browser Mod](https://github.com/thomasloven/hass-browser_mod)
- [Cover Time Based Rf (Script/Entity)](https://github.com/nagyrobi/home-assistant-custom-components-cover-rf-time-based)
- [Generate Readme](https://github.com/custom-components/readme)
- [HACS](https://github.com/hacs/integration)
- [Local Tuya](https://github.com/rospogrigio/localtuya)
- [Smartthinq Lge Sensors](https://github.com/ollo69/ha-smartthinq-sensors)
- [Watchman](https://github.com/dummylabs/thewatchman)

### Custom dashboard cards
- [Button Card](https://github.com/custom-cards/button-card)
- [Slider Button Card](https://github.com/rohankapoorcom/slider-button-card)
- [State Switch](https://github.com/thomasloven/lovelace-state-switch)

***

This readme file was _also_ auto-generated by Home Assistant via [this custom integration](https://github.com/custom-components/readme)