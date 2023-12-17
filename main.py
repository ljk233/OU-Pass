# %%
"""main.py
"""

import src.api as api


def main():
    # Path the parameters
    params_path = "parameters.toml"

    # Load the pipeline parameters
    pipeline_params = api.load_parameters(params_path, "pipeline")

    # Load the path parameters
    path_params = api.load_parameters(params_path, "path")

    # Load the raw data
    csv_pandas_handler = api.create_data_handler(
        pipeline_params["raw_format"], pipeline_params["backend"]
    )
    # raw_data = csv_pandas_handler()
    # Clean the raw data
    # Build the features
    # Train the model
    # Test the model

    return csv_pandas_handler


main()

# %%
