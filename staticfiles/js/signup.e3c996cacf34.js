$(document).ready(function(){
    console.log('working')
    function readURL(input) {

        if (input.files && input.files[0]) {
          var reader = new FileReader();
      
          reader.onload = function(e) {
              console.log(e.target.result)
            $('#profile-img-tag').attr('src', e.target.result);
          }
      
          reader.readAsDataURL(input.files[0]);
        }
      }
      
      $('input[type="file"]').change(function() {
          console.log('lmao')
        readURL(this[0]);
      });
})