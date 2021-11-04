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
