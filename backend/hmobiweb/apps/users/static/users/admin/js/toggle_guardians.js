window.addEventListener('load', function () {
    (function($) {
        $(function() {
            var selectField = $('#id_type'),
                guardian_add = $('#guardian-group');
    
            function toggleVerified(value) {
                if (value === 'PATIENT') {
                    guardian_add.show();
                } else {
                    guardian_add.hide();
                }
            }
    
            // show/hide on load based on pervious value of selectField
            toggleVerified(selectField.val());
    
            // show/hide on change
            selectField.change(function() {
                toggleVerified($(this).val());
            });
        });
    })(django.jQuery);
})