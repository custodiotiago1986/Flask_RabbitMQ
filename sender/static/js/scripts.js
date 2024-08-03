$(document).ready(function() {
    $('#start-button').click(function() {
        $.post('/start', function(response) {
            alert(response);
        });
    });

    $('#stop-button').click(function() {
        $.post('/stop', function(response) {
            alert(response);
        });
    });
});
