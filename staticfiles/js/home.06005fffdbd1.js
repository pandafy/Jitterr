function check_if_liked(){
    $('div.action.vote ').each( function(){
        let element = $(this)
        var userid = $('input[name="user_id_js"]').val();
        var jitid = $(this).attr('value')
        $.ajax({
            type : 'GET',
            url : 'check_like',
            data : {
                user_id : userid,
                jit_id : jitid,
            },
            success : function(liked){
                console.log(liked['liked'])
                
                if(liked['liked'] == 'True')
                {
                    console.log('sdfdhkjhkjhss')
                    element.addClass('voted');
                    element.children('span.vote-icon').children('span.vote-icon').addClass('voted')
                    element.children('span.vote-icon').addClass('voted');
                }
                console.log('post')
            }

        })
})
}

$(document).ready(function(){
// This fucntion should be kept at top

    check_if_liked();

//////////////////////////////////////

    var fakedata = ['test1','test2','test3','mohit','ietsanders'];

$(".search-bar").autocomplete({
    appendTo: "#results",
	source : function(request,response){
        $.ajax({
            type : "GET",
            url : 'search/user/result',
            data : {
                q : request.term,
            },
            _renderItem: function( ul, item ) {
                console.log('fired')
                return $( "<li>" )
                  
                  .html("fgdgd" )
                  .appendTo( ul );
              },
            success:function(data){
                /*console.log(data.result["0"].first_name)
                arr = []
                for(var i =0; i< data.result.length; ++i)
                {
                    console.log(data.result[''+String(i) +''])
                    //console.log(i.first_name);
                    arr.push(data.result[''+String(i) +''].first_name);
                };
                console.log(arr)
                response(function(){
                    return arr
                })*/

                response($.map(data.result, function (item) {
                    return {
                        label: item.first_name,
                        value: item.first_name,
                        key : item.id
                    };
                }));

            },
            
        })
    } 
	
});


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

    
    $('.action.vote').click(function(){
        
        $(this).toggleClass('voted');
        $(this).children('span.vote-icon').toggleClass('voted');
        
        
        $(this).children('form').submit(function(e){e.preventDefault()})
        var jitid = $(this).attr('value');
        var userid = $('input[name="user_id_js"]').val();
        console.log(userid)
        var like_count = $(this).children().children('form').children('span.count')
        var csrftToken = $(this).children().children('form').children('input').val()

        let link = 'jits/liked'
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

