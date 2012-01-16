window.onload=function(){
	
	var offsetLeft=$('menu').offsetLeft;
	Event.observe('menu', 'mousemove', function(event){
		
		coordinateX=Event.pointerX(event)-offsetLeft;
		$('slider').style.marginLeft=coordinateX-20+'px';
		
	});
	
}



