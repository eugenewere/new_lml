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
               $(this).removeClass('hidden-mast')
         }else {
             $(this).addClass('hidden-mast');
             $('#usernonemessage').show()
         }
         if (valuee.toLowerCase() === 'all'){
             $('#usernonemessage').hide()
             $(this).removeClass('hidden-mast');
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
               $('#usernonemessage').hide()
               $(this).removeClass('hidden-mast')
         }else {
             $(this).addClass('hidden-mast');
             $('#usernonemessage').show()
         }
         if (valuee.toLowerCase() === 'all'){
             $('#usernonemessage').hide()
             $(this).removeClass('hidden-mast')
         }
    });
});

