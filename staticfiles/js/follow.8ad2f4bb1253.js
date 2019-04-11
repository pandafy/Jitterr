$(document).ready(function(){
    $('#follow-btn').click(function(e){
        e.preventDefault()
        let user_id = $('input[name="user_id_js"]')
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
                    $('#follow-btn').html('Following') 
                }
        })
    })
});