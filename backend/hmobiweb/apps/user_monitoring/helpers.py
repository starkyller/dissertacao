from jsonschema import (
    validate, 
    exceptions as jsonschema_exceptions
)

def validateDataSample(userSolutionObj, jsonObj, errorClassValidator):
    """Validates a json object against a specific json schema

    Parameters
    ----------
    userSolutionObj : UserSolutions
        The object of the User solution
    jsonObj : JSON
        The object to be validated
    errorClassValidator: class
        The class with the exceptions
    Returns
    -------
    nothing
    """
    try:
        _schema = userSolutionObj.solution.sampleJsonSchema
        validate(instance=jsonObj, schema=_schema)

    except jsonschema_exceptions.SchemaError as e:
        raise errorClassValidator.ValidationError(e.message, code='invalid')
    except jsonschema_exceptions.ValidationError as e:
        raise errorClassValidator.ValidationError({'dataSample': [e.message,]})
    except Exception as e:
        raise errorClassValidator.ValidationError(e, code='invalid')

    return