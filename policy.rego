package authz

 default allow = false

     allow {
         input.method == "GET"
        input.path == "/data"
        input.user == "alice"
       }
