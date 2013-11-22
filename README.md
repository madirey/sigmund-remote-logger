sigmund
=======
Sigmund is a remote logging service for Django.


getting started
===============


sigmund-server
==============
1. Add `sigmund` to INSTALLED_APPS
2. Add SigmundResource to urls.py
3. Run `python manage.py syncdb`
4. If cross-domain support is required:
   - Add SIGMUND_ALLOW_ORIGIN=<regex> to settings.py
   - Add sigmund.middleware.SigmundAllowOriginMiddleware
     to installed middleware



sigmund-client
==============
1. Add `sigmund` to INSTALLED_APPS
2. Add some things to settings.py:
   - SIGMUND_URL = 'http://sigmund-logger.herokuapp.com'
   - SIGMUND_USERNAME = 'slartibartfast'
   - SIGMUND_API_KEY = '993daadec549438eb5a2125f8b96e2d7'
3. Set up your log handler:

   ```
   LOGGING = {
      ...
      'handlers': {
         'sigmund': {
            'level': 'INFO',
            'class': 'sigmund.logging.handlers.SigmundHandler',
         },
         ...
      'loggers': {
         'bagels': {
            'handlers': ['sigmund', 'debug'],
            'level': 'DEBUG',
            'propagate': True,
         },
         ...
      },
      ...
   ```
4. Start logging!

   ```
   import logging
   logger = logging.getLogger('bagels')
   logger.warning("you can't handle the truth!")
   ```
