$('.search-input').focus(function(){
    $(this).parent().addClass('focus');
  }).blur(function(){
    $(this).parent().removeClass('focus');
  })

$(document).ready(function(){
  $('.log-btn').click(function(){
      $('.log-status').addClass('wrong-entry');
      $('.alert').fadeIn(500);
      setTimeout( "$('.alert').fadeOut(1500);",3000 );
  });
  $('.form-control').keypress(function(){
      $('.log-status').removeClass('wrong-entry');
  });

});

$( function() {
  var availableTags = [
    "ActionScript",
    "AppleScript",
    "Asp",
    "BASIC",
    "C",
    "C++",
    "Clojure",
    "COBOL",
    "ColdFusion",
    "Erlang",
    "Fortran",
    "Groovy",
    "Haskell",
    "Java",
    "JavaScript",
    "Lisp",
    "Perl",
    "PHP",
    "Python",
    "Ruby",
    "Scala",
    "Scheme"
  ];
  $( "#tags" ).autocomplete({
    source: availableTags
  });
} );