$(document).ready(function(){
    
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