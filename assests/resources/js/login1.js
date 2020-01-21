/*var lbtn = document.getElementById("loginbtn");

lbtn.addEventListener("click", function(){
    var userEmail = document.getElementById("usr").value;
    var userPass = document.getElementById("pass").value;
    $.ajax({
      type:'POST',
      url:'usr_login/',
      data:{
         num1:userEmail,
         num2:userPass,
         csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
      },
      success: function(data){
          alert(data); // this is currently returning FALSE
      }
  })
 });*/