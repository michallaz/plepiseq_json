#!/usr/bin/env python3

import argparse
import json

import fastjsonschema


def validate_json(schema_file: str, json_file_path: str):
    with open(schema_file) as schema_file:
        schema_file = json.load(schema_file)
        validate = fastjsonschema.compile(schema_file)
    with open(json_file_path) as json_file:
        json_file = json.load(json_file)
    return validate(json_file)


def main():
    parser = argparse.ArgumentParser(description='Validate JSON file against JSON schema')
    parser.add_argument('schema', type=str, help='JSON schema file')
    parser.add_argument('json', type=str, help='JSON file to validate')
    args = parser.parse_args()

    validation_result = validate_json(args.schema, args.json)
    print(validation_result)


if __name__ == '__main__':
    main()
