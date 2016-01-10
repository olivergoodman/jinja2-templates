//script for personal page

//finding page title, sending to backend
function findTitle(){
	var title = document.getElementsByTagName("title")[0].innerHTML;
	$.get("/page_title/" + title);
}


//document ready
$(document).ready(function(){
	console.log("it's working");
	$('div.hidden').fadeIn(2000).removeClass("hidden"); //title not fading right now
	//$('div.slideR').animate({right: "-500px"}, 1000);
	$('div.slideL').animate({left: "-500px"}, 1000);

	findTitle();
});

