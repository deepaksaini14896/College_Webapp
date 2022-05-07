import jwt
import datetime

# Secret Key
secret = "123"
# Algorithm
algorithm="HS256"

# create token
def create_token(phone, user_type):
	token = jwt.encode( {
							'user_type' : user_type,
							'phone': phone,
							'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=(60 * 3))
						},
						secret, algorithm)
	return token

# check token
def check_token(token):
	try:
		decoded = jwt.decode(token, secret, algorithm)
	except jwt.ExpiredSignatureError:
		return 	3, None
	except jwt.InvalidTokenError:
		return 2, None
	return 1, decoded