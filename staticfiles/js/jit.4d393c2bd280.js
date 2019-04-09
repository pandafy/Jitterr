$(document).ready(function(){
    $('textarea').click(function(){
        $('button.btn.new-post.submit').disabled()
    });


    $('textarea').keypress(function(){
        if ($('textarea').val() != '')
         $('div.actions').addClass('editing');
        else   
        $('div.actions').removeClass('editing');

        
    });
  
    $('new-post').click(function(){
        $('textarea').focus();
    })
});