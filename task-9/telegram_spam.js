<script type="text/javascript">
var message = "Hi"; 
var count = 100 ; 
var i = 0 ;
var timer = setInterval(function(){
	document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = message;
	$('.im_submit').trigger('mousedown');	
	i++;
	if( i  == count )
	clearInterval(timer);
} , 1000 ) ;
</script>