 $('#defaultOpen').on("click",function () {
            $('.l1').show("fast");
            $("#all .holder").jPages({
                   containerID : "torsch",
                   perPage      : 8,
                   midRange     : 2,
                   startPage    : 1,
                   first       : false,
                   delay :0,
                   fallback :0,
                   previous: "◀",
                   next: "▶",
                   last        : false,
                   callback    : function( pages,items ){
                        $("#legend1").html("Page " + pages.current + " of " + pages.count);
                        $("#legend2").html(items.range.start + " - " + items.range.end + " of " + items.count);
                   }
                });
        });
$('#sentbtn').on("click",function () {
     $('.l2').show("fast");
     $("#sentt .holder").jPages({
           containerID : "torsch2",
           perPage      : 8,
           midRange     : 2,
           startPage    : 1,
           first       : false,
           previous: "◀",
           next: "▶",
           last        : false,
             delay :0,
           fallback :0,
           callback    : function( pages,items ){
                $("#legend3").html("Page " + pages.current + " of " + pages.count);
                $("#legend4").html(items.range.start + " - " + items.range.end + " of " + items.count);
           }
        });
});
$('#inbbtn').on("click",function () {
    $('.l3').show("fast");
    $("#inboxx .holder").jPages({
           containerID : "torsch3",
           perPage      : 8,
           midRange     : 2,
           startPage    : 1,
           first       : false,
           previous: "◀",
           next: "▶",
           last        : false,
            delay :0,
           fallback :0,
           callback    : function( pages,items ){
                $("#legend5").html("Page " + pages.current + " of " + pages.count);
                $("#legend6").html(items.range.start + " - " + items.range.end + " of " + items.count);
           }
        });
});
$('#strbtn').on("click",function () {
    $('.l4').show("fast");
    $("#starrd .holder").jPages({
           containerID : "torsch4",
           perPage: 8,
           midRange: 2,
           startPage: 1,
           first: false,
           previous: "◀",
           next: "▶",
           last        : false,
            delay :0,
           fallback :0,
           callback    : function( pages,items ){
                $("#legend7").html("Page " + pages.current + " of " + pages.count);
                $("#legend8").html(items.range.start + " - " + items.range.end + " of " + items.count);
           }
        });
});
$('#trashbtn').on("click",function () {
    $('.l7').show("fast");
    $("#trashhe .holder").jPages({
           containerID : "torsch7",
           perPage: 8,
           midRange: 2,
           startPage: 1,
           first: false,
           previous: "◀",
           next: "▶",
           last        : false,
        delay :0,
           fallback :0,
           callback    : function( pages,items ){
                $("#legend9").html("Page " + pages.current + " of " + pages.count);
                $("#legend10").html(items.range.start + " - " + items.range.end + " of " + items.count);
           }
        });
});
$('#prodbtn').on("click",function () {
    $('.l5').show("fast");
    $("#prodct .holder").jPages({
           containerID : "torsch5",
           perPage: 8,
           midRange: 2,
           startPage: 1,
           first: false,
           previous: "◀",
           next: "▶",
           last        : false,
            delay :0,
           fallback :0,
           callback    : function( pages,items ){
                $("#legend11").html("Page " + pages.current + " of " + pages.count);
                $("#legend12").html(items.range.start + " - " + items.range.end + " of " + items.count);
           }
        });
});
$('#workbtn').on("click",function () {
    $('.l6').show("fast");
    $("#workkk .holder").jPages({
           containerID : "torsch6",
           perPage: 8,
           midRange: 2,
           startPage: 1,
           first: false,
           previous: "◀",
           next: "▶",
           last        : false,
         delay :0,
           fallback :0,
           callback    : function( pages,items ){
                $("#legend13").html("Page " + pages.current + " of " + pages.count);
                $("#legend14").html(items.range.start + " - " + items.range.end + " of " + items.count);
           }
        });
});
$('#miscbtn').on("click",function () {
    $('.l8').show("fast");
    $("#misccc .holder").jPages({
           containerID : "torsch8",
           perPage: 8,
           midRange: 2,
           startPage: 1,
           first: false,
           previous: "◀",
           next: "▶",
           last        : false,
            delay :0,
           fallback :0,
           callback    : function( pages,items ){
                $("#legend15").html("Page " + pages.current + " of " + pages.count);
                $("#legend16").html(items.range.start + " - " + items.range.end + " of " + items.count);
           }
        });
});
$('#undbtn').on("click",function () {
                $('.l9').show("fast");
                $("#undeff .holder").jPages({
                       containerID : "torsch9",
                       perPage: 8,
                       midRange: 2,
                       startPage: 1,
                       first: false,
                       previous: "◀",
                       next: "▶",
                       last        : false,
                        delay :0,
                       fallback :0,
                       callback    : function( pages,items ){
                            $("#legend17").html("Page " + pages.current + " of " + pages.count);
                            $("#legend18").html(items.range.start + " - " + items.range.end + " of " + items.count);
                       }
                    });
            });

$(document).ready(function() {
    let activeTab = localStorage.getItem('activemessage');
    if (activeTab) {
        if (!$('#' + activeTab).hasClass(' active')) {
            $('#' + activeTab).addClass(' active')
            $('#' + activeTab).trigger('click');
        }

    }
    else {
        $('#defaultOpen').click();
        if (!$('#defaultOpen').hasClass(' active')) {
            $('#defaultOpen').addClass(' active')
        }

    }
});

function openCity(evt,k, cityName) {
      // Declare all variables
      localStorage.setItem('activemessage', k.id);
      var i, tabcontent, tablinks;

      // Get all elements with class="tabcontent" and hide them
      tabcontent = document.getElementsByClassName("tabcontentt");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }

      // Get all elements with class="tablinks" and remove the class "active"
      tablinks = document.getElementsByClassName("tablinks");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
      }

      // Show the current tab, and add an "active" class to the button that opened the tab
      document.getElementById(cityName).style.display = "block";
      evt.currentTarget.className += " active";
}