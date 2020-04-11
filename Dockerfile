FROM homeassistant/home-assistant:0.108.3

COPY custom_components /config/custom_components
COPY .devcontainer/*.yaml /config/