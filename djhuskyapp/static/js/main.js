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
            console.log(id);
            console.log(title);
            console.log(artist);

            addToQueue(title, artist, id);
        });
    });

    function addToQueue(name, artist, id) {
        var listToAddTo = $("#queue");
<<<<<<< HEAD
        var result = [
            "<div class='containerthing'>",
            "   <img src='../static/img/up-arrow.png' width='20px' height='20px'>",
            "   <img src='../static/img/down-arrow.png' width='20px' height='20px'>",
            "   <div class='song'>",
            "       <p class='title'>" + name + "</p>",
            "       <p class='artist'>" + artist + "</p>",
            "   </div>",
            "</div>",
            "<div style='clear: both;'></div>"].join("\n");
=======
        var result = "<div class='containerthing'>" +
            "<img src='../static/img/up-arrow.png' width='20px' height='20px'>" +
            "<img src='../static/img/down-arrow.png' width='20px' height='20px'>" +
            "<div class='song'>" +
            "<p class='title'>" + name + "</p>" +
            "<p class='artist'>" + artist + "</p>" +
            "</div>" +
            "<div style='clear: both;'></div>";
>>>>>>> 0c1dd70ef4b5f0cbedc31b7fc7700a8010293570
        listToAddTo.append(result);
    }

});
