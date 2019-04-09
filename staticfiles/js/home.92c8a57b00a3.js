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

    $('.action.vote').click(function(){
        jitid = $(this).attr('value');
        userid = $('input[name="user_id_js"]').val();
        let comment = (this).children().children('span.count')
        $.post(
            url : '/jits/liked',
            data : {
                'userid' : jitid,
                'jitid' : userid
            },
            function increaselike(likes) {
                comment.html(likes.no_of_likes)              
            },
        );
    })

});