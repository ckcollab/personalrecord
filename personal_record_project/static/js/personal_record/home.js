$(document).ready(function() {
    var home_view_model = {
        workouts: ko.observableArray()
    };

    var create_search_string = function() {
        var str = $('#workout_search').serialize().toLowerCase();
        console.log(str);
        return str;
    };

    var get_set_list = function(search_string) {
        search_string = search_string || '';

        $.get('api/set/' + search_string)
            .success(function(data) {
                console.log(data);
                home_view_model.workouts(data);
            })
            .error(function() {
                console.log('erra')
            });
    };



    // Search exercise names containing back order by heaviest weight and most reps
    // ?search=back&ordering=-weight,-reps
    //
    // Most reps with the most weight
    // ?search=back&ordering=-reps,-weight



    $('input[type="text"], input[type="number"]').each(function(i, obj){
        $(this).keyup(function() {
            create_search_string();
        });
    });

    $('.checkbox input').change(function() {
        create_search_string();
    });

    $('select').change(function() {
        // Style when value selected
        if($(this).val() == 0) {
            $(this).addClass("nothing_selected");
        } else {
            $(this).removeClass("nothing_selected");
        }

        create_search_string();
    });

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
