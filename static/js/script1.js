<!--
    // Define the images array to display in summary section
    var summaryImgArray = [];
    var i = 0; // loop index
    time = 5000;

    // Add images to the array
    summaryImgArray.push("avatar_g.jpg");
    summaryImgArray.push("bridge.jpg");
    summaryImgArray.push("skies.jpg");

    // Get the summary image node
    var sumImg = document.getElementById("summImg");

    // Create a function to change the img
    function changeImg(){
        sumImg.src = "{{ url_for('static', filename='img/"summaryImgArray[i]"') }}";
        if (i<summaryImgArray.length){
            i = 0;
        }
        else{
            i++;
        }
    }

    // set the call to the function every interval
    setTimeout("changeImg", time);
//-->
