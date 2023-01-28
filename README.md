# PyURL Shortener

A URL shortener that works locally without the need for an external database.  
All it's index is created and maintained in the local storage.

# Design Idea

Simple http server running in the background:  
eg.: http://localhost:8081/?u=gh when opened in the browser,
it only finds which is the correct full URL (resolves by id)  
and then redirects permanently to that address ;)

# TODO

- Allow insertion of new URLs to be shortened.
    - Command line tool to shorten URLs?
- Maybe opening a shortened link from the terminal?
- Backup of the database?
