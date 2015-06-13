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

$("#graph1_plot").click(function(){
    $("#graph1_canvas").hide();
    $("#loader1").show();
    $.post( "/bargraph/", { city1: $("#city_sel1").val(), city2: $("#city_sel2").val() })
      .done(function( data ) {
          $("#loader").hide();
          $("#graph1_canvas").show();
          $("#graph1_canvas").attr("src",data);


      }).fail(function(data){
        alert("An Error Occured!");
        $("#loader").hide();
        alert(data);


      });
});

$("#graph2_plot").click(function(){
    $("#graph2_canvas").hide();
    $("#loader2").show();
    $.post( "/line/", { year: $("#year").val(), city: $("#city").val() })
      .done(function( data ) {
          $("#loader").hide();
          $("#graph2_canvas").show();
          $("#graph2_canvas").attr("src",data);


      }).fail(function(data){
        alert("An Error Occured!");
        $("#loader").hide();
        alert(data);


      });
});