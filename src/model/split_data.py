"""model/split_data.py
"""

import pandas as pd
from sklearn import model_selection

from ._base import dataset


def train_test_split(data: pd.DataFrame, modelling_params: dict) -> dataset.Datasets:
    # Unpack the parameters
    response = modelling_params["response"]
    test_size = modelling_params["test_size"]
    random_state = modelling_params["random_state"]

    # Collect data as X, y
    X = data.drop(columns=response)
    y = data[response]

    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Initalise the training and testing datasets
    training_dataset = dataset.Dataset(X_train, y_train)
    testing_dataset = dataset.Dataset(X_test, y_test)

    # Collect the datasets together

    train_test_datasets = dataset.Datasets(training_dataset, testing_dataset)

    return train_test_datasets
