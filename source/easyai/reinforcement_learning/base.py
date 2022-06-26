from abc import ABC
from typing import Any, Tuple, Dict

from library.imports import import_class


def build_collector_from_config(
    collector_def: type, config: Dict[str, Dict]
) -> Collector:
    """Uses standard config definition to instantiate objects
    and add them to the defined Collector

    :param config: _description_
    :type config: Dict[str, Dict]
    :param collector_def: _description_
    :type collector_def: type
    :return: _description_
    :rtype: Collector
    """

    collector = collector_def()

    for callable_obj_def in config:

        assert "name" in callable_obj_def

        class_def = import_class(callable_obj_def["name"])
        collector.append(class_def(**callable_obj_def.get("kwargs", {})))

    return collector