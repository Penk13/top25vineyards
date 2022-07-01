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

  // If user select anything
	$(".filter-checkbox").on("change", function(){
    closeFilterDropdown();
    syncFilterCheckbox($(this));
    showSelectedFilter();
    filterBar();
    filterData();
	});
  
});

// Sync Filter Checkbox on Filter Bar and Offcanvas
function syncFilterCheckbox(current){
  $('input[type=checkbox]').each(function(index) {
    if (current.next("label").text() == $(this).next("label").text()) {
      $(this).prop('checked', current.prop('checked'));
    }
  });
}

// Close Filter Dropdown
function closeFilterDropdown(){
  $('.dropdown-btn.show').removeClass('show');
  $('.dropdown-menu.show').removeClass('show');
  $('.collapse-btn').addClass('collapsed');
  $('.list-group.show').removeClass('show');
}

// Remove Selected Filter
function removeSelectedFilter(text){
  $('input[type=checkbox]:checked').each(function(index) {
    if (text == $(this).next("label").text()) {
      $(this).prop('checked', false).change();
    }
  });
  $(this).remove();
}

// Filter Data
function filterData(){
  var _data={};
    _data = {defaultVineyards, perPage};

		$(".filter-checkbox").each(function(index,ele){
			var _filterVal=$(this).val();
			var _filterKey=$(this).data('filter');
			_data[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
			 	return el.value;
			});
		});
    
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
        $('html, body').animate({scrollTop: $("#filteredVineyards").offset().top-300}, 100); 
        $('#view-filtered-vineyards').text("View all " + res.total_vineyards + " Vineyards");
			}
		});
}

// Show Selected Filters
function showSelectedFilter(){
  var $checkedCheckbox = $('input[type="checkbox"]:checked');
  var selectedFilters = $checkedCheckbox.map(function() {
    return $(this).next("label").text();
  }).get();

  // Remove Duplicate
  selectedFilters = [...new Set(selectedFilters)];
  
  var list = "";
  for(i=0; i<selectedFilters.length; i++){
    list += "<button class='btn btn-secondary btn-sm ps-3 pe-2 mx-1 selected-filter' type='button' onclick='removeSelectedFilter(\""+selectedFilters[i]+"\")' >"+selectedFilters[i]+"<span class='ps-2 pe-1'>x</span>"+"</button>";
  }
  $(".selectedFilters").html(list);
}

// Filter Bar
function filterBar(){
  // From World Region
  var world_region = $('.worldRegionItem div').children('input[type="checkbox"]:checked').val();
  var world_region_country = $('.worldRegionItem div').children('input[type="checkbox"]:checked').attr("country");
  var world_region_wine_region = $('.worldRegionItem div').children('input[type="checkbox"]:checked').attr("wine_region");

  // From Country
  var country = $('.countryItem div').children('input[type="checkbox"]:checked').val();
  var country_world_region = $('.countryItem div').children('input[type="checkbox"]:checked').attr("world_region");
  var country_wine_region = $('.countryItem div').children('input[type="checkbox"]:checked').attr("wine_region");

  // From Wine Region
  var wine_region = $('.wineRegionItem div').children('input[type="checkbox"]:checked').val();
  var wine_region_world_region = $('.wineRegionItem div').children('input[type="checkbox"]:checked').attr("world_region");
  var wine_region_country = $('.wineRegionItem div').children('input[type="checkbox"]:checked').attr("country");

  // Convert to JS Array
  world_region !== undefined ? world_region = world_region.split(',') : world_region = [];
  world_region_country !== undefined ? world_region_country = world_region_country.split(',') : world_region_country = [];
  world_region_wine_region !== undefined ? world_region_wine_region = world_region_wine_region.split(',') : world_region_wine_region = [];
  country !== undefined ? country = country.split(',') : country = [];
  country_world_region !== undefined ? country_world_region = country_world_region.split(',') : country_world_region = [];
  country_wine_region !== undefined ? country_wine_region = country_wine_region.split(',') : country_wine_region = [];
  wine_region !== undefined ? wine_region = wine_region.split(',') : wine_region = [];
  wine_region_world_region !== undefined ? wine_region_world_region = wine_region_world_region.split(',') : wine_region_world_region = [];
  wine_region_country !== undefined ? wine_region_country = wine_region_country.split(',') : wine_region_country = [];

  function showAllFilter() {
    $('.worldRegionItem').show();
    $('.countryItem').show();
    $('.wineRegionItem').show();
    $('.worldRegionItem div').children('input[type="checkbox"]').attr("disabled", false);
    $('.countryItem div').children('input[type="checkbox"]').attr("disabled", false);
    $('.wineRegionItem div').children('input[type="checkbox"]').attr("disabled", false);
    $('.count-vineyards').css("opacity", "1.0");
  }

  // Case 1: Select World Region
  if(world_region.length == 1 && country.length == 0 && wine_region == 0) {
    showAllFilter();
    $('.worldRegionItem div').children(':checkbox:not(:checked)').attr("disabled", true);
    $('.worldRegionItem div').children(':checkbox:not(:checked)').next().next().css("opacity", "0.5");
    if(world_region_country!==undefined){
      $('.countryItem').each(function(i, obj) {        
        if ($.inArray($(obj).attr('id'), world_region_country) == -1)
        {
          $(obj).hide();
        }
      });
    }
    if(world_region_wine_region!==undefined){
      $('.wineRegionItem').each(function(i, obj) {        
        if ($.inArray($(obj).attr('id'), world_region_wine_region) == -1)
        {
          $(obj).hide();
        }
      });
    }
  } 
  // Case 2: Select Country
  else if(world_region.length == 0 && country.length == 1 && wine_region == 0){
    showAllFilter();
    $('.countryItem div').children(':checkbox:not(:checked)').attr("disabled", true);
    $('.countryItem div').children(':checkbox:not(:checked)').next().next().css("opacity", "0.5");
    $('.worldRegionItem div').children(':checkbox').attr("disabled", true);
    $('.worldRegionItem div').children(':checkbox').next().next().css("opacity", "0.5");
    if(country_wine_region!==undefined){
      $('.wineRegionItem').each(function(i, obj) {        
        if ($.inArray($(obj).attr('id'), country_wine_region) == -1)
        {
          $(obj).hide();
        }
      });
    }
  }
  // Case 3: Select Wine Region
  else if(world_region.length == 0 && country.length == 0 && wine_region.length == 1) {
    showAllFilter();
    $('.wineRegionItem div').children(':checkbox:not(:checked)').attr("disabled", true);
    $('.wineRegionItem div').children(':checkbox:not(:checked)').next().next().css("opacity", "0.5");
    $('.worldRegionItem div').children(':checkbox').attr("disabled", true);
    $('.worldRegionItem div').children(':checkbox').next().next().css("opacity", "0.5");
    $('.countryItem div').children(':checkbox').attr("disabled", true);
    $('.countryItem div').children(':checkbox').next().next().css("opacity", "0.5");
  }
  // Case 4: Select World Region and Country
  else if(world_region.length == 1 && country.length == 1 && wine_region.length == 0) {
    showAllFilter();
    $('.worldRegionItem div').children(':checkbox').attr("disabled", true);
    $('.worldRegionItem div').children(':checkbox').next().next().css("opacity", "0.5");
    $('.countryItem div').children(':checkbox:not(:checked)').attr("disabled", true);
    $('.countryItem div').children(':checkbox:not(:checked)').next().next().css("opacity", "0.5");
    if(country_wine_region!==undefined){
      $('.wineRegionItem').each(function(i, obj) {        
        if ($.inArray($(obj).attr('id'), country_wine_region) == -1)
        {
          $(obj).hide();
        }
      });
    }
  }
  // Case 5: Select World Region and Wine Region
  else if(world_region.length == 1 && country.length == 0 && wine_region.length == 1) {
    showAllFilter();
    $('.worldRegionItem div').children(':checkbox').attr("disabled", true);
    $('.worldRegionItem div').children(':checkbox').next().next().css("opacity", "0.5");
    $('.countryItem div').children(':checkbox').attr("disabled", true);
    $('.countryItem div').children(':checkbox').next().next().css("opacity", "0.5");
    $('.wineRegionItem div').children(':checkbox:not(:checked)').attr("disabled", true);
    $('.wineRegionItem div').children(':checkbox:not(:checked)').next().next().css("opacity", "0.5");
  }
  // Case 6: Select Country and Wine Region
  else if(world_region.length == 0 && country.length == 1 && wine_region.length == 1) {
    showAllFilter();
    $('.worldRegionItem div').children(':checkbox').attr("disabled", true);
    $('.worldRegionItem div').children(':checkbox').next().next().css("opacity", "0.5");
    $('.countryItem div').children(':checkbox').attr("disabled", true);
    $('.countryItem div').children(':checkbox').next().next().css("opacity", "0.5");
    $('.wineRegionItem div').children(':checkbox:not(:checked)').attr("disabled", true);
    $('.wineRegionItem div').children(':checkbox:not(:checked)').next().next().css("opacity", "0.5");
  }
  // Case 7: Select World Region, Country, and Wine Region
  else if(world_region.length == 1 && country.length == 1 && wine_region.length == 1) {
    showAllFilter();
    $('.worldRegionItem div').children(':checkbox').attr("disabled", true);
    $('.worldRegionItem div').children(':checkbox').next().next().css("opacity", "0.5");
    $('.countryItem div').children(':checkbox').attr("disabled", true);
    $('.countryItem div').children(':checkbox').next().next().css("opacity", "0.5");
    $('.wineRegionItem div').children(':checkbox:not(:checked)').attr("disabled", true);
    $('.wineRegionItem div').children(':checkbox:not(:checked)').next().next().css("opacity", "0.5");
  }
  // Case 8: Nothing Selected
  else if(world_region.length == 0 && country.length == 0 && wine_region.length == 0) {
    showAllFilter();
  }
  else {
    alert("Error");
  }
}

// Reset Filter
function resetAllFilters(){
  $('input[type=checkbox]:checked').each(function(index) {
    $(this).prop('checked', false).change();
  });
  $(this).remove();
}

// Vineyard Section Pagination
function loadMore(currentPage){
  var _data={};
  _data = {currentVineyards, perPage, currentPage};

  // Run Ajax
  $.ajax({
    url:'/load-more-data',
    data:_data,
    dataType:'json',
    beforeSend:function(){
      $(".ajaxLoader").show();
    },
    success:function(res){
      $("#filteredVineyards").html(res.data);
      $(".ajaxLoader").hide();
      $('html, body').animate({scrollTop: $("#filteredVineyards").offset().top-300}, 100); 
      $('#view-filtered-vineyards').text("View all " + res.total_vineyards + " Vineyards");
    }
  });
};
