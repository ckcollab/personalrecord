$(document).ready(function() {
    var home_view_model = {
        currently_searching: ko.observable(),
        backup_search_queued: ko.observable(),
        search_error: ko.observable(),
        workouts: ko.observableArray()
    };

    var get_search_string = function() {
        // This generates a string like name=taco&reps=3
        var str = $('#workout_search').serialize().toLowerCase();
        console.log(str);
        return '?' + str;
    };

    var do_search = function() {
        // Only search if we have enough input
        var form = getFormObj('#workout_search');

        if(form.weight && form.weight < 10) {
            return;
        }

        if(!home_view_model.currently_searching()) {
            get_set_list(get_search_string());
        } else if(!home_view_model.backup_search_queued()) {
            home_view_model.backup_search_queued(true);
            // make sure search ends in proper state, url matches form
            setTimeout(function() {
                home_view_model.backup_search_queued(false);
                do_search();
            }, 500);
        }
    };

    var get_set_list = function(search_string) {
        search_string = search_string || location.search;
        url = 'api/set/' + search_string;

        home_view_model.currently_searching(true);

        $.get(url)
            .success(function(data) {
                home_view_model.workouts(data);

                home_view_model.search_error(false);
                home_view_model.currently_searching(false);

                window.history.pushState({"content": $('#content').html()}, "Title", '/' + search_string);
            })
            .error(function() {
                home_view_model.search_error(true);
                home_view_model.currently_searching(false);
            });

        //setTimeout(function() {
        //    home_view_model.currently_searching(false);
        //}, 1500);
    };




    // Search exercise names containing back order by heaviest weight and most reps
    // ?search=back&ordering=-weight,-reps
    //
    // Most reps with the most weight
    // ?search=back&ordering=-reps,-weight



    // Interactive handlers
    $('input[type="text"], input[type="number"]').each(function(i, obj){
        $(this).keyup(function() {
            do_search();
        });
        $(this).keydown(function(event){
            // on backspace
            if(event.which == 8) {
                do_search();
            }
        });
    });

    $('.checkbox input').change(function() {
        do_search();
    });

    $('select').change(function() {
        // Style when value selected
        if($(this).val() == 0) {
            $(this).addClass("nothing_selected");
        } else {
            $(this).removeClass("nothing_selected");
        }

        do_search();
    });

    //$('.workout').click(function(){
    //    $(this)
    //});

    // Apply KnockoutJS binding
    ko.applyBindings(home_view_model);

    // Init
    get_set_list('?ordering=-weight');

    var url_params = getUrlVars();

    for(param in url_params) {
        $('input[name="' + param + '"]').val(url_params[param]);
    }

    $('.search_indicators').show();
});

function getFormObj(form_selector) {
    var formObj = {};
    var inputs = $(form_selector).serializeArray();
    $.each(inputs, function (i, input) {
        formObj[input.name] = input.value;
    });
    return formObj;
}

function getUrlVars() {
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars[hash[0]] = hash[1];
    }
    return vars;
}

window.onpopstate = function(e){
    if(e.state){
        document.getElementById("content").innerHTML = e.state.content;
    }
};
