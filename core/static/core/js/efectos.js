$(document).ready(function(){
    $(".img-hover").hover(function(){
        

        $(this).animate(
            {
                width: '350px',
                height: '350px'
            },
            1000
            );
    }, function (){
        $(this).animate(
            {
                width: '400px',
                height: '400px'
            },
            1000
            );
    });
    
     
});