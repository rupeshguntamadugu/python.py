////////  Load Tour Start Page (if not there now)  ////////

if (window.location.href != "https://seleniumbase.io/error_page/") {
    window.location.href="https://seleniumbase.io/error_page/";
}

////////  Resources  ////////

function injectCSS(css_link) {var head = document.getElementsByTagName("head")[0];var link = document.createElement("link");link.rel = "stylesheet";link.type = "text/css";link.href = css_link;link.crossorigin = "anonymous";head.appendChild(link);};
function injectJS(js_link) {var head = document.getElementsByTagName("head")[0];var script = document.createElement("script");script.src = js_link;script.defer;script.type="text/javascript";script.crossorigin = "anonymous";script.onload = function() { null };head.appendChild(script);};
function injectStyle(css) {var head = document.getElementsByTagName("head")[0];var style = document.createElement("style");style.type = "text/css";style.appendChild(document.createTextNode(css));head.appendChild(style);};
injectJS("https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js");

function loadResources() { if ( typeof jQuery !== "undefined" ) {
injectCSS("https://cdnjs.cloudflare.com/ajax/libs/bootstrap-tour/0.12.0/css/bootstrap-tour-standalone.min.css");
injectStyle("        .tour-tour-element {            pointer-events: none !important;        }        :not(.tour-tour-element) .orphan.tour-tour {            box-shadow: 0 0 0 88422px rgba(0, 0, 0, 0.42);            pointer-events: auto !important;        }        ");
injectJS("https://cdnjs.cloudflare.com/ajax/libs/bootstrap-tour/0.12.0/js/bootstrap-tour-standalone.min.js");} else { window.setTimeout("loadResources();",100); } }
loadResources()

////////  Tour Code  ////////

function loadTour() { if ( typeof Tour !== "undefined" ) {

    // Bootstrap Tour
    var tour = new Tour({
    container: 'body',
    animation: true,
    keyboard: true,
    orphan: true,
    smartPlacement: true,
    autoscroll: true,
    backdrop: true,
    backdropContainer: 'body',
    backdropPadding: 3,
    });
    tour.addSteps([
    {

        title: '',
        content: 'Welcome to the Octocat Tour!',
        orphan: true,
        autoscroll: true,
        backdrop: false,
        placement: 'top',
        smartPlacement: true,
        duration: 0,
        },{
        element: '#parallax_octocat:first',
        title: '',
        content: 'This is Octocat',
        orphan: true,
        autoscroll: true,
        backdrop: true,
        placement: 'top',
        smartPlacement: true,
        duration: 0,
        },{
        element: '#octobi_wan_catnobi:first',
        title: '',
        content: 'This is Octobi-Wan Catnobi',
        orphan: true,
        autoscroll: true,
        backdrop: true,
        placement: 'top',
        smartPlacement: true,
        duration: 0,
        },{
        element: '#parallax_error_text:first',
        title: '',
        content: '<h1><b>Ooops!!!</b></h1>',
        orphan: true,
        autoscroll: true,
        backdrop: true,
        placement: 'top',
        smartPlacement: true,
        duration: 0,
        },{
        element: '#speeder:first',
        title: '',
        content: 'This is a Star Wars speeder.',
        orphan: true,
        autoscroll: true,
        backdrop: true,
        placement: 'top',
        smartPlacement: true,
        duration: 0,
        },{
        element: '#parallax_sign:first',
        title: '',
        content: 'This is a sign with a 500-Error',
        orphan: true,
        autoscroll: true,
        backdrop: true,
        placement: 'top',
        smartPlacement: true,
        duration: 0,
        },{
        element: 'img[alt*=\"404\"]:first',
        title: '',
        content: 'This is not the page you\'re looking for.',
        orphan: true,
        autoscroll: true,
        backdrop: true,
        placement: 'top',
        smartPlacement: true,
        duration: 0,
        },{

        title: '😃 ☀️ 😁',
        content: '<b>Have a great day!</b>',
        orphan: true,
        autoscroll: true,
        backdrop: false,
        placement: 'top',
        smartPlacement: true,
        duration: 0,
        },{

        title: '⭐',
        content: '<b>And may the Force be with you!</b>',
        orphan: true,
        autoscroll: true,
        backdrop: false,
        placement: 'top',
        smartPlacement: true,
        duration: 0,
        },]);
    // Initialize the tour
    tour.init();
    // Start the tour
    tour.start();
    $tour = tour;
    $tour.restart();

} else { window.setTimeout("loadTour();",100); } }
loadTour()
