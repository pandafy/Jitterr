$(document).ready(function(){
    $('textarea').click(function(){
        $('button.btn.new-post.submit').disabled()
    });


    $('textarea').on('change',function(){
        if ($('textarea').val() != '')
         $('div.actions').addClass('editing');
        else   
        $('div.actions').removeClass('editing');

        $('.char-count').html($('textarea').val().length)
    });
        $('div.actions').addClass('editing');
});