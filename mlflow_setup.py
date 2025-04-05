import os
import mlflow

# Ensure the tracking credentials are set
os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("DAGSHUB_USER")
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("DAGSHUB_TOKEN")

# Set the tracking URI explicitly
mlflow.set_tracking_uri("https://dagshub.com/ads994672/my-first-repo.mlflow")

# Debugging output
print("MLflow Tracking URI:", mlflow.get_tracking_uri())
print("DagsHub Username:", os.getenv("MLFLOW_TRACKING_USERNAME"))
