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
    $('a[href="#top"]').click(function () {
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
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
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
// $('.filemanager--file .filemanager--remove').each(function(){
//     $(this).click(function (ee) {
//         console.log(ee)
//         ee.stopPropagation()
//         // setTimeout(function () {
//         //     $(this).closest('li').removeClass('ui-selected');
//         //     $('#clearAll').hide();
//         //     $('#detetemodal').hide();
//         // }, 4);
//     });
// });
$('form#fileform').submit( function (event) {
    event.preventDefault()
    var formdata = $(this).serializeArray();
    formdata.push({ name: "content-type", value: $('#fileform').attr('data-doc') });
    formdata.push({ name: "filee", value: $('#fileform input[type="file"]').val() });

    $('form#fileform').ajaxSubmit({
        type: "POST",
        url: $('form#fileform').attr('action'),
        success: function(result){
            if(result['success'] === 'success'){
                 swal.fire({
                    title: "Success!",
                    text: result['msg'],
                    type: "success",
                    confirmButtonText: "Retry"
                });
                 setTimeout(function () {
                     location.reload(true)
                 },1500)
            }
            else {
                 swal.fire({
                    title: "Error!",
                    text:  result['msg'],
                    type: "error",
                    confirmButtonText: "Retry"
                });
            }
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
    $('#inputGroupFile02').change(function(e){
        $('#rlabel').text(e.target.files[0].name + '  (' + formatFileSize(e.target.files[0].size, 2) +')');
        $('#filestatus').removeClass('text-danger text-success')
        $('#filestatus').text('')
        // {#$('form').attr('data-doc', e.target.files[0].type);#}
        $('#filed').val(e.target.files[0].type);

        var fileext = ["application/pdf", ]
        // console.log(e.target.files[0].type)
        if ( fileext.includes(e.target.files[0].type ) ) {
            // console.log( 'It is validated!' , e.target.files[0].size)
             $('#filestatus').removeClass('text-danger')
             $('#filestatus').addClass('text-success')
             $('#filestatus').text('Valid Document')
        }
        else {
             $('#filestatus').removeClass('text-success')
             $('#filestatus').addClass('text-danger')
             $('#filestatus').text('InValid Document. Only .pdf files are allowed')
            $('#inputGroupFile02').val('');
            $('#rlabel').text('Input was reset, please upload again a pdf file ');
            $('#rlabel').css('color','red')
        }
    });
    function formatFileSize(bytes,decimalPoint) {
       if(bytes === 0) return '0 Bytes';
       var k = 1000,
           dm = decimalPoint || 2,
           sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
           i = Math.floor(Math.log(bytes) / Math.log(k));
       return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }
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
    $('.file_delete').click(function () {
        let idd = $(this).attr('data-fid')
        const csrftoken = getCookie('csrftoken');
        var loc = window.location.origin + '/candidate_files_delete/'
        var data = {
            'file_id': idd,
            'X-CSRFToken': csrftoken
        }
        $.ajax({
            url: loc,
            type: 'POST',
            data: {
                'file_id': idd,
            },
            headers: {
                'X-CSRFToken': csrftoken,  //for object property name, use quoted notation shown in second
            },
            dataType: 'json',
            success: function (data) {
                // console.info(data);
                if(data['success'] === 'success'){
                    $('#filedeletemodal'+idd).modal('hide');
                    $('li[data-file='+idd+']').fadeOut()
                    swal.fire({
                        title: "Success",
                        text: data['msg'],
                        type: "success",
                        confirmButtonText: "Continue"
                    });
                    $('#filecount').text(data['files_count']+' Files');
                    $('#sotrageprogress').css('width', data['per']+'%');
                    $('#storagebytes').text('Storage '+data['size']+' Used');
                    $('.filemanager--info').html('');
                    $('.filemanager--info').append(
                       '<h5 style="padding: 19px 0;font-weight: bolder;">No Details</h5>'
                    );
                    if(data['per'] <= 85.00){
                        if($('#sotrageprogress').hasClass('progress-bar-danger')){
                            $('#sotrageprogress').removeClass('progress-bar-danger').addClass('progress-bar-success')
                            $('#storagealert').hide()
                        }
                    }
                }
                else if(data['error'] === 'error'){
                    // console.log(data)
                    swal.fire({
                        title: "Error",
                        text: data['msg'],
                        type: "error",
                        confirmButtonText: "Retry"
                    });
                }

            }
        });

    });
    $('#deleteSelected').click(function () {
        var file_ids = [];
        $('.filemanager--file.ui-selected').each(function () {
            file_ids.push($(this).attr('data-file'));
        });
        console.log(file_ids);
        const csrftoken = getCookie('csrftoken');
        var loc = window.location.origin + '/candidate_files_delete_multiple/'

        $.ajax({
            url: loc,
            type: 'POST',
            data: {'file_ids[]': file_ids,},
            headers: {'X-CSRFToken': csrftoken,},
            dataType: 'json',
            success: function (data) {
                // console.info(data);
                if(data['success'] === 'success'){
                    for (var ig of file_ids) {
                        $('li[data-file='+ig+']').fadeOut()
                    }
                    $('#filedeletemodalp').modal('hide');
                    // filedeletemodalp
                    $('#detetemodal, #clearAll').fadeOut();
                    swal.fire({
                        title: "Success",
                        text: data['msg'],
                        type: "success",
                        confirmButtonText: "Continue"
                    });
                    $('#filecount').text(data['files_count']+' Files');
                    $('#sotrageprogress').css('width', data['per']+'%');
                    $('#storagebytes').text('Storage '+data['size']+' Used');
                    $('.filemanager--info').html('');
                    $('.filemanager--info').append(
                       '<h5 style="padding: 19px 0;font-weight: bolder;">No Details</h5>'
                    );
                    if(data['per'] <= 85.00){
                        if($('#sotrageprogress').hasClass('progress-bar-danger')){
                            $('#sotrageprogress').removeClass('progress-bar-danger').addClass('progress-bar-success')
                            $('#storagealert').hide()
                        }
                    }
                }
                else if(data['error'] === 'error'){
                    console.log(data)
                    swal.fire({
                        title: "Error",
                        text: data['msg'],
                        type: "error",
                        confirmButtonText: "Retry"
                    });
                }
            }
        });
    });

});
















