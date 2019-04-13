function check_if_liked(){
    $('div.action.vote ').each( function(){
        let element = $(this)
        var userid = $('input[name="user_id_js"]').val();
        var jitid = $(this).attr('value')
        $.ajax({
            type : 'GET',
            url : window.location.origin + '/check_like',
            data : {
                user_id : userid,
                jit_id : jitid,
            },
            success : function(liked){
                
                if(liked['liked'] == 'True')
                {
                    element.children('span.vote-icon').children('i').removeClass('far')   
                    element.children('span.vote-icon').children('i').addClass('fas') 
                }
                else
                {
                    element.children('span.vote-icon').children('i').removeClass('fas')   
                    element.children('span.vote-icon').children('i').addClass('far') 
                }

                if(liked['count']==0)
                    element.children('span.count').html('')
                else
                    element.children('span.count').html(liked['count']) 

            }

        })
})
}

$(document).ready(function(){
// This fucntion should be kept at top

    check_if_liked();

//////////////////////////////////////

    var fakedata = ['test1','test2','test3','mohit','ietsanders'];




    let logged_user = $('input[name="user_id_js"]')

    if($(location).attr('href') == '/user/' + logged_user )
        $('.btn.edit-profile-btn').hide()
    

    //text area
    $("textarea").focusin(function(){
        $(this).css("height", "47px");
      });
      $("textarea").focusout(function(){
          if ($(this).val() == '')
                $(this).css("height", "35px");
      });

    
    $('#new-post-btn-top').click(function(){
        if(window.location.pathname == '/')
            $('textarea').focus()
        else{
            $('form.new-post-form').slideDown('slow');
        }
    })


    $('div.action.vote').click(function(){
        
        $(this).children('span.vote-icon').children('i').toggleClass('fas')   
        $(this).children('span.vote-icon').children('i').toggleClass('far')        
     
        
        var jitid = $(this).attr('value');
        var userid = $('input[name="user_id_js"]').val();
        var like_count = $(this).children('span.count')

        let link = window.location.origin + '/jits/liked'
        $.ajax({
            type : "GET",
            url : link, //updates
            data : {
                'userid' : userid,
                'jitid' : jitid,
            },
            success :function increaselike(likes) {
                if (likes['likes'] != 0)
                    like_count.html(likes['likes'] ) 
                else
                    like_count.html('')          
            }
        });
    })

});

