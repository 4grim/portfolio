// Content Width Setting
	// On load
	$( document ).ready(function() {
		var pageWidth = $( document ).width();
		console.log(pageWidth);
		var contentWidth = pageWidth - 260;
		console.log(contentWidth);
		$( "#main-content" ).css( "width", contentWidth );
	})

	// On resize
	$(window).resize(function() {
		var pageWidth = $( document ).width();
		console.log(pageWidth);
		var contentWidth = pageWidth - 260;
		console.log(contentWidth);
		$( "#main-content" ).css( "width", contentWidth );
	});
// End Content Width Setting

// Project Image Height Generator
$( document ).ready(function() {
    var img = $('.project-image');
    var width = $(img).css('width');
    $(img).css('height', width);
})
// End Project Image Height Generator