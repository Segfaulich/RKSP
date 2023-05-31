$(document).ready(function() {

  $('#search_form').submit(function(event) {
    event.preventDefault();
    var query = $('input[name="query"]').val();

    $.ajax({
      url: searchUrl,
      type: 'GET',
      data: { query: query },
      success: function(data) {
        var paginator = $(data).find('#pagination').html();

        if (typeof paginator === 'undefined') {
            $('#pagination').hide();
        } else {
            $('#pagination').html(paginator).show();
        }

        var genre_result = $(data).find('#genre_select').html();
		var search_result = $(data).find('#book-list').html();

        $('#book-list').html(search_result);
        $('#genre_select').html(genre_result);

        var newUrl = searchUrl + '?query=' + query;
        history.pushState(null, '', newUrl);
      },
      error: function(xhr, status, error) {
        // Обрабатываем ошибку
        console.log(error);
      }
    });
  });

  $('#delete_form').submit(function(event) {
    event.preventDefault();
    var form = $('#delete_form');
    var url = form.attr('action');

    $.ajax({
      url: url,
      type: 'POST',
      data: form.serialize(),
      success: function(data) {
        var paginator = $(data).find('#pagination').html();

        if (typeof paginator === 'undefined') {
            $('#pagination').hide();
        } else {
            $('#pagination').html(paginator).show();
        }

        var genre_result = $(data).find('#genre_select').html();
        var books = $(data).find('#book-list').html();

        $('#genre_select').html(genre_result);
        $('#book-list').html(books);

      },
      error: function(xhr, status, error) {
        // Обрабатываем ошибку
        console.log(error);
      }
    });
  });

  $('.delete_req_form').submit(function(event) {
    event.preventDefault();
    var form = $(this);
    var url = form.attr('action');

    $.ajax({
      url: url,
      type: 'POST',
      data: form.serialize(),
      success: function(data) {
        console.log(100);
        var paginator = $(data).find('#pagination').html();

        if (typeof paginator === 'undefined') {
            $('#pagination').hide();
        } else {
            $('#pagination').html(paginator).show();
        }

        var requests = $(data).find('.delete-requests').html();

        $('.delete-requests').html(requests);

      },
      error: function(xhr, status, error) {
        // Обрабатываем ошибку
        console.log(error);
      }
    });
  });

});

$(document).on('change', '#genre_select', function(event) {
  event.preventDefault();
  var genreUrl = $(this).val();
  console.log(genreUrl);

  $.ajax({
    url: genreUrl,
    type: 'GET',
    success: function(data) {
      var paginator = $(data).find('#pagination').html();

      if (typeof paginator === 'undefined') {
        $('#pagination').hide();
      } else {
        $('#pagination').html(paginator).show();
      }

      var genre_result = $(data).find('#book-list').html();

      $('#book-list').html(genre_result);

      history.pushState(null, '', genreUrl);
    },
    error: function(xhr, status, error) {
      // Обрабатываем ошибку
      console.log(error);
    }
  });
});


$(document).on('click', '.menu-link', function(event) {
  event.preventDefault();

  var url = $(this).attr('href');

  $.ajax({
    url: url,
    type: 'GET',
    success: function(data) {
      var paginator = $(data).find('#pagination').html();

      if (typeof paginator === 'undefined') {
        $('#pagination').hide();
      } else {
        $('#pagination').html(paginator).show();
      }

      var content = $(data).find('#content').html();
      var log_field = $(data).find('.last').html();

      $('#content').html(content);
      $('.last').html(log_field);
      history.pushState(null, '', url);
    },
    error: function(xhr, status, error) {
      console.log(error);
    }
  });
});
