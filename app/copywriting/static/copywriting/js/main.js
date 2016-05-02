(function($) {
    'use strict'

    function setupForms() {
        $('#landing-page-analyze-form').submit(function(e) {
            e.preventDefault();

            submitForm(this);
        });
    }

    function submitForm(form) {
        var data = $(form).serialize();

        $(form).find(':input').prop('disabled', true);

        $(form).find('[type="submit"]').after('<i class="landing-page-analyze-spinner fa fa-cog fa-2x fa-spin"></i>');

        $.ajax({
            method: $(form).attr('method'),
            url: $(form).attr('action'),
            dataType: 'html',
            data: data,
            context: form,
            success: function(data) {
                $(form).find(':input').prop('disabled', false);
                $(form).find('.landing-page-analyze-spinner').remove();

                addLandingPageToPage(data);

                setupLandingPageDeleteButtons();
            },
            error: function(data) {
                $(form).find(':input').prop('disabled', false);
                $(form).find('.landing-page-analyze-spinner').remove();
            }
        });
    }

    function addLandingPageToPage(landingpage) {
        var $landingpage = $(landingpage);
        $landingpage.prependTo($('#landing-pages')).hide()
        .slideDown(400, function() {
            $(this).addClass('landing-page-show');
        });

        $('#landing-pages .landing-page').last().slideUp(function() {
            $(this).remove();
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
            { complete: loadLandingPages.bind(null, $(button).attr('href')) }
        );
    }

    function loadLandingPages(url) {
        $('#landing-pages').empty()
            .append('<div class="landing-pages-spinner"><i class="fa fa-cog fa-5x fa-spin"></i><div>')
            .load(url + ' .landing-page, .landing-page-nav', function() {
                setupPagination();

                setupLandingPageDeleteButtons();

                displayLandingPages();
            });
    }

    function setupLandingPageDeleteButtons() {
        $('.landing-page-delete').click(function(e) {
            e.preventDefault();

            $.ajax({
                method: 'DELETE',
                url: $(this).attr('href'),
                headers: {
                    'X-CSRFToken': Cookies.get('csrftoken')
                },
                context: this,
                success: function(data) {
                    $(this).closest('.landing-page').slideUp(400, function() {
                        $(this).remove();
                    });
                },
                error: function(data) {
                }
            });
        });
    }

    function displayLandingPages() {
        $('.landing-page').each(function(index, element) {
            setTimeout(function() {
                $(element).addClass('landing-page-show');
            }, index * 300);
        });
    }

    $(function() {
        setupForms();

        setupPagination();

        setupLandingPageDeleteButtons();

        displayLandingPages();
    });
})(jQuery);
