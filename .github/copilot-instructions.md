# SmartThings Custom - AI Agent Instructions

This document provides essential context for AI agents working with the SmartThings Custom integration for Home Assistant.

## Project Overview

This is a custom fork of the official Home Assistant SmartThings integration, focused on improving support for Samsung AC devices. The integration enables Home Assistant to communicate with SmartThings devices and manage their states and capabilities.

## Architecture & Components

### Core Components
- Integration is structured as a Home Assistant custom component (`custom_components/smartthings/`)
- Key platform files (e.g., `climate.py`, `light.py`, `sensor.py`) implement device-specific functionality
- Common utilities and constants in `const.py` and `util.py`
- Authentication and setup handled through `config_flow.py` and `application_credentials.py`

### Data Flow
1. SmartThings cloud API communication using `pysmartthings` library
2. Device state changes flow through the integration via capabilities defined in `const.py`
3. Events and state updates are propagated to Home Assistant entities

## Development Guidelines

### Adding Device Support
- New device types should be implemented in appropriate platform files (e.g., `climate.py` for HVAC)
- Follow existing patterns for entity setup and state management
- Reference `const.py` for standard capabilities and attributes

### Authentication
- Integration uses OAuth2 with specific scopes defined in `const.py`:
```python
SCOPES = [
    "r:devices:*",
    "w:devices:*",
    "x:devices:*",
    # ... other scopes
]
```

### Key Files
- `manifest.json`: Integration metadata and dependencies
- `const.py`: Core constants and capability mappings
- Platform files (e.g., `climate.py`, `light.py`): Device-type implementations
- `config_flow.py`: Setup and configuration workflow

## Integration Points
- SmartThings Cloud API
- Home Assistant core integration framework
- Device-specific APIs (particularly Samsung AC devices)

## Testing
Test modifications by:
1. Installing via HACS or manual copy to `custom_components/`
2. Restarting Home Assistant
3. Testing with actual SmartThings devices

## Common Patterns
- Device capabilities are mapped to Home Assistant features via constants in `const.py`
- Entity states and attributes follow Home Assistant conventions
- Platform implementations extend base classes from `entity.py`

For issues or questions, refer to the [GitHub issue tracker](https://github.com/savino/smartthings-ha-custom/issues).