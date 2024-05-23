$('#add-memory, #edit-place').on('click', function () {
    $('.overlay').fadeIn()
})

$('.close-popup').on('click', function () {
    $('.overlay').fadeOut()
})

$(document).on('mousedown', function (e) {
    let htmlPopup = $('.popup');
    if (e.target != htmlPopup[0] && htmlPopup.has(e.target).length === 0) {
        $('.overlay').fadeOut();
    }
});