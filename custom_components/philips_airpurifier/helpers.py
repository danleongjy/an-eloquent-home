"""Helper functions for Philips air purifier status."""

from typing import Any

from .const import PhilipsApi


def extract_name(status: dict[str, Any]) -> str:
    """Extract the name from the status."""
    for name_key in [PhilipsApi.NAME, PhilipsApi.NEW_NAME, PhilipsApi.NEW2_NAME]:
        name = status.get(name_key)
        if name:
            return name
    return ""


def extract_model(status: dict[str, Any]) -> str:
    """Extract the model from the status."""
    for model_key in [
        PhilipsApi.MODEL_ID,
        PhilipsApi.NEW_MODEL_ID,
        PhilipsApi.NEW2_MODEL_ID,
    ]:
        model = status.get(model_key)
        if model:
            return model[:9]
    return ""
