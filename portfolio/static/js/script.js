// Content Width Setting
	// On load
	$( document ).ready(function() {
		var pageWidth = $( document ).width();
		var contentWidth = pageWidth - 260;
		var heroWidth = pageWidth - 200;
		if ( document.getElementById( "hero" ) ) {
			$( "#hero" ).css( "width", heroWidth );
		}
		$( "#content-margin" ).css( "width", contentWidth );
	})

	// On resize
	$(window).resize(function() {
		var pageWidth = $( document ).width();
		var contentWidth = pageWidth - 260;
		var heroWidth = pageWidth - 200;
		if ( document.getElementById( "hero" ) ) {
			$( "#hero" ).css( "width", heroWidth );
		}
		$( "#content-margin" ).css( "width", contentWidth );
	});
// End Content Width Setting

// Project Image Height Generator
$( document ).ready(function() {
    var img = $('.project-image');
    var width = $(img).css('width');
    $(img).css('height', width);
})
// End Project Image Height Generator