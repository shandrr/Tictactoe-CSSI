$(document).ready(function() {
	
	//tab

	$(".tab_content").hide(); //hide all content
	$("ul.tabs li:first").addClass("active").show(); //activate first tab
	$(".tab_content:first").show(); //show first tab content

	$("ul.tabs li").click(function() {

		$("ul.tabs li").removeClass("active"); //remove "active" class
		$(this).addClass("active"); //add "active" class to selected tab
		$(".tab_content").hide(); //hide all tab content

		var activeTab = $(this).attr("title"); //sets variable "activeTab" to list item title
		$(activeTab).fadeIn(); //fade in ID set to activeTab
		return false;
	});
});


window.onload=function(){
	
	var offsetLeft=$('menu').offsetLeft;
	Event.observe('menu', 'mousemove', function(event){
		
		coordinateX=Event.pointerX(event)-offsetLeft;
		$('slider').style.marginLeft=coordinateX-20+'px';
		
	});
	
}
