function myFunction(form) {
    var isLogin = false;
    var dict = {
        "Alice": 25, "Bob": 22, "James": 15, "Jenifer": 29,
        "Sarah": 30, "Lukah": 18, "Steve": 41,"s":1
    };
    var name =form.uname.value;
    var password=form.psw.value;

    if (name in dict) {
        if (dict[name] == password) {
            
           isLogin = true;
            
           
            
           
            
        }
        else {
            alert("Login Failed");
        }
    }
    
    
    if(isLogin){

       
         window.location.href = "suc.html";
         alert("Login Success");
    }
    

  }

