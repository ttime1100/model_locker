$(function() {
	// body...


 // $('body').hide();

  /* $(window).on("scroll", function(){
         if( $(this).scrollTop() > 10 ){
             $("nav.navbar").addClass("mybg-dark");
             $(".navbar-dark .navbar-nav .nav-link").css({"color" : "#fff"});
             
         }else{
            $("nav.navbar").removeClass("mybg-dark");
             $(".navbar-dark .navbar-nav .nav-link").css({"color" : "rgba(255,255,255,.5)"});
         }
      });
     */
      
     $(document).ready(function(){
  $(".fancybox").fancybox({
        openEffect: "none",
        closeEffect: "none"
    }); 
     });
    
     $(function(){
		$(".myform").on("click", function(e){
			$("body").toggleClass("myoverlay");
		
		});
		$(document).on("click",function(e){
			if( $(e.target).is("body, .myform") == false ){
				$("body").removeClass("myoverlay");
			}
		});
	
	});
      
      $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
      });
      
      





});
