(function($) {
    'use strict'

    function submitForm(form) {
        var data = $(form).serialize();

        $(form).find(':input').prop('disabled', true);

        $(form).find('[type="submit"]').after('<i class="landing-page-analyze-spinner fa fa-cog fa-2x fa-spin"></i>');

        $.ajax({
            method: $(form).attr('method'),
            url: $(form).attr('action'),
            data: data,
            success: function(data) {
                $(form).find(':input').prop('disabled', false);
                $(form).find('.landing-page-analyze-spinner').remove();
            }.bind(form),
            error: function(data) {
                $(form).find(':input').prop('disabled', false);
                $(form).find('.landing-page-analyze-spinner').remove();
            }.bind(form)
        });
    }

    function setupPagination() {
        $('.pager a').click(function(e) {
            e.preventDefault();

            paginate(this);
        });
    }

    function paginate(button) {
        $('html, body').animate(
            { scrollTop: '0px' },
            {
                complete: function() {
                    $('#landing-pages')
                    .empty()
                    .append('<div class="landing-pages-spinner"><i class="fa fa-cog fa-5x fa-spin"></i><div>')
                    .load(
                        $(button).attr('href') + ' .landing-page, .landing-page-nav',
                        function() {
                            setupPagination();

                            displayLandingPages();
                        }
                    );
                }
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
