import yaml


def parse_config(config_path):
    with open(config_path) as input_stream:
        try:
            config = yaml.safe_load(input_stream)
        except yaml.YAMLError as exc:
            raise exc

    return config or None


# # Test

if __name__ == "__main__":
    tc = parse_config(f'/mnt/e/source/mahuri_hive/hive_config.yaml')
    print("Sucess")