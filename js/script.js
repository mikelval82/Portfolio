AOS.init({
  duration: 600
});
  

(function($) {
    'use strict';

 
// post gallery

        $('.post_gallery').owlCarousel({
            loop:true,
            margin:1,
            nav:true,
            dots: false,
            navText : ["<i class='ti-angle-left'></i>","<i class='ti-angle-right'></i>"],
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:2
                },
                1000:{
                    items:4
                }
            }
        });

         // SCROLL TO TOP
  
  $(window).on('scroll', function () {
    if ($(window).scrollTop() > 70) {
        $('.backtop').addClass('reveal');
    } else {
        $('.backtop').removeClass('reveal');
    }
});

 // Sticky Menu
 // 
  $(window).on ('scroll', function (){
    if ($('.navigation').offset().top > 100) {
      $('.navigation').addClass('fixed-nav');
    } else {
      $('.navigation').removeClass('fixed-nav');
    }
  });

  /* Closes the Responsive Menu on Menu Item Click*/
    $('.navbar-collapse .navbar-nav a').on('click', function () {
        $('.navbar-toggler:visible').click();
    });
    

 

    $('a.smoth-scroll').on('click', function (e) {
        var anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $(anchor.attr('href')).offset().top - 50
        }, 1000);
        e.preventDefault();
    });

 
 $('.testimonial-slider').slick({
		slidesToShow: 1,
		infinite: true,
		dots: true,
		arrows: false,
		autoplay: true,
		autoplaySpeed: 5000
	});


  
    $(window).on ('load', function (){ // makes sure the whole site is loaded

          // ----------------------- 
        // Progress Bar--------------------
        // 
    $('.progress-bar').each(function(){
            var width = $(this).data('percent');
            $(this).css({'transition': 'width 3s'});
            $(this).appear(function() {
                console.log('hello');
                $(this).css('width', width + '%');
                $(this).find('.count').countTo({
                    from: 0,
                    to: width,
                    speed: 3000,
                    refreshInterval: 50
                });
            });
        });


    });  //End On Load Function


  


})(jQuery);

// Contact Form Handler with FormSpree
$(document).ready(function() {
    $('#contactForm').on('submit', function(e) {
        e.preventDefault();
        
        var form = $(this);
        var name = $('#name').val().trim();
        var email = $('#email').val().trim();
        var subject = $('#subject').val().trim();
        var message = $('#message').val().trim();
        
        // Email validation regex
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        
        // Reset previous messages
        $('.contact__msg').removeClass('alert-success alert-danger').hide();
        
        // Validation
        if(name === '' || email === '' || subject === '' || message === '') {
            $('.contact__msg')
                .removeClass('alert-success')
                .addClass('alert-danger')
                .text('Please fill in all fields.')
                .fadeIn();
            return false;
        }
        
        if(!emailRegex.test(email)) {
            $('.contact__msg')
                .removeClass('alert-success')
                .addClass('alert-danger')
                .text('Please enter a valid email address.')
                .fadeIn();
            return false;
        }
        
        // Disable submit button
        $('#submit').prop('disabled', true).val('Sending...');
        
        // Send to FormSpree
        $.ajax({
            url: form.attr('action'),
            method: 'POST',
            data: form.serialize(),
            dataType: 'json',
            success: function(response) {
                $('.contact__msg')
                    .removeClass('alert-danger')
                    .addClass('alert-success')
                    .text('Thank you for your message! I will get back to you soon.')
                    .fadeIn();
                
                // Reset form
                form[0].reset();
                
                // Re-enable button
                $('#submit').prop('disabled', false).val('Send Message');
            },
            error: function(xhr, status, error) {
                $('.contact__msg')
                    .removeClass('alert-success')
                    .addClass('alert-danger')
                    .text('Oops! There was an error sending your message. Please try again.')
                    .fadeIn();
                
                // Re-enable button
                $('#submit').prop('disabled', false).val('Send Message');
            }
        });
        
        return false;
    });
});