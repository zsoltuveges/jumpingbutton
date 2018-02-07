var trickyButton = document.getElementById('trick');
var jumped = false;
trickyButton.addEventListener('mouseover', function(){
    trickyButton.style.left = (jumped ? 50 : 100) + 'px';
    jumped = !jumped;
});


var clickableButton = document.getElementById('clickable');
clickableButton.addEventListener('click', function () {
    alert('I knew you selected this :)');
});