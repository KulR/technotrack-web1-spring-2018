$(document).ready(function () {

    $('#id_categories').tokenize2();

    // function openDialog() {
    //     $('.modal').modal('show');
    //
    // }
    //
    //
    // function closeDialog() {
    //     $('#modal').modal('toggle');
    // }

    $(document).on('click', '.QEditLink', function (event) {
        // openDialog();
        $('#modalHeaderTitle').replaceWith('<h1>Update question</h1>');
        $.get(this.href, function (data) {
            $('#dialogBody').html(data)
        });
        event.preventDefault();
    });

    $(document).on('click', '#QNewLink', function (event) {
        // openDialog();
        $('#modalHeaderTitle').replaceWith("<h1>Create new question</h1>");
        $.get(this.href, function (data) {
            $('#dialogBody').html(data)
        });
        event.preventDefault();
    });


    $(document).on('click', '.CNewLink', function (event) {
        //openDialog();
        $('#modalHeaderTitle').replaceWith("<h1>Create new comment</h1>");
        $.get(this.href, function (data) {
            $('#dialogBody').html(data)
        });
        event.preventDefault();
    });

    $(document).on('click', '.CEditLink', function (event) {
        //openDialog();
        $('#modalHeaderTitle').replaceWith('<h1>Update comment</h1>');
        $.get(this.href, function (data) {
            $('#dialogBody').html(data)
        });
        event.preventDefault();
    });


    $(document).on('click', '.like', function (event) {
        // console.log(this.parentNode.action);
        var form = this.parentNode;
        $.get(this.parentNode.action, function (data) {
            let likes = document.querySelector('#' + $(form).data('success-id'));
            // if (likes.classList.contains('liked'))
            //     likes.innerText = Number(likes.innerText) - 1;
            // else
            //     likes.innerText = Number(likes.innerText) + 1;
            likes.innerText = data;
            likes.classList.toggle('liked');
        });
        event.preventDefault();
    });

    //have some question with open-close modal window
    // $(document).on('click', '[data-dismiss="modal"]', function (event) {
    //     console.log('try to close modal');
    //     closeDialog();
    //     //
    //     event.preventDefault();
    // });

    $(document).on('submit', '[data-formtype="ajaxForm"]', function (event) {
        var form = this;
        $.post(this.action, $(this).serialize(), function (data) {
            if (data == "OK") document.location.reload();
            // if (data == "OK") alert("It work");
            else
                $('#' + $(form).data('success-container-id')).html(data);
        });
        event.preventDefault();
    });


    window.setInterval(function () {
        try {
            let src = $('.QCommentsRefresh')[0].href;
            // console.log(src);
            $.get(src, function (data) {
                $('#qComments').replaceWith("<div id='qComments'>" + data + "</div>")
            });
        } catch (e) {
        }
    }, 30000);


    $(document).on('click', '.QCommentsRefresh', function RefreshComment(event) {
        // console.log(this);
        $.get(this.href, function (data) {
            $('#qComments').replaceWith("<div id='qComments'>" + data + "</div>")
        });
        event.preventDefault();
    });

});

