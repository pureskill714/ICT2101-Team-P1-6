$(document).ready(function(){

    $('#forward').click(function(){
        $("#cmds").append("Move forward<br>");
        cmd+="w";
//        $("#cmdList").val(function() {
//            return this.value + "1";
//        });
    });

    $('#backward').click(function(){
        $("#cmds").append("Move backward<br>");
        cmd+="s";
//        $("#cmdList").val(function() {
//            return this.value + "2";
//        });
    });

    $('#left').click(function(){
        $("#cmds").append("Move left<br>");
        cmd+="a";
//        $("#cmdList").val(function() {
//            return this.value + "3";
//        });
    });

    $('#right').click(function(){
        $("#cmds").append("Move right<br>");
        cmd+="d";
//        $("#cmdList").val(function() {
//            return this.value + "4";
//        });
    });

    $('#clear').click(function(){
        $("#cmds").empty();
        cmd = "";
    });

    $('#submit').click(function(){
//        alert(cmd);
        $(this).prev().val(cmd);
    });


});

