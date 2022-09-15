from schema import Schema, And, Use, Optional, SchemaError

register_schema = Schema({
    'username': And(Use(str)),
    "email": And(Use(str)),
    "password": And(Use(str)),
})

login_schema = Schema({
    "email": And(Use(str)),
    "password": And(Use(str)),
})