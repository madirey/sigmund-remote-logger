peyote
======

Peyote is a remote logging service for Django.


installation
============
1. Add `peyote` to INSTALLED_APPS
2. Add PeyoteResource to urls.py
3. Run `python manage.py syncdb`
4. If cross-domain support is required:
   - Add PEYOTE_ALLOW_ORIGIN=<regex> to settings.py
   - Add peyote.middleware.PeyoteAllowOriginMiddleware
     to installed middlware
