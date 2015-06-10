// On Hover Events..
$("#graph1_init").hover(
    	              
    	              function(){
    	              	
    	                  $("#graph1_desc").slideDown()
    	              }
    	              ,
    	              function(){
    	              	
    	              	$("#graph1_desc").slideUp();
                      }
                    ); 
    $("#graph2_init").hover(
    	              
    	              function(){
    	              	
    	                  $("#graph2_desc").slideDown()
    	              }
    	              ,
    	              function(){
    	              	
    	              	$("#graph2_desc").slideUp();
                      }
                    ); 
    $("#graph3_init").hover(
    	              
    	              function(){
    	              	
    	                  $("#graph3_desc").slideDown()
    	              }
    	              ,
    	              function(){
    	              	
    	              	$("#graph3_desc").slideUp();
                      }
                    ); 

// On Click Events
$("#graph1_init").click(function(){
    $("#dashboard_icons").slideUp();
    $("#graph2_wrapper").slideUp();
    $("#graph3_wrapper").slideUp();
    $("#about_desc").slideUp();
    $("#graph1_wrapper").slideDown();

});
$("#graph2_init").click(function(){
    $("#dashboard_icons").slideUp();
    $("#graph1_wrapper").slideUp();
    $("#graph3_wrapper").slideUp();
    $("#about_desc").slideUp();
    $("#graph2_wrapper").slideDown();

});
$("#graph3_init").click(function(){
    $("#dashboard_icons").slideUp();
    $("#graph1_wrapper").slideUp();
    $("#graph2_wrapper").slideUp();
    $("#about_desc").slideUp();
    $("#graph3_wrapper").slideDown();

});
$("#graph1_init_side").click(function(){
    $("#dashboard_icons").slideUp();
    $("#graph2_wrapper").slideUp();
    $("#graph3_wrapper").slideUp();
    $("#about_desc").slideUp();
    $("#graph1_wrapper").slideDown();

});
$("#graph2_init_side").click(function(){
    $("#dashboard_icons").slideUp();
    $("#graph1_wrapper").slideUp();
    $("#graph3_wrapper").slideUp();
    $("#about_desc").slideUp();
    $("#graph2_wrapper").slideDown();

});
$("#graph3_init_side").click(function(){
    $("#dashboard_icons").slideUp();
    $("#graph1_wrapper").slideUp();
    $("#graph2_wrapper").slideUp();
    $("#about_desc").slideUp();
    $("#graph3_wrapper").slideDown();

});

$("#dashboard").click(function(){
    $("#graph1_wrapper").slideUp();
    $("#graph2_wrapper").slideUp();
    $("#graph3_wrapper").slideUp();
    $("#about_desc").slideUp();
    $("#dashboard_icons").slideDown();

});

$("#dashboard_side").click(function(){
    $("#graph1_wrapper").slideUp();
    $("#graph2_wrapper").slideUp();
    $("#graph3_wrapper").slideUp();
    $("#graph3_wrapper").slideUp();
    $("#about_desc").slideUp();
    $("#dashboard_icons").slideDown();

});

$("#about").click(function(){
    $("#graph1_wrapper").slideUp();
    $("#graph2_wrapper").slideUp();
    $("#graph3_wrapper").slideUp();
    $("#dashboard_icons").slideUp();
    $("#about_desc").slideDown();

});

