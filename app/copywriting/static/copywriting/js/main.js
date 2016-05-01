(function($) {
    'use strict'

    function submitForm(form) {
        var data = $(form).serialize();

        $(form).find(':input').prop('disabled', true);

        $.ajax({
            method: $(form).attr('method'),
            url: $(form).attr('action'),
            data: data,
            success: function(data) {
                $(form).find(':input').prop('disabled', false);
            }.bind(form),
            error: function(data) {
                //todo
            }
        });
    }

    function setupPagination() {
        $('.pager a').click(function(e) {
            e.preventDefault();

            paginate(this);
        });
    }

    function paginate(button) {
        $('html, body').animate({ scrollTop: '0px' });

        $('#landing-pages').load(
            $(button).attr('href') + ' .landing-page, .landing-page-nav',
            function() {
                setupPagination();

                displayLandingPages();
            }
        );
    }

    function displayLandingPages() {
        $('.landing-page').each(function(index, element) {
            setTimeout(function() {
                $(element).removeClass('landing-page-hidden');
            }, index * 300);
        });
    }

    $(function() {
        $('form').submit(function(e) {
            e.preventDefault();

            submitForm(this);
        });

        setupPagination();

        displayLandingPages();
    });
})(jQuery);
