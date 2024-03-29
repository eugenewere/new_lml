 $(document).ready(function(){
   var spinner = $('#signuploader');
   $("#employeeform").submit(function(e){
        e.preventDefault();
        spinner.show();
        var new_form_data = new FormData(this);
        $.ajax({
            method : 'POST',
            processData: false,
            contentType: false,
            cache: false,
            data : new_form_data,
            enctype: 'multipart/form-data',
            url :  $("#employeeform").attr('action'),
            success : function(response){
                spinner.hide();
                if (response.results === 'success') {
                     $('#error_div').fadeOut();
                    $("#employeeform")[0].reset();
                    swal.fire({
                        title: "Success!",
                        text: response.success,
                        type: "success",
                        confirmButtonText: "Continue",
                    });
                    setTimeout(function () {
                        window.location = window.location.origin + "/companypayment/";
                    }, 5000);
                }
                else {
                    // console.log(JSON.stringify(response['form']))
                    // console.log(JSON.parse(response['form']))
                    var resp = response['form']
                    let k = JSON.stringify(resp)
                    let str = JSON.parse(resp)
                    for (var key in str) {
                      if (str.hasOwnProperty(key)) {
                        // console.log(key);
                        // console.log(str[key][0]['message']);
                        $('#errorlist').append(
                            '<li class="text-capitalize">'+
                               '<span>'+ key +'</span>'+
                               ' <a href="#" class="error">'+
                                  str[key][0]['message']+
                               '</a>'+
                            '</li>'
                        )
                      }
                    }
                    $('#error_div').show();
                    setTimeout(function () {
                        swal.fire({
                            title: "Error!",
                            text: "Form Is Invalid. Correct the errors above",
                            type: "error",
                            confirmButtonText: "Retry"
                        });
                    }, 2000);
                }
            },
            error : function(response){
                console.log(response);
                spinner.hide();
            }
        });
   });
});