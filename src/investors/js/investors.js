$(function () {
    let investors_web_list = {
        'amp': 'https://application.ampclearing.com/apply/default.aspx',
        'pricefutures': 'https://accountapplication.admis.com/OnlineApp/OApp/?Office=0x4fb02af2e2a7f71cda277426573d06e1ea39929d'
    };
    $('#investors-signup').find('button[type="submit"]').click(function () {
        window.open(investors_web_list[$('select[name="chosen_broker"]').val()]);
    })
})