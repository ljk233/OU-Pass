"""features/_base/builder.py
"""

from abc import ABC, abstractmethod


class AbstractFeatureBuilder(ABC):
    @abstractmethod
    def build_features(self, data):
        raise NotImplementedError()


class FeatureBuilder(AbstractFeatureBuilder):
    def __init__(self):
        pass
