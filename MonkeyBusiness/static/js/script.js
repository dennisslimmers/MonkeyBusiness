/**
 * Created by Xander on 08/11/2016.
 */
function validate() {
    console.log("test");
    if(document.getElementsByClassName("vBox").checked){
        document.getElementsByClassName("vBox").value = 1;
        document.getElementsByClassName("hBox").value = 0;
    }
    else{
        document.getElementsByClassName("vBox").value = 0;
        document.getElementsByClassName("hBox").value = 1;
    }


}

$(document).ready(function () {
    console.log("test");
});