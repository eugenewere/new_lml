function shortlistmessage() {
            swal.fire({
            title: "Error!",
            text: "You have already shortlisted this user",
            type: "error",
            confirmButtonText: "Continue"
           });
        }
function shortlist(shortlist){

    var user = document.getElementById(shortlist.id);
    var company = user.getAttribute('data-employer');

     $.ajax({
        type: "POST",
        url : "{% url 'LML:shortlistemployees' %}",
        data:{
            'customer_id' : user.id,
            'company_id' : company,
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
        },
        dataType:'json',
        success : function searchSuccess(data){
            if(data.is_shortlisted){
                errorshortlisting(data);
                console.log();
            }
            else if(data.shortlisted){
               shortlisted(data);
               var user = document.getElementById(shortlist.id);
               user.innerText='Shortlisted';
               user.style.color='green';
            }
        },

    });
     function shortlisted(k){

        swal.fire({
        title: "Success!",
        text: k.success_message,
        type: "success",
        confirmButtonText: "Continue"
       });
    }
     function errorshortlisting(k){
        swal.fire({
        title: "Error!",
        text: k.error_message,
        type: "error",
        confirmButtonText: "Continue"
       });
    }

}
function shortlist2(shortlist){

    var user = $(shortlist).attr('data-customer')
    var company = $(shortlist).attr('data-employer')
    console.log(user, company)

     $.ajax({
        type: "POST",
        url : "{% url 'LML:shortlistemployees' %}",
        data:{
            'customer_id' : Number(user),
            'company_id' : Number(company),
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
        },
        dataType:'json',
        success : function searchSuccess(data){
            if(data.is_shortlisted){
                errorshortlisting(data);
                console.log();
            }
            else if(data.shortlisted){
               shortlisted(data);
               $('[data-shortlistbtn ]').fadeOut();
            }
        },

    });
     function shortlisted(k){

        swal.fire({
        title: "Success!",
        text: k.success_message,
        type: "success",
        confirmButtonText: "Continue"
       });
    }
     function errorshortlisting(k){
        swal.fire({
        title: "Error!",
        text: k.error_message,
        type: "error",
        confirmButtonText: "Continue"
       });
    }

}
$(function () {
    $(".sortskill").slice(0, 2).show();
    $(".sortexperience").slice(0, 2).show();
    $(".sorteducation").slice(0, 2).show();
    $("#loadMore").on('click', function (e) {
        e.preventDefault();
        $(".sortskill:hidden").slice(0, 2).slideDown();
        if ($(".sortskill:hidden").length === 0) {
            $("#loadMore").fadeOut('slow');
        }
        $('html,body').animate({
            scrollTop: $(this).offset().top
        }, 1500);

    });
    $("#loadMore2").on('click', function (e) {
        e.preventDefault();
        $(".sortexperience:hidden").slice(0, 2).slideDown();
        if ($(".sortexperience:hidden").length === 0) {
            $("#loadMore2").fadeOut('slow');
        }
        $('html,body').animate({
            scrollTop: $(this).offset().top
        }, 1500);

    });
    $("#loadMore3").on('click', function (e) {
        e.preventDefault();
        $(".sorteducation:hidden").slice(0, 2).slideDown();
        if ($(".sorteducation:hidden").length === 0) {
            $("#loadMore3").fadeOut('slow');
        }
        $('html,body').animate({
            scrollTop: $(this).offset().top
        }, 1500);

    });
});