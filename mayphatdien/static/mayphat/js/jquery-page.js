$('.slider-fashion').slick({
    dots          : true,
    infinite      : false,
    speed         : 300,
    slidesToShow  : 4,
    slidesToScroll: 1,
    responsive    : [{
        breakpoint: 1024,
        settings  : {
            slidesToShow  : 5,
            slidesToScroll: 1,
            infinite      : true,
            dots          : true
        }
    }, {
        breakpoint: 600,
        settings  : {
            slidesToShow  : 3,
            slidesToScroll: 1
        }
    }, {
        breakpoint: 480,
        settings  : {
            slidesToShow  : 2,
            slidesToScroll: 1
        }
    }]
});
$('.slider-brand').slick({
    dots          : true,
    infinite      : false,
    speed         : 300,
    slidesToShow  : 5,
    slidesToScroll: 1,
    responsive    : [{
        breakpoint: 1024,
        settings  : {
            slidesToShow  : 5,
            slidesToScroll: 1,
            infinite      : true,
            dots          : true
        }
    }, {
        breakpoint: 600,
        settings  : {
            slidesToShow  : 3,
            slidesToScroll: 1
        }
    }, {
        breakpoint: 480,
        settings  : {
            slidesToShow  : 1,
            slidesToScroll: 1
        }
    }]
});
$('.slider-prod-cost-down').slick({
    dots          : true,
    infinite      : false,
    speed         : 300,
    slidesToShow  : 2,
    slidesToScroll: 1,
    responsive    : [{
        breakpoint: 1024,
        settings  : {
            slidesToShow  : 2,
            slidesToScroll: 1,
            infinite      : true,
            dots          : true
        }
    }, {
        breakpoint: 600,
        settings  : {
            slidesToShow  : 2,
            slidesToScroll: 1
        }
    }, {
        breakpoint: 480,
        settings  : {
            slidesToShow  : 2,
            slidesToScroll: 1
        }
    }]
});
$('.slider-prod-new').slick({
    dots          : true,
    infinite      : false,
    speed         : 300,
    slidesToShow  : 3,
    slidesToScroll: 1,
    responsive    : [{
        breakpoint: 1024,
        settings  : {
            slidesToShow  : 3,
            slidesToScroll: 1,
            infinite      : true,
            dots          : true
        }
    }, {
        breakpoint: 600,
        settings  : {
            slidesToShow  : 2,
            slidesToScroll: 1
        }
    }, {
        breakpoint: 480,
        settings  : {
            slidesToShow  : 2,
            slidesToScroll: 1
        }
    }]
});
$('.slider-brand').slick({
    dots          : true,
    infinite      : false,
    speed         : 300,
    slidesToShow  : 5,
    slidesToScroll: 1,
    responsive    : [{
        breakpoint: 1024,
        settings  : {
            slidesToShow  : 5,
            slidesToScroll: 1,
            infinite      : true,
            dots          : true
        }
    }, {
        breakpoint: 600,
        settings  : {
            slidesToShow  : 2,
            slidesToScroll: 1
        }
    }, {
        breakpoint: 480,
        settings  : {
            slidesToShow  : 1,
            slidesToScroll: 1
        }
    }]
});
$('.slider-fashion-4-prod').slick({
    dots          : true,
    infinite      : false,
    speed         : 300,
    slidesToShow  : 4,
    slidesToScroll: 1,
    responsive    : [{
        breakpoint: 1024,
        settings  : {
            slidesToShow  : 4,
            slidesToScroll: 1,
            infinite      : true,
            dots          : true
        }
    }, {
        breakpoint: 600,
        settings  : {
            slidesToShow  : 2,
            slidesToScroll: 1
        }
    }, {
        breakpoint: 480,
        settings  : {
            slidesToShow  : 1,
            slidesToScroll: 1
        }
    }]
});
$('.news-detail-rel').slick({
    dots          : true,
    infinite      : false,
    speed         : 300,
    slidesToShow  : 5,
    slidesToScroll: 1,
    responsive    : [{
        breakpoint: 1024,
        settings  : {
            slidesToShow  : 5,
            slidesToScroll: 1,
            infinite      : true,
            dots          : true
        }
    }, {
        breakpoint: 600,
        settings  : {
            slidesToShow  : 3,
            slidesToScroll: 1
        }
    }, {
        breakpoint: 480,
        settings  : {
            slidesToShow  : 1,
            slidesToScroll: 1
        }
    }]
});
/*$('img').addClass('img-responsive');*/
$(window).load(function () {
    /*$('#imgpages-producter').smoothproducts();*/
});
$("table").addClass("table-responsive table-bordered");
$(".aligncenter").addClass("center-block");
$(".alignleft").addClass("pull-left");
$(".alignright").addClass("pull-right");
$(".post-ratings").addClass("hidden-xs hidden-sm");
$(".modal-body input").addClass("form-control");
$(".single-post ul.products li").removeClass("product columns-1 first").addClass("list-slider-fashion col-xs-6 col-md-3");
$(document).ready(function () {
    var $scrollbar = $("#thuong-dongho");
    $scrollbar.tinyscrollbar();
});
$(function () {
    /* TinyNav.js 1 */
    $('#slectmenu').tinyNav({
        active: 'selected',
        indent: '-',
        label : ''
    });
});
$(function () {
    var note    = $('#demthoigian'),
        ts      = new Date(2020, 10, 30), /* năm / tháng / ngày */
        newYear = true;
    if ((new Date()) > ts) {
        /* The new year is here! Count towards something else. */
        /* Notice the *1000 at the end - time must be in milliseconds */
        ts = (new Date()).getTime() + 10 * 24 * 60 * 60 * 1000;
        newYear = false;
    }
    $('#countdown').countdown({
        timestamp: ts,
        callback : function (days, hours, minutes, seconds) {
            var message = "";
            message += "<ul><li><strong>" + hours + "<i>:</i> </strong>" + " Giờ" + (hours == 1 ? '' : '') + "</li> ";
            message += "<li><strong>" + minutes + "<i>:</i> </strong>" + " Phút" + (minutes == 1 ? '' : '') + " </li> ";
            message += "<li><strong>" + seconds + " </strong>" + " Giây" + (seconds == 1 ? '' : '') + " </li></ul>";
            note.html(message);
        }
    });
});
jQuery(document).ready(function ($) {
    /* browser window scroll (in pixels) after which the "back to top" link is shown */
    var offset              = 300,
        /* browser window scroll (in pixels) after which the "back to top" link opacity is reduced */
        offset_opacity      = 1200,
        /* duration of the top scrolling animation (in ms) */
        scroll_top_duration = 700,
        /* grab the "back to top" link */
        $back_to_top        = $('.cd-top');
    /* hide or show the "back to top" link */
    $(window).scroll(function () {
        ($(this).scrollTop() > offset) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
        if ($(this).scrollTop() > offset_opacity) {
            $back_to_top.addClass('cd-fade-out');
        }
    });
    /* smooth scroll to top */
    $back_to_top.on('click', function (event) {
        event.preventDefault();
        $('body,html').animate({
                scrollTop: 0
            }, scroll_top_duration
        );
    });
});

