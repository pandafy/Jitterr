$(document).ready(function(){
    


    $('textarea').keypress(function(){
        if ($('textarea').val() != '')
         {
             $('div.actions').addClass('editing');
             $('follow-btn').prop('disabled','false')
         }
        else
        {   
        $('div.actions').removeClass('editing');
            
        }
        $(this).parent('div.inputs').parent().children().children('span.char-count').html($('textarea').val().length)
    });
  
        $('div.actions').addClass('editing');
});