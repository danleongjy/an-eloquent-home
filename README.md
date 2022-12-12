# An Eloquent Home

Hello!  This repo contains the configuration for our [Home Assistant](https://www.home-assistant.io/) setup.  What started as a curiosity to while away the time during Covid lockdowns in 2020 is now the primary way in which we interact with and control our home.  We follow a few principles in our setup:
1. __Automation first__: Things should just adjust themselves in response to changes in the environment, without needing user intervention
2. __Maximum flexibility__: Devices, user interfaces and even the automation logic are as modular as possible, so it is easy to modify one part without affecting the whole
3. __Maximum redundancy__: The only things built into our walls are data and power cables.  All smart devices can be moved or removed easily, and a non-smart fallback option is always available.

## Hub
* Refurbished [Lenovo Thinkcentre M92p Tiny](https://www.lenovo.com/hk/en/desktops-and-all-in-ones/thinkcentre/m-series-tiny/2941/p/11TC1TMM92P2941)
* [Home Assistant Operating System](https://github.com/home-assistant/operating-system/releases/download/9.3/haos_ova-9.3.qcow2.xz) running in a [Proxmox VM](https://www.proxmox.com/)
* 4 cores, 4GB RAM, 32GB storage

## Entities

Domain | Number
-- | --
[`automation`](https://www.home-assistant.io/components/automation) | 75
[`binary_sensor`](https://www.home-assistant.io/components/binary_sensor) | 86
[`button`](https://www.home-assistant.io/components/button) | 109
[`camera`](https://www.home-assistant.io/components/camera) | 1
[`climate`](https://www.home-assistant.io/components/climate) | 6
[`cover`](https://www.home-assistant.io/components/cover) | 2
[`device_tracker`](https://www.home-assistant.io/components/device_tracker) | 18
[`fan`](https://www.home-assistant.io/components/fan) | 6
[`input_boolean`](https://www.home-assistant.io/components/input_boolean) | 16
[`input_datetime`](https://www.home-assistant.io/components/input_datetime) | 12
[`input_number`](https://www.home-assistant.io/components/input_number) | 24
[`input_select`](https://www.home-assistant.io/components/input_select) | 6
[`input_text`](https://www.home-assistant.io/components/input_text) | 26
[`light`](https://www.home-assistant.io/components/light) | 56
[`media_player`](https://www.home-assistant.io/components/media_player) | 4
[`number`](https://www.home-assistant.io/components/number) | 164
[`person`](https://www.home-assistant.io/components/person) | 3
[`remote`](https://www.home-assistant.io/components/remote) | 6
[`script`](https://www.home-assistant.io/components/script) | 30
[`select`](https://www.home-assistant.io/components/select) | 47
[`sensor`](https://www.home-assistant.io/components/sensor) | 323
[`sun`](https://www.home-assistant.io/components/sun) | 1
[`switch`](https://www.home-assistant.io/components/switch) | 21
[`update`](https://www.home-assistant.io/components/update) | 10
[`vacuum`](https://www.home-assistant.io/components/vacuum) | 1
[`weather`](https://www.home-assistant.io/components/weather) | 1
[`zone`](https://www.home-assistant.io/components/zone) | 1
Total | 1055

## Core Integrations
- [<img src="https://brands.home-assistant.io/_/asuswrt/icon.png" height="24"/>](https://brands.home-assistant.io/_/asuswrt/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/asuswrt/icon.png" height="24"/>](https://brands.home-assistant.io/_/asuswrt/icon.png#gh-light-mode-only) [AsusWRT](https://home-assistant.io/integrations/asuswrt)
- [<img src="https://brands.home-assistant.io/_/broadlink/icon.png" height="24"/>](https://brands.home-assistant.io/_/broadlink/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/broadlink/icon.png" height="24"/>](https://brands.home-assistant.io/_/broadlink/icon.png#gh-light-mode-only) [Broadlink](https://home-assistant.io/integrations/broadlink)
- [<img src="https://brands.home-assistant.io/_/google_assistant/icon.png" height="24"/>](https://brands.home-assistant.io/_/google_assistant/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/google_assistant/icon.png" height="24"/>](https://brands.home-assistant.io/_/google_assistant/icon.png#gh-light-mode-only) [Google Assistant](https://home-assistant.io/integrations/google_assistant)
- [<img src="https://brands.home-assistant.io/_/cast/icon.png" height="24"/>](https://brands.home-assistant.io/_/cast/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/cast/icon.png" height="24"/>](https://brands.home-assistant.io/_/cast/icon.png#gh-light-mode-only) [Google Cast](https://home-assistant.io/integrations/cast)
- [<img src="https://brands.home-assistant.io/_/mobile_app/icon.png" height="24"/>](https://brands.home-assistant.io/_/mobile_app/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/mobile_app/icon.png" height="24"/>](https://brands.home-assistant.io/_/mobile_app/icon.png#gh-light-mode-only) [Home Assistant Companion](https://home-assistant.io/integrations/mobile_app)
- [<img src="https://brands.home-assistant.io/_/mqtt/icon.png" height="24"/>](https://brands.home-assistant.io/_/mqtt/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/mqtt/icon.png" height="24"/>](https://brands.home-assistant.io/_/mqtt/icon.png#gh-light-mode-only) [MQTT](https://home-assistant.io/integrations/mqtt)
- [<img src="https://brands.home-assistant.io/_/neato/icon.png" height="24"/>](https://brands.home-assistant.io/_/neato/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/neato/icon.png" height="24"/>](https://brands.home-assistant.io/_/neato/icon.png#gh-light-mode-only) [Neato](https://home-assistant.io/integrations/neato)
- [<img src="https://brands.home-assistant.io/_/tasmota/icon.png" height="24"/>](https://brands.home-assistant.io/_/tasmota/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/tasmota/icon.png" height="24"/>](https://brands.home-assistant.io/_/tasmota/icon.png#gh-light-mode-only) [Tasmota](https://home-assistant.io/integrations/tasmota)
- [<img src="https://brands.home-assistant.io/_/zha/icon.png" height="24"/>](https://brands.home-assistant.io/_/zha/dark_icon.png#gh-dark-mode-only)[<img src="https://brands.home-assistant.io/_/zha/icon.png" height="24"/>](https://brands.home-assistant.io/_/zha/icon.png#gh-light-mode-only) [ZigBee Home Automation](https://home-assistant.io/integrations/zha)
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

Generated by the [custom readme integration](https://github.com/custom-components/readme)