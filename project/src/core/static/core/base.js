$(document).ready(function () {
    function openDialog() {
        $('.modal').modal('show');

    }
    
    $(document).on('click', '.QEditLink', function (event) {
        openDialog();
        event.preventDefault();
    } )
    
});

