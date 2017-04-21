console.log('gsg')

var now = new Date();
var minutes = now.getMinutes();
var seconds = now.getSeconds();
console.log (minutes)

var clock = $('.your-clock').FlipClock({
    clockFace: 'MinuteCounter',
	countdown: true,
    stop: function() {
	    // do something
	    // reset the counter and it will start again
        console.log('here');
        sendJS({'category':category}, 'getCurrentArticle', function(r){});
        setTimeout(refreshArticle, 2200);
	    this.setTime(interval);
    }
  });

minutes_seconds = minutes * 60 +seconds; 
console.log (minutes_seconds)

timestuff = minutes_seconds;

while (timestuff >= 900){
	timestuff = timestuff - 900;
}

timestuff = (timestuff - 900)*(-1);

if(remainingTime <=1){
    clock.setTime(2);
} else{
    clock.setTime(remainingTime);
}

clock.start();



function refreshArticle(){
    sendJS({'category':category}, 'getCurrentArticle', function(r){
        if(r['ok']){
            $('#articleContent').hide();
            $('#articleImg').hide();
            $('#articleTitle').text(r['article']['title']);
            $('#articleLink').attr('href', r['article']['url']);
            if('img' in r['article'] && r['article']['img']){
                $('#articleImg').attr('src', r['article']['img']);
                $('#articleImg').show();
            }
            if('content' in r['article'] && r['article']['content']){
                //r['article']['content'].replace(/(?:\r\n|\r|\n)/g, '<br>')
                $('#articleContent').html(r['article']['content'].replace(/(?:\r\n|\r|\n)/g, '<br>'));
                $('#articleContent').show();
            }

        }


    });
}

refreshArticle();
