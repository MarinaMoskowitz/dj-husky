$(document).ready(function() {



    $.ajax({
        url: "/api/parties/21/?format=json"
    }).success(function(response) {

        var party_title = response.name;
        $("#partyname").html(party_title);

        console.log(JSON.stringify(party_title));
    });

<<<<<<< HEAD


=======
>>>>>>> 143e06c13529ccf7ffc239159fedd5300e90901b

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
<<<<<<< HEAD
        console.log(selected_songs);
        selected_songs.each(function() {
            var title = $(this).attr();
            console.log($(this).text());
        });
        for (var i= 0, len=selected_songs.length; i < len; i++) {
            addToQueue("test", "TEST", "123");
        }
=======

        selected_songs.each(function() {
            var result = this.innerHTML;
            console.log(result);
            console.log($(result).attr('id'));
            console.log($(result).val('title ui-selectee'));
            console.log($(result).attr('class'));
            console.log($(result).attr('artist.ui-selectee'));
            //console.log(result.id);
        });
>>>>>>> 143e06c13529ccf7ffc239159fedd5300e90901b
    });

    function addToQueue(name, artist, id) {
        var listToAddTo = $("#queue");
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
        listToAddTo.append(result);
    }

});
