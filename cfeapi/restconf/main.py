from django.conf import settings
import datetime

REST_FRAMEWORK = {
	"DEFAULT_AUTHENTICATION_CLASSES":(
		'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
		"rest_framework.authentication.SessionAuthentication",
		# "rest_framework.authentication.BasicAuthentication",

	),
	"DEFAULT_PERMISSION_CLASSES":(
	"rest_framework.permissions.IsAuthenticatedOrReadOnly",
	),
    "DEFAULT_PAGINATION_CLASS":
    "cfeapi.restconf.pagination.CustomPagination",
    "DEFAULT_FILTER_BACKENDS":(
    "rest_framework.filters.SearchFilter",
    "rest_framework.filters.OrderingFilter",
    ),
    "SEARCH_PARAM":"search",
    "ORDERING_PARAM":"ordering",
}

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'accounts.api.utils.jwt_response_payload_handler', # customized in accounts.utils

    'JWT_SECRET_KEY': settings.SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    # 'JWT_ALLOW_REFRESH': False,
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT', # Autherization: JWT <token> Bearer 
    'JWT_AUTH_COOKIE': None,

}