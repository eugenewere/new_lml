 $(document).ready(function () {
     // companyjoindate
    var endpoint2 = window.location.origin+'/lmladmin/company_graph/';
    var comapnyjoindata =  [];
    var companyjoinlabel = [];
    function companyjoin(){
        $.ajax({
            method: "GET",
            url : endpoint2,
            success : function (data) {
                companyjoinlabel = data.labels3;
                comapnyjoindata= data.defaultData3;
                setCompanyBarGraph();
            },
            error : function (error_data) {
                // console.log(error_data);
            },
        });
     }
    companyjoin();

    $('#companyjoinselect').change(function () {
        var valuee = $(this).val();
        $('#morris_totalrevenue23').remove(); // this is my <canvas> element
        $('#companyjoinchartwrapper').append('<canvas id="morris_totalrevenue23"><canvas>');
        var canvas = document.getElementById('morris_totalrevenue23');
        var ctx =canvas.getContext('2d');
        if (valuee.toLowerCase() === 'bar'){
            var myChart = new Chart(ctx, {
                type: valuee.toLowerCase(),
                data: {
                    labels: companyjoinlabel,
                    datasets: [
                        {
                            label: 'Companies',
                            data: comapnyjoindata,
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
        else if (valuee.toLowerCase() === 'line'){
            var myChart = new Chart(ctx, {
                type: valuee.toLowerCase(),
                data: {
                    labels: companyjoinlabel,
                    datasets: [
                        {
                            label: 'Companies',
                            data: comapnyjoindata,
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
    $('#formdata').change(function () {
        // console.log($(this).serialize());
        var endpointg = window.location.origin+'/lmladmin/company_graph_time_filter/';
        $.ajax({
            method: "POST",
            url : endpointg,
            data: $(this).serialize(),
            success : function (data) {
                $('#companyjoinreset').fadeIn();
                $('#morris_totalrevenue23').remove(); // this is my <canvas> element
                $('#companyjoinchartwrapper').append('<canvas id="morris_totalrevenue23"><canvas>');
                companyjoinlabel = data.labels3;
                comapnyjoindata= data.defaultData3;
                setCompanyBarGraph();
            },
            error : function (error_data) {
                console.log(error_data);
            },
        });
    });
    $('#companyjoinreset').click(function () {
        $('#companyjoinreset').hide();
        companyjoin();
    });
    function setCompanyBarGraph() {
        var ctx = document.getElementById('morris_totalrevenue23').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: companyjoinlabel,
                datasets: [{
                    label: 'Company',
                    data: comapnyjoindata,
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
                            stepSize:1
                        }
                    }]
                }
            }
        });
    }candidatejoinchart
    // companyjoindate




    var endpoint = window.location.origin+'/lmladmin/customer_graph/';
    var candidatejoindata =  [];
    var candidatejoinlabel = [];
    function candidatejoinchart(){
        $.ajax({
        method: "GET",
        url : endpoint,
        success : function (data) {
            candidatejoinlabel = data.labels2;
            candidatejoindata= data.defaultData2;
            setCustomerBarGraph();
        },
        error : function (error_data) {
            console.log(error_data);
        },
    });
    }
    candidatejoinchart();
    function setCustomerBarGraph() {
        var ctx = document.getElementById('candidatejoinchart').getContext('2d');

        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: candidatejoinlabel,
                datasets: [{
                    label: 'Customers ',
                    data: candidatejoindata,
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
                            stepSize: 1
                        }
                    }]
                }
            }
        });
    }
    $('#candidatejoinselect').change(function () {
        var valuee = $(this).val();
        $('#candidatejoinchart').remove(); // this is my <canvas> element
        $('#candidatejoinwrapper').append('<canvas id="candidatejoinchart"><canvas>');
        var canvas = document.getElementById('candidatejoinchart');
        var ctx =canvas.getContext('2d');
        if (valuee.toLowerCase() === 'bar'){
            var myChart = new Chart(ctx, {
                type: valuee.toLowerCase(),
                data: {
                    labels: companyjoinlabel,
                    datasets: [
                        {
                            label: 'Candidate',
                            data: candidatejoindata,
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
        else if (valuee.toLowerCase() === 'line'){
            var myChart = new Chart(ctx, {
                type: valuee.toLowerCase(),
                data: {
                    labels: candidatejoinlabel,
                    datasets: [
                        {
                            label: 'Candidate',
                            data: candidatejoindata,
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
    $('#candformdata').change(function () {
        // console.log($(this).serialize());
        var candidateendpointg = window.location.origin+'/lmladmin/candidate_graph_time_filter/';
        $.ajax({
            method: "POST",
            url : candidateendpointg,
            data: $(this).serialize(),
            success : function (data) {
                $('#candidatejoinreset').fadeIn();
                $('#candidatejoinchart').remove(); // this is my <canvas> element
                $('#candidatejoinwrapper').append('<canvas id="candidatejoinchart"><canvas>');
                candidatejoinlabel = data.labels3;
                candidatejoindata= data.defaultData3;
                setCustomerBarGraph();
            },
            error : function (error_data) {
                console.log(error_data);
            },
        });
    });
    $('#candidatejoinreset').click(function () {
        $('#candidatejoinreset').hide();
        candidatejoinchart();
    });




    var endpoin_reg = window.location.origin+'/lmladmin/registration_graph/';
    var reglabels= [];
    var company_data =[];
    var candidate_data =[];
    function initRegChart() {
        $.ajax({
            method: "GET",
            url : endpoin_reg,
            success : function (data) {

                reglabels = data['labels'];
                candidate_data= data['candidatedata'];
                company_data= data['companydata'];
                setRegChart();

            },
            error : function (error_data) {
                console.log(error_data);
            },
        });
    }
    initRegChart();
    function setRegChart(){
        var ctx = document.getElementById('registrationchart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: reglabels,
                datasets: [
                    {
                        label: 'Company',
                        data: company_data,
                        borderColor: [
                            'rgba(255, 159, 64, 1)',
                        ],
                        borderWidth: 1
                    },
                    {
                        label: 'Candidate',
                        data: candidate_data,

                        borderColor: [

                            'rgb(7, 177, 7, 50)',


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
    $('#regchartselect').change(function () {
        var valuee = $(this).val();
        $('#registrationchart').remove(); // this is my <canvas> element
        $('#registrationchartwrapper').append('<canvas id="registrationchart"><canvas>');
        var canvas = document.getElementById('registrationchart');
        var ctx =canvas.getContext('2d');
        if (valuee.toLowerCase() === 'bar'){
            var myChart = new Chart(ctx, {
                type: valuee.toLowerCase(),
                data: {
                    labels: reglabels,
                    datasets: [
                        {
                            label: 'Company',
                            data: company_data,
                            backgroundColor:  'rgb(7, 177, 7, 50)',
                            borderColor: 'rgba(255, 159, 64, 1)',
                            borderWidth: 1
                        },
                        {
                            label: 'Candidate',
                            data: candidate_data,
                            backgroundColor: 'rgba(255, 159, 64, 1)',
                            borderColor: 'rgb(7, 177, 7, 50)',
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
        }else if (valuee.toLowerCase() === 'line'){
            var myChart = new Chart(ctx, {
                type: valuee.toLowerCase(),
                data: {
                    labels: reglabels,
                    datasets: [
                        {
                            label: 'Company',
                            data: company_data,
                            borderColor: [
                                'rgba(255, 159, 64, 1)',
                            ],
                            borderWidth: 1
                        },
                        {
                            label: 'Candidate',
                            data: candidate_data,

                            borderColor: [

                                'rgb(7, 177, 7, 50)',


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
    });
    $('#registrationformdata').change(function () {
        // console.log($(this).serialize());
        var registrationendpoint = window.location.origin+'/lmladmin/registration_graph_time/';
        $.ajax({
            method: "POST",
            url : registrationendpoint,
            data: $(this).serialize(),
            success : function (data) {
                $('#registrationjoinreset').fadeIn();
                $('#registrationchart').remove();
                $('#registrationchartwrapper').append('<canvas id="registrationchart"><canvas>');
                reglabels = data['labels'];
                candidate_data= data['candidatedata'];
                company_data= data['companydata'];
                setRegChart();
            },
            error : function (error_data) {
                // console.log(error_data);
            },
        });
    });
    $('#registrationjoinreset').click(function () {
        $(this).hide();
        initRegChart();
    });




    var endpoin_status_pay = window.location.origin+'/lmladmin/companystatuspaymentgraph/';
    var reg_statuslabels= [];
    var statuscompany_data =[];
    var stepSize = 100000;
    initstatuspaychart();
    function initstatuspaychart(){
        $.ajax({
            method: "GET",
            url : endpoin_status_pay,
            success : function (data) {
                reg_statuslabels = data['labels'];
                statuscompany_data= data['companydata'];
                setStatusPayChart()
            },
            error : function (error_data) {
                console.log(error_data);
            },
        });
    }
    function setStatusPayChart() {
         var ctx = document.getElementById('statuspaychart').getContext('2d');
         var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: reg_statuslabels,
                    datasets: [
                        {
                            label: 'Company',
                            data: statuscompany_data,
                            backgroundColor:  'rgb(7, 177, 7, 50)',
                            borderColor:  'rgba(255, 159, 64, 1)',
                            borderWidth: 1
                        },
                    ]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: false,
                                stepSize:stepSize,
                            }
                        }]
                    }
                }
            });
    }

    $('#statuspaychartselect').change(function () {
        var valuee = $(this).val();
        $('#statuspaychart').remove();
        $('#statuspaychartwrapper').append('<canvas id="statuspaychart"><canvas>');
        var canvas = document.getElementById('statuspaychart');
        var ctx =canvas.getContext('2d');
        var myChart = new Chart(ctx, {
            type: valuee.toLowerCase(),
            data: {
                labels: reg_statuslabels,
                datasets: [
                    {
                        label: 'Company Status Payment',
                        data: statuscompany_data,
                        backgroundColor:  'rgb(7, 177, 7, 50)',
                        borderColor: 'rgba(255, 159, 64, 1)',
                        borderWidth: 1
                    },
                ]
            },
            pointStyle:'crossRot',
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: false,
                            stepSize:stepSize,
                        }
                    }]
                }
            }
        });
    });
    $('#statuspaychartselectformdata').change(function () {
        // console.log($(this).serialize());
        var registrationendpoint = window.location.origin+'/lmladmin/companystatuspaymentgraphtime/';
        $.ajax({
            method: "POST",
            url : registrationendpoint,
            data: $(this).serialize(),
            success : function (data) {
                $('#statuspaychartselectreset').fadeIn();
                $('#statuspaychart').remove();
                $('#statuspaychartwrapper').append('<canvas id="statuspaychart"><canvas>');
                reg_statuslabels = data['labels'];
                statuscompany_data= data['companydata'];
                setStatusPayChart();
            },
            error : function (error_data) {
                // console.log(error_data);
            },
        });
    });
    $('#statuspaychartselectreset').click(function () {
        $(this).hide();
        stepSize = 100000;
        initstatuspaychart();
    });
    $('#stepsize').keyup(function () {
        var v = $(this).val();
        // console.log(v , 'rfrrr');
        if(v >= 50000){
            // console.log(v);
            stepSize = v;
            $('#statuspaychartselectreset').fadeIn();
            $('#statuspaychart').remove();
            $('#statuspaychartwrapper').append('<canvas id="statuspaychart"><canvas>');
            setStatusPayChart();
        }
    });







 });
