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

    function paginate(button) {
        $('#landing-pages').load(
            $(button).attr('href') + ' #landing-pages',
            function() {
            }
        );
    }

    $(function() {
        $('form').submit(function(e) {
            e.preventDefault();

            submitForm(this);
        });

        $('.pager a').click(function(e) {
            e.preventDefault();

            paginate(this);
        });
    });
})(jQuery);
