$(document).ready(function() {
    $('.replytxt').each(function () {
        ClassicEditor
            .create(document.querySelector('#' + $(this).attr('id')), {
                removePlugins: ['Insert image', 'Insert table', 'Insert media'],
                toolbar: ['heading', 'Paragraph', 'Highlight', 'bold', 'italic', 'Indent', 'IndentBlock', 'undo', 'redo', 'link', 'bulletedList', 'numberedList'],

            })
            .catch(error => {
                console.error(error);
            });
    });

    $('.pop-email').each(function () {
        $(this).on("click", function (e) {
            $('.pop-email').hasClass('expand')? $('.pop-email').removeClass('expand'): $('.pop-email').removeClass('expand');

            $(this).addClass('expand')

        })
    });
    $('.x-touch').each(function () {
    $(this).on("click", function (e) {
       // $(this).parent('.pop-email').removeClass('expand');
       // console.log($(this).closest('.pop-email'))
       $('.pop-email').hasClass('expand')? $('.pop-email').removeClass('expand'): $('.pop-email').removeClass('expand');
       e.stopPropagation();
    })
});
    function getCookie(name) {
         var cookieValue = null;
         if (document.cookie && document.cookie != '') {
             var cookies = document.cookie.split(';');
             for (var i = 0; i < cookies.length; i++) {
                 var cookie = jQuery.trim(cookies[i]);
                 // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
     }
    $('.media-list li').each(function () {
        $(this).click(function () {

            if($(this).hasClass('mail-unread')){
                console.log($(this).find('.favorite:first i').attr('data-star-message'))
                let $msg_id = $(this).find('.favorite:first i').attr('data-star-message');
                var data={'message_id': $msg_id, 'csrfmiddlewaretoken':getCookie('csrftoken') }
                let loc = window.location.origin + '/ws/message_read/'
                $.post(loc, data, function(response){
                    // console.log(response)
                    if(response["test"] === "success"){
                        if(response["msg_count"] <= 0){
                            $('title').text(response.title)
                            $('.inbox-unread-badge').fadeOut('slow')
                        }else {
                            $('.inbox-unread-badge').text(response.msg_count)
                            $('title').text(response.title)
                        }

                    }else {
                         console.log('error')
                    }
                })
                // $(this).hasClass('mail-unread') ? $('[data-message-wrapper='+$(this).attr('data-message-wrapper')+']').removeClass('mail-unread').addClass('mail-read') : $('[data-message-wrapper='+$(this).attr('data-message-wrapper')+']').removeClass('mail-unread').addClass('mail-read');

            }
            else {
                // console.log('no class')
            }
            $(this).hasClass('mail-unread') ? $('[data-message-wrapper='+$(this).attr('data-message-wrapper')+']').removeClass('mail-unread').addClass('mail-read') : $('[data-message-wrapper='+$(this).attr('data-message-wrapper')+']').removeClass('mail-unread').addClass('mail-read');


        });
    });

    $(".allreplyform").each(function () {
    var idd = $(this).attr('id');
    // console.log(idd);

    $('#'+idd ).on("submit", function (e) {
        e.preventDefault();
        var form_data =  $(this).serialize();
        console.log(form_data);
        var urll = $(this).attr('action');
        $(this).ajaxSubmit({
            type:'POST',
            url: urll,
            success: function(response) {
                if(response["test"] === "success"){
                    window.location.reload();
                }else {
                     swal.fire({
                        title: "Error!",
                        text: "Could Mark As Read The Messages",
                        type: "error",
                        confirmButtonText: "Ok",
                    });
                }
            }
        })

    })
});
});