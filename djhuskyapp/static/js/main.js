$(document).ready(function() {
    $(".sidebar.left").sidebar();

    $(".sidebar.left").blur();

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
        $(".sidebar.left").trigger("sidebar:toggle");
    });


    $("#songinput").keypress(function(event) {
        var song_query = $("#songinput").val();
        if (event.which == 13) {
            $.ajax({
                url: "https://api.spotify.com/v1/search?q=" + song_query + "&type=track&market=US"
            }).success(function(response) {
                var data = response.tracks.items;
                var result = "";
                for (var i = 0, len=data.length; i < len; i++) {
                    var title = data[i].name;
                    var artist = data[i].artists[0].name;

                    result += "<div class='song'><p class='title'>" + title + "</p>" + "<p class='artist'>" + artist + "</p></div><div style='clear: both;''></div>";
                }
                $("#results").html(result);
            });


            event.preventDefault();
        }
    });

    $('#results').selectable();
});
