 var list = document.getElementsByClassName('list1');
for (i = 0; i < list.length; i++) {
    var anchor = list[i].getElementsByClassName('anchor');
    for (a = 0; a < anchor.length; a++) {
        $(anchor[i]).on('click', function (e) {
            list[i].classList.add('visible');
            if (list[i].hasClass('visible')) {
                list[i].removeClass('visible');
            } else {
                list[i].classList.add('visible');
            }
        });
        $(anchor[i]).on('blur', function (e) {
            list[i].removeClass('visible');
        });
    }
}
function validateEmail(email) {
  const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(email);
}
function validatePhoneNumber(phone) {
  const  keRegexPattern = /^(?:254|\+254|0)?(7(?:(?:[129][0-9])|(?:0[0-8])|(4[0-1]))[0-9]{6})$/;
  return keRegexPattern.test(phone);
}
function validURL(str) {
  var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
    '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
    '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
  return !!pattern.test(str);
}
$('[data-email1]').keyup(function () {
      const email = $(this).val();
      const $result = $("[data-answer-email1]");
       $('[data-email1]').removeClass('is-valid-custom is-invalid-custom')

      $result.text("");

      if (validateEmail(email)) {
        $result.text(email + " is valid ");
        $result.css("color", "green");
      } else {
        $result.text(email + " is not valid ");
        $result.css("color", "red");
      }
      return false;
});
$('[data-url]').keyup(function () {
      const email = $(this).val();
      const $result = $("[data-answer-url1]");
       $('[data-url]').removeClass('is-valid-custom is-invalid-custom')

      $result.text("");

      if (validURL(email)) {
        $result.text(email + " is valid ");
        $result.css("color", "green");
        $('[data-url]').removeClass('is-invalid-custom').addClass('is-valid-custom');
      } else {
        $result.text(email + " is not valid ");
        $result.css("color", "red");
        $('[data-url]').removeClass('is-valid-custom').addClass('is-invalid-custom');
      }
      return false;
});
$('[data-email1]').donetyping(function(){

  var testvalue = $(this).val()
     $.ajax({
        method : 'POST',
        data : {'testvalue':testvalue},
        url :  window.location.origin+"/checkifemailexists/",
        success:function (data) {
            console.log('success '+data)
            if(data['results'].toLowerCase() === 'success'){
                $('[data-answer-email1]').text(data['answer']);
                $('[data-answer-email1]').css("color", "green");
                $('[data-email1]').removeClass('is-invalid-custom').addClass('is-valid-custom')

            }
            else if(data['results'].toLowerCase() === 'error'){
                 $('[data-answer-email1]').text(data['answer']);
                 $('[data-answer-email1]').css("color", "red");
                  $('[data-email1]').removeClass('is-valid-custom').addClass('is-invalid-custom')
            }

        } ,
        error:function (data) {
            console.log('error '+data)
        } ,

     });
});
$('[data-username1]').donetyping(function(){
     $('[data-username1]').removeClass('is-valid-custom is-invalid-custom')
     var testvalue = $(this).val()
     $.ajax({
        method : 'POST',
        data : {'testvalue2':testvalue},
        url :   window.location.origin+"/checkifusernameexists/",
        success:function (data) {
            // console.log('success '+ data)
            if(data['results'].toLowerCase() === 'success'){
                $('[data-answer-username1]').text(data['answer']);
                $('[data-answer-username1]').css("color", "green");
                $('[data-username1]').removeClass('is-invalid-custom').addClass('is-valid-custom')

            }
            else if(data['results'].toLowerCase() === 'error'){
                 $('[data-answer-username1]').text(data['answer']);
                 $('[data-answer-username1]').css("color", "red");
                 $('[data-username1]').removeClass('is-valid-custom').addClass('is-invalid-custom')
            }

        } ,
        error:function (data) {
            console.log('error '+data)
        } ,

     });
});
$('[data-phoneno]').donetyping(function () {
      const email = $(this).val();
      const $result = $("[data-answer-phoneno]");
       $('[data-phoneno]').removeClass('is-valid-custom is-invalid-custom')
      $result.text("");
      if (validatePhoneNumber(email)) {
        $result.text(email + " is valid ");
        $result.css("color", "green");
        $('[data-phoneno]').removeClass('is-invalid-custom').addClass('is-valid-custom')

      } else {
        $result.text(email + " is not valid ");
        $result.css("color", "red");
        $('[data-phoneno]').removeClass('is-valid-custom').addClass('is-invalid-custom')
      }
      return false;
});
$('#clonebuttonexp').click(function () {
    var $clonedbox = $('.expduplicat:first').clone(true);
    $($clonedbox).insertBefore($(this)).find('input').val("");
});
$('#cloneskill').click(function () {
     var $clonedboxx = $('.dublicat-box2:first').clone(true);
     // $($clonedboxx).insertAfter('.dublicat-box2:last').find('input').val("");
     $($clonedboxx).insertBefore($(this)).find('input').val("");
});
function removeParent(e) {
    if ($('.expduplicat').length > 1){
       $(e).parent().remove();
    }
}
function removeParent2(e) {
    if ($('.dublicat-box2').length > 1){
       $(e).parent().remove();
    }
}
$('#trmscond').change(function () {
    if($(this).prop("checked", true)){
        if($('input').hasClass('is-valid-custom')){
             $('#submitbutton').removeAttr('disabled');
        }else if ($('input').hasClass('is-invalid-custom')){
             $('#submitbutton').attr('disabled');
             $(this).prop("checked", false)
             swal.fire({
                title: "Error!",
                text: "Please Fix Any Form Errors To Continue.",
                type: "error",
                confirmButtonText: "Retry"
            });

        }


    }else if($(this).prop("checked", false)){
        $('#submitbutton').attr('disabled');
    }
});
$('[data-age]').change(function () {
      const email = $(this).val();
      const $result = $("[data-answer-age]");
       $('[data-age]').removeClass('is-valid-custom is-invalid-custom')
        var day = new Date(email).getDay();
        var month = new Date(email).getMonth();
        var year = new Date(email).getFullYear();
        var age = 18;
        var setDate = new Date(year + age, month - 1, day);
        var currdate = new Date();
        $result.text("");

        if (currdate >= setDate) {
            $result.text('Age is valid ');
            $result.css("color", "green");

            $('[data-age]').removeClass('is-invalid-custom').addClass('is-valid-custom')
        } else {
            $result.text('Age is not valid ');
            $result.css("color", "red");
             $('[data-age]').removeClass('is-valid-custom').addClass('is-invalid-custom')
        }






      return false;
});
$('#countyselectt').change(function () {
    let value = $(this).find('option:selected').attr('data-countynumber');
    console.log(value, this.value);
    if (value){
        $('[data-region]').find('option').each(function () {

            if ($(this).attr('data-countyregion') === value){
                $(this).show();
            }else {
                $(this).hide()
            }
        });
    }

});