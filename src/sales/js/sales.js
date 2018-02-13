$(function () {
    $('#salesContractCheck').click(() => {
        $('.salesContractCheckBtn').prop('disabled', function (i, v) {
            return !v;
        });
    })
});