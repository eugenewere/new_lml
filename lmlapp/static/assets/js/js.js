
    function openDisability() {
    var disability = document.getElementsByClassName('des')[0];

        disability.style.display="block";
        disability.setAttribute('required','required');
    }
    function closeDisability() {
     var disability = document.getElementsByClassName('des')[0];
        disability.style.display="none";
        if (disability.hasAttribute('required')){
            disability.removeAttribute('required');
        }

    }




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




    function showEmployment() {
        var clonebutton1 = document.getElementById('clonebutton1');
        var clonebutton2 = document.getElementById('clonebutton2');
        var employer = document.getElementsByClassName('employerwrapper');

         for(i=0; i<employer.length; i++){
            employer[i].style.display="block";
            // employer[i].setAttributeNode('required')[i]
            // employer[i].getElementsByTagName('textarea')[i].setAttribute('required','required');

         }

         // for(x=0; x<employer.length; x++){
         //    employer[x].getElementsByTagName('input')[x].setAttribute('required','required');
         // }
        clonebutton1.style.display = "block";
        clonebutton2.style.display = "block";
    }
    function hideEmployment() {
        var clonebutton1 = document.getElementById('clonebutton1');
        var clonebutton2 = document.getElementById('clonebutton2');
        var employer = document.getElementsByClassName('employerwrapper');

        for(i=0; i<employer.length; i++){
            employer[i].style.display="none";

        }
         clonebutton1.style.display = "none";
         clonebutton2.style.display = "none";
    }


function readURL(input) {

if (input.files && input.files[0]) {
    var reader = new FileReader();
     var disclaimer= document.getElementById("disclaimer");
        reader.onload = function (element) {
            $('.blah').attr('src', element.target.result).css('visibility', 'visible');
            disclaimer.style.visibility = "hidden";
        };
        reader.readAsDataURL(input.files[0]);
        }
    }




// (function ($) {
//     // USE STRICT
//     "use strict";
//     $(".animsition").animsition({
//       inClass: 'fade-in-left',
//       outClass: 'fade-out-right',
//       inDuration: 900,
//       outDuration: 900,
//       linkElement: 'a:not([target="_blank"]):not([href^="#"]):not([class^="chosen-single"]):not([class^="not_a_link"]) textarea:not([class^="form-control"])',
//       loading: true,
//       loadingParentElement: 'html',
//       loadingClass: 'Loader-bg',
//       loadingInner: '<div class="loader">' +
//                           '<span></span>' +
//                           '<span></span>' +
//                           '<span></span>' +
//                           '<span></span>' +
//                       '</div>',
//       timeout: false,
//       touchSupport  :   true,
//       timeoutCountdown: 5000,
//       onLoadEvent: true,
//       browser: ['animation-duration', '-webkit-animation-duration'],
//       overlay: false,
//       overlayClass: 'animsition-overlay-slide',
//       overlayParentElement: 'body',
//       transition: function (url) {
//         window.location.href = url;
//       }
//     });
//
//
//   })(jQuery);


//  $(function () {
//    $('#search').onclick(function shortlist(data) {
//        $(".search-results-wrapper").removeClass("search-results-wrapper").addClass("search-results-wrapper-active");
//        $.ajax({
//            type: "POST",
//            url : "{% url 'Shoppy:searchbar' %}",
//            data:{
//                'search_text' : $('#search').val(),
//                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
//            },
//            success : searchSuccess,
//            dataType:'html',
//        });
//        var search = document.getElementById('search').value;
//        var search_result= document.getElementById('searchwrapper');
//        if(search.length === 0){
//            search_result.classList.remove('search-results-wrapper-active');
//            search_result.classList.add('search-results-wrapper');
//        }
//    });
// });
// function searchSuccess(data, textStatus, jqXHR){
//    $('#search_results').html(data);
// }




// var logo = document.getElementById("upload-pic");
//         var first_name = document.getElementById('firstname');
//         var last_name = document.getElementById('lastname');
//         var gender = document.getElementById('gender');
//         var email = document.getElementById('email');
//         var username = document.getElementById('username');
//         var phonnumber = document.getElementById('phonnumber');
//         var dateofbirth = document.getElementById('dateofbirth');
//         var maritalstatus = document.getElementById('maritalstatus');
//         var job_type = document.getElementById('job_type');
//         var category = document.getElementById('category');
//
//         var disability_choice = document.getElementsByClassName('disability_choice');
//
//         var disability = document.getElementById('disability');
//         var country = document.getElementById('country');
//         var county = document.getElementById('county');
//         var region = document.getElementById('region');
//         var landmark = document.getElementById('landmark');
//
//         var qualifications = document.querySelectorAll('[name=qualifications]');
//         var course = document.querySelectorAll('[name=course]');
//         var graduation_date = document.querySelectorAll('[name=graduation_date]');
//         var school = document.querySelectorAll('[name=school]');
//         var reg_number = document.querySelectorAll('[name=reg_number]');
//
//         var biography = document.querySelectorAll('[name=biography]');
//
//         var employer_name = document.querySelectorAll('[name=employer_name]');
//         var company_name = document.querySelectorAll('[name=company_name]');
//         var company_email = document.querySelectorAll('[name=company_email]');
//         var company_phone = document.querySelectorAll('[name=company_phone]');
//         var position_held = document.querySelectorAll('[name=position_held]');
//         var date_from = document.querySelectorAll('[name=date_from]');
//         var date_to = document.querySelectorAll('[name=date_to]');
//         var experience = document.querySelectorAll('[name=experience]');
//
//         var skill = document.querySelectorAll('[name=skill]');
//         var referee = document.querySelectorAll('[name=referee]');
//         var referee_phonenumber = document.querySelectorAll('[name=referee_phonenumber]');
//
//         var account_url = document.querySelectorAll('[name=account_url]');
//         var password1 = document.querySelectorAll('[name=password1]');
//         var password2 = document.querySelectorAll('[name=password2]');

// 'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
//                 "profile_image":logo.val(),
//                 "first_name":first_name.val(),
//                 "last_name":last_name.val(),
//                 "gender":gender.val(),
//                 "email":email.val(),
//                 "username":username.val(),
//                 "phone_number":phonnumber.val(),
//                 "date_of_birth":dateofbirth.val(),
//                 "marital_status":maritalstatus.val(),
//                 "job_type":job_type.val(),
//                 "category":category.val(),
//
//                 "disability_choice":disability_choice.val(),
//                 "disability":disability.val(),
//                 "country":country.val(),
//                 "county":county.val(),
//                 "region":region.val(),
//                 "landmark":landmark.val(),
//
//                 "qualifications":qualifications.val(),
//                 "school":school.val(),
//                 "course":course.val(),
//                 "graduation_date":graduation_date.val(),
//                 "reg_number":reg_number.val(),
//                 "biography":biography.val(),
//                 "employer_name":employer_name.val(),
//                 "company_name":company_name.val(),
//                 "company_email":company_email.val(),
//                 "company_phone":company_phone.val(),
//                 "position_held":position_held.val(),
//                 "date_from":date_from.val(),
//                 "date_to":date_to.val(),
//                 "experience":experience.val(),
//
//                 "skill":skill.val(),
//                 "referee":referee.val(),
//                 "referee_phonenumber":referee_phonenumber.val(),
//
//                 "account_url":account_url.val(),
//                 "password1":password1.val(),
//                 "password2":password2.val(),