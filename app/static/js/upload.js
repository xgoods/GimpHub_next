
$('#uploadbutton').click(function(){

    dictionary={}
    dictionary['title']=$('#title-upload').val()
    dictionary['url']=$('#url-upload').val()
    dictionary['category']=$('#categoriesupload').val()
    
    
    sendJS(dictionary,'upload',function(){
        //alert('Upload Succuess')
        $('.upload-button-3').eq(0).click();
    })

})
