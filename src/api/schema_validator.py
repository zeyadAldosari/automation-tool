from jsonschema import Validator, Draft202012Validator
from jsonschema.exceptions import ValidationError, SchemaError

def validate_schema(instance: dict, schema: dict, *, where: str = ""):
    try:
        Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
        if errors:
            first = errors[0]
            path = list(first.path)
            at = f" at $.{'/'.join(map(str, path))}" if path else ""
            raise AssertionError(
                f"Schema validation failed{(' for ' + where) if where else ''}{at}: {first.message}"
            )
    except ValidationError as e:
        path = list(e.path)
        at = f" at $.{'/'.join(map(str, path))}" if path else ""
        raise AssertionError(
            f"Schema validation error{(' for ' + where) if where else ''}{at}: {e.message}"
        )
    except SchemaError as e:
        raise AssertionError(
            f"Schema error{(' for ' + where) if where else ''}: {e.message}"
        )
