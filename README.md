# iptime-debug

LAN Command Injection on ipTime Routers (v15.xx)

## Notes

A user will first need to initialize the device by create a new "admin" account to prevent needing to fill out "captchas" on authentication. ipTime routers will also need to "CSRF Block" toggle turned off under "Firewall" settings in the WebUI.

This script was tested specifically against `15.04.6` and `15.01.4` on a N704SE but should be usable up to any more recent versions and devices.

This script uses the requests library, you will need to install it from PiP.

## Changeable Variables

- `IP_ADDR` should be set to the IP address of the router.
- `WEBUI_USR` should be set to a valid admin username for the WebUI.
- `WEBUI_PWD` should be set to a valid admin password for the WebUI.
- `COMMAND_LIST` should contain all commands to be executed as root on the system.
- `VERBOSE` can be toggled to have more information logged upon command execution.

## Warning

This package is not associated with ipTime, please use at your own risk.
