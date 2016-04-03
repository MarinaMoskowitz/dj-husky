$(document).ready(function() {
    $(".sidebar.left").sidebar();

    $('#songinput').focus(function() {
        if ($(this).val()=='Enter a song') {
            $(this).val('');
        }
    });

    $('#songinput').blur(function() {
        if ($(this).val()==='') {
            $(this).val('Enter a song');
        }
    });

    $("i").click(function() {
        $(".sidebar.left").sidebar().trigger("sidebar:open");
    });

    // $('#queue').selectable();
    //
});
