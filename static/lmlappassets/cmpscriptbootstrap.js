// ClassicEditor
//     .create( document.querySelector( '#brief_details' ), {
//           removePlugins: [  'Image','Table','Media','Image' ],
//         toolbar: {
//         items: [
//           'heading',
//           '|',
//           'bold',
//           'italic',
//           '|',
//           'bulletedList',
//           'numberedList',
//           '|',
//           'undo',
//           'redo'
//         ]
//       },
//     } )
//     .then( editor => {
//             // console.log( editor );
//         const wordCountPlugin = editor.plugins.get( 'WordCount' );
//         const wordCountWrapper = document.getElementById( 'word-count' );
//
//         wordCountWrapper.appendChild( wordCountPlugin.wordCountContainer );
//     } )
//     .catch( error => {
//             // console.error( error );
//     } );
 $(document).ready(function() {
             // City Select
             $('.choose-city').select2();
             $('.choose-region').select2();
             $('.choose-qualification').select2();
             $('.choose-university').select2();
             $('.choose-phd').select2();
             $('.choose-bachelor').select2();
             $('.choose-masters').select2();
             $('.choose-diploma').select2();
             $('.choose-certificate').select2();
             $('.choose-category').select2();
             $('.choose-category2').select2();
             $('.choose-entity').select2();
             $('.marital').select2();
             $('.marital2').select2();
         });
 $('input').each(function () {
     $(this).bind("change keyup input",function () {
        if($(this).val()===''){
             $(this).removeClass('is-valid-custom is-invalid-custom')
        }
     });
 });
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
 $('[data-email1]').bind("change keyup input", function () {
      const email = $(this).val();
      const $result = $("[data-answer-email1]");
       $('[data-email1]').removeClass('is-valid-custom is-invalid-custom')

      $result.text("");

      if (validateEmail(email)) {
        $result.text(email + " is valid ");
        $result.css("color", "green");
         $('[data-email1]').removeClass('is-invalid-custom').addClass('is-valid-custom')
      } else {
        $result.text(email + " is not valid ");
        $result.css("color", "red");
        $('[data-email1]').removeClass('is-valid-custom').addClass('is-invalid-custom')
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
                    $('[data-email1]').removeClass('is-invalid-custom').addClass('is-valid-custom');

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
        url :  window.location.origin+"/checkifusernameexists/",
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
 $('#trmscond').on('change',function () {
    if($(this).prop("checked") === true){
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
        }else {
            $('#submitbutton').removeAttr('disabled');
        }
    }else if($(this).prop("checked") === false){
        $('#submitbutton').attr('disabled', 'disabled');
    }
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
 $('[data-url]').each(function () {
     $(this).bind("change keyup input",function () {
          const email = $(this).val();
          const $result = $(this).parent().parent().find('small');
           $(this).removeClass('is-valid-custom is-invalid-custom')

          $result.text("");

          if (validURL(email)) {
            $result.text(email + " is valid ");
            $result.css("color", "green");
            $(this).removeClass('is-invalid-custom').addClass('is-valid-custom');
          } else {
            $result.text(email + " is not valid ");
            $result.css("color", "red");
            $(this).removeClass('is-valid-custom').addClass('is-invalid-custom');
          }
          return false;
     });
 });