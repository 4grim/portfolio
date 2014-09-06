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