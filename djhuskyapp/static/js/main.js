$(document).ready(function() {



    $.ajax({
        url: "/api/parties/21/?format=json"
    }).success(function(response) {

        var party_title = response.name;

        $("#partyname").val("Welcome to " + party_title + "!");

    });

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
                    var uri = data[i].uri.substring(14);

                    result += "<li><div class='song', id=" + uri + "><p class='title'>" + title + "</p>" + "<p class='artist'>" + artist + "</p></div><div style='clear: both;''></div></li>";
                }
                $("#results").html(result);
            });
            event.preventDefault();
        }
    });


    $('#results').selectable();

    $("#button").click(function() {

        var selected_songs = $(".ui-selected");

        selected_songs.each(function() {
            var id = $(this.innerHTML).attr('id');
            var title = $(this).find('.title').text();
            var artist = $(this).find('.artist').text();
            addToQueue(title, artist, id);
        });


    });

    function addToQueue(name, artist, id) {
        addToVisualQueue(name, artist);

        var data = {
            "track_id": id,
            "party": 21
        };

        console.log(JSON.stringify(data));

        $.ajax({
            type: "POST",
            url:"/api/songs/",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(data),
            success: function() {alert("success");}
        });
    }

    function addToVisualQueue(name, artist) {
        var listToAddTo = $("#queue");
        var result = "<div class='containerthing'>" +
            "<img src='../static/img/up-arrow.png' width='20px' height='20px'>" +
            "<img src='../static/img/down-arrow.png' width='20px' height='20px'>" +
            "<div class='song'>" +
            "<p class='title'>" + name + "</p>" +
            "<p class='artist'>" + artist + "</p>" +
            "</div>" +
            "<div style='clear: both;'></div>";
        listToAddTo.append(result);
    }

});
