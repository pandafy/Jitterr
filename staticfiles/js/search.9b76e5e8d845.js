var searchURL = window.location.origin+'/search/user/result'

$(".search-bar").autocomplete({
    appendTo: "#results",
	source : function(request,response){
        $.ajax({
            type : "GET",
            url : searchURL,
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
                        key : item.id,
                        avatar : item.avatar
                    };
                }));

            },
            
        })
    } 
	
}).data( "ui-autocomplete" )._renderItem = function( ul, item ) {
    $('.search-bar').data("id",item.key)
    return $( "<li>" )
      .data( "ui-autocomplete-item", item )
      .append('<img src = "' + item.avatar + '" class = "avatar small" style=" float: right; right: 38px; top: 4px;position: relative;">' )
      .append( "<a "+'href ="user/'+ item.key +'">' + item.label + "" + "</a>" )
      .appendTo( ul );
  };