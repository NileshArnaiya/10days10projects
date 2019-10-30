function submitQuiz(){
    var total = 5;
    var score = 0;

    // Get User Input
    var form = document.forms["quiz"][0];
    var q1 = document.forms["quiz"]["q1"].value;
    var q2 = document.forms["quiz"]["q2"].value;
    var q3 = document.forms["quiz"]["q3"].value;
    var q4 = document.forms["quiz"]["q4"].value;
    var q5 = document.forms["quiz"]["q5"].value;

    // Validation
    for (i = 1; i <= total; i++) {
        if (eval('q' + i) == null || eval('q' + i) == '') {
            var popup = document.getElementsByClassName("popup");
            console.log(typeof popup);
            popup.innerHTML = 'You missed question ' + i;
            alert('You missed question ' + i);
            return false;
        }
    }

    // Set Correct Answers
    var answers = ["d", "d", "e", "b", "d"];

    // Check Answers
    for (i = 1; i <= total; i++) {
        if (eval('q' + i) == answers[i - 1]) {
            score++;
        }
    }

    // Display Results
    var results = document.getElementById('results');
    results.innerHTML = '<h3>You scored <span>' + score + '</span> out of <span>' + total + '</span></h3>';
    alert('You scored ' + score + ' out of ' + total);


    document.getElementById("quiz").reset();
    return false;
}