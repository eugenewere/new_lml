$(document).ready(function(){
    $(function(){
    $(".customer").slice(0, 6).show();
    $("#load").click(function(e){
        e.preventDefault();
        $(".customer:hidden").slice(0, 6).show();
        if($(".customer:hidden").length == 0){
            spinner.hide();
            swal.fire({
                title: "Error!",
                text: "No more categories to load",
                type: "error",
                confirmButtonText: "Retry"
            });
        }
    });
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('.totop a').fadeIn();
        } else {
            $('.totop a').fadeOut();
        }
    });
});
    $('a[data-toggle="pill"]').on('show.bs.tab', function(e) {
        // console.log('yess');
        localStorage.setItem('activeTab5', $(e.target).attr('href'));
    });
        let activeTab2 = localStorage.getItem('activeTab5');
        if(activeTab2){
            $('#simple-design-tab1 a[href="' + activeTab2 + '"]').tab('show');
        }

    $('a[data-toggle="tab"]').on('show.bs.tab', function(e) {
        // console.log('yess');
        localStorage.setItem('activeTab6', $(e.target).attr('href'));
    });
    let activeTab = localStorage.getItem('activeTab6');
    if(activeTab){
        $('#simple-design2 a[href="' + activeTab + '"]').tab('show');
    }
    $('.text-edit').each(function () {
       ClassicEditor
        .create( document.querySelector( '#'+$(this).attr('id') ), {
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
    });
    setTimeout(function () {
        $('.lild').addClass('active');
    }, 3000)
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


    var endpoint = window.location.origin+'/candidateShortlistGraph/';
    var defaultData =  [];
    var labels = [];
    function initShortlistGraph() {
        $.ajax({
            method: "GET",
            url: endpoint,
            success: function (data) {
                labels = data.labels2;
                defaultData = data.defaultData2;
                setCustomerBar(labels, defaultData);
                // console.log(data);
            },
            error: function (error_data) {
                console.log(error_data);
            },
        });
    }
    initShortlistGraph();
    function  setCustomerBar(x, y){
             var ctx = document.getElementById('customers2').getContext('2d');
            var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: x,
                datasets: [{
                    label: 'Candidate Shortlist Bar',
                    data: y,
                    backgroundColor: [
                         'rgb(7, 177, 7, 50)',
                        'rgba(255, 159, 64, 1)',

                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgb(129,255,46)',
                        'rgb(255,217,66)',
                        'rgb(255,131,255)',
                        'rgb(1,53,255)',
                        'rgb(7, 177, 7)',
                        'rgb(36,255,221)',
                        'rgb(145,255,39)',
                    ],
                    borderColor: [
                        'rgba(255, 159, 64, 1)',
                        'rgb(7, 177, 7, 50)',
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgb(129,255,46)',
                        'rgb(255,217,66)',
                        'rgb(255,131,255)',
                        'rgb(1,53,255)',
                        'rgb(7, 177, 7)',
                        'rgb(36,255,221)',
                        'rgb(145,255,39)',

                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true,
                            stepSize: 1,
                        }
                    }]
                }
            }
        });
        }
    $('#statuspaychartselect').change(function () {
        var valuee = $(this).val();
        $('#customers2').remove(); // this is my <canvas> element
        $('#graph-container').append('<canvas id="customers2"><canvas>');
        var canvas = document.getElementById('customers2');
        var ctx =canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        if (valuee.toLowerCase() === 'bar'){
            var myChart = new Chart(ctx, {
                type: valuee.toLowerCase(),
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Candidates',
                            data: defaultData,
                            backgroundColor: [
                                 'rgb(7, 177, 7, 50)',
                                'rgba(255, 159, 64, 1)',

                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgb(129,255,46)',
                                'rgb(255,217,66)',
                                'rgb(255,131,255)',
                                'rgb(1,53,255)',
                                'rgb(7, 177, 7)',
                                'rgb(36,255,221)',
                                'rgb(145,255,39)',
                            ],
                            borderColor: [
                                'rgba(255, 159, 64, 1)',
                                'rgb(7, 177, 7, 50)',
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgb(129,255,46)',
                                'rgb(255,217,66)',
                                'rgb(255,131,255)',
                                'rgb(1,53,255)',
                                'rgb(7, 177, 7)',
                                'rgb(36,255,221)',
                                'rgb(145,255,39)',

                            ],
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: false,
                                stepSize:1
                            }
                        }]
                    }
                }
            });
        }
        else if (valuee.toLowerCase() === 'line'){
            var myChart = new Chart(ctx, {
                type: valuee.toLowerCase(),
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Candidates',
                            data: defaultData,
                            backgroundColor:'rgb(7, 177, 7, 50)',
                            borderColor:  'rgb(7,16,40)',
                            borderWidth: 1,
                            pointBorderColor: "#cbb668",
                            pointBackgroundColor: "#cbb668",
                        }
                    ]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: false,
                                stepSize:1
                            }
                        }]
                    }
                }
            });
        }
    });
    $('#shortlistformdata').change(function () {
        // console.log($(this).serialize());
        var registrationendpoint =window.location.origin+'/candidateShortlistGraphTime/';
        $.ajax({
            method: "POST",
            url : registrationendpoint,
            data: $(this).serialize(),
            success : function (data) {
                $('#shortlistreset').fadeIn();
                $('#customers2').remove(); // this is my <canvas> element
                $('#graph-container').append('<canvas id="customers2"><canvas>');
                labels = data['labels'];
                defaultData= data['companydata'];
                setCustomerBar(labels, defaultData);
            },
            error : function (error_data) {
                // console.log(error_data);
            },
        });
    });
    $('#shortlistreset').on('change', function () {
         var value = $(this).val();
         const csrftoken = getCookie('csrftoken');
         $.ajax({
            method: "POST",
            url : endpoint,
            data:{'value': value.toLowerCase()},
            headers: {
                'X-CSRFToken': csrftoken,  //for object property name, use quoted notation shown in second
            },
            dataType: 'json',
            success : function (data) {
                labels = data.labels2;
                defaultData= data.defaultData2;
                $('#customers2').remove(); // this is my <canvas> element
                $('#graph-container').append('<canvas id="customers2"><canvas>');
                setCustomerBar(labels, defaultData);
                // console.log(data);
            },
            error : function (error_data) {
                console.log(error_data);
            },
        });

    })
    $('#shortlistjoinreset').click(function () {
        $(this).hide();
        initShortlistGraph();
    });





    //all
        $('[data-search]').on('keyup', function() {
            var searchVal = $(this).val();
            var filterItems = $('[data-filter-item]');
            console.log(searchVal)

            if ( searchVal != '' ) {
                filterItems.addClass('hidden');
                $('[data-filter-item][data-filter-name*="' + searchVal.toLowerCase() + '"]').removeClass('hidden');
                console.log(searchVal + '11')
            } else {
                filterItems.removeClass('hidden');
                console.log(searchVal + '22')
            }
        });
        $('#sortselectall').change(function () {
            var ascending = false;
            if($(this).val().toLowerCase() === 'az'){
                var sorted = $('.c_all').sort(function(a,b){
                    return (ascending === ($(a).data('sort').toLowerCase() < $(b).data('sort').toLowerCase())) ? 1 : -1;
                });
                ascending = ascending ? false : true;
                $('#listall').html(sorted);
            }else if ($(this).val().toLowerCase() === 'za'){
                var sortedd = $('.c_all').sort(function(a,b){
                    return (ascending === ($(a).data('sort').toLowerCase() < $(b).data('sort').toLowerCase())) ? -1 : 1;
                });
                ascending = ascending ? true : false;
                $('#listall').html(sortedd);
            }
        });
        $(function () {
    $(".c_all").slice(0, 4).show();
    $("#loadall").on('click', function (e) {
        e.preventDefault();
        $(".c_all:hidden").slice(0, 4).slideDown(function () {

        });
        if ($(".c_all:hidden").length === 0) {
            $("#loadall").fadeOut('slow');
        }
        $("#tabcont").animate({ scrollTop: $('#tabcont').prop("scrollHeight")}, 1500);
    });
});
    //endall
    //basic
        $('[data-search2]').on('keyup', function() {
            var searchVal = $(this).val();
            var filterItems = $('[data-filter-item2]');

            if ( searchVal !== '' ) {
                filterItems.addClass('hidden');
                $('[data-filter-item2][data-filter-name2*="' + searchVal.toLowerCase() + '"]').removeClass('hidden');
            } else {
                filterItems.removeClass('hidden');
            }
        });
        $('#sortselectbasic').change(function () {
            var ascending = false;
            if($(this).val().toLowerCase() === 'az'){
                var sorted = $('.c_basic').sort(function(a,b){
                    return (ascending === ($(a).data('sort').toLowerCase() < $(b).data('sort').toLowerCase())) ? 1 : -1;
                });
                ascending = ascending ? false : true;
                $('#listbasic').html(sorted);
            }else if ($(this).val().toLowerCase() === 'za'){
                var sortedd = $('.c_basic').sort(function(a,b){
                    return (ascending === ($(a).data('sort').toLowerCase() < $(b).data('sort').toLowerCase())) ? -1 : 1;
                });
                ascending = ascending ? true : false;
                $('#listbasic').html(sortedd);
            }
        });
        $(function () {
            $(".c_basic").slice(0, 4).show();
            $("#loadbasic").on('click', function (e) {
                e.preventDefault();
                $(".c_basic:hidden").slice(0, 4).slideDown(function () {

                });
                if ($(".c_basic:hidden").length === 0) {
                    $("#loadbasic").fadeOut('slow');
                }
                $("#tabcont").animate({ scrollTop: $('#tabcont').prop("scrollHeight")}, 1500);
            });
        });
    //endbasic
    //premium
        $('[data-search3]').on('keyup', function() {
            var searchVal = $(this).val();
            var filterItems = $('[data-filter-item3]');

            if ( searchVal !== '' ) {
                filterItems.addClass('hidden');
                $('[data-filter-item3][data-filter-name3*="' + searchVal.toLowerCase() + '"]').removeClass('hidden');
            } else {
                filterItems.removeClass('hidden');
            }
        });
        $('#sortselectpremium').change(function () {
            var ascending = false;
            if($(this).val().toLowerCase() === 'az'){
                var sorted = $('.c_premium').sort(function(a,b){
                    return (ascending === ($(a).data('sort').toLowerCase() < $(b).data('sort').toLowerCase())) ? 1 : -1;
                });
                ascending = ascending ? false : true;
                $('#listpremium').html(sorted);
            }else if ($(this).val().toLowerCase() === 'za'){
                var sortedd = $('.c_premium').sort(function(a,b){
                    return (ascending === ($(a).data('sort').toLowerCase() < $(b).data('sort').toLowerCase())) ? -1 : 1;
                });
                ascending = ascending ? true : false;
                $('#listpremium').html(sortedd);
            }
        });
        $(function () {
            $(".c_premium").slice(0, 4).show();
            $("#loadpremium").on('click', function (e) {
                e.preventDefault();
                $(".c_premium:hidden").slice(0, 4).slideDown(function () {

                });
                if ($(".c_premium:hidden").length === 0) {
                    $("#loadpremium").fadeOut('slow');
                }
                $("#tabcont").animate({ scrollTop: $('#tabcont').prop("scrollHeight")}, 1500);
            });
        });
    //endpremium
    //ultimate
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
        $('#sortselectultimate').change(function () {
            var ascending = false;
            if($(this).val().toLowerCase() === 'az'){
                var sorted = $('.c_ultimate').sort(function(a,b){
                    return (ascending === ($(a).data('sort').toLowerCase() < $(b).data('sort').toLowerCase())) ? 1 : -1;
                });
                ascending = ascending ? false : true;
                $('#listultimate').html(sorted);
            }else if ($(this).val().toLowerCase() === 'za'){
                var sortedd = $('.c_ultimate').sort(function(a,b){
                    return (ascending === ($(a).data('sort').toLowerCase() < $(b).data('sort').toLowerCase())) ? -1 : 1;
                });
                ascending = ascending ? true : false;
                $('#listultimate').html(sortedd);
            }
        });
        $(function () {
            $(".c_ultimate").slice(0, 4).show();
            $("#loadultimate").on('click', function (e) {
                e.preventDefault();
                $(".c_ultimate:hidden").slice(0, 4).slideDown(function () {

                });
                if ($(".c_ultimate:hidden").length === 0) {
                    $("#loadultimate").fadeOut('slow');
                }
                $("#tabcont").animate({ scrollTop: $('#tabcont').prop("scrollHeight")}, 1500);
            });
        });
    //endultimate
        $('.pdf-btn').each(function () {
            $(this).on('click', function () {
                var file_name =  $(this).attr('data-tran');
                var id = $(this).closest('.receipt').find('.pdf-wrapper').attr('id');
                const element =document.getElementById(id);
                var opt = {
                    margin:       0.21,
                    filename:     file_name,
                    image:        {type: 'jpeg', quality: 1},
                    html2canvas:  {
                        scale: 7,
                        quality: 4,
                        imageTimeout:0,
                        logging: true,
                        letterRendering: true,
                        useCORS: true
                    },
                    jsPDF:  { unit: 'in', format: 'a4', orientation: 'portrait', floatPrecision:'smart' }
                };

                html2pdf()
                    .set(opt)
                    .from(element)
                    .toContainer()
                    .toCanvas()
                    .toImg()
                    .toPdf()
                    .save();
            });
        });
        $('#paymenttab').on('click ',function () {
           setTimeout(function () {
                $('.lild').addClass('active');
                $('.lilid2').addClass('active');
            }, 500)
        });


});

