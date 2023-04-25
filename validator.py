import yaml

pi3_valid_map = {
    "valid_config_keys": {"metadata", "diagnostics"},
    "valid_metadata_keys": {"experiment", "angle_measurement", "distance_measurement"},
    "valid_diagnostic_list_keys": {"AXUV", "BPROBE", "IONDOPPLER", "POLARIMETER", "IDS", "LIGHT", "THOMPSON", "INTERFEROMETER"},
    "valid_diagnostic_keys": {"location", "from_r", "from_phi", "from_z", "from_diameter", "to_r", "to_phi", "to_z", "cone_angle", "drawing_file"},
    "AXUV": {
      "location": str,
      "from_r": float,
      "from_z": float,
      "from_phi": float,
      "from_diameter": None,
      "to_r": float,
      "to_z": float,
      "to_phi": float,
      "cone_angle": None,
      "drawing_file": None,
    },
    "BPROBE": {
      "location": str,
      "from_r": float,
      "from_z": float,
      "from_phi": float,
      "from_diameter": None,
      "to_r": None,
      "to_z": None,
      "to_phi": None,
      "cone_angle": None,
      "drawing_file": str,
    },
    "IONDOPPLER": {
      "location": str,
      "from_r": float,
      "from_z": float,
      "from_phi": float,
      "from_diameter": float,
      "to_r": float,
      "to_z": float,
      "to_phi": float,
      "cone_angle": float,
      "drawing_file": str,
    },
    "POLARIMETER": {
      "location": str,
      "from_r": float,
      "from_z": float,
      "from_phi": float,
      "from_diameter": None,
      "to_r": float,
      "to_z": float,
      "to_phi": float,
      "cone_angle": None,
      "drawing_file": None,
    },
    "IDS": {
      "location": str,
      "from_r": float,
      "from_z": float,
      "from_phi": float,
      "from_diameter": None,
      "to_r": float,
      "to_z": float,
      "to_phi": float,
      "cone_angle": None,
      "drawing_file": None,
    },
    "LIGHT": {
      "location": str,
      "from_r": float,
      "from_z": float,
      "from_phi": float,
      "from_diameter": float,
      "to_r": float,
      "to_z": float,
      "to_phi": float,
      "cone_angle": float,
      "drawing_file": str,
    },
    "THOMPSON": {
      "location": str,
      "from_r": float,
      "from_z": float,
      "from_phi": float,
      "from_diameter": None,
      "to_r": None,
      "to_z": None,
      "to_phi": None,
      "cone_angle": None,
      "drawing_file": None,
    },
    "INTERFEROMETER": {
      "location": str,
      "from_r": float,
      "from_z": float,
      "from_phi": float,
      "from_diameter": None,
      "to_r": float,
      "to_z": float,
      "to_phi": float,
      "cone_angle": None,
      "drawing_file": None,
    },
}

def validate_yaml(yaml_config:dict) -> dict:
    invalid_keys = []
    invalid_values = []
    #Check base keys
    for key in yaml_config.keys():
        if not key in pi3_valid_map['valid_config_keys']:
            invalid_keys.append(key)
    # Check metadata keys
    for key in yaml_config['metadata']:
        if not key in pi3_valid_map['valid_metadata_keys'] and yaml_config['metadata'][key]:
            invalid_keys.append(key)
        
    # Validate nested diagnostics
    for diagnostic_type in yaml_config["diagnostics"]:
        # print(diagnostic_type)
        if not diagnostic_type in pi3_valid_map['valid_diagnostic_list_keys']:
            invalid_keys.append(f"diagnostics.{diagnostic_type}")
        for diagnostic in yaml_config['diagnostics'][diagnostic_type]:
            # print(diagnostic)
            for value in yaml_config['diagnostics'][diagnostic_type][diagnostic]:
                vector = yaml_config['diagnostics'][diagnostic_type][diagnostic][value]
                if not value in pi3_valid_map['valid_diagnostic_keys']:
                    invalid_keys.append(f"diagnostics.{diagnostic_type}.{diagnostic}.{value}")
                # TODO - need to check types of values after clarification, add to invalid_keys
                # print(value)
                # print(f"MAP: {pi3_valid_map[diagnostic_type][value]}")
                print(type(vector))

with open('location_vector_schema.yaml', 'r', encoding='UTF-8') as file:
    config = yaml.safe_load(file)
    validate_yaml(config)
