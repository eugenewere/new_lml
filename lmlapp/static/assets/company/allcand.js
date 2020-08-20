$('#sortselect').change(function () {
            var ascending = false;
            if($(this).val().toLowerCase() === 'az'){
                var sorted = $('#listtt .sortusers').sort(function(a,b){
                    return (ascending === ($(a).data('order') < $(b).data('order'))) ? 1 : -1;
                });
                ascending = ascending ? false : true;

                $('#listtt').html(sorted);
            }else if ($(this).val().toLowerCase() === 'za'){
                var sortedd = $('#listtt .sortusers').sort(function(a,b){
                    return (ascending === ($(a).data('order') < $(b).data('order'))) ? -1 : 1;
                });
                ascending = ascending ? true : false;

                $('#listtt').html(sortedd);

            }

    });
$('#sortstatus').change(function (){
    var valuee = $(this).val();
    $('.sortusers').each(function () {
         if(valuee.toLowerCase() === $(this).attr('data-status').toLowerCase()){
               $('#usernonemessage').hide();
               $(this).show('slow');
         }else {
             $(this).hide('slow');
             $('#usernonemessage').show();
         }
         if (valuee.toLowerCase() === 'all'){
             $('#usernonemessage').hide();
             $(this).fadeIn();
         }
    });
});
$(function () {
    $(".sortusers").slice(0, 8).show();
    $("#loadMore").on('click', function (e) {
        e.preventDefault();
        $(".sortusers:hidden").slice(0, 8).slideDown(function () {
            $('#usernonemessage').hide();
        });
        if ($(".sortusers:hidden").length === 0) {
            $("#loadMore").fadeOut('slow');
        }
        $('html,body').animate({
            scrollTop: $(this).offset().top
        }, 1500);

    });
});
$('[data-search4]').on('keyup', function() {
    var searchVal = $(this).val();
    var filterItems = $('[data-filter-item4]');

    if ( searchVal != '' ) {
        filterItems.addClass('hidden');
        $('[data-filter-item4][data-filter-name4*="' + searchVal.toLowerCase() + '"]').removeClass('hidden');
    } else {
        filterItems.removeClass('hidden');
    }
});
$('#sortjobtype').change(function (){
    var valuee = $(this).val();
    $('.sortusers').each(function () {
         if(valuee.toLowerCase() === $(this).attr('data-jobtype').toLowerCase()){
               $('#usernonemessage').hide();
               $(this).show('slow');
         }else {
             $(this).hide('slow');
             $('#usernonemessage').show();
         }
         if (valuee.toLowerCase() === 'all'){
             $('#usernonemessage').hide();
             $(this).fadeIn();
         }
    });
});

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