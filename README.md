sigmund
======

Sigmund is a remote logging service for Django.


installation
============
1. Add `sigmund` to INSTALLED_APPS
2. Add SigmundResource to urls.py
3. Run `python manage.py syncdb`
4. If cross-domain support is required:
   - Add SIGMUND_ALLOW_ORIGIN=<regex> to settings.py
   - Add sigmund.middleware.SigmundAllowOriginMiddleware
     to installed middleware
