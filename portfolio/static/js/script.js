// Main Site Navigation Highlighting for Page
$( document ).ready(function() {
	var pathnames = location.pathname;
	$('a.nav-link').each(function(i, o){ 
		if ($(o).attr('href') == pathnames) {
			$(o).css('background-color', '#59594C');
		}
	});
});
// End Main Site Navigation Highlighting for Page

// Project Image Height Generator
$( document ).ready(function() {
    var img = $('.project-image');
    var width = $(img).css('width');
    $(img).css('height', width);
})
// End Project Image Height Generator