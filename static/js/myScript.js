// Default Carousel
$().ready(function () {
  $(".slick-carousel").slick({
    centerPadding: "370px",
    infinite: true,
    slidesToShow: 1,
    prevArrow: false,
    nextArrow: false,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 5000,
    centerMode: true,
    responsive: [
      {
        breakpoint: 1400,
        settings: {
          centerPadding: "330px",
          slidesToShow: 1,
        },
      },
      {
        breakpoint: 978,
        settings: {
          centerPadding: "100px",
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 768,
        settings: {
          centerPadding: "0px",
          slidesToShow: 1,
        },
      },
    ],
  });
});

// Homepage Carousel
$().ready(function () {
  $(".slick-carousel-homepage").slick({
    centerPadding: "0px",
    infinite: true,
    slidesToShow: 1,
    prevArrow: false,
    nextArrow: false,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 5000,
    fade: true,
  });
});

// Yard Cover Carousel
$().ready(function () {
  $(".slick-carousel-yard-cover").slick({
    centerPadding: "0px",
    infinite: true,
    slidesToShow: 1,
    prevArrow: false,
    nextArrow: false,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 5000,
    fade: true,
  });
});

// Show Preview (rr_form.html)
function preview() {
  var totalRating = document.getElementById("totalRating").innerText;
  document.getElementById("totalRatingPreview").innerHTML = totalRating;
  var titleValue = document.getElementById("titleValue").value;
  document.getElementById("titlePreview").innerHTML = titleValue;
  var reviewValue = document.getElementById("reviewValue").value;
  document.getElementById("reviewPreview").innerHTML = reviewValue;
  console.log(totalRating, titleValue);
}

// Show Live Total Rating Calculation (rr_form.html)
function liveCalculation() {
  var recommendedValue = Number(document.getElementById("recommendedRange").value);
  var valueValue = Number(document.getElementById("valueRange").value);
  var serviceValue = Number(document.getElementById("serviceRange").value);
  var cleanlinessValue = Number(document.getElementById("cleanlinessRange").value);
  var locationValue = Number(document.getElementById("locationRange").value);
  var sustainabilityValue = Number(document.getElementById("sustainabilityRange").value);
  var totalRating =
    (recommendedValue +
      valueValue +
      serviceValue +
      cleanlinessValue +
      locationValue +
      sustainabilityValue) /
    6;
  document.getElementById("totalRating").innerHTML = totalRating.toFixed(2);
}

// Read more & Read less (on vineyard detail reviews)
function moreLess(element) {
  var half = "half-" + element.id;
  var full = "full-" + element.id;
  var halfDisplay = document.getElementById(half).style.display;
  console.log(halfDisplay);
  if (halfDisplay == "none") {
    document.getElementById(half).style.display = "block";
    document.getElementById(full).style.display = "none";
  } else if (halfDisplay == "block") {
    document.getElementById(half).style.display = "none";
    document.getElementById(full).style.display = "block";
  }
}

// Read more & Read less (on recent reviews)
function sidebarMoreLess(element) {
  var half = "half-" + element.id + "-sidebar";
  var full = "full-" + element.id + "-sidebar";
  var halfDisplay = document.getElementById(half).style.display;
  console.log(halfDisplay);
  if (halfDisplay == "none") {
    document.getElementById(half).style.display = "block";
    document.getElementById(full).style.display = "none";
  } else if (halfDisplay == "block") {
    document.getElementById(half).style.display = "none";
    document.getElementById(full).style.display = "block";
  }
}

// Change width of text below your rating (rr_form.html)
$(document).ready(function () {
  $("#text-below-your-rating").css({
    width: $("#your-rating").width() + "px",
  });
  $(window).resize(function () {
    $("#text-below-your-rating").css({
      width: $("#your-rating").width() + "px",
    });
  });
});

// Refresh captcha
$(function() {
  // Add refresh button after field (this can be done in the template as well)
  $('img.captcha').after(
          $('<a href="#void" class="captcha-refresh btn btn-secondary m-3">Refresh</a>')
          );

  // Click-handler for the refresh-link
  $('.captcha-refresh').click(function(){
      var $form = $(this).parents('form');
      var url = location.protocol + "//" + window.location.hostname + ":"
                + location.port + "/captcha/refresh/";

      // Make the AJAX-call
      $.getJSON(url, {}, function(json) {
          $form.find('input[name="captcha_0"]').val(json.key);
          $form.find('img.captcha').attr('src', json.image_url);
      });

      return false;
  });
});

// Filter Checkbox
$(document).ready(function(){
  $(".ajaxLoader").hide();

  // User can only select one location
  $('.location-checkbox').change(function(){
    // "this" is current checkbox
    $('.location-checkbox').not(this).prop('disabled', this.checked);
  });

	$(".filter-checkbox").on("change", function(){
    console.log("TEST");
		var _data={};
    _data = {currentVineyards};
		$(".filter-checkbox").each(function(index,ele){
			var _filterVal=$(this).val();
			var _filterKey=$(this).data('filter');
			_data[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			 	return el.value;
			});
		});
    
    console.log(_data);
    
    // Run Ajax
		$.ajax({
			url:'/filter-data',
			data:_data,
			dataType:'json',
			beforeSend:function(){
				$(".ajaxLoader").show();
			},
			success:function(res){
				$("#filteredVineyards").html(res.data);
				$(".ajaxLoader").hide();
			}
		});

	});
});

// Reset Filter
function resetAllFilters(){
  $('.filter-checkbox').prop('checked', false).change();
}

// Vineyard Section Pagination
$(document).ready(function(){
	$("#loadMore").on('click',function(){
		var _totalCurrentProducts=$(".vineyard-box").length;
		var _limit=$(this).attr('data-limit');
		var _total=$(this).attr('data-total');
    console.log(_totalCurrentProducts, _limit, _total);

    // Run Ajax
		$.ajax({
			url:'/load-more-data',
			data:{
				limit:_limit,
				offset:_totalCurrentProducts
			},
			dataType:'json',
			beforeSend:function(){
				$("#loadMore").attr('disabled',true);
				// $(".load-more-icon").addClass('fa-spin');
			},
			success:function(res){
				$("#filteredVineyards").append(res.data);
				$("#loadMore").attr('disabled',false);
				// $(".load-more-icon").removeClass('fa-spin');

				var _totalShowing=$(".vineyard-box").length;
				if(_totalShowing==_total){
					$("#loadMore").remove();
				}
			}
		});

  });
});
