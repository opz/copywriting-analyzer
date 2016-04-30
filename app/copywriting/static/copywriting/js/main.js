(function($) {
    'use strict'

    $(function() {
        $('form').submit(function(e) {
            e.preventDefault();

            var data = $(this).serialize();

            $(this).find(':input').prop('disabled', true);

            $.ajax({
                method: $(this).attr('method'),
                url: $(this).attr('action'),
                data: data,
                success: function(data) {
                    $(this).find(':input').prop('disabled', false);
                    console.log(data);
                }.bind(this)
            });
        });
    });
})(jQuery);
