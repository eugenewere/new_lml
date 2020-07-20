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

			$('.dublicat-box:last-child', $wrapp).clone(true,true).appendTo($wrapp).find('.qualifications').attr('id', id).find('input').val('').find('select').val('').focus();
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
	

			
})(jQuery);