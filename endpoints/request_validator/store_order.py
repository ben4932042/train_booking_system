from flask_restful import reqparse

def vaildator():
    validator = reqparse.RequestParser()
    
    validator.add_argument(
        'autoticket',
        required=True,
        type=bool,
        location='json',
        help='autoticket is required and type is Boolean'
    )
    
    validator.add_argument(
        'uuid',
        required=True,
        type=str,
        location='json',
        help='uuid is required and type is String'
    )
    
    validator.add_argument(
        'prefer',
        required=True,
        type=int,
        location='json',
        help='prefer is required and type is Integer'
    )
    
    validator.add_argument(
        'car_type',
        required=True,
        type=int,
        location='json',
        help='car_type is required and type is Integer'
    )
    
    validator.add_argument(
        'number',
        required=True,
        type=int,
        location='json',
        help='number is required and type is Integer'
    )

    return validator
    