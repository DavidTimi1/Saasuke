import os

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = '/'


# Google OAuth2 Settings
GOOGLE_OAUTH2_ID = os.environ.get("google-client-id")
GOOGLE_OAUTH2_SECRET = os.environ.get("google-client-secret")

# Facebook OAuth2 Settings
FACEBOOK_KEY = os.environ.get("fb-app-id")
FACEBOOK_SECRET = os.environ.get("fb-app-secret")
