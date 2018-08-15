# MultiThreaded Recursive-URL-Extraction

Recursive-URL-Extraction as the name suggest is a recursive way of url extraction. There will be an initial entry for a URL in the queue, it will extracts all the URL's from the first url (by popping the element from queue) and puts the result back in the queue and performs this operation recursively until the limit is reached.

How To Use: -
    
    Usage is by running the recursive_url.py file.

Configurations: -

    You can set the intial URL by setting "URL"  in the constants.py file.
    You can set the number of threads required by setting "NUMBER_OF_THREADS"  in the constants.py file.
    You can set the LIMIT (Number of urls to be extracted) by setting the "LIMIT"  in the constants.py file.
