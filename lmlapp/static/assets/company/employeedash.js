$(function(){
    $(".customer").slice(0, 6).show(); // select the first ten
    $("#load").click(function(e){ // click event for load more
        e.preventDefault();
        $(".customer:hidden").slice(0, 6).show(); // select next 10 hidden divs and show them
        if($(".customer:hidden").length == 0){ // check if any hidden divs still exist
            spinner.hide();
            swal.fire({
                title: "Error!",
                text: "No more categories to load",
                type: "error",
                confirmButtonText: "Retry"
            });
        }
    });
    $('a[href=#top]').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 600);
        return false;
    });

    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('.totop a').fadeIn();
        } else {
            $('.totop a').fadeOut();
        }
    });

});
$(document).ready(function(){
    $('a[data-toggle="pill"]').on('show.bs.tab', function(e) {

        localStorage.setItem('activeTab2', $(e.target).attr('href'));
    });
    var activeTab = localStorage.getItem('activeTab2');
    if(activeTab){
        $('#simple-design-tab a[href="' + activeTab + '"]').tab('show');
    }
});