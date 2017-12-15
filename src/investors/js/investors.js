$(function () {
    let investors_web_list = {
        'amp': 'https://application.ampclearing.com/apply/default.aspx'
    };
    $('#investors-signup').find('button[type="submit"]').click(function () {
        window.open(investors_web_list[$('select[name="chosen_broker"]').val()]);
    })
})