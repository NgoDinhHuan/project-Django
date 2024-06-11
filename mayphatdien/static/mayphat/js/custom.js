/* fix .live menthor in jquery 1.9 and above */
jQuery.fn.extend({
    live: function (event, callback) {
        if (this.selector) {
            jQuery(document).on(event, this.selector, callback);
        }
        return this;
    }
});
/*=========================================*/
/*check empty content element*/
function isEmpty(el) {
    return !$.trim(el.html()).length;
}
/*Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position*/
function sticky_menu(menu, sticky) {
    if (typeof menu === 'undefined' || !jQuery.isNumeric(sticky)) sticky = 0;
    if ($(window).scrollTop() >= sticky) {
        if ($('#just-for-height').length === 0) {
            menu.after('<div id="just-for-height" style="height:' + menu.height() + 'px"></div>')
        }
        menu.addClass("sticky");
    } else {
        menu.removeClass("sticky");
        $('#just-for-height').remove();
    }
}
/*=========================================*/
/* check current page in menu header */
var curren_page = $('.menu-sidebar .menusanpham a[href="' + window.location.href + '"]');
curren_page.parent().addClass('current-menu-item');
curren_page.closest('.menusanpham > li').addClass('current-menu-item');
/**/
$(document).ready(function () {
    /* change position left-right of sub-menu */
    var ww = $(window).width();
    $('.menu-item-has-children .level1').each(function () {
        var offsetLv1 = $(this).offset().left;
        var offsetLv2 = offsetLv1 + $(this).width();
        if (offsetLv1 > (ww * 0.7)) {
            $(this).addClass('menu-float-left');
        }
        $(this).find('.level2').each(function () {
            if (offsetLv2 > (ww * 0.7)) {
                $(this).addClass('menu-float-left');
            }
        });
    });
    $(window).resize(function () {
        var ww = $(window).width();
        $('.has-sub .level1').each(function () {
            var offsetLv1 = $(this).offset().left;
            var offsetLv2 = offsetLv1 + $(this).width();
            if (offsetLv1 > (ww / 2)) {
                $(this).css({
                    'left' : 'auto',
                    'right': '0'
                })
            }
            $(this).find('.level2').each(function () {
                if (offsetLv2 > (ww / 2)) {
                    $(this).css({
                        'left' : 'auto',
                        'right': '100%'
                    });
                }
            });
        });
    });
    /**/
    /*hidden payment title if content empty*/
    if (isEmpty($('footer .footer-left .social-footer ul')))
        $('footer .footer-left .social-footer h5').hide();
    /**/
    /*Get the navbar*/
    var menu = $("#header .bottom-header");
    /*Get the offset position of the navbar*/
    var sticky = menu.offset().top + 1;
    /*When the user scrolls the page, execute myFunction*/
    if ($(window).width() > 767) {
        /*sticky_menu(menu, sticky);*/
        $(window).on('scroll', function () {
            /*sticky_menu(menu, sticky);*/
        });
    }
});
$('.menu-header nav ul li.menu-item-has-children > a').on('click', function(e) {
    if ($(window).width() < 991) {
        e.preventDefault();
        $(this).parent().toggleClass('open');
    }
});
$('.product .images .thumbnails').slick({
    dots          : false,
    arrows        : true,
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
            slidesToShow  : 3,
            slidesToScroll: 1
        }
    }, {
        breakpoint: 480,
        settings  : {
            slidesToShow  : 3,
            slidesToScroll: 1
        }
    }]
});
function gotoCart(pid){
var csrftoken = $("[name=csrfmiddlewaretoken]").val();
$.ajax({
    url: '/postgiohang/',
    contentType: 'application/json',
    type: 'post',
    headers:{
    "X-CSRFToken": csrftoken
    },
    data: pid,
    success: function(response){
        var data = $.parseJSON(response);
        $('.cart-item').html("GIỎ HANG "+data);
    }
});
}