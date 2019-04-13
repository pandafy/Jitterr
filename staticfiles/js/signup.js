$(document).ready(function(){
    console.log('working')
    function readURL(files) {

        if (files && files[0]) {
          var reader = new FileReader();
      
          reader.onload = function(e) {
            $('#profile-img-tag').attr('src', e.target.result);
            $('span.avatar').hide()
          }
      
          reader.readAsDataURL(files[0]);
        }
      }
      
      $('input[type="file"]').change(function() {
        readURL($(this)[0].files);
      });
})