
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
$('#gridview').click( function () {
if(! $(this).hasClass('active')){
$('#listview').removeClass('active')
$(this).addClass('active')
}
if($(".filemanager--files").hasClass('ui-container filemanager--list')){
 console.log('grid')
$('.filemanager--files').removeClass('ui-container filemanager--list')
}
});
$('#listview').click(function () {
    if(! $(this).hasClass('active')){
        $('#gridview').removeClass('active')
        $(this).addClass('active')

    }
    if(!$(".filemanager--files").hasClass('ui-container filemanager--list')){
        console.log('list')
        $('.filemanager--files').addClass('ui-container filemanager--list')
    }
});

$('.filemanager--file').each(function () {
$(this).click(function () {
var fname =$(this).attr('data-filename');
var titlee =$(this).attr('data-titlee');
var desc =$(this).attr('data-desc');
var sizee =$(this).attr('data-sizee');

$('.filemanager--info').html('')
$('.filemanager--info').append(
    '<h5 style="padding: 19px 0;font-weight: bolder;">File '+ titlee +' details</h5>'+
    '<ul>'+
       ' <li style="height: 95px;">'+
            '<div class="filemanager--fileicon">'+
               '<span style="color: #2AC27B;" class="fas fa-file-pdf"></span>'+
            '</div>'+
        '</li>'+
        '<li data-toggle2="tooltip" data-toggle="tooltip" data-placement="top" title="Name: '+ fname +'"><span style="font-weight: bolder;">Name: </span> '+ fname +'</li>'+
        '<li data-toggle2="tooltip" data-toggle="tooltip" data-placement="top" title="Size: '+ sizee +'"><span style="font-weight: bolder;">Size: </span> '+ sizee +'</li>'+
        '<li data-toggle2="tooltip" data-toggle="tooltip" data-placement="top" title="Title: '+ titlee +'"><span style="font-weight: bolder;">Title: </span> '+ titlee +'</li>'+
        '<li data-toggle2="tooltip" data-toggle="tooltip" data-placement="top" title="Details: '+ desc +'"><span style="font-weight: bolder;">Details: </span></br> '+ desc +'</li>'+
    '</ul>'
)
$('[data-toggle2="tooltip"]').tooltip()
});
});
$('#selectAll').click(function () {
$('.filemanager--file').each(function () {
$(this).addClass('ui-selected');
});
$('#clearAll').fadeIn();
$('#detetemodal').fadeIn();
});
$('#clearAll').click(function () {
if($('.filemanager--file').hasClass('ui-selected')){
$('.filemanager--file').removeClass('ui-selected');
}
if($('.ui-selected').length  === 0 ){
$(this).fadeOut();
$('#detetemodal').fadeOut();
}

});
$('.filemanager--file').each(function(){
$(this).click(function (e) {
// console.log(e)
if(e.target.className.toLowerCase() !== 'filemanager--remove ttb' && e.target.className.toLowerCase() !== 'fas fa-caret-down'){

    if($(this).hasClass('ui-selected')){
        $(this).removeClass('ui-selected')
    }else {
        $(this).addClass('ui-selected');
    }
    if($('.ui-selected').length  === 0 ){
       $('#clearAll').fadeOut();
        $('#detetemodal').fadeOut();
    }else {
        $('#clearAll').fadeIn();
    $('#detetemodal').fadeIn();
    }
}


});
});
$("[data-search]").on("keyup", function() {
          var value = $(this).val().toLowerCase();

          if(value !== '') {
            $(".filemanager--file").filter(function() {
              $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
          } else {
              $(".filemanager--file").show();
          }
        });