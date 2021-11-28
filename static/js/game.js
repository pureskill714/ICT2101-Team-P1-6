$(document).ready(function(){

    $('#forward').click(function(){
        $("#cmds").append("Move forward<br>");
        cmd+="1";
        $("#cmdList").val(function() {
            return this.value + "1";
        });
    });

    $('#backward').click(function(){
        $("#cmds").append("Move backward<br>");
        cmd+="2";
        $("#cmdList").val(function() {
            return this.value + "2";
        });
    });

    $('#left').click(function(){
        $("#cmds").append("Move left<br>");
        cmd+="3";
        $("#cmdList").val(function() {
            return this.value + "3";
        });
    });

    $('#right').click(function(){
        $("#cmds").append("Move right<br>");
        cmd+="4";
        $("#cmdList").val(function() {
            return this.value + "4";
        });
    });

    $('#clear').click(function(){
        $("#cmds").empty();
        cmd = "";
//        alert($("#cmdList").val())
    });

    $('#submit').click(function(){
//        alert(cmd);
        $(this).prev().val(cmd);
    });



});

