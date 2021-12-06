var timeElapsed = 0;
var timerID = -1;
function tick() {
    timeElapsed++
    document.getElementById("time").innerHTML = timeElapsed;
}

function start() {
    if(timerID == -1){
        timerID = setInterval(tick, 1000);
    }
}

function stop() {
    if(timerID != -1){
        clearInterval(timerID)
        timerID = -1
    }
}

function calculateScore(time,count,level=1){
    var score = Math.round(((1/time) * 500 * level)/count*10)
    return score;
}
$(document).ready(function(){
    start();
    var stop = "s";
    $('#forward').click(function(){
        $("#cmds").append("Move forward<br>");
        cmd+="w";
    });

    $('#backward').click(function(){
        $("#cmds").append("Move backward<br>");
        cmd+="x";
    });

    $('#left').click(function(){
        $("#cmds").append("Move left<br>");
        cmd+="a";
    });

    $('#right').click(function(){
        $("#cmds").append("Move right<br>");
        cmd+="d";
    });

    $('#clear').click(function(){
        $("#cmds").empty();
        cmd = "";
    });

    $('#submit').click(function(){
//        alert(cmd);
        $(this).prev().val(cmd);
    });
    $("#stop").click(function(){

        $.ajax({
          url: "/sendcommand",
          type: "get",
          data: {cmd: stop},
          success: function(response) {
            var new_html = response.html;
          },
        });
    });


});

