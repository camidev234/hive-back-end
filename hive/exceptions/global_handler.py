from rest_framework.views import exception_handler
from hive.utils.api_response import ApiErrorResponse
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed, PermissionDenied
from rest_framework import status
from users.models.user import User

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if isinstance(exc, ValidationError):
        error_response = ApiErrorResponse(400, errors=exc.detail, message="A validation error ocurred, please check the fields")
        return Response(error_response.get_response(), status=status.HTTP_400_BAD_REQUEST)
    
    # if response is None:
    #     error_response = ApiErrorResponse(500, message="An unexpected error occurred")
    #     return Response(error_response.get_response(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if isinstance(exc, User.DoesNotExist):
        error_response = ApiErrorResponse(404, message="The user does not exists")
        return Response(error_response.get_response(), status=status.HTTP_401_UNAUTHORIZED)
    
    return response

