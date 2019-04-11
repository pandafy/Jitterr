$(document).ready(function(){
    $('#follow-btn').click(function(e){
        let user_id = $('input[name="user_id_js"]').val()
        let follow_id = $('#follow-btn').attr('value')
        $.ajax({
            type : 'GET',
            url : '/follow',
            data : {
                user_id : user_id,
                follow_id : follow_id
            },
            success : function callback(data)
                {
                    if(data.following == "True")
                        $('#follow-btn').html('Following') 
                    else
                    $('#follow-btn').html('Follow') 
                }
            })
        
      
    })
});