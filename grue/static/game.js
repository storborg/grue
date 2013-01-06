(function($) {

  function scrollToBottom() {
    $('html, body').animate({ 
      scrollTop: $(document).height() - $(window).height()
    }, 200);
  }

  function submit(move) {
    $.ajax({
      url: '/move',
      type: 'POST',
      data: {
        move: move || ''
      },
    }).done(function(data) {
      var chunk = $('<div>');

      $('.js-location').text(data.location);
      $('.js-moves').text(data.moves);
      $('.js-score').text(data.score);

      chunk.html(data.response.replace(/\r\n/g, '<br>'));

      $('#js-output').append(chunk);

      scrollToBottom();
    });
  }

  function moveHandler(e) {
    var move = $('#move').val(),
        moveRecord = $('<div>');

    e.preventDefault();
    e.stopPropagation();

    moveRecord.text('> ' + move);

    $('#js-output').append(moveRecord);
    $('#move').val('');

    submit(move);

    scrollToBottom();
  }

  $('#move-form').submit(moveHandler);

  $(document).click(function (e) {
    $('#move').focus();
  });

  submit();

}(jQuery));
