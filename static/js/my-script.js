$(document).ready(function () {
    var $table = $("#infoTable")
    $table.on('click', 'input[class="buttonDelete"]', function (e) {
        $(this).closest('tr').remove()
    })

    $("#addBtn").on('click', function () {
        $("#addData").submit();
    });

    $("#editBtn").on('click', function () {
        $("#editForm").submit();
    });

    $('table').on('click', 'button[class="buttonDelete"]', function (e) {
        $(this).closest('tr').remove()
    });

    $('#modalDelete').on('show.bs.modal', function (e) {
        $(this).find('.btnYesClass').attr('href', $(e.relatedTarget).data('href'));
    });
});