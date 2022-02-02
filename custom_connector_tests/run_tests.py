import json
import sys
import importlib
from custom_connector_tests.invokers.base_test_invoker import BaseConnectorTestInvoker
from jsonschema import validate

def main():
    module_name = sys.argv[1]
    class_name = sys.argv[2]
    config_file_path = sys.argv[3]

    module = importlib.import_module(module_name)
    class_ = getattr(module, class_name)
    connector_handler = class_()

    try:
        test_config = json.load(open(config_file_path))
    except ValueError as e:
        print("Error while parsing Configuration File. Invalid JSON. " + str(e))
        sys.exit(1)

    print("Validating the schema")
    schema = json.load(open("./custom_connector_tests/configuration/ConfigSchema.json"))
    validate(test_config, schema)
    test_invoker = BaseConnectorTestInvoker(connector_handler, test_config)

    test_invoker.invoke_configuration_handler_tests()
    test_invoker.invoke_metadata_handler_tests()
    test_invoker.invoke_record_handler_tests()

    print("Tests completed successfully, see above logs for results")

if __name__ == '__main__':
    main()
