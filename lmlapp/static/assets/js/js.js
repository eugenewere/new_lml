
   $('.disability_choice').click(function () {
        var html ='<div id="disbledtxtarea" class="col-md-12 col-sm-12" style="padding: 0;">' +
                        '<label for="disability"></label>' +
                        '<textarea style="max-width: 100%;" required name="disability" id="disability" class="des form-control" placeholder="What type of disability"></textarea>' +
                 '</div>'

        if($(this).val().toLowerCase()==='disabled'){
            $('#disabilityparent').append(html);
            ClassicEditor
                .create( document.querySelector( '#disability' ), {
                      removePlugins: [  'Image','Table','Media','Image' ],
                    toolbar: {
                    items: [
                      'heading',
                      '|',
                      'bold',
                      'italic',
                      '|',
                      'bulletedList',
                      'numberedList',
                      '|',
                      'undo',
                      'redo'
                    ]
                  },
                } )
                .then( editor => {
                        // console.log( editor );
                    const wordCountPlugin = editor.plugins.get( 'WordCount' );
                    const wordCountWrapper = document.getElementById( 'word-count' );

                    wordCountWrapper.appendChild( wordCountPlugin.wordCountContainer );
                } )
                .catch( error => {
                        // console.error( error );
                } );

        }else if($(this).val().toLowerCase()==='not_disabled'){
            if($('#disbledtxtarea:visible')){
                $('#disbledtxtarea').remove();
            }
        }

   });




function showEducation(data) {
        var y = document.getElementById(data.id);
        var x = y.parentElement;

        if (y.value === 'Phd') {
            x.children[2].style.display = "block";
            x.children[7].style.display = "block";
            x.children[1].style.display = "block";
            x.children[8].style.display = "block";
            if (x.children[3].style.display === "block" || x.children[5].style.display === "block" || x.children[6].style.display === "block" || x.children[4].style.display === "block") {
                x.children[3].style.display = "none";
                x.children[5].style.display = "none";
                x.children[6].style.display = "none";
                x.children[4].style.display = "none";
            }
        }
        else if (y.value === 'Masters') {
            x.children[3].style.display = "block";
            x.children[7].style.display = "block";
            x.children[1].style.display = "block";
            x.children[8].style.display = "block";
            if (x.children[2].style.display === "block" || x.children[5].style.display === "block" || x.children[6].style.display === "block" || x.children[4].style.display === "block") {
                x.children[2].style.display = "none";
                x.children[6].style.display = "none";
                x.children[5].style.display = "none";
                x.children[4].style.display = "none";
            }
        }
        else if (y.value === "Bachelor") {
            x.children[4].style.display = "block";
            x.children[7].style.display = "block";
            x.children[1].style.display = "block";
            x.children[8].style.display = "block";
            if (x.children[2].style.display === "block" || x.children[5].style.display === "block" || x.children[6].style.display === "block" || x.children[3].style.display === "block") {
                x.children[2].style.display = "none";
                x.children[6].style.display = "none";
                x.children[5].style.display = "none";
                x.children[3].style.display = "none";
            }
        }
        else if (y.value === "Diploma") {
            x.children[5].style.display = "block";
            x.children[7].style.display = "block";
            x.children[1].style.display = "block";
            x.children[8].style.display = "block";
            if (x.children[2].style.display === "block" || x.children[3].style.display === "block" || x.children[6].style.display === "block" || x.children[4].style.display === "block") {
                x.children[2].style.display = "none";
                x.children[6].style.display = "none";
                x.children[3].style.display = "none";
                x.children[4].style.display = "none";
            }
        }
        else if (y.value === "Certificate") {
            x.children[6].style.display = "block";
            x.children[7].style.display = "block";
            x.children[1].style.display = "block";
            x.children[8].style.display = "block";
            if ( x.children[2].style.display === "block" || x.children[3].style.display === "block" || x.children[5].style.display === "block" || x.children[4].style.display === "block") {
                x.children[2].style.display = "none";
                x.children[5].style.display = "none";
                x.children[3].style.display = "none";
                x.children[4].style.display = "none";
            }
        }

}



$('.experinput').click(function () {
    console.log($(this).val());
    if($(this).val().toLowerCase() === 'one'){
        $('.multi-boxmine').show()
    }
    else if($(this).val().toLowerCase() === 'two'){
        $('.multi-boxmine').hide()
    }
});


function readURL(input) {

if (input.files && input.files[0]) {
     var reader = new FileReader();
     // var disclaimer= document.getElementById("");
        reader.onload = function (element) {
            $('.blah').attr('src', element.target.result).css('visibility', 'visible');
            $('#disclaimer').text('Change Profile')
        };
        reader.readAsDataURL(input.files[0]);
        }
    }



//
// $('#element').donetyping(callback[, timeout=1000])
// Fires callback when a user has finished typing. This is determined by the time elapsed
// since the last keystroke and timeout parameter or the blur event--whichever comes first.
//   @callback: function to be called when even triggers
//   @timeout:  (default=1000) timeout, in ms, to to wait before triggering event if not
//              caused by blur.
// Requires jQuery 1.7+
//
;(function($){
    $.fn.extend({
        donetyping: function(callback,timeout){
            timeout = timeout || 2000; // 1 second default timeout
            var timeoutReference,
                doneTyping = function(el){
                    if (!timeoutReference) return;
                    timeoutReference = null;
                    callback.call(el);
                };
            return this.each(function(i,el){
                var $el = $(el);
                // Chrome Fix (Use keyup over keypress to detect backspace)
                // thank you @palerdot
                $el.is(':input') && $el.on('keyup keypress paste',function(e){
                    // This catches the backspace button in chrome, but also prevents
                    // the event from triggering too preemptively. Without this line,
                    // using tab/shift+tab will make the focused element fire the callback.
                    if (e.type=='keyup' && e.keyCode!=8) return;

                    // Check if timeout has been set. If it has, "reset" the clock and
                    // start over again.
                    if (timeoutReference) clearTimeout(timeoutReference);
                    timeoutReference = setTimeout(function(){
                        // if we made it here, our timeout has elapsed. Fire the
                        // callback
                        doneTyping(el);
                    }, timeout);
                }).on('blur',function(){
                    // If we can, fire the event since we're leaving the field
                    doneTyping(el);
                });
            });
        }
    });
})(jQuery);


$(document).ready(function() {
        $('#email').blur(function() {
            var email = $('#email').val();
            if (IsEmail(email) == false) {
                $('#sign-up').attr('disabled', true);
                $('#popover-email').removeClass('hide');
            } else {
                $('#popover-email').addClass('hide');
            }
        });
        $('#password').keyup(function() {
            var password = $('#password').val();
            if (checkStrength(password) == false) {
                $('#sign-up').attr('disabled', true);
            }
        });
        $('#confirm-password').blur(function() {
            if ($('#password').val() !== $('#confirm-password').val()) {
                $('#popover-cpassword').removeClass('hide');
                $('#sign-up').attr('disabled', true);
            } else {
                $('#popover-cpassword').addClass('hide');
            }
        });
        $('#contact-number').blur(function() {
            if ($('#contact-number').val().length != 10) {
                $('#popover-cnumber').removeClass('hide');
                $('#sign-up').attr('disabled', true);
            } else {
                $('#popover-cnumber').addClass('hide');
                $('#sign-up').attr('disabled', false);
            }
        });
        $('#sign-up').hover(function() {
            if ($('#sign-up').prop('disabled')) {
                $('#sign-up').popover({
                    html: true,
                    trigger: 'hover',
                    placement: 'below',
                    offset: 20,
                    content: function() {
                        return $('#sign-up-popover').html();
                    }
                });
            }
        });

        function IsEmail(email) {
            var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            if (!regex.test(email)) {
                return false;
            } else {
                return true;
            }
        }

        function checkStrength(password) {
            var strength = 0;


            //If password contains both lower and uppercase characters, increase strength value.
            if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)) {
                strength += 1;
                $('.low-upper-case').addClass('text-success');
                $('.low-upper-case i').removeClass('fa-file-text').addClass('fa-check');
                $('#popover-password-top').addClass('hide');


            } else {
                $('.low-upper-case').removeClass('text-success');
                $('.low-upper-case i').addClass('fa-file-text').removeClass('fa-check');
                $('#popover-password-top').removeClass('hide');
            }

            //If it has numbers and characters, increase strength value.
            if (password.match(/([a-zA-Z])/) && password.match(/([0-9])/)) {
                strength += 1;
                $('.one-number').addClass('text-success');
                $('.one-number i').removeClass('fa-file-text').addClass('fa-check');
                $('#popover-password-top').addClass('hide');

            } else {
                $('.one-number').removeClass('text-success');
                $('.one-number i').addClass('fa-file-text').removeClass('fa-check');
                $('#popover-password-top').removeClass('hide');
            }

            //If it has one special character, increase strength value.
            if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/)) {
                strength += 1;
                $('.one-special-char').addClass('text-success');
                $('.one-special-char i').removeClass('fa-file-text').addClass('fa-check');
                $('#popover-password-top').addClass('hide');

            } else {
                $('.one-special-char').removeClass('text-success');
                $('.one-special-char i').addClass('fa-file-text').removeClass('fa-check');
                $('#popover-password-top').removeClass('hide');
            }

            if (password.length > 7) {
                strength += 1;
                $('.eight-character').addClass('text-success');
                $('.eight-character i').removeClass('fa-file-text').addClass('fa-check');
                $('#popover-password-top').addClass('hide');

            } else {
                $('.eight-character').removeClass('text-success');
                $('.eight-character i').addClass('fa-file-text').removeClass('fa-check');
                $('#popover-password-top').removeClass('hide');
            }




            // If value is less than 2

            if (strength < 2) {
                $('#result').removeClass()
                $('#password-strength').addClass('progress-bar-danger');

                $('#result').addClass('text-danger').text('Very Week');
                $('#password-strength').css('width', '10%');
            } else if (strength == 2) {
                $('#result').addClass('good');
                $('#password-strength').removeClass('progress-bar-danger');
                $('#password-strength').addClass('progress-bar-warning');
                $('#result').addClass('text-warning').text('Week')
                $('#password-strength').css('width', '60%');
                return 'Week'
            } else if (strength == 4) {
                $('#result').removeClass()
                $('#result').addClass('strong');
                $('#password-strength').removeClass('progress-bar-warning');
                $('#password-strength').addClass('progress-bar-success');
                $('#result').addClass('text-success').text('Strength');
                $('#password-strength').css('width', '100%');

                return 'Strong'
            }

        }

    });





