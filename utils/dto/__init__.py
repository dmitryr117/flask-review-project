from schema import SchemaError

def check_dto(conf_schema, conf):
    try:
        conf_schema.validate(conf)
        return True
    except SchemaError:
        return False