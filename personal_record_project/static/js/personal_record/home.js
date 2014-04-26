$(document).ready(function() {
    var currently_searching = false;

    var home_view_model = {
        workouts: ko.observableArray()
    };

    var get_search_string = function() {
        // This generates a string like name=taco&reps=3
        var str = $('#workout_search').serialize().toLowerCase();
        console.log(str);
        return '?' + str;
    };

    var do_search = function() {
        if(!currently_searching) {
            get_set_list(get_search_string());
        }
    };

    var get_set_list = function(search_string) {
        search_string = search_string || '';

        currently_searching = true;

        $.get('api/set/' + search_string)
            .success(function(data) {
                console.log(data);
                home_view_model.workouts(data);

                currently_searching = false;
            })
            .error(function() {
                console.log('erra');

                currently_searching = false;
            });
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

    $('.workout').click(function(){
        $(this)
    });

    // Apply KnockoutJS binding
    ko.applyBindings(home_view_model);

    // Init
    get_set_list();
});

function getFormObj(form_selector) {
    var formObj = {};
    var inputs = $(form_selector).serializeArray();
    $.each(inputs, function (i, input) {
        formObj[input.name] = input.value;
    });
    return formObj;
}
