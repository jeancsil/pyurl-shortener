# PyURL Shortener

A URL shortener that works locally without the need for an external database.  
All it's index is created and maintained in the local storage.



# Design Idea
Simple http server running in the background:  
eg.: http://localhost:8081/?u=gh when opened in the browser,
it only finds which is the correct full URL (resolves by id)  
and then redirects permanently to that address ;)