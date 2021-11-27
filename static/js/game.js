$(document).ready(function(){
    var cmd = ""; //use to store the cmd select by user
    $('#forward').click(function(){
        $("#cmds").append("Move forward<br>");
        cmd+="1";
    });

    $('#backward').click(function(){
        $("#cmds").append("Move backward<br>");
        cmd+="2";
    });

    $('#left').click(function(){
        $("#cmds").append("Move left<br>");
        cmd+="3";
    });

    $('#right').click(function(){
        $("#cmds").append("Move right<br>");
        cmd+="4";
    });

    $('#clear').click(function(){
        $("#cmds").empty();
        cmd = "";
    });

    $('#submit').click(function(){
        alert(cmd);
        $(this).prev().val(cmd);
    });

});