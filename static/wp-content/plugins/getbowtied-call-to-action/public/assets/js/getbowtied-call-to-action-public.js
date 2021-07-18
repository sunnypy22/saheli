jQuery( function ($) {

	"use strict";

	if( typeof Cookies.get("keep_canvas_open") === 'undefined' ) {
		Cookies.set("keep_canvas_open", '1');
	}

	if( Cookies.get("keep_canvas_open") === '1' ) {
		$('body').addClass('show-call-to-action-canvas');
	}

	$('.call-to-action-toggle, .call-to-action-close').on( 'click', function() {
		$('body').toggleClass('show-call-to-action-canvas');

		Cookies.set("keep_canvas_open", $('body').hasClass('show-call-to-action-canvas') ? '1' : '0');
    });

	$('.call-to-action-latest-layout-image, .call-to-action-layout-image').on( 'click', function(e) {
		e.preventDefault();

		$('body').toggleClass('show-call-to-action-canvas');

		Cookies.set("keep_canvas_open", $('body').hasClass('show-call-to-action-canvas') ? '1' : '0');

		var button = $(this);
		setTimeout(function(){ $(location).attr( 'href', button.attr('href') ); }, 350);
    });
});
