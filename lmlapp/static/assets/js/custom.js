/*************************************
@@File: Job Stock  Template Custom Js

All custom js files contents are below
**************************************
* 01. Company Brand Carousel
* 02. Client Story testimonial
* 03. Bootstrap wysihtml5 editor
* 04. Tab Js
* 05. Add field Script
**************************************/

(function($){
"use strict";

	 
	 $(window).on('load', function () {
		$('.Loader').delay(350).fadeOut('slow');
		$('body').delay(350).css({ 'overflow': 'visible' });
	});


	 /*---Company Brand Carousel --*/
	 $("#company-brands").owlCarousel({
		items:5,
		itemsDesktop:[1199,5],
		itemsDesktopSmall:[979,4],
		itemsTablet:[768,3],
		itemsMobile: [600, 2],
		loop:true,
		pagination: false,
		navigation:false,
		navigationText:["",""],
		autoPlay:true
	});
	
	/*--- Client Story testimonial --*/
	$("#client-testimonial-slider").owlCarousel({
		items:3,
		itemsDesktop:[1199,3],
		itemsDesktopSmall:[979,2],
		itemsTablet:[768,1],
		pagination: false,
		navigation:false,
		navigationText:["",""],
		autoPlay:true
	});
	
	/*------ Grid Slider ----*/
	$('.grid-slide').slick({
		  slidesToShow:3,
		  arrows:false,
		  autoplay:true,
		  infinite: true,
		  responsive: [

			{
			  breakpoint: 988,
			  autoplay:true,
		      infinite: true,
			  settings: {
				arrows:false,
				centerMode: true,
				slidesToShow:2
			  }
			},{
			  breakpoint: 1085,
			  autoplay:true,
		      infinite: true,
			  settings: {
				arrows:false,
				centerMode: true,
				slidesToShow:4
			  }
			},
			{
			  breakpoint: 768,
			  autoplay:true,
		      infinite: true,
			  settings: {
				arrows:false,
				centerMode: true,
				slidesToShow:1
			  }
			},
			{
			  breakpoint: 480,
			  autoplay:true,
			  infinite: true,
			  settings: {
				arrows: false,
				centerPadding: '0px',
				slidesToShow: 1
			  }
			}
		  ]
	});
	
	/*------ Grid Slider ----*/
	$('.grid-slide-2').slick({
	  slidesToShow:3,
	  arrows:false,
	  autoplay:true,
	  infinite: true,
	  responsive: [
		{
		  breakpoint: 768,
		  settings: {
			arrows:false,
			centerMode: true,
			slidesToShow:1
		  }
		},
		{
		  breakpoint: 480,
		  settings: {
			arrows: false,
			centerPadding: '0px',
			slidesToShow: 1
		  }
		}
	  ]
	});
	
	$(document).ready(function () {
		// City Select
		$('.choose-city').select2();
		$('.choose-region').select2();
		// $('.choose-qualification').select2();
		// $('.choose-university').select2();
		// $('.choose-phd').select2();
		// $('.choose-bachelor').select2();
		// $('.choose-masters').select2();
		// $('.choose-diploma').select2();
		// $('.choose-certificate').select2();
		$('.choose-category').select2();
		$('.choose-category2').select2();
		$('.choose-entity').select2();
		$('.marital').select2();
		$('.marital2').select2();

	});





	// Category Select
	$('#j-category').select2({
		placeholder: "Choose Category...",
		allowClear: true
	});
	
	/*---Tab Js --*/
	$("#simple-design-tab a").on('click', function(e){
		e.preventDefault();
		$(this).tab('show');
	});
	
	/*-----Add field Script------*/
	$('.extra-field-box').each(function() {
    var $wrapp = $('.multi-box', this);

		$(".add-field", $(this)).click(function() {

			var multibox = document.getElementsByClassName('multi-box')[0];
			var new_id = multibox.children.length + 1;
			var duplicatedbox = multibox.getElementsByClassName('dublicat-box');
			var duplica =duplicatedbox[0].getElementsByClassName('duplicate');
			var x =duplica[0].getElementsByClassName('me');
			var select = x[0].getElementsByTagName('select')[0].getAttribute('id');
			var id = select+new_id;
			console.log(id);
			var f= x[0].getElementsByTagName('select')[0].getAttribute('id');

			$('.dublicat-box:last-child', $wrapp)
				.clone(true).appendTo($wrapp)
				.find('.qualifications')
				.attr('id', id).find('input')
				.val('')
				.find('select')
				.val('')
				.focus();
		});
    	$('.dublicat-box .remove-field', $wrapp).on('click', function() {
        if ($('.dublicat-box', $wrapp).length > 1)
            $(this).parent('.dublicat-box').remove();
		});
	});
			// var $wrapp = $('.multi-box');
			// var new_id = $wrapp.children.length + 1;
			// $('.dublicat-box:last-child', $wrapp).clone(true,true).appendTo($wrapp).find('input').val('').find('select').attr('id', new_id);

	//   Background image ------------------
		var a = $(".bg");
		a.each(function (a) {
			if ($(this).attr("data-bg")) $(this).css("background-image", "url(" + $(this).data("bg") + ")");
		});
		
		$('.slideshow-container').slick({
			slidesToShow: 1,
			autoplay: true,
			autoplaySpeed:2000,
			arrows: false,
			fade: true,
			cssEase: 'ease-in',
			infinite: true,
			speed:2000
		});
	
	
	// --------- Job List --------
	var options = {
		url: "./assets/js/resources/joblist.json",

		getValue: "name",

		list: {
			match: {
				enabled: true
			}
		}
	};
	$("#joblist").easyAutocomplete(options);

	// --------- Companies --------
	var options = {
		url: "./assets/js/resources/companies.json",

		getValue: "name",

		list: {
			match: {
				enabled: true
			}
		}
	};

	$("#companies").easyAutocomplete(options);
	
	// --------- Location --------
	var options = {
		url: "./assets/js/resources/location.json",

		getValue: "name",

		list: {
			match: {
				enabled: true
			}
		}
	};

	$("#location").easyAutocomplete(options);
		
	// Styles ------------------
    function csselem() {
        $(".slideshow-container .slideshow-item").css({
            height: $(".slideshow-container").outerHeight(true)
        });
        $(".slider-container .slider-item").css({
            height: $(".slider-container").outerHeight(true)
        });
    }
    csselem();	

	// $('.expduplicat button.remove-field2').each(function(){
	// 	console.log('this');
	// 	$(this).click(function (e) {
	// 		console.log($(this) , e);
	// 		if ($('.expduplicat').length > 1){
	// 		   $(this).parent().remove();
	// 		}
	// 	});
	// });


			
})(jQuery);
function changeToText(e) {
	var input = $(e).parent().parent().find('input');
	$(input).attr('type', 'text')
	jQuery(e).hide('fast',function () {
		jQuery(e).parent().find('.k12').show('fast');
	})


}
function changeToPassowrd(e) {
	var input = $(e).parent().parent().find('input');
	$(input).attr('type', 'password')
	jQuery(e).hide('fast',function () {
		jQuery(e).parent().find('.k11').show('fast');
	});

}
function openRightMenu() {
                document.getElementById("rightMenu").style.display = "block";
            }
function closeRightMenu() {
	document.getElementById("rightMenu").style.display = "none";
}
$(window).load(function() {
	// Animate loader off screen
	setTimeout(function () {
		 $(".Loader-bg").fadeOut('slow');
	}, 1000);

});
$('[data-toggle="tooltip"]').tooltip({ boundary: 'window' })
$(document).ready( function () {
	if($('#myTable').length){
		$('#myTable').DataTable();
	}

} );
var pswd = document.getElementsByClassName('password')[0];
var txt = document.getElementsByClassName('txt')[0];
var psd = document.getElementsByClassName('psd')[0];
function changeText() {
	pswd.setAttribute('type','text');
	psd.style.display="block";
	txt.style.display = "none";
	txt.style.transition = 0.4+"s";
}
function changePassword() {
	pswd.setAttribute('type','password');
	psd.style.display="none";
	txt.style.display = "block";
	txt.style.transition = 0.4+"s";
}
$('[data-reset-password]').click(function () {
	$('#logincontainer').hide('fast', function () {
		$('#resetemail').show('fast');
	});
});
$('[data-login-email]').click(function () {
	$('#resetemail').hide('fast', function () {
		$('#logincontainer').show('fast');
	});
});
var msgst = setInterval(getMessageStatus, 5000);
function getMessageStatus() {
	var location =  window.location.origin + "/ws/message_count/";
	$.ajax({
        url: location,
        type: 'GET',
        dataType: 'json', // added data type
        success: function(res) {setNotification(res)}
    });
}
function setNotification(data) {
	if(data.test === 'success'){
		if(data.msg_count === 0){
			$('.blob').fadeOut('slow');
			$('.message-txt').text('Message')
		}else {
			$('.blob').fadeIn('slow');
			$('.message-txt').text('Message ('+data.msg_count+')')
		}
	}
	else {
		// console.log('claerd')
		$('.blob').fadeOut('slow');
		$('.message-txt').text('Message');
		clearInterval(msgst);
	}
}
// Takes an array of hours as number and a function to execute
function executeOnHours(hours, callback) {
  callback(); // First, execute once
  let now = new Date();
  const hoursWithToogle = hours.map(h => {
    return {
      value: h,
      executedToday: now.getHours() === h // Don't run now if already on the given hour
    }
  });
  setInterval(() => {
    now = new Date();
    const triggers = hoursWithToogle.filter(h => {
      if (!h.executedToday && h.value === now.getHours()) {
        return h.executedToday = true;
      } else if (h.value !== now.getHours()) {
        h.executedToday = false; // Clean the boolean on the next hour
      }
    });
    if (triggers.length) callback(); // Trigger the action if some hours match
  }, 30000); // Fix a precision for the check, here 30s
}

executeOnHours([0, 12], function() {
  console.log('Something is done');
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
$('.shortlistcandidate').each(function () {
	$(this).click(function (e) {
		e.preventDefault();
		let idd = $(this).attr('data-candidate')
		const csrftoken = getCookie('csrftoken');
		var $item = $(this);
		var loc = window.location.origin + '/shortlist/'
		$.ajax({
			type: "POST",
			url : loc,
			data:{
				'customer_id' :idd,
			},
			headers: {
				'X-CSRFToken': csrftoken,
			},
			dataType:'json',
			success : function(data){
				if(data['success'] === 'success'){
					if(data['status'] === 'shortlisted'){
						swal.fire({
							title: "Success!",
							text: data['msg'],
							type: "success",
							confirmButtonText: "Ok"
					   });
					   $($item).text('');
					   $($item).append(
						   'Shortlisted  <i style="color: #06D15B; margin-left: auto" class="fas fa-check-circle"></i>'
					   )
					   $($item).closest('.paid-candidate-box').find('.paid-candidate-box-thumb').append(
						   '<i  class="fas fa-check-circle shortlist_noti_icon" data-toggle="tooltip" data-placement="right" title="You Have Shortlisted." style="color: #06D15B; position: absolute; left: 11px;top: 0; font-size: 19px;"></i>'
					   );
					   $('[data-toggle="tooltip"]').tooltip();
					}
					else if (data['status'] === 'unshortlisted'){
						swal.fire({
							title: "Success!",
							text: data['msg'],
							type: "success",
							confirmButtonText: "Ok"
					   });
					   $($item).text('');
					   $($item).append(
						   'Shortlist'
					   )
					   $($item).closest('.paid-candidate-box').find('.shortlist_noti_icon').hide();
					}
				}
				else if(data['error'] === 'error'){
					 swal.fire({
							title: "Error!",
							text: data['msg'],
							type: "error",
							confirmButtonText: "Cancel"
					   });

				}
			},
			error:function (data) {
				console.log(data);
			}

		});
	});
});
$('.shortlistcandidate2').each(function () {
	$(this).click(function (e) {
		e.preventDefault();
		let idd = $(this).attr('data-candidate')
		const csrftoken = getCookie('csrftoken');
		var $item = $(this);
		var loc = window.location.origin + '/shortlist/'
		$.ajax({
			type: "POST",
			url : loc,
			data:{
				'customer_id' :idd,
			},
			headers: {
				'X-CSRFToken': csrftoken,
			},
			dataType:'json',
			success : function(data){
				if(data['success'] === 'success'){
					if(data['status'] === 'shortlisted'){
						swal.fire({
							title: "Success!",
							text: data['msg'],
							type: "success",
							confirmButtonText: "Ok"
					   });
					   $('.shortlistcandidate2').fadeOut();
					}
					else if (data['status'] === 'unshortlisted'){
						swal.fire({
							title: "Success!",
							text: data['msg'],
							type: "success",
							confirmButtonText: "Ok"
					   });
					   $($item).text('');
					   $($item).append(
						   'Shortlist'
					   )
					   $($item).closest('.paid-candidate-box').find('.shortlist_noti_icon').hide();
					}
				}
				else if(data['error'] === 'error'){
					 swal.fire({
							title: "Error!",
							text: data['msg'],
							type: "error",
							confirmButtonText: "Cancel"
					   });

				}
			},
			error:function (data) {
				console.log(data);
			}

		});
	});
});
$('.shortlistcandidate3').each(function () {
	$(this).click(function (e) {
		e.preventDefault();
		let idd = $(this).attr('data-candidate')
		const csrftoken = getCookie('csrftoken');
		var $item = $(this);
		var loc = window.location.origin + '/shortlist/'
		$.ajax({
			type: "POST",
			url : loc,
			data:{
				'customer_id' :idd,
			},
			headers: {
				'X-CSRFToken': csrftoken,
			},
			dataType:'json',
			success : function(data){
				if(data['success'] === 'success'){
					if (data['status'] === 'unshortlisted'){
						swal.fire({
							title: "Success!",
							text: data['msg'],
							type: "success",
							confirmButtonText: "Ok"
					   });


					   setTimeout(function () {
							$($item).closest('.paid-candidate-container[data-parentorall=custm-'+idd+']').fadeOut(function () {
									$(this).remove();
							});
					   },1000);
						// console.log($($item).closest('.paid-candidate-container'));
					}
				}
				else if(data['error'] === 'error'){
					 swal.fire({
							title: "Error!",
							text: data['msg'],
							type: "error",
							confirmButtonText: "Cancel"
					   });
				}
			},
			error:function (data) {
				console.log(data);
			}

		});
	});
});