////////////////////////////////////////////////////////
///////////////Floating menu///////////////////////////
////////////////////////////////////////////////////////


var num = 50; //number of pixels before modifying styles

$(window).bind('scroll', function () {
  if (jQuery(window).scrollTop() > num) {
    jQuery('.main-menu').addClass('floating-menu');
  } else {
    jQuery('.main-menu').removeClass('floating-menu');
  }
});


////////////////////////////////////////////////////////
///////////////Section equal height///////////////////////////
////////////////////////////////////////////////////////


function equalizeHeight() {
  var section = $('html').not('.ie6').find('.section'); // getting the sections in all but ie8
  section.css({'min-height': (($(window).height()-30))+'px'});
  $(window).resize(function(){
    section.css({'min-height': (($(window).height()-30))+'px'});
  });
}

equalizeHeight();


////////////////////////////////////////////////////////
///////////////on scroll animation effects///////////////////////////
////////////////////////////////////////////////////////


new WOW().init();

////////////////////////////////////////////////////////
///////////////Smooth scroll for top navbar///////////////////////////
////////////////////////////////////////////////////////


$.scrollUp({
  animation: 'fade',
  topDistance: '10',
  scrollText: '<span class="ion-arrow-up-b" style="color: #FFF"></span>',
  activeOverlay: false,
});


////////////////////////////////////////////////////////
///////////////Image hovers effects and captions///////////////////////////
////////////////////////////////////////////////////////


$(window).load(function(){
  $('.hcaption').hcaptions({effect: "fade"});
});


////////////////////////////////////////////////////////
///////////////nivo Lightbox///////////////////////////
////////////////////////////////////////////////////////


$(document).ready(function(){
  $('a.nivo-light').nivoLightbox({
    effect: 'fade',
    theme: 'default',
    keyboardNav: true  
  });
});


////////////////////////////////////////////////////////
///////////////main slider ///////////////////////////
////////////////////////////////////////////////////////
            

jQuery(document).ready(function() {
  jQuery('#carousel-slider').carousel({
    interval: 5000
  });
  jQuery('#carousel-gallery').carousel();
  var offset = 220;
  var duration = 500;
  jQuery(window).scroll(function() {
    if (jQuery(this).scrollTop() > offset) {
      jQuery('.back-to-top').fadeIn(duration);
    } else {
      jQuery('.back-to-top').fadeOut(duration);
    }
  });
  
  jQuery('.back-to-top').click(function(event) {
    event.preventDefault();
    jQuery('html, body').animate({scrollTop: 0}, duration);
    return false;
  });
});


////////////////////////////////////////////////////////
///////////////contact form ///////////////////////////
////////////////////////////////////////////////////////

$('#contact-form').bootstrapValidator({
//    live: 'disabled',
  message: 'This value is not valid',
  feedbackIcons: {
    valid: 'glyphicon glyphicon-ok',
    invalid: 'glyphicon glyphicon-remove',
    validating: 'glyphicon glyphicon-refresh'
  },
  fields: {
    Name: {
      validators: {
        notEmpty: {
          message: 'The Name is required and cannot be empty'
        }
      }
    },
    email: {
      validators: {
        notEmpty: {
          message: 'The email address is required'
        },
        emailAddress: {
          message: 'The email address is not valid'
        }
      }
    },
    Message: {
      validators: {
        notEmpty: {
          message: 'The Message is required and cannot be empty'
        }
      }
    }
  }
});