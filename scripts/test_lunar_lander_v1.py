from hyperfetch import tuning

# Path to your YAML config file
config_path = "configs/lunar_lander_v1.yml"

# Writes each trial's best hyperparameters to log folder
tuning.tune(config_path)

