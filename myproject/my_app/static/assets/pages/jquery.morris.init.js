$(function() {


var colorDanger = "#FF1744";
var homeBar = Morris.Donut({
  element: 'donut-example',
  resize: true,
  colors: [
    '#E0F7FA',
    '#B2EBF2',
    '#80DEEA',
    '#4DD0E1',
    '#26C6DA',
    '#00BCD4',
    '#00ACC1',
    '#0097A7',
    '#00838F',
    '#006064'
  ],
  //labelColor:"#cccccc", // text color
  //backgroundColor: '#333333', // border color
  data: [
    {label:"Dato Ej.1", value:123, color:colorDanger},
    {label:"Dato Ej.2", value:369},
    {label:"Dato Ej.3", value:246},
    {label:"Dato Ej.4", value:159},
    {label:"Dato Ej.5", value:357}
  ]
});

$(".Profile_Chart_tab").click(always_callback);

 var always_callback=  $(".Profile_Chart_tab").click('click', function (event) {
    event.preventDefault();
  $(this).addClass('Profile_Chart_tab');
    homeBanner(event);
});





function homeBanner(e)
{
    var target = $(e.target).attr("href") // activated tab
 
    switch (target) {
      case "#Profile_Chart":
        homeBar.redraw();
        $(window).trigger('resize');
        break;
      
    }

}



});