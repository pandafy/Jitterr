$(document).ready(function(){
    
    var fakedata = ['test1','test2','test3','mohit','ietsanders'];

    $(".search-bar").autocomplete({
        appendTo: "#results",
        source : fakedata,
	
    });

    $(".search-bar").change(function(){
        if($(this).val().length != 0)
            $('.fa.fa-search').hide()
        else    
        $('.fa.fa-search').show()
    })

    //text area
    $("textarea").focusin(function(){
        $(this).css("height", "47px");
      });
      $("textarea").focusout(function(){
          if ($(this).val() == '')
                $(this).css("height", "35px");
      });

    //vote icon 
    $('.action.vote').click(function(){
        $(this).toggleClass('voted');
        $(this).children('span.vote-icon').toggleClass('voted');
    });

});