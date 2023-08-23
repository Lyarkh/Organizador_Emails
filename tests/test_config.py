import pytest

from organizador_emails.models.config import Config

# Test data
test_data = {
    'key1': 'value1',
    'key2': {'inner_key1': 'inner_value1', 'inner_key2': 'inner_value2'},
}


def test_config_instance_creation():
    config = Config(test_data)
    assert isinstance(config, Config)


def test_config_attributes():
    config = Config(test_data)
    assert hasattr(config, 'key1')
    assert hasattr(config, 'key2')


def test_config_attribute_values():
    config = Config(test_data)
    assert config.key1 == 'value1'


def test_nested_config_instance():
    config = Config(test_data)
    assert isinstance(config.key2, Config)


def test_nested_config_attributes():
    config = Config(test_data)
    assert hasattr(config.key2, 'inner_key1')
    assert hasattr(config.key2, 'inner_key2')


def test_nested_config_attribute_values():
    config = Config(test_data)
    assert config.key2.inner_key1 == 'inner_value1'
    assert config.key2.inner_key2 == 'inner_value2'
