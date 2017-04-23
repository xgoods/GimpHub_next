$(document).ready(function(){

    var socket = io.connect('http://' + document.domain + ':' + location.port + '/' + 'chat', {});
    var user = makeid() + '-user';
    var onlineUsers = [];
    var awayUsers = [];
   // var room = category;
    var room = project;

    console.log(project);

    $('#tmpUser').text(user);

    socket.emit('connect');
    socket.on('connectConfirm', function(msg) {

    });

    $('#testbtn').click(function(){
        socket.emit('requestUpdate', project, 1);
    })

    var $canvas = $("#canvas")[0],
        context = $canvas.getContext("2d");



    var img = new Image();

    img.onload = function(){
        var height = img.height;
        var width = img.width;

        // code here to use the dimensions
    }

    img.src = // source goes here;



    socket.on('imageUpdate', function(update){
        for(let i = 0, arr = update["updates"] ; i < arr.length; i++){


        context.fillStyle = "rgb(" + arr[i][2] + "," + arr[i][3] + "," +arr[i][4] +")";
        context.fillRect(arr[i][0],arr[i][1],1,1);




        }
    })


    window.onbeforeunload = function() {
        socket.emit('userDisconnect', user, room);
    }

    socket.on('joined', function(msg) {

        console.log("client has joined! room {0} (self) user {1}".format(msg['room'], msg['user']));


    });



    socket.on('chatMsg', function(msg){
        console.log('reply');
        console.log(msg);
        if(msg['room'] == room){
            var chatBox = $('#chatbox .textoutput');
            if(chatBox){
                chatBox.append("{0}: {1}\n".format(msg['user'], msg['data']));
                chatBox[0].scrollTop = chatBox[0].scrollHeight;
            }else{
                console.log("Message Received for non-existent chatbox {0}".format(msg['room']))
            }
        }
    });
    socket.emit('joined', user, project);
    $(document).ready(function () {
        $('#userNameChangeForm').on('submit', function(e) {
            user = $('#userNameChange').val();
            $('#tmpUser').text(user);
            e.preventDefault();
            $.ajax({
                url : $(this).attr('action') || window.location.pathname,
                type: "POST",
                data: $(this).serialize(),
                success: function (data) {
                    console.log('success');
                    console.log(data);
                    if(data['ok']){
                        $('#userNameChangeRow').fadeOut(500);
                        socket.emit('joined', user, room);
                        setupChatBoxEvents($('#chatbox'));
                    }else{
                        $('#userNameChangeError').text("Error!");
                    }
                    //$("#form_output").html(data);
                },
                error: function (jXHR, textStatus, errorThrown) {
                    console.log('failure');
                    console.log(errorThrown);
                    $('#userNameChangeError').text("Error!");
                    //alert(errorThrown);
                }
            });
        });
    });

    // socket.on('changedStatus', function(msg) {
    //     if(msg['status'] == 'away' && isInArray(msg['user'], onlineUsers)){
    //         var index = onlineUsers.indexOf(msg['user']);
    //         onlineUsers.splice(index, 1);
    //         awayUsers.push(msg['user']);
    //     }else if(msg['status'] == 'online' && isInArray(msg['user'], awayUsers)){
    //         var index = awayUsers.indexOf(msg['user']);
    //         awayUsers.splice(index, 1);
    //         onlineUsers.push(msg['user']);
    //     }
    //     updateUsersStatus();
    // });

    // socket.on('checkUsersOnlineInit', function(msg) {
    //     socket.emit('checkUsersOnlineConfirm', user,  room);
    // });

    // socket.emit('checkUsersOnlineInit');
    // socket.on('checkUsersOnlineConfirm', function(msg) {
    //     if(msg['mode'] == 'staff'){
    //         if(msg['status'] == 'online' && !isInArray(msg['user'], onlineUsers)){
    //             onlineUsers.push(msg['user']);
    //         }else if(msg['status'] == 'away' && !isInArray(msg['user'], awayUsers)){
    //             awayUsers.push(msg['user']);
    //         }
    //     }
    //     updateUsersStatus();
    // });

    function setupChatBoxEvents(chatbox){
        var button = chatbox.find('.chatsendbtn');
        button.unbind();
        button.click(function(){
            sendChatMsgHandler(chatbox);
        });
        var inputline = chatbox.find('.chatmsginput');
        inputline.unbind();
        inputline.keypress(function(e){
            if(e.which == 13) {
                e.preventDefault();
                sendChatMsgHandler(chatbox);
            }
        });
        $('#chatmsginput').show();
        $('#chatsendbtn').show();
    }

    function sendChatMsgHandler(chatbox){
        var data = chatbox.find('.chatmsginput').val();
        console.log(data);
        socket.emit('chatMsg', user, room, data);
        chatbox.find('.chatmsginput').val('');
    }

});

