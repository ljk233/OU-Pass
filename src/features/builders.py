"""features.build_features
"""

import pandas as pd

from ._base import builder


class PandasFeatureBuilder(builder.FeatureBuilder):
    def __init__(self):
        super().__init__()

    def build_features(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.assign(
            is_female=lambda x: x["gender"].map(lambda s: 1 if s == "female" else 0),
            is_maths=lambda x: x["qual_link"].map(lambda s: 1 if s == "maths" else 0),
        ).drop(columns=["gender", "qual_link"])


def create_feature_builder(backend: str) -> builder.FeatureBuilder:
    match backend:
        case "pandas":
            return PandasFeatureBuilder()
        case _:
            raise NotImplementedError(f"Backend {backend} is not supported.")
