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

var textarea = document.querySelector('textarea');

textarea.addEventListener('keyup', function(){
	if(this.scrollTop > 0){
		this.style.height = this.scrollHeight + "px";
  }
});